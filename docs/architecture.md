# QFL Architecture

Status: Phase 0 (planned architecture, nothing implemented yet)

## Style

Modular monolith: one repository, one application, separate internal modules. Modules are logical boundaries, not separate processes or services.

## Domains

- **Data**: ingestion, validation, normalization, storage
- **Research**: analytics, features, experiments
- **Simulation**: backtesting, paper trading
- **Risk**: limits and controls
- **Execution**: orders and broker adapters (much later)
- **Portfolio**: positions and performance
- **Interface**: CLI first, other interfaces later

Only Data and the CLI are planned for the first phases.

## Planned data flow

```text
CoinGecko API
     |
Adapter (external format -> QFL internal model)
     |
Validation
     |
Normalization
     |
SQLite storage
     |
Query interface
     |
CLI
```

Later phases add analytics, backtesting, risk checks, and paper trading on top of stored data.

## External systems

- CoinGecko API (rate limits and data granularity apply)

## Assumptions

- Single user, running locally
- Python and SQLite to start
- All timestamps stored in UTC

## Security assumptions

- Secrets (API keys, tokens) never go in the repository, logs, or screenshots
- Secrets live in a local `.env` file, which is git-ignored
- Paper trading only; no real money until much later and only after validation

## Known limitations

- Nothing is implemented yet
- SQLite allows one writer at a time and may need replacing later
- Free API tiers limit request rate and data history
- Not designed for high-frequency trading