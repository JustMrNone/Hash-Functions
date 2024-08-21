# Rainbow Hashing Script

## Overview

The `CreateRainbow.py` script hashes each line of a given text file using various hashing algorithms. The hashed values are then saved in a CSV file alongside the original text.

The `Reverse.py` script reads a list of hash values from a file and compares them against a dictionary of key-value pairs from a CSV file. It then outputs the corresponding keys for matched hash values to a new CSV file. If a hash value is not found, it logs "Nothing found" for that value.

## Features

**CreateRainbow.py:**

- Supports multiple hashing algorithms (e.g., `sha256`, `md5`).
- Outputs hashed values to a CSV file.
- Lists available hashing algorithms on request.

**Reverse.py:**

- Reads hash values from a text file.
- Reads key-value pairs from a CSV file.
- Compares the hash values to the dictionary values.
- Outputs matched key-value pairs to a new CSV file.
- Logs "Nothing found" for unmatched hash values.

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

**To compare hash values with a dictionary and output the results to a CSV file:**

```sh
   python Reverse.py <hash_values_file> <dictionary_csv_file>
```

- <hash_values_file>: The text file containing the hash values you want to compare.
- <dictionary_csv_file>: The CSV file containing key-value pairs where values are expected to match the hash values.

### For Example and in this case

To compare hash values stored in hashvalues.txt with the dictionary in output.csv, and save the matched results in a new CSV file:

```sh
   python Reverse.py hashvalues.txt output.csv
```

