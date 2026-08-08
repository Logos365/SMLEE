import argparse
import math
from pathlib import Path

import cv2
import numpy as np


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def frame_at(cap: cv2.VideoCapture, second: float):
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(second * fps))
    ok, frame = cap.read()
    return frame if ok else None


def content_crop(frame):
    # Ignore the YouTube/player edges if they are present in captured material.
    h, w = frame.shape[:2]
    return frame[int(h * 0.02) : int(h * 0.98), int(w * 0.02) : int(w * 0.98)]


def hash_image(frame, size=16):
    gray = cv2.cvtColor(content_crop(frame), cv2.COLOR_BGR2GRAY)
    small = cv2.resize(gray, (size, size), interpolation=cv2.INTER_AREA)
    return small.astype(np.float32)


def diff_score(a, b) -> float:
    return float(np.mean(np.abs(a - b)))


def make_contact_sheet(video: Path, out_path: Path, interval: int = 30) -> None:
    cap = cv2.VideoCapture(str(video))
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    total = cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0
    duration = total / fps if fps else 0
    thumbs = []
    for second in range(0, int(duration) + 1, interval):
        frame = frame_at(cap, second)
        if frame is None:
            continue
        thumb = cv2.resize(frame, (240, 135), interpolation=cv2.INTER_AREA)
        cv2.putText(
            thumb,
            f"{second//60:02d}:{second%60:02d}",
            (8, 124),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 0, 0),
            3,
            cv2.LINE_AA,
        )
        cv2.putText(
            thumb,
            f"{second//60:02d}:{second%60:02d}",
            (8, 124),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            1,
            cv2.LINE_AA,
        )
        thumbs.append(thumb)
    if not thumbs:
        raise RuntimeError("No frames found for contact sheet")
    cols = 4
    rows = math.ceil(len(thumbs) / cols)
    sheet = np.full((rows * 135, cols * 240, 3), 255, dtype=np.uint8)
    for idx, thumb in enumerate(thumbs):
        y = (idx // cols) * 135
        x = (idx % cols) * 240
        sheet[y : y + 135, x : x + 240] = thumb
    ensure_dir(out_path.parent)
    cv2.imwrite(str(out_path), sheet)


def extract_slides(
    video: Path,
    out_dir: Path,
    sample_interval: float = 1.0,
    threshold: float = 12.0,
    min_gap: float = 4.0,
) -> int:
    ensure_dir(out_dir)
    cap = cv2.VideoCapture(str(video))
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
    duration = total / fps if fps else 0

    selected = []
    last_hash = None
    last_saved_second = -min_gap
    second = 0.0
    while second <= duration:
        frame = frame_at(cap, second)
        if frame is None:
            second += sample_interval
            continue
        hsh = hash_image(frame)
        changed = last_hash is None or diff_score(last_hash, hsh) >= threshold
        if changed and (second - last_saved_second) >= min_gap:
            selected.append((second, frame.copy()))
            last_hash = hsh
            last_saved_second = second
        second += sample_interval

    for idx, (second, frame) in enumerate(selected, start=1):
        name = f"slide_{idx:03d}_{int(second//60):02d}m{int(second%60):02d}s.png"
        cv2.imwrite(str(out_dir / name), frame)
    return len(selected)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("video", type=Path)
    parser.add_argument("--out-dir", type=Path, default=Path("youtube_slide_extract/slides_png"))
    parser.add_argument("--contact-sheet", type=Path)
    parser.add_argument("--threshold", type=float, default=12.0)
    parser.add_argument("--sample-interval", type=float, default=1.0)
    parser.add_argument("--min-gap", type=float, default=4.0)
    args = parser.parse_args()

    if args.contact_sheet:
        make_contact_sheet(args.video, args.contact_sheet)
    count = extract_slides(
        args.video,
        args.out_dir,
        sample_interval=args.sample_interval,
        threshold=args.threshold,
        min_gap=args.min_gap,
    )
    print(f"saved {count} slide images to {args.out_dir}")


if __name__ == "__main__":
    main()
