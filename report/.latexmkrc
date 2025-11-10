# Latexmk configuration for pgx-lower-thesis.tex
# Redirect all build artifacts to ./build directory

$out_dir = 'build';
$aux_dir = 'build';

# Use pdflatex
$pdf_mode = 1;
$postscript_mode = 0;
$dvi_mode = 0;

# Set TEXINPUTS to find unswthesis.cls in 04_metadata
$ENV{TEXINPUTS} = './04_metadata:';
