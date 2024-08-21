# Rainbow Hashing Script

## Overview

The `CreateRainbow.py` script hashes each line of a given text file using various hashing algorithms. The hashed values are then saved in a CSV file alongside the original text.

## Features

- Supports multiple hashing algorithms (e.g., `sha256`, `md5`).
- Outputs hashed values to a CSV file.
- Lists available hashing algorithms on request.

## Requirements

- Python 3.x
- `hashlib` (part of Python standard library)
- `csv` (part of Python standard library)

## Usage

### Command-Line Usage

**To list available hash algorithms:**

```sh
   python CreateRainbow.py print
```

**To hash a file and save the results to a CSV file:**
To hash file contents using a specific hash algorithm:

```sh
python CreateRainbow.py <filename> <hash_algorithm>
```
