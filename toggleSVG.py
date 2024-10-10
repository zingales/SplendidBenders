
from enum import Enum
import xml.etree.ElementTree as ET
import logging


# White,Blue,Green,Red,Black

ResourceType = Enum('Type', ['Lotus', 'Water', 'Earth', 'Fire', 'Air'])

class Toggler:

    SVG_XML_HREF_TAG = '{http://www.w3.org/1999/xlink}href'

    def __init__(self) -> None:
        self.onIds = set()
        self.offIds = set()

        self.updateStyle = dict()

        self.imageHrefUpdate = {
            'stone-texture.jpg':r"file:///D:/Dropbox/Eppe's%20Stuff/Avatar%20Splenor%20Assets/Inkscape_SVG/stone-texture.jpg", 
            'goldOrbDB.png': r"file:///D:/Dropbox/Eppe's%20Stuff/Avatar%20Splenor%20Assets/Inkscape_SVG/goldOrbDB.png", 
            'wood.jpg': r"file:///D:/Dropbox/Eppe's%20Stuff/Avatar%20Splenor%20Assets/Inkscape_SVG/wood.jpg",
            'dark-wood.png': r"file:///D:/Dropbox/Eppe's%20Stuff/Avatar%20Splenor%20Assets/Inkscape_SVG/dark-wood.png",
            }

        self.updateImageHref = None


    def execute(self, input_svg, output_svg):
        
        # Parse the SVG file
        tree = ET.parse(input_svg)
        root = tree.getroot()

        # Find the SVG namespace
        namespaces = {'svg': 'http://www.w3.org/2000/svg'}

        styleUpdateIds = list(self.updateStyle.keys())
        # Iterate over all <g> elements
        for group in root.findall('.//svg:g', namespaces):
            id = group.get("id")
            if id in self.onIds:
                updatedStyle = group.get('style', '').replace('display:inline;', '').replace('display:none;', '').replace('display:none', '').replace('display:inline', '')
                group.set('style', updatedStyle)
                group.set('display', 'inline')
            elif id in self.offIds:
                updatedStyle = group.get('style', '').replace('display:inline;', '').replace('display:none;', '').replace('display:none', '').replace('display:inline', '')
                group.set('style', updatedStyle)
                group.set('display', 'none')
            elif id in styleUpdateIds:
                originalStyle = group.get('style', '')
                group.set('style', f'{self.updateStyle[id]};{originalStyle}')

   

        for image in root.findall('.//svg:image', namespaces):
            imageHref = image.get(self.SVG_XML_HREF_TAG)
            if imageHref in self.imageHrefUpdate:
                image.set(self.SVG_XML_HREF_TAG, self.imageHrefUpdate[imageHref])
            if self.updateImageHref is not None:
                if image.get('id') == 'AvatarScreenShot':
                    original_image_path = image.get(self.SVG_XML_HREF_TAG)
                    image.set(self.SVG_XML_HREF_TAG, str(self.updateImageHref))
                    # print(image.get('{http://www.w3.org/1999/xlink}href'))
                    print(f"updated image path {original_image_path} to {self.updateImageHref}")

        
            
        # Write the modified SVG to a new file
        tree.write(output_svg)

class VIPCardRequirement:
    TypeToFillColor = {
        ResourceType.Air: "#e9ab00",
        ResourceType.Lotus: "#fff9ea",
        ResourceType.Water: "#e9ab00",
        ResourceType.Earth: "#2c7106",
        ResourceType.Fire: "#d4160e",
    }

    def __init__(self, id, cards, fourthCardId, num3Id, num4Id):
        self.id = id
        self.cards = cards
        self.fourthCardId = fourthCardId
        self.num3Id = num3Id
        self.num4Id = num4Id
        self.onType = None
        self.isThree = True

    def clone(self):
        slot = VIPCardRequirement(self.id, self.cards, self.fourthCardId, self.num3Id, self.num4Id)
        slot.onType = self.onType
        return slot
    
    def setTypeAndCount(self, type, isThree):
        self.onType = type
        self.isThree = isThree

    def turnOff(self):
        self.onType = None

    def addToToggler(self, toggler):
        if self.onType:
            toggler.updateStyle[self.cards] = f"fill: {self.TypeToFillColor[self.onType]}"
            if self.isThree:
                toggler.onIds.add(self.num3Id)
                toggler.offIds.add(self.num4Id)
                toggler.offIds.add(self.fourthCardId)
            else:
                toggler.offIds.add(self.num3Id)
                toggler.onIds.add(self.num4Id)
                toggler.onIds.add(self.fourthCardId)
        else:
            toggler.offIds.add(self.id)
        



    

class RequirementsSlot:
    def __init__(self, id, air_id, lotus_id, water_id, earth_id, fire_id):
        self.id = id
        self.air_id = air_id
        self.lotus_id = lotus_id
        self.water_id = water_id
        self.earth_id = earth_id
        self.fire_id = fire_id
        self.onType = None

    def clone(self):
        slot = RequirementsSlot(self.id, self.air_id, self.lotus_id, self.water_id, self.earth_id, self.fire_id)
        slot.onType = self.onType
        return slot

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


if __name__ == "__main__":
    from pathlib import Path
    assetsPath = Path(r"D:\Dropbox\Eppe's Stuff\Avatar Splenor Assets")
    resourceCardTemplateSvg = assetsPath/ "Inkscape_SVG" / "AllCards_v3.svg"

    input_svg = resourceCardTemplateSvg
            # Parse the SVG file
    tree = ET.parse(input_svg)
    root = tree.getroot()

    # Find the SVG namespace
    namespaces = {'svg': 'http://www.w3.org/2000/svg'}
    for image in root.findall('.//svg:image', namespaces):
        if image.get('id') == 'AvatarScreenShot':
            print(image)
            original_image_path = image.get('{http://www.w3.org/1999/xlink}href')
            print(original_image_path)
            image.set('{http://www.w3.org/1999/xlink}href', r'a_new_path')
            print(image.get('{http://www.w3.org/1999/xlink}href'))
    pass