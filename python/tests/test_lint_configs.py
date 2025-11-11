"""Tests for lint-configs package functionality."""

import tempfile
from pathlib import Path

import pytest

from lint_configs import __version__, copy_config_to_project, get_python_config_path


def test_version():
    """Test that version is defined."""
    assert __version__ == "1.0.0"


def test_get_python_config_path():
    """Test that get_python_config_path returns valid path."""
    config_path = get_python_config_path()
    assert isinstance(config_path, Path)
    assert config_path.exists()
    assert config_path.name == "pyproject-linters.toml"
    assert config_path.is_file()


def test_get_python_config_path_content():
    """Test that config file has expected content."""
    config_path = get_python_config_path()
    content = config_path.read_text()
    
    # Check for key sections
    assert "[tool.ruff]" in content
    assert "[tool.mypy]" in content
    assert "[tool.pylint" in content
    assert "[tool.coverage" in content
    assert "[tool.black]" in content


def test_copy_config_to_empty_directory():
    """Test copying config to an empty directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        target_dir = Path(tmpdir)
        
        result_path = copy_config_to_project(target_dir=target_dir)
        
        assert result_path.exists()
        assert result_path.name == "pyproject.toml"
        assert result_path.parent == target_dir
        
        content = result_path.read_text()
        assert "agentic-guardrails" in content
        assert f"Package version: {__version__}" in content
        assert "[tool.ruff]" in content


def test_copy_config_when_pyproject_exists():
    """Test copying config when pyproject.toml already exists."""
    with tempfile.TemporaryDirectory() as tmpdir:
        target_dir = Path(tmpdir)
        existing_pyproject = target_dir / "pyproject.toml"
        existing_pyproject.write_text("[project]\nname = 'test'\n")
        
        result_path = copy_config_to_project(target_dir=target_dir)
        
        # Should create pyproject-linters.toml instead
        assert result_path.exists()
        assert result_path.name == "pyproject-linters.toml"
        
        # Original should be unchanged
        assert existing_pyproject.read_text() == "[project]\nname = 'test'\n"
        
        # New file should have lint configs
        content = result_path.read_text()
        assert "agentic-guardrails" in content
        assert "[tool.ruff]" in content


def test_copy_config_merge_mode():
    """Test copying config with merge mode."""
    with tempfile.TemporaryDirectory() as tmpdir:
        target_dir = Path(tmpdir)
        existing_pyproject = target_dir / "pyproject.toml"
        original_content = "[project]\nname = 'test'\nversion = '1.0.0'\n"
        existing_pyproject.write_text(original_content)
        
        result_path = copy_config_to_project(
            target_dir=target_dir,
            merge_with_existing=True
        )
        
        # Should append to existing pyproject.toml
        assert result_path.exists()
        assert result_path.name == "pyproject.toml"
        
        content = result_path.read_text()
        
        # Should contain original content
        assert "[project]" in content
        assert "name = 'test'" in content
        
        # Should contain new lint config
        assert "agentic-guardrails" in content
        assert "[tool.ruff]" in content
        
        # Should have separator
        assert "Linting Configuration from agentic-guardrails" in content


def test_copy_config_merge_mode_without_existing_file():
    """Test merge mode when no pyproject.toml exists (should create new file)."""
    with tempfile.TemporaryDirectory() as tmpdir:
        target_dir = Path(tmpdir)
        
        result_path = copy_config_to_project(
            target_dir=target_dir,
            merge_with_existing=True
        )
        
        # Should create new pyproject.toml
        assert result_path.exists()
        assert result_path.name == "pyproject.toml"
        
        content = result_path.read_text()
        assert "agentic-guardrails" in content
        assert "[tool.ruff]" in content


def test_copied_config_has_customization_instructions():
    """Test that copied config includes customization instructions."""
    with tempfile.TemporaryDirectory() as tmpdir:
        target_dir = Path(tmpdir)
        
        result_path = copy_config_to_project(target_dir=target_dir)
        content = result_path.read_text()
        
        # Check for customization instructions
        assert "known-first-party" in content
        assert "source" in content
        assert "module" in content


def test_copied_config_has_update_instructions():
    """Test that copied config includes update instructions."""
    with tempfile.TemporaryDirectory() as tmpdir:
        target_dir = Path(tmpdir)
        
        result_path = copy_config_to_project(target_dir=target_dir)
        content = result_path.read_text()
        
        # Check for update instructions
        assert "To update:" in content
        assert "pip install --upgrade agentic-guardrails" in content


def test_copy_config_returns_path_object():
    """Test that copy_config_to_project returns a Path object."""
    with tempfile.TemporaryDirectory() as tmpdir:
        target_dir = Path(tmpdir)
        
        result_path = copy_config_to_project(target_dir=target_dir)
        
        assert isinstance(result_path, Path)
