# toolkit
Collection of useful Python command line tools

## Getting Started
These instructions will get you a copy of the project up and running on your local machine.

## Prerequisites
You'll need to have Python installed. Start by downloading and installing the latest version of [Python 3](https://www.python.org/downloads/).
> *Note: The `toolkit` scripts have not been tested with Python 2 and may not work without changing some things.*

## Installation
Download the latest version from GitHub using Git:
```
git clone https://github.com/zloether/toolkit.git
```
This will create a directory called *toolkit* and all the code will be in it.

Switch to the *toolkit* directory:
```
cd toolkit
```

Install the required packages:
```
pip install -r requirements.txt
```

## Usage
The scripts are all located in the `toolkit` directory

|Script name|Function|
|---|---|
|base64-encode.py|base64 encoder|
|base64-decode.py|base64 decoder|
|file_modified.py|shows the last modified date for input file(s)|
|hashes.py|computes various hash functions in input|
|network_info.py|returns useful network info for the current host|
|rotator.py|performs character rotation on input|