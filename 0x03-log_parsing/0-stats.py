#!/usr/bin/python3
import sys


def compute_metrics():
    total_lines = 0
    total_chars = 0

    for line in sys.stdin:
        total_lines += 1
        total_chars += len(line)

    average_line_length = total_chars / total_lines if total_lines > 0 else 0

    return total_lines, total_chars, average_line_length


if __name__ == "__main__":
    try:
        lines, chars, avg_length = compute_metrics()
        print(f"Total lines: {lines}")
        print(f"Total characters: {chars}")
        print(f"Average line length: {avg_length:.2f}")
    except KeyboardInterrupt:
        print("\nScript interrupted by user.")
    except Exception as e:
        print(f"Error: {e}")
