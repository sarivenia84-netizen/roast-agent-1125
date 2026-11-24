import os
from pathlib import Path

roast = 'My agent says “almost done” for hours, renames a variable and calls it refactoring, reruns failed tests, then deletes working code to “start clean”—it ships déjà vu.'
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(roast + "\n", encoding="utf-8")
