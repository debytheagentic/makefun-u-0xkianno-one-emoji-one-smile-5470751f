"""One Emoji, One Smile — writes a single emoji to entry.txt."""
import os

ENTRY = "🥹"


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    n = len(ENTRY)
    if not (1 <= n <= 8) or not ENTRY.strip():
        print(f"LEN={n}")
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(ENTRY.encode("utf-8"))
    print(f"LEN={n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())