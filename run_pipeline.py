import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
PYTHON = sys.executable

def run(script_name: str):
    script_path = BASE_DIR / "src" / script_name
    print(f"\n--- Running {script_name} ---")
    subprocess.check_call([PYTHON, str(script_path)])

def main():
    run("01_load_raw.py")
    run("02_run_transform.py")
    print("\n✅ Pipeline complete (raw load + transform)")

if __name__ == "__main__":
    main()
