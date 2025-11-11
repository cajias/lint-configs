# Canonical Linter Configurations

A collection of strict, opinionated linter configurations for multiple languages, designed to enforce code quality and consistency across all projects in an organization.

## Philosophy

**If it's worth enabling, it's worth enforcing everywhere.**

This repository provides canonical linting configurations with:
- **Minimal ignores** - Only rules that conflict with formatters are ignored
- **Maximum strictness** - All quality checks enabled
- **Language consistency** - Similar principles across all languages
- **Easy adoption** - Simple to integrate into any project

## Available Configurations

### 🐍 [Python](./python/)

Comprehensive linting for Python projects using:
- **Ruff** - 40+ rule categories enabled
- **MyPy** - Strict mode type checking
- **Black** - Code formatting
- **Pylint** - Duplicate code detection
- **80% coverage** required

**Key features:**
- Type hints everywhere
- Docstrings required
- Security checks (Bandit)
- Complexity limits
- No duplicate code

[View Python README →](./python/README.md)

## Coming Soon

- 🟦 **TypeScript/JavaScript** - ESLint, Prettier, TypeScript strict mode
- ⚙️ **Go** - golangci-lint with comprehensive linters
- 🦀 **Rust** - Clippy with all lints
- ☕ **Java** - Checkstyle, SpotBugs, PMD
- 💎 **Ruby** - RuboCop with strict defaults

## Quick Start

### Method 1: Git Submodule (Recommended)

Add as a submodule to any project:

```bash
# In your project root
git submodule add https://github.com/YOUR_ORG/lint-configs .lint-configs
git submodule update --init

# Copy the config for your language
cp .lint-configs/python/pyproject.toml ./pyproject.toml

# Or create a symlink
ln -s .lint-configs/python/pyproject.toml ./pyproject.toml
```

**Benefits:**
- Keep configs synchronized across projects
- Easy updates via `git submodule update --remote`
- Version controlled config changes
- Single source of truth for the organization

### Method 2: Direct Copy

Copy the configuration files directly:

```bash
# Python
curl -O https://raw.githubusercontent.com/YOUR_ORG/lint-configs/main/python/pyproject.toml

# TypeScript (coming soon)
curl -O https://raw.githubusercontent.com/YOUR_ORG/lint-configs/main/typescript/.eslintrc.js
```

### Method 3: Template Repository

Use as a template when creating new projects:

```bash
git clone https://github.com/YOUR_ORG/lint-configs
cd lint-configs
cp -r python/. ../my-new-project/
```

## Structure

```
lint-configs/
├── README.md              # This file
├── python/
│   ├── README.md          # Python-specific usage guide
│   └── pyproject.toml     # Canonical Python config
├── typescript/            # Coming soon
│   ├── README.md
│   ├── .eslintrc.js
│   ├── .prettierrc.js
│   └── tsconfig.json
├── go/                    # Coming soon
│   ├── README.md
│   └── .golangci.yml
└── rust/                  # Coming soon
    ├── README.md
    └── clippy.toml
```

## Usage Examples

### For New Projects

When starting a new project:

```bash
# 1. Create your project
mkdir my-new-project && cd my-new-project
git init

# 2. Add lint-configs as submodule
git submodule add https://github.com/YOUR_ORG/lint-configs .lint-configs

# 3. Copy relevant config
cp .lint-configs/python/pyproject.toml .

# 4. Customize for your project
# Edit pyproject.toml to add your package name

# 5. Commit
git add .
git commit -m "Add linting configuration"
```

### For Existing Projects

Gradually adopt the configuration:

```bash
# 1. Add as submodule
git submodule add https://github.com/YOUR_ORG/lint-configs .lint-configs

# 2. Copy config
cp .lint-configs/python/pyproject.toml .

# 3. See what needs to be fixed
ruff check .
mypy .

# 4. Fix incrementally
ruff check . --fix              # Auto-fix what's possible
ruff check . --select=I --fix   # Fix imports
# ... continue with other categories

# 5. Commit when ready
git commit -am "Apply canonical linting configuration"
```

### Keeping Configs Up to Date

Update all projects to the latest config:

