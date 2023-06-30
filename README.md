# QR Code Generator
## Installation
In your favorite python env, install qrcode: `pip install qrcode`.

## Usage

General command: `python qrcodegen.py`.

Options:
- -l: Type of logo: github, twitter, paper, None
- -t: Text/url to encode
- -o: Output filename

```bash
# GitHub
python qrcodegen.py -l github -t https://github.com/automl/SAWEI -o qrcode_github.png

# Paper
python qrcodegen.py -l paper -t https://arxiv.org/abs/2306.04262 -o qrcode_paper.png

# AutoML Twitter
python qrcodegen.py -l twitter -t https://twitter.com/AutoML_org -o qrcode_twitter_automl.png

# Personal
python qrcodegen.py -l twitter -t https://twitter.com/CBen00 -o qrcode_twitter_personal.png
```