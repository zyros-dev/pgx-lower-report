#!/bin/bash
# Build script for pgx-lower-thesis.tex with artifacts in ./build
# Uses latexmk which respects the .latexmkrc configuration

latexmk pgx-lower-thesis.tex
cp build/pgx-lower-thesis.pdf pgx-lower-thesis.pdf

echo "✓ Build complete. PDF: pgx-lower-thesis.pdf"
