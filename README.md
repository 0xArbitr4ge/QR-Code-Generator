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

## 📝 Examples

### Generate a QR code for a website:
```bash
python main.py "https://github.com/"
```

### Generate a QR code with custom size and border:
```bash
python main.py "Hello, World!" -s 15 -b 2
```
  
### Generate a QR code with high error correction:
```bash
python main.py "Important information" -e H
```
  
### Generate a QR code with custom colors:
```bash
python main.py "Colorful QR" --fg blue --bg yellow
```
  
### Save to a specific file:
```bash
python main.py "Custom filename" -o my_qrcode.png
```
  
## 💡 Tips

- Higher error correction levels (Q, H) make QR codes more reliable but also larger
- For scanning from screens, the default error correction (M) is usually sufficient
- For printed QR codes that might get damaged, use higher error correction (H)
- Use larger sizes (-s 20 or higher) for printing QR codes
- QR codes work best with high contrast (black and white), but you can experiment with colors

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
