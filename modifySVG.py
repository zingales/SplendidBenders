import xml.etree.ElementTree as ET

def toggle_group_visibility(svg_file, output_file, group_id=None):
    # Parse the SVG file
    tree = ET.parse(svg_file)
    root = tree.getroot()

    # Find the SVG namespace
    namespaces = {'svg': 'http://www.w3.org/2000/svg'}

    # Iterate over all <g> elements
    for group in root.findall('.//svg:g', namespaces):
        if group_id is None or group.get('id') == group_id:
            # Get the current 'visibility' or 'display' attribute
            visibility = group.get('visibility')
            display = group.get('display')

            # Toggle visibility or display attribute
            if visibility == 'hidden' or display == 'none':
                group.set('visibility', 'visible')
                group.set('display', 'inline')
            else:
                group.set('visibility', 'hidden')
                group.set('display', 'none')

    # Write the modified SVG to a new file
    tree.write(output_file)

# Example usage:
svg_file = 'input.svg'   # Path to the input SVG file
output_file = 'output.svg'  # Path to the output SVG file with toggled visibility
group_id = 'group1'  # Optional: specific group id to toggle, or None to toggle all groups

toggle_group_visibility(svg_file, output_file, group_id)
