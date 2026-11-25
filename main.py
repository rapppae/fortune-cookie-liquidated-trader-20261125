"""Entry for make.fun bounty: Fortune Cookie for the Liquidated Trader
Slug: u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c
Entry text (91 characters, 19 words (limit 20 words), gate max 160). Written to /output/entry.txt with no trailing newline.
"""
import os

ENTRY = """A great loss is coming, but so is a greater lesson: never bet rent money on a green candle."""

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
