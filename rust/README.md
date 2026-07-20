<!-- markdownlint-disable MD013 -->

# cajias-lint-configs (Rust)

> Strict Clippy and Rust linting configurations — the same uncompromising bar as the rest of the `lint-configs` family.

[![Crates.io](https://img.shields.io/crates/v/cajias-lint-configs.svg)](https://crates.io/crates/cajias-lint-configs)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../LICENSE)

## Installation

Add as a dev-dependency:

```toml
[dev-dependencies]
cajias-lint-configs = "0.1"
```

Or use the CLI directly with `cargo run`:

```bash
cargo install cajias-lint-configs
cajias-lint-configs init
```

## Usage

### Scaffold configuration files

```bash
cajias-lint-configs init
```

This writes `clippy.toml` and `deny.toml` into the current directory.

### Copy the `[lints]` section

Add the following to your `Cargo.toml` to enable the recommended lint profile:

```toml
[lints.rust]
unsafe_code = "forbid"

[lints.clippy]
pedantic = "warn"
nursery = "warn"
unwrap_used = "warn"
expect_used = "warn"
panic = "warn"
todo = "warn"
```

### Use constants in build scripts

```rust
use cajias_lint_configs::{CLIPPY_TOML, DENY_TOML};

// Write configs programmatically in a build.rs or test helper
std::fs::write("clippy.toml", CLIPPY_TOML).unwrap();
std::fs::write("deny.toml", DENY_TOML).unwrap();
```

## Configuration files

| File | Tool | Description |
|------|------|-------------|
| `clippy.toml` | `cargo clippy` | Complexity cap (10), max args (5), and footgun blacklist |
| `deny.toml` | `cargo deny` | Advisory checks, licence allow-list, duplicate-version detection |

## Rules philosophy

| Concern | Setting |
|-|-|
| Unsafe code | `forbid` |
| Clippy pedantic | `warn` (treat as errors in CI with `-- -D warnings`) |
| Clippy nursery | `warn` |
| Unwrap / expect / panic | `warn` |
| Cognitive complexity | ≤ 10 per function |
| Function arguments | ≤ 5 |
| Security advisories | `deny` |
| Yanked crates | `deny` |

## CI integration

```yaml
- name: Clippy
  run: cargo clippy --all-targets --all-features -- -D warnings

- name: cargo-deny
  uses: EmbarkStudios/cargo-deny-action@v2
```

## Publishing

Releases are automated via release-please and published to [crates.io](https://crates.io/crates/cajias-lint-configs) when a `cajias-lint-configs-v*` tag is pushed.

## License

[MIT](../LICENSE)
