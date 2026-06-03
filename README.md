<!-- markdownlint-disable MD013 MD033 MD040 MD041 MD049 -->

```
██╗     ██╗███╗   ██╗████████╗    ██████╗ ██████╗ ███╗   ██╗███████╗██╗ ██████╗ ███████╗
██║     ██║████╗  ██║╚══██╔══╝   ██╔════╝██╔═══██╗████╗  ██║██╔════╝██║██╔════╝ ██╔════╝
██║     ██║██╔██╗ ██║   ██║█████╗██║     ██║   ██║██╔██╗ ██║█████╗  ██║██║  ███╗███████╗
██║     ██║██║╚██╗██║   ██║╚════╝██║     ██║   ██║██║╚██╗██║██╔══╝  ██║██║   ██║╚════██║
███████╗██║██║ ╚████║   ██║      ╚██████╗╚██████╔╝██║ ╚████║██║     ██║╚██████╔╝███████║
╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝       ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝
```

<p align="center"><em>Preferred linter configurations for common languages</em></p>

<p align="center">
  <img src="https://img.shields.io/github/languages/top/cajias/lint-configs?style=for-the-badge" alt="Language">
  <a href="https://github.com/cajias/lint-configs/actions"><img src="https://img.shields.io/github/actions/workflow/status/cajias/lint-configs/ci.yml?style=for-the-badge" alt="Build"></a>
  <a href="https://github.com/cajias/lint-configs/blob/main/LICENSE"><img src="https://img.shields.io/github/license/cajias/lint-configs?style=for-the-badge" alt="License"></a>
  <a href="https://github.com/cajias/lint-configs/stargazers"><img src="https://img.shields.io/github/stars/cajias/lint-configs?style=for-the-badge" alt="Stars"></a>
  <img src="https://img.shields.io/badge/AI--ready-strict-FACC15?style=for-the-badge" alt="AI-ready strict">
</p>

**Preferred linter configurations for common languages — strict, shareable, and built to catch the kind of slop that AI-generated code loves to sneak in.** `lint-configs` bundles battle-tested [ESLint](https://eslint.org/), [markdownlint](https://github.com/DavidAnson/markdownlint), [Ruff](https://docs.astral.sh/ruff/), [MyPy](https://mypy-lang.org/), [Black](https://black.readthedocs.io/), and [Pylint](https://pylint.readthedocs.io/) rule sets into installable packages, so every project you touch enforces the same uncompromising bar with a single dependency.

<table>
<tr><td><b>TypeScript / JavaScript</b></td><td>The <code>@lint-configs/eslint-config</code> npm package ships 220+ ESLint rules across security (XSS, eval, unsafe regex), Node.js, React hooks + accessibility, strict TypeScript, and complexity limits. Available as flat (<code>./flat</code>) or legacy (<code>./legacy</code>) configs.</td></tr>
<tr><td><b>Markdown</b></td><td>The <code>@lint-configs/markdownlint-config</code> npm package provides 40+ documentation rules: 120-char line length, ATX-style headings, fenced code blocks with language hints, and consistent 2-space list indentation.</td></tr>
<tr><td><b>Python</b></td><td>Drop-in <code>ruff.toml</code> and <code>pyproject</code> configs for Ruff (40+ rule categories: E, F, I, B, W, C90, PLR, SIM, RET, ANN), MyPy strict typing, Black formatting, and Pylint duplicate-code detection.</td></tr>
<tr><td><b>Formatter-aware</b></td><td>Only disables rules that genuinely conflict with formatters (Prettier / Black). Everything else stays on, so linter and formatter never fight.</td></tr>
<tr><td><b>Mirrored strictness</b></td><td>Each language's config mirrors the others' rigor — line length, complexity (max 10), security scanning, dead-code detection, and import sorting are aligned across the stack.</td></tr>
<tr><td><b>CI-verified packaging</b></td><td>GitHub Actions lints every config, checks formatting, and proves both the npm and PyPI packages actually install before anything ships.</td></tr>
</table>

## Installation

These are configuration packages — install the one(s) for your stack.

### TypeScript / JavaScript

```bash
npm install --save-dev @lint-configs/eslint-config eslint typescript
```

### Markdown

```bash
npm install --save-dev @lint-configs/markdownlint-config markdownlint-cli
```

### Python

The Python configs are plain TOML files. Install the tools they drive, then reference the configs:

```bash
pip install ruff mypy black pylint
```

## Usage

### TypeScript / JavaScript

Create `eslint.config.js` and spread the shared flat config:

```javascript
import config from '@lint-configs/eslint-config/flat';

export default [
  ...config,
  {
    languageOptions: {
      parserOptions: {
        project: './tsconfig.json',
      },
    },
  },
];
```

A legacy `.eslintrc` consumer can import `@lint-configs/eslint-config/legacy` instead.

### Markdown

Create `.markdownlint.json`:

```json
{
  "extends": "@lint-configs/markdownlint-config"
}
```

### Python

Point your `pyproject.toml` at the shared Ruff config:

```toml
[tool.ruff]
extend = "python/ruff.toml"
```

## Configuration

| Feature                 | TypeScript        | Python      | Markdown  |
| ----------------------- | ----------------- | ----------- | --------- |
| Line length             | Configurable      | 100         | 120       |
| Type checking           | TypeScript strict | MyPy strict | N/A       |
| Security                | XSS, eval, regex  | Bandit (S)  | N/A       |
| Complexity              | Max 10            | Max 10      | N/A       |
| Dead code detection     | Yes               | Yes         | N/A       |
| Import sorting          | Yes               | Yes         | N/A       |
| Code formatting         | Prettier          | Black       | Prettier  |
| Documentation standards | N/A               | N/A         | 40+ rules |

> "If it's worth enabling, it's worth enforcing everywhere."

The guiding philosophy: enforce strict quality standards for AI-generated code, only disable rules that conflict with formatters, and keep every language's strictness in lockstep.

## How it works

The repo is a monorepo of independently versioned, independently published config packages:

```text
lint-configs/
├── typescript/   @lint-configs/eslint-config   (npm, 220+ ESLint rules)
├── markdown/     @lint-configs/markdownlint-config (npm, 40+ rules)
└── python/       Ruff / MyPy / Black / Pylint TOML configs (PyPI)
```

The `typescript/` and `markdown/` packages are npm workspaces; `python/` builds a distributable package via `python -m build`. Releases are automated with release-please, and CI verifies that every package installs cleanly before publish.

## Development

```bash
# Clone
git clone https://github.com/cajias/lint-configs.git
cd lint-configs

# Install workspace dev dependencies
npm install

# Lint Markdown across the repo
npm run lint

# Auto-fix lint issues
npm run lint:fix

# Check / apply formatting
npm run format:check
npm run format
```

Python configs live under `python/`; lint them locally with `ruff check .`, `black --check .`, and `mypy .` from that directory — the same commands CI runs.

Config changes ripple out to every project consuming these packages, so please open an issue with concrete false-positive / conflict examples and get consensus before submitting a PR. See [CONTRIBUTING.md](./CONTRIBUTING.md) for details.

## License

Licensed under the [MIT License](./LICENSE).
