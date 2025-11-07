#!/bin/bash
# Build script for exploring-jit.tex with artifacts in ./build
# Uses latexmk which respects the .latexmkrc configuration

latexmk exploring-jit.tex
cp build/exploring-jit.pdf exploring-jit.pdf

echo "✓ Build complete. PDF: exploring-jit.pdf"
