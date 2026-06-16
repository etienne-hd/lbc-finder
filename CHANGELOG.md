## 1.1.3

### Changed

- Bump [lbc](https://github.com/etienne-hd/lbc) version from `1.1.3` to `1.1.4`.

## 1.1.2

### Added

- Added `uv` project metadata and lockfile

### Changed

- Migrated the container build process to `uv` and removed the legacy `requirements.txt`
- Reformatted the codebase with `ruff`

## 1.1.1

### Added

- Automatic installation of Python libraries from `config/requirements.txt` when running the Docker container.

### Changed

- Moved `config.py` to `config/__init__.py` to allow multiple configuration files in Docker.

### Updated

- Discord example updated to reflect the new configuration structure.

## 1.1.0

### Added

- Docker support 🎉

### Changed

- Project source code moved to `/lbc-finder`
- `id.json` and `logs` are now stored in `/data` for persistent storage (useful for Docker)

## 1.0.1

### Added

- Retry-based error handling for ad handler calls (#3)
- `contains` method in `ID` class (#3)

### Changed

- Bumped [lbc](https://github.com/etienne-hd/lbc) to 1.1.2

## 1.0.0

- Initial release
