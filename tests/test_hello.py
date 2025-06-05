import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))
from hello import main


def test_main_prints_message(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from bonacchilab-github-io!\n"