```bash
# In your project
cd .lint-configs
git pull origin main
cd ..

# Copy updated config
cp .lint-configs/python/pyproject.toml .

# Test changes
ruff check .

# Commit if all looks good
git add pyproject.toml .lint-configs
git commit -m "Update linting configuration"
```

## Configuration Principles

All configurations in this repository follow these principles:

### 1. Minimal Ignores

Only ignore rules that:
- Conflict with code formatters (e.g., line length when using Black/Prettier)
- Are fundamentally broken or produce false positives

### 2. Maximum Enforcement

Enable all available quality checks:
- Type safety
- Security scanning
- Complexity limits
- Code duplication detection
- Style consistency

### 3. Smart Exceptions

Reasonable per-file ignores for:
- Test files (allow asserts, magic values)
- Generated code (skip most checks)
- Scripts (allow prints, simple structure)

### 4. Coverage Requirements

Enforce minimum test coverage:
- Python: 80%
- TypeScript: 80%
- Go: 80%
- Others: TBD

## CI/CD Integration

### GitHub Actions

Create `.github/workflows/lint.yml`:

```yaml
name: Lint

on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          submodules: true  # Important: fetch lint-configs submodule

      - name: Set up environment
        uses: actions/setup-python@v5
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: pip install -e ".[dev]"

      - name: Run linters
        run: |
          black --check .
          ruff check .
          mypy .
          pytest --cov
```

### GitLab CI

Create `.gitlab-ci.yml`:

```yaml
lint:
  image: python:3.9
  before_script:
    - git submodule update --init
    - pip install -e ".[dev]"
  script:
    - black --check .
    - ruff check .
    - mypy .
    - pytest --cov
```

## Contributing

### Adding a New Language

1. Create a directory: `mkdir <language>/`
2. Add canonical config files
3. Create `<language>/README.md` with:
   - Quick start instructions
   - Configuration overview
   - Usage examples
   - Customization guide
4. Update this root README with the new language
5. Open a PR

### Updating Existing Configs

1. Open an issue explaining:
   - Why the change is needed
   - Examples of false positives or conflicts
   - Impact on existing projects
2. Get consensus from the team
3. Make the change
4. Update the language-specific README
5. Open a PR

**Important:** Config changes affect all projects using these configs. Be conservative with changes.

## Language-Specific Guides

Each language directory contains:

- **`README.md`** - Detailed usage guide for that language
- **Config files** - The canonical configuration
- **Examples** - Sample projects using the config

See the language-specific READMEs for:
- Installation instructions
- Tool versions
- Customization options
- Migration guides
- Troubleshooting

## Philosophy: Why Strict Linting?

### Benefits

1. **Catch bugs early** - Type checking and linting catch issues before code review
2. **Consistent code style** - No bikeshedding in reviews
3. **Easier onboarding** - New developers know what's expected
4. **Better refactoring** - Type hints enable safe changes
5. **Living documentation** - Code is self-documenting
6. **Prevent technical debt** - Complexity and duplication caught early

### Trade-offs

- **Initial migration cost** - Existing projects need updates
- **Learning curve** - Developers must learn stricter patterns
- **False positives** - Occasionally need `# noqa` or similar

We believe the long-term benefits far outweigh these costs.

## FAQ

### Why not just use defaults?

Defaults are often too permissive. This leads to:
- Inconsistent code across projects
- Issues caught late in code review
- Technical debt accumulation

### Can I customize for my project?

Yes! These are starting points. You can:
- Add per-file ignores for special cases
- Adjust complexity thresholds
- Add project-specific rules

But document why and consider if it should be in the canonical config.

### What if I disagree with a rule?

1. Try following the rule for a while
2. If it's genuinely problematic, open an issue
3. Discuss with the team
4. Update the canonical config if consensus is reached

### How do I handle legacy code?

Use per-file ignores:

```toml
[tool.ruff.lint.per-file-ignores]
"legacy/**/*.py" = ["ANN", "D"]  # Relax for legacy code
```

But create tickets to gradually improve legacy code.

## Support

- **Issues:** Open an issue for questions or problems
- **Discussions:** Use GitHub Discussions for general questions
- **Contributing:** See CONTRIBUTING.md (coming soon)

## License

MIT

## Maintainers

This repository is maintained by the Engineering team. Changes require review and approval from at least 2 maintainers.
