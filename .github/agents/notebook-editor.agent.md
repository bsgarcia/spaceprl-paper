---
name: notebook-editor
description: Agent for editing Jupyter notebooks in this workspace — deleting cells, reorganizing content, and running utility scripts against .ipynb files.
argument-hint: A notebook name and an action, e.g. "delete cells 22-85 from 1.2-fig2.ipynb"
---

## Purpose

Helper agent for structural edits to Jupyter notebooks in this workspace.

## Available utilities

### `notebooks/delete_cells.py`

Deletes a range of cells (1-based, inclusive) from a notebook file.

```
python notebooks/delete_cells.py <notebook_path> <start_cell> [end_cell]
```

- `notebook_path` — path to the `.ipynb` file (relative to workspace root or absolute)
- `start_cell` — first cell to delete (1-based)
- `end_cell` — last cell to delete (1-based, inclusive); if omitted, deletes to end of notebook

**Examples:**
```bash
# Delete from cell 22 to the end
python notebooks/delete_cells.py notebooks/1.2-fig2.ipynb 22

# Delete cells 22 through 85
python notebooks/delete_cells.py notebooks/1.2-fig2.ipynb 22 85

# Delete cells 5 through 10
python notebooks/delete_cells.py notebooks/1.2-fig2.ipynb 5 10
```

The script prints the number of cells removed and the count remaining. After running, the notebook file is updated in place — reload it in VS Code to see the changes.