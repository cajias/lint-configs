"""Command-line interface for lint-configs package."""

import argparse
import sys
from pathlib import Path

from lint_configs import __version__, copy_config_to_project, get_python_config_path


def main() -> int:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="lint-configs",
        description="Manage canonical linting configurations for Python projects",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # copy command
    copy_parser = subparsers.add_parser(
        "copy",
        help="Copy linting configuration to your project",
    )
    copy_parser.add_argument(
        "--target",
        type=Path,
        default=None,
        help="Target directory (default: current directory)",
    )
    copy_parser.add_argument(
        "--merge",
        action="store_true",
        help="Merge with existing pyproject.toml (requires manual merge)",
    )
    
    # show command
    show_parser = subparsers.add_parser(
        "show",
        help="Show path to the configuration file",
    )
    show_parser.add_argument(
        "--cat",
        action="store_true",
        help="Print the configuration content",
    )
    
    args = parser.parse_args()
    
    if args.command == "copy":
        try:
            config_path = copy_config_to_project(
                target_dir=args.target,
                merge_with_existing=args.merge,
            )
            return 0
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1
    
    elif args.command == "show":
        config_path = get_python_config_path()
        if args.cat:
            print(config_path.read_text())
        else:
            print(config_path)
        return 0
    
    else:
        parser.print_help()
        return 0


if __name__ == "__main__":
    sys.exit(main())
