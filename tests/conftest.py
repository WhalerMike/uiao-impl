"""Shared pytest fixtures for uiao-impl tests."""
from __future__ import annotations

from pathlib import Path

import pytest

from canon_paths import CANON_ROOT, DATA_DIR, GENERATION_INPUTS_DIR


@pytest.fixture
def project_root() -> Path:
    """Return the uiao-impl project root directory."""
    return Path(__file__).resolve().parent.parent


@pytest.fixture
def canon_root() -> Path:
    """Return the resolved canon root (uiao-core checkout)."""
    return CANON_ROOT


@pytest.fixture
def canon_dir() -> Path:
    """Return the generation-inputs/ directory from canon."""
    return GENERATION_INPUTS_DIR


@pytest.fixture
def data_dir() -> Path:
    """Return the data/ directory from canon."""
    return DATA_DIR


@pytest.fixture
def exports_dir(project_root: Path, tmp_path: Path) -> Path:
    """Return a temporary exports directory for test output."""
    out = tmp_path / "exports" / "oscal"
    out.mkdir(parents=True)
    return out


@pytest.fixture
def sample_canon_entry() -> dict:
    """Return a minimal canon-like dict for unit tests."""
    return {
        "id": "test-entry-001",
        "name": "Test Canon Entry",
        "description": "A test entry for unit testing.",
        "category": "testing",
    }
