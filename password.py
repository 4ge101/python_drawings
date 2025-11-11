# generate_combinations.py
# Generates all combinations (with repetition) from a charset
# for lengths 1..5. Use only for local/educational purposes.

import itertools
import sys
from time import time

CHARSET = "manishet0123456789!@#$&"
MAX_LEN = 5

# Change this to a filename to save results instead of printing.
# Example: OUTPUT_FILE = "combos.txt"
OUTPUT_FILE = None

# How often to print a progress update
STATUS_EVERY = 100000

def generate_and_output(charset, max_len, output_file=None):
    counter = 0
    start = time()
    out = None
    try:
        if output_file:
            out = open(output_file, "w", encoding="utf-8")
            write = lambda s: out.write(s + "\n")
        else:
            write = lambda s: print(s, flush=False)

        for length in range(1, max_len + 1):
            # itertools.product yields tuples of characters
            for tup in itertools.product(charset, repeat=length):
                s = "".join(tup)
                write(s)
                counter += 1
                if counter % STATUS_EVERY == 0:
                    elapsed = time() - start
                    print(f"[status] generated {counter:,} combos — length={length} — elapsed={elapsed:.1f}s", file=sys.stderr)
    finally:
        if out:
            out.close()
    total_time = time() - start
    print(f"Done. Generated {counter:,} combinations in {total_time:.1f}s.", file=sys.stderr)


if __name__ == "__main__":
    print(f"CHARSET length = {len(CHARSET)}")
    est = sum(len(CHARSET) ** L for L in range(1, MAX_LEN + 1))
    print(f"Estimated total combinations (1..{MAX_LEN}): {est:,}")
    if OUTPUT_FILE:
        print(f"Writing output to {OUTPUT_FILE!r}")
    else:
        print("Printing to stdout (this will be large).")
    generate_and_output(CHARSET, MAX_LEN, OUTPUT_FILE)
