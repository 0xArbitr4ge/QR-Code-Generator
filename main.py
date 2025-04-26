#!/usr/bin/env python3

import argparse
import os
import qrcode
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H

def generate_qr_code(data, output_file, size=10, border=4, error_correction='M', 
                    fg_color='black', bg_color='white'):
    """Generate a QR code and save it to a file"""
    
    # Set error correction level
    error_correction_levels = {
        'L': ERROR_CORRECT_L,  # About 7% error correction capability
        'M': ERROR_CORRECT_M,  # About 15% error correction capability
        'Q': ERROR_CORRECT_Q,  # About 25% error correction capability
        'H': ERROR_CORRECT_H   # About 30% error correction capability
    }
    
    error_level = error_correction_levels.get(error_correction.upper(), ERROR_CORRECT_M)
    
    # Create QR code instance
    qr = qrcode.QRCode(
        version=None,  # Will auto-determine size
        error_correction=error_level,
        box_size=size,
        border=border
    )
    
    # Add data
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create image
    img = qr.make_image(fill_color=fg_color, back_color=bg_color)
    
    # Save image
    img.save(output_file)
    
    return output_file

def get_output_file(data, output=None):
    """Determine output filename if not specified"""
    if output:
        return output
    
    # Create a filename from the data (limited length)
    max_filename_len = 20
    filename = "".join(c if c.isalnum() else "_" for c in data)
    if len(filename) > max_filename_len:
        filename = filename[:max_filename_len]
    
    return f"qrcode_{filename}.png"

def main():
    parser = argparse.ArgumentParser(description="Generate QR codes from text or URLs")
    
    # Required argument
    parser.add_argument("data", help="Text or URL to encode in the QR code")
    
    # Optional arguments
    parser.add_argument("-o", "--output", help="Output file (PNG format)")
    parser.add_argument("-s", "--size", type=int, default=10, help="Size of each box in pixels (default: 10)")
    parser.add_argument("-b", "--border", type=int, default=4, help="Border size in boxes (default: 4)")
    parser.add_argument("-e", "--error", choices=["L", "M", "Q", "H"], default="M", 
                        help="Error correction level: L (7%%), M (15%%), Q (25%%), H (30%%) (default: M)")
    parser.add_argument("--fg", default="black", help="Foreground color (default: black)")
    parser.add_argument("--bg", default="white", help="Background color (default: white)")
    
    args = parser.parse_args()
    
    # Determine output file
    output_file = get_output_file(args.data, args.output)
    
    # Generate QR code
    generated_file = generate_qr_code(
        args.data, 
        output_file, 
        args.size, 
        args.border, 
        args.error, 
        args.fg, 
        args.bg
    )
    
    print(f"QR code generated and saved to {generated_file}")

if __name__ == "__main__":
    main()
