# yjpath

A CLI tool to extract JSONPath from YAML files.

## Installation

### Install with pip

```sh
pip install yjpath
```

## Usage

### Example YAML (config.yaml)

```yaml
database:
  user: admin
  password: secret
server:
  host: localhost
  port: 8080
```

### Basic Usage

```console
$ yjpath config.yaml
.database.user
.database.password
.server.host
.server.port
```

### Options

| Option    | Description                                                  |
| --------- | ------------------------------------------------------------ |
| `--dot`   | Displays output in dot-separated format (default)            |
| `--slash` | Displays output in slash-separated format (`/database/user`) |

#### Example

```console
$ yjpath config.yaml --slash
/database/user
/database/password
/server/host
/server/port
```
