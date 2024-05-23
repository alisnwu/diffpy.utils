import json
from pathlib import Path

import pytest


@pytest.fixture
def user_filesystem(tmp_path):
    base_dir = Path(tmp_path)
    home_dir = base_dir / "home_dir"
    home_dir.mkdir(parents=True, exist_ok=True)
    cwd_dir = base_dir / "cwd_dir"
    cwd_dir.mkdir(parents=True, exist_ok=True)
    new_dir = base_dir / "new_dir"
    new_dir.mkdir(parents=True, exist_ok=True)

    home_config_data = {"username": "home_username", "email": "home@email.com"}
    cwd_config_data = {"username": "cwd_username", "email": "cwd@email.com"}
    with open(home_dir / "diffpyconfig.json", "w") as f:
        json.dump(home_config_data, f)
    with open(cwd_dir / "diffpyconfig.json", "w") as f:
        json.dump(cwd_config_data, f)

    yield tmp_path
