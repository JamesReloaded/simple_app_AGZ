# Simple Integration Test - by AGZ

This is a Simple Integration for VGS Redact/Reveal features for data.

## Installation

Verify if all the required packages are installed on your system before running the app

* for python 2.x
```bash
pip install -r requirements.txt
```

* for python 3.x (in case multiple versions are installed)
```bash
pip3 install -r requirements.txt
```

## Configuration

After verifying all the requirements are met, create a .env file on the same location as the simple_app.py file. You will need the following:
* Vault ID
* Username
* Password
* Environment

The .env file should look like the following:
```bash
# environment variables for VGS connectivity
VAULT_ID = "<your_vault_id>"
VGS_ENV = "sandbox"
VGS_USER = "<your_username>"
VGS_PASS = "<your_password>"
```

## Usage

```bash
py simple_app.py
```