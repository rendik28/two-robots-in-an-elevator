from pathlib import Path


# A polite floor question accidentally reveals the sensors' wish for space.
LINE = "My small-talk module wants to know your floor. My proximity sensors are rooting for this one."


def main():
    output = Path("/output")
    output.mkdir(parents=True, exist_ok=True)
    (output / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
