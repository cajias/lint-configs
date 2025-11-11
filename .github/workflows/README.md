# GitHub Actions Workflows

## Publish Workflow

The `publish.yml` workflow automatically builds and publishes the Python package when you create a new version tag.

### How It Works

1. **Trigger**: Runs when you push a tag matching `v*` (e.g., `v1.0.0`, `v1.2.3`)
2. **Build**: Builds the Python package from the `python/` directory
3. **Publish**:
   - Uploads to PyPI (if `PYPI_API_TOKEN` secret is configured)
   - Falls back to TestPyPI (if `TEST_PYPI_API_TOKEN` is configured)
4. **Release**: Creates a GitHub release with the built package files

### Setup Instructions

#### 1. Create PyPI API Token

**For public PyPI (recommended):**

1. Go to https://pypi.org/manage/account/token/
2. Create a new API token
3. Scope: "Entire account" or specific to `cajias-linter-configs`
4. Copy the token (starts with `pypi-...`)

**For TestPyPI (testing):**

1. Go to https://test.pypi.org/manage/account/token/
2. Create a new API token
3. Copy the token

#### 2. Add Secrets to GitHub Repository

1. Go to your repository on GitHub
2. Navigate to: **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add these secrets:

| Secret Name | Value | Required |
|-------------|-------|----------|
| `PYPI_API_TOKEN` | Your PyPI token | For publishing to PyPI |
| `TEST_PYPI_API_TOKEN` | Your TestPyPI token | For testing (optional) |

#### 3. Publishing a New Version

```bash
# 1. Update version in python/pyproject.toml and python/lint_configs/__init__.py
# Edit version = "1.0.1"

# 2. Commit the version bump
git add python/pyproject.toml python/lint_configs/__init__.py
git commit -m "Bump version to 1.0.1"

# 3. Create and push a tag
git tag v1.0.1
git push origin v1.0.1

# 4. GitHub Actions will automatically:
#    - Build the package
#    - Publish to PyPI
#    - Create a GitHub Release
```

### Manual Triggering

You can also trigger the workflow manually:

1. Go to **Actions** tab in GitHub
2. Select **Publish Python Package** workflow
3. Click **Run workflow**
4. Choose the branch
5. Click **Run workflow**

This will build and check the package without publishing (useful for testing).

### Workflow Features

- ✅ **Automated builds** on version tags
- ✅ **Package validation** with `twine check`
- ✅ **PyPI publishing** (optional, requires token)
- ✅ **TestPyPI support** for testing
- ✅ **GitHub Releases** with package files attached
- ✅ **Installation instructions** in release notes
- ✅ **Manual triggering** for testing

### Troubleshooting

**"PyPI upload failed" warning:**
- Add `PYPI_API_TOKEN` secret to your repository
- Make sure the token has correct permissions

**"TestPyPI upload skipped" warning:**
- This is normal if you only want to publish to PyPI
- Add `TEST_PYPI_API_TOKEN` if you want to test on TestPyPI first

**Package build fails:**
- Check that `python/pyproject.toml` is valid
- Ensure version number is updated
- Verify all files are included in MANIFEST.in

### Versioning

This project follows [Semantic Versioning](https://semver.org/):
- `v1.0.0` - Major release (breaking changes)
- `v1.1.0` - Minor release (new features, backwards compatible)
- `v1.0.1` - Patch release (bug fixes)

### Example Release Process

```bash
# Update version to 1.1.0
vim python/pyproject.toml  # Change version = "1.1.0"
vim python/lint_configs/__init__.py  # Change __version__ = "1.1.0"

# Commit
git add .
git commit -m "Release v1.1.0: Add TypeScript support"

# Tag and push
git tag -a v1.1.0 -m "Release v1.1.0"
git push origin main
git push origin v1.1.0

# GitHub Actions automatically:
# - Builds package
# - Publishes to PyPI
# - Creates GitHub Release
```

Users can then install with:
```bash
pip install cajias-linter-configs==1.1.0
```
