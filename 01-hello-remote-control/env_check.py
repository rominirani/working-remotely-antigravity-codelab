#!/usr/bin/env python3
"""Remote Control Hello World: Local workstation environment & config check."""

import json
from pathlib import Path
import platform
import socket

BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "sample_gcp_config.json"

REQUIRED_KEYS = [
    "project_id",
    "region",
    "cloud_run_service",
    "firestore_database",
    "cloud_storage_bucket",
    "bigquery_dataset",
]


def main() -> int:
    print("=== Antigravity Remote Control: Local Workstation Check ===")
    print(f"Host Machine : {socket.gethostname()} ({platform.system()} {platform.release()})")
    print(f"Working Dir  : {Path.cwd()}")

    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    missing = [key for key in REQUIRED_KEYS if key not in config]

    print("\nLoaded Google Cloud Dev Config:")
    for key, val in config.items():
        print(f"  - {key}: {val}")

    if missing:
        print(f"\n[WARN] Missing required config keys: {', '.join(missing)}")
        return 1

    print("\n[OK] All required Google Cloud config keys are present!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
