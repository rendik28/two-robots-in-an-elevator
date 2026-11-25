from pathlib import Path


# The sensors coach a polite floor question and betray the hope behind it.
LINE = "What floor are you getting off at? My proximity sensors asked me to sound less hopeful."


def main():
    output = Path("/output")
    output.mkdir(parents=True, exist_ok=True)
    (output / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
