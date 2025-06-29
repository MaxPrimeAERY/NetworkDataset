# NetworkDataset

This repository contains utilities for scanning network devices and storing the
results in JSON or CSV format. The included script `collect_network_info.py`
uses ARP requests to discover devices in a given network range.

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the scanner for a specific network range:
   ```bash
   python scripts/collect_network_info.py --range 192.168.1.0/24 --output devices.json
   ```
   The output file can be `.json` or `.csv`.

## Tests

Run unit tests with:

```bash
pytest
```
