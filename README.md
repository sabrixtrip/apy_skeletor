# Apy Skeletor

Apy Skeletor is a simple Python toolkit for interacting with REST APIs from the command line. It provides helper classes for making HTTP requests, handling user input, displaying messages, and parsing command-line arguments.

## Features

- **CLI Helper (`Cli`)**: 
  - Easy user prompts (including hidden input for secrets)
  - Informational, warning, and critical messages
  - Section and item formatting for menus
  - Pretty-printing JSON content
  - Simple verification and waiting utilities
  - Command-line argument parsing for user, password, and token

- **Network Helper (`Net`)**:
  - Simplified HTTP requests (GET, POST, PUT, DELETE)
  - Automatic token handling
  - JSON response parsing
  - Error handling and logging

- **UserAPI Example**:
  - Demonstrates how to use `Net` to interact with a RESTful user API (CRUD operations)

## Example Usage

```python
from apy.cli import Cli
from apy.net import Net

cli = Cli()
net = Net()

cli.item("Stations by TAG")
reply = net.get("http://all.api.radio-browser.info/json/stats")

if cli.verify("Getting stations...", reply['status'], 200):
    cli.content(reply['body'])
else:
    cli.warning(reply['log'])
```

## UserAPI Example

```python
from apy.cli import Cli
from apy.net import Net
from apy.cli import UserAPI

api = UserAPI("https://api.example.com", token="your_token_here")
user = api.get_user(1)
print(user)
```

## Requirements

- Python 3.6+
- Standard library only (no external dependencies)

## File Structure

- `apy/cli.py` - CLI helper and UserAPI example class
- `apy/net.py` - Network helper for HTTP requests
- `testdrive.py` - Example script using the helpers
  
