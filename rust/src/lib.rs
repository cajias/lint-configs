//! Strict Clippy and Rust linting configurations.
//!
//! This crate distributes opinionated, battle-tested linting configurations for
//! Rust projects. Embed them via the string constants below, or run the bundled
//! `cajias-lint-configs` CLI to scaffold both files in your project root.
//!
//! # Quick start
//!
//! ```bash
//! cargo add --dev cajias-lint-configs
//! cargo run --bin cajias-lint-configs -- init
//! ```
//!
//! Or copy the constants directly:
//!
//! ```rust
//! use cajias_lint_configs::{CLIPPY_TOML, DENY_TOML};
//!
//! println!("{}", CLIPPY_TOML);
//! println!("{}", DENY_TOML);
//! ```

/// Canonical `clippy.toml` configuration.
///
/// Enables the strictest Clippy settings: cognitive-complexity cap of 10,
/// maximum function argument count of 5, and disallows common footguns.
pub const CLIPPY_TOML: &str = include_str!("../clippy.toml");

/// Canonical `deny.toml` configuration for [`cargo-deny`](https://embarkstudios.github.io/cargo-deny/).
///
/// Denies advisories, restricts licence categories, and bans known-bad crates.
pub const DENY_TOML: &str = include_str!("../deny.toml");
