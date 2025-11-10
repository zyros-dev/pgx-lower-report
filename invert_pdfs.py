#!/usr/bin/env python3
"""
Script to invert colors of PDF documents for dark mode viewing.
Converts PDFs to images, inverts colors, and converts back to PDF.
"""

import os
import sys
from pathlib import Path
from PIL import Image, ImageOps
from pdf2image import convert_from_path
from io import BytesIO
from PyPDF2 import PdfWriter, PdfReader
import img2pdf

def invert_pdf(input_path, output_path):
    """
    Invert colors of a PDF file.

    Args:
        input_path: Path to the input PDF
        output_path: Path to save the inverted PDF
    """
    try:
        print(f"Processing: {input_path}")

        # Convert PDF to images
        print("  Converting PDF to images...")
        images = convert_from_path(input_path, dpi=300)

        # Invert colors for each image
        print(f"  Inverting colors for {len(images)} page(s)...")
        inverted_images = []
        for i, image in enumerate(images):
            # Convert to RGB if needed
            if image.mode != 'RGB':
                image = image.convert('RGB')

            # Invert colors
            inverted = ImageOps.invert(image)
            inverted_images.append(inverted)

        # Convert images back to PDF
        print("  Converting images back to PDF...")
        image_list = []
        for img in inverted_images:
            # Save to bytes
            img_bytes = BytesIO()
            img.save(img_bytes, format='PNG')
            img_bytes.seek(0)
            image_list.append(img_bytes.getvalue())

        # Create PDF from images
        pdf_bytes = img2pdf.convert(image_list)

        # Write to file
        with open(output_path, 'wb') as f:
            f.write(pdf_bytes)

        print(f"  ✓ Saved to: {output_path}")
        return True

    except Exception as e:
        print(f"  ✗ Error: {str(e)}")
        return False

def main():
    """Main function to process all PDFs in samples_theses directory."""
    source_dir = Path('./samples_theses')
    output_dir = Path('./dark_samples_theses')

    # Verify source directory exists
    if not source_dir.exists():
        print(f"Error: {source_dir} directory not found!")
        sys.exit(1)

    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)

    # Find all PDF files
    pdf_files = list(source_dir.glob('*.pdf'))

    if not pdf_files:
        print("No PDF files found in samples_theses directory")
        sys.exit(1)

    print(f"Found {len(pdf_files)} PDF file(s) to process\n")

    successful = 0
    failed = 0

    # Process each PDF
    for pdf_file in pdf_files:
        output_path = output_dir / pdf_file.name
        if invert_pdf(pdf_file, output_path):
            successful += 1
        else:
            failed += 1

    # Summary
    print(f"\n{'='*50}")
    print(f"Processing complete!")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Output directory: {output_dir.absolute()}")

if __name__ == '__main__':
    main()
