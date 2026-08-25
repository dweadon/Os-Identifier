# OS Identifier

A lightweight Python library for identifying the operating system and Linux distribution of the current machine.

## Features

- Detects operating system (Linux, Windows, macOS)
- Identifies Linux distribution name and version
- Raises clear exceptions for unsupported or unknown systems

## Usage

```python
from main import Os
run = Os()

try:
  run.send_back()
except AssertionError as y:
  print(y)
```

## Example Output
Os: Debian GNU/Linux, Version: 12

## License

MIT
