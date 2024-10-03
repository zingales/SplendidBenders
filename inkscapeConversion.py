import subprocess

from ResourceCardGenerator import generateResourceCad, ResourceType

__INKSCAPE_PATH = '/Applications/Inkscape.app/Contents/MacOS/inkscape'

def svg_to_png(svg_file, output_file):
    subprocess.run([__INKSCAPE_PATH, svg_file, "--export-filename", output_file])
    print(f'Finished Converting {svg_file} to {output_file}')



oneTrayPath = 'output/OneTray.svg'
requirements = {ResourceType.Air:7}
generateResourceCad(oneTrayPath, requirements, 0, ResourceType.Fire, image='')

twoTrayPath = 'output/TwoTray.svg'
requirements = {ResourceType.Air:7, ResourceType.Water:3}
generateResourceCad(twoTrayPath, requirements, 1, ResourceType.Lotus, image='')

threeTrayPath = 'output/ThreeTray.svg'
requirements = {ResourceType.Air:1, ResourceType.Water:4, ResourceType.Earth:2}
generateResourceCad(threeTrayPath, requirements, 3, ResourceType.Air, image='')

fourTrayPath_2 = 'output/FourTray_2.svg'
requirements = {ResourceType.Water:5, ResourceType.Lotus:3, ResourceType.Earth:3, ResourceType.Air:3}
generateResourceCad(fourTrayPath_2, requirements, 2, ResourceType.Earth, image='')

fourTrayPath_4 = 'output/FourTray_4.svg'
requirements = {ResourceType.Earth:5, ResourceType.Lotus:3, ResourceType.Water:3, ResourceType.Air:3}
generateResourceCad(fourTrayPath_4, requirements, 4, ResourceType.Water, image='')

fourTrayPath_5 = 'output/FourTray_5.svg'
requirements = {ResourceType.Fire:5, ResourceType.Water:3, ResourceType.Earth:3, ResourceType.Air:3}
generateResourceCad(fourTrayPath_5, requirements, 5, ResourceType.Fire, image='')



paths = [
    oneTrayPath,
    twoTrayPath,
    threeTrayPath,
    fourTrayPath_2,
    fourTrayPath_4,
    fourTrayPath_5
]

for path in paths:
    svg_to_png(path, path.replace(".svg", '.png'))