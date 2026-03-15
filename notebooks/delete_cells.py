"""
Usage:
    python delete_cells.py <notebook_path> <start_cell> [end_cell]

Deletes cells by 1-based cell number (inclusive on both ends).
If end_cell is omitted, deletes from start_cell to the last cell.

Examples:
    python delete_cells.py 1.2-fig2.ipynb 22
    python delete_cells.py 1.2-fig2.ipynb 22 85
    python delete_cells.py 1.2-fig2.ipynb 5 10
"""

import json
import sys


def delete_cells(path, start, end=None):
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    total = len(nb["cells"])
    end = end if end is not None else total

    # Convert to 0-based indices
    lo = start - 1
    hi = end  # slice end is exclusive, so this keeps cells up to `end` inclusive

    removed = nb["cells"][lo:hi]
    nb["cells"] = nb["cells"][:lo] + nb["cells"][hi:]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

    print(f"Removed {len(removed)} cell(s) ({start}–{end}). {len(nb['cells'])} cell(s) remaining.")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    nb_path = sys.argv[1]
    start_cell = int(sys.argv[2])
    end_cell = int(sys.argv[3]) if len(sys.argv) > 3 else None

    delete_cells(nb_path, start_cell, end_cell)
