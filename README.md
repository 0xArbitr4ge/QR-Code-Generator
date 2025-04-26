# 📱 QR Code Generator

A simple command-line tool to generate QR codes from text or URLs.

## ✨ Features

- 🔍 Generate QR codes from any text or URL
- 🔧 Customize QR code size and border
- 🔒 Adjust error correction level for better scanning reliability
- 🎨 Customize foreground and background colors
- 💾 Automatic file naming or custom output path

## 📋 Requirements

- Python 3.6 or higher
- qrcode library
- Pillow library

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/0xArbitr4ge/qr-code-generator.git
cd qr-code-generator
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Make the script executable (Unix/Linux/macOS):
```bash
chmod +x main.py
```

## 🔍 Usage

```bash
python main.py <data> [options]
```

## ⚙️ Options

- `data`: Text or URL to encode in the QR code (required)
- `-o, --output`: Output file (PNG format)
- `-s, --size`: Size of each box in pixels (default: 10)
- `-b, --border`: Border size in boxes (default: 4)
- `-e, --error`: Error correction level: L (7%), M (15%), Q (25%), H (30%) (default: M)
- `--fg`: Foreground color (default: black)
- `--bg`: Background color (default: white)

