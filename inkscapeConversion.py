import subprocess
from ResourceCardGenerator import generateResourceCad, ResourceType

__INKSCAPE_PATH = '/Applications/Inkscape.app/Contents/MacOS/inkscape'

def svg_to_png(svg_file, output_file):
    subprocess.run([__INKSCAPE_PATH, svg_file, "--export-filename", output_file])




oneTrayPath = 'output/OneTray.svg'
requirements = {ResourceType.Air:7}
generateResourceCad(oneTrayPath, requirements, 0, ResourceType.Fire, image='')

twoTrayPath = 'output/TwoTray.svg'
requirements = {ResourceType.Air:7, ResourceType.Water:3}
generateResourceCad(twoTrayPath, requirements, 1, ResourceType.Lotus, image='')

threeTrayPath = 'output/ThreeTray.svg'
requirements = {ResourceType.Air:1, ResourceType.Water:4, ResourceType.Earth:2}
generateResourceCad(twoTrayPath, requirements, 3, ResourceType.Air, image='')

fourTrayPath = 'output/FourTray.svg'
requirements = {ResourceType.Water:5, ResourceType.Lotus:3, ResourceType.Earth:3, ResourceType.Air:3}
generateResourceCad(fourTrayPath, requirements, 2, ResourceType.Earth, image='')



paths = [
    oneTrayPath,
    twoTrayPath,
    threeTrayPath,
    fourTrayPath
]

for path in paths:
    svg_to_png(path, path.replace(".svg", '.png'))