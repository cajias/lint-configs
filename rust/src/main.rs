//! CLI entry-point for `cajias-lint-configs`.
//!
//! Run `cajias-lint-configs init` to write `clippy.toml` and `deny.toml` into
//! the current directory.

use std::io::Write as _;
use std::path::Path;

use cajias_lint_configs::{CLIPPY_TOML, DENY_TOML};

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let subcommand = args.get(1).map(String::as_str);

    match subcommand {
        Some("init") => init(),
        Some("show-clippy") => println!("{CLIPPY_TOML}"),
        Some("show-deny") => println!("{DENY_TOML}"),
        _ => usage(),
    }
}

fn init() {
    write_file("clippy.toml", CLIPPY_TOML);
    write_file("deny.toml", DENY_TOML);
    println!("✅  Wrote clippy.toml and deny.toml");
    println!("Next: add the [lints] section from the README to your Cargo.toml");
}

fn write_file(name: &str, content: &str) {
    let path = Path::new(name);
    let mut file = match std::fs::OpenOptions::new()
        .write(true)
        .create_new(true)
        .open(path)
    {
        Ok(f) => f,
        Err(e) if e.kind() == std::io::ErrorKind::AlreadyExists => {
            eprintln!("⚠️  {name} already exists — skipping (delete it first to overwrite)");
            return;
        }
        Err(e) => {
            eprintln!("❌  Failed to write {name}: {e}");
            std::process::exit(1);
        }
    };
    if let Err(e) = file.write_all(content.as_bytes()) {
        eprintln!("❌  Failed to write {name}: {e}");
        std::process::exit(1);
    }
}

fn usage() {
    eprintln!(
        "cajias-lint-configs — scaffold strict Rust linting configurations\n\
        \n\
        USAGE:\n\
          cajias-lint-configs init          Write clippy.toml and deny.toml here\n\
          cajias-lint-configs show-clippy   Print clippy.toml to stdout\n\
          cajias-lint-configs show-deny     Print deny.toml to stdout"
    );
    std::process::exit(1);
}
