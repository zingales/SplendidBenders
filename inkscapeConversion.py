import subprocess

__INKSCAPE_PATH = '/Applications/Inkscape.app/Contents/MacOS/inkscape'

def svg_to_png(svg_file, output_file):
    subprocess.run([__INKSCAPE_PATH, svg_file, "--export-filename", output_file])

svg_to_png("input.svg", "output.png")