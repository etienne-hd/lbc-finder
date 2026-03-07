## v1.1.1

### Added
- Automatic installation of Python libraries from `config/requirements.txt` when running the Docker container.

### Changed
- Moved `config.py` to `config/__init__.py` to allow multiple configuration files in Docker.

### Updated
- Discord example updated to reflect the new configuration structure.

## v1.1.0

### Added
- Docker support 🎉

### Changed
- Project source code moved to `/lbc-finder`
- `id.json` and `logs` are now stored in `/data` for persistent storage (useful for Docker)

## v1.0.1

### Added
- Retry-based error handling for ad handler calls (#3)
- `contains` method in `ID` class (#3)

### Changed
- Bumped [lbc](https://github.com/etienne-hd/lbc) to v1.1.2

## v1.0.0
- Initial release