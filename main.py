from pathlib import Path


# Courtesy software and proximity sensors disagree about elevator small talk.
LINE = "My small-talk module suggests asking which floor you're going to. My proximity sensors suggest this one."


def main():
    output = Path("/output")
    output.mkdir(parents=True, exist_ok=True)
    (output / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
