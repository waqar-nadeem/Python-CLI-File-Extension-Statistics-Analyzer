import os
import argparse
from collections import defaultdict

def analyze(directory):
    stats = defaultdict(int)
    for root, _, files in os.walk(directory):
        for file in files:
            ext = os.path.splitext(file)[1].lower() or "no_extension"
            stats[ext] += 1
    for ext, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
        print(f"{ext}: {count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    args = parser.parse_args()
    analyze(args.directory)
