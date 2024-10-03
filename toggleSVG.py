
from enum import Enum
import xml.etree.ElementTree as ET


ResourceType = Enum('Type', ['Air', 'Lotus', 'Water', 'Earth','Fire'])

class Toggler:

    def __init__(self) -> None:
        self.onIds = set()
        self.offIds = set()


    def execute(self, input_svg, output_svg):
        
        # Parse the SVG file
        tree = ET.parse(input_svg)
        root = tree.getroot()

        # Find the SVG namespace
        namespaces = {'svg': 'http://www.w3.org/2000/svg'}

        # Iterate over all <g> elements
        for group in root.findall('.//svg:g', namespaces):
            if group.get('id') in self.onIds:
                updatedStyle = group.get('style', '').replace('display:inline;', '').replace('display:none;', '').replace('display:none', '').replace('display:inline', '')
                group.set('style', updatedStyle)
                group.set('display', 'inline')
            elif group.get('id') in self.offIds:
                updatedStyle = group.get('style', '').replace('display:inline;', '').replace('display:none;', '').replace('display:none', '').replace('display:inline', '')
                group.set('style', updatedStyle)
                group.set('display', 'none')
   
        # Write the modified SVG to a new file
        tree.write(output_svg)

class RequirementsSlot:
    def __init__(self, id, air_id, lotus_id, water_id, earth_id, fire_id):
        self.id = id
        self.air_id = air_id
        self.lotus_id = lotus_id
        self.water_id = water_id
        self.earth_id = earth_id
        self.fire_id = fire_id
        self.onType = None

    def setType(self, type):
        self.onType = type

    def turnOff(self):
        self.onType = None

    def addToToggler(self, toggler):
        if self.onType:
            toggler.onIds.add(self.id)
            requirementIds = {self.air_id, self.lotus_id, self.water_id, self.earth_id, self.fire_id}
            if self.onType == ResourceType.Air:
                toShow = self.air_id
            elif self.onType == ResourceType.Earth:
                toShow = self.earth_id
            elif self.onType == ResourceType.Lotus:
                toShow = self.lotus_id
            elif self.onType == ResourceType.Water:
                toShow = self.water_id
            elif self.onType == ResourceType.Fire:
                toShow = self.fire_id

            requirementIds.remove(toShow)
            toggler.onIds.add(toShow)
            toggler.offIds.update(requirementIds)

        else:
            toggler.offIds.add(self.id)
