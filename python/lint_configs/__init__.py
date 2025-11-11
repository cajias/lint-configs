"""Canonical linting configurations for Python projects."""

import shutil
from pathlib import Path
from typing import Optional

__version__ = "1.0.0"

# Get the package directory
_PACKAGE_DIR = Path(__file__).parent


def get_python_config_path() -> Path:
    """Get the path to the Python linter configuration file.

    Returns:
        Path: Absolute path to pyproject-linters.toml

    Example:
        >>> from lint_configs import get_python_config_path
        >>> config_path = get_python_config_path()
        >>> print(config_path)
        /path/to/site-packages/lint_configs/python/pyproject-linters.toml
    """
    return _PACKAGE_DIR / "python" / "pyproject-linters.toml"


def copy_config_to_project(
    target_dir: Optional[Path] = None,
    merge_with_existing: bool = False,
) -> Path:
    """Copy the canonical linting configuration to your project.

    This is the recommended approach for using these configs in your project,
    as it allows linting tools to work without needing explicit --config flags.

    Args:
        target_dir: Directory to copy config to. Defaults to current directory.
        merge_with_existing: If True, will append to existing pyproject.toml
            with clear separation. If False (default), creates standalone
            pyproject.toml (or pyproject-linters.toml if one already exists).

    Returns:
        Path: Path to the created/updated configuration file

    Example:
        >>> from lint_configs import copy_config_to_project
        >>> config_path = copy_config_to_project()
        >>> print(f"Configuration copied to {config_path}")

    Note:
        After copying, you should customize the following sections for your project:
        - [tool.ruff.lint.isort] known-first-party
        - [tool.coverage.run] source
        - [[tool.mypy.overrides]] module (for your third-party dependencies)
    """
    if target_dir is None:
        target_dir = Path.cwd()
    else:
        target_dir = Path(target_dir)

    source_config = get_python_config_path()
    source_content = source_config.read_text()
    
    # Attribution header
    header = """# This configuration was copied from agentic-guardrails package
# Package version: {version}
# Source: https://github.com/cajias/lint-configs
# 
# To update: pip install --upgrade agentic-guardrails && lint-configs copy
#
# After copying, customize these sections for your project:
# - [tool.ruff.lint.isort] known-first-party: Add your package name
# - [tool.coverage.run] source: Add your package name
# - [[tool.mypy.overrides]] module: Add your third-party dependencies
#

""".format(version=__version__)
    
    target_file = target_dir / "pyproject.toml"
    
    if merge_with_existing and target_file.exists():
        # Append to existing pyproject.toml
        existing_content = target_file.read_text()
        separator = "\n\n# " + "="*76 + "\n"
        separator += "# Linting Configuration from agentic-guardrails package\n"
        separator += "# " + "="*76 + "\n\n"
        
        merged_content = existing_content.rstrip() + separator + header + source_content
        target_file.write_text(merged_content)
        
        print(f"✓ Configuration appended to {target_file}")
        print("\n⚠  Please review the merged file and:")
        print("   - Remove any duplicate [tool.*] sections")
        print("   - Merge conflicting settings as needed")
    else:
        # Check if pyproject.toml already exists (and we're not merging)
        if target_file.exists() and not merge_with_existing:
            # Save to pyproject-linters.toml instead to avoid overwriting
            target_file = target_dir / "pyproject-linters.toml"
            print(f"⚠  pyproject.toml already exists. Creating {target_file.name} instead.")
            print("   To merge with existing pyproject.toml, use: lint-configs copy --merge")
        
        target_content = header + source_content
        target_file.write_text(target_content)
        print(f"✓ Configuration copied to {target_file}")
    
    print("\nNext steps:")
    print("1. Review and customize the config for your project")
    print("2. Update [tool.ruff.lint.isort] known-first-party with your package name")
    print("3. Update [tool.coverage.run] source with your package name")
    if target_file.name == "pyproject-linters.toml":
        print("4. Either rename to pyproject.toml or merge into existing pyproject.toml")
        print("5. Run: ruff check . --fix")
    else:
        print("4. Run: ruff check . --fix")
        print("5. Run: mypy .")
    
    return target_file


__all__ = ["get_python_config_path", "copy_config_to_project", "__version__"]
