from toggleSVG import Toggler, RequirementsSlot, ResourceType
import logging

class OddTray:
    TrayId = 'g1763'

    NUMBERS_A = {
        7:'text75',
        6:'text77',
        5:'text20',
        4:'text78',
        3:'text18',
        2:'text11',
        1:'text9'
    }

    NUMBERS_B = {
        7:'text81',
        6:'text80',
        5:'text38',
        4:'text79',
        3:'text35',
        2:'text33',
        1:'text31'
    }

    NUMBERS_C = {
        7:'text85',
        6:'text84',
        5:'text67',
        4:'text83',
        3:'text65',
        2:'text47',
        1:'text46'
    }

    
    SLOT_A = RequirementsSlot(
        id='g1762', 
        numbers=NUMBERS_A,
        air_id='g66', 
        lotus_id='g64', 
        water_id='g62', 
        earth_id='g60', 
        fire_id='g1757'
    )

    SLOT_B = RequirementsSlot(
        id='g1755', 
        numbers=NUMBERS_B,
        air_id='g74', 
        lotus_id='g72', 
        water_id='g70', 
        earth_id='g68', 
        fire_id='g1751'
    )

    SLOT_C = RequirementsSlot(
        id='g1749', 
        numbers=NUMBERS_C, 
        air_id='g82', 
        lotus_id='g80', 
        water_id='g78', 
        earth_id='g76', 
        fire_id='g1745'
    )
        
    def __init__(self, requirements) -> None:
        
        self.slotA = self.SLOT_A.clone()
        self.slotB = self.SLOT_B.clone()
        self.slotC = self.SLOT_C.clone()

        if len(requirements) == 1:
            
            self.slotC.turnOff()
            self.slotA.turnOff()
            aType = list(requirements.keys())[0]
            self.slotB.setTypeAndCount(aType, requirements[aType])



        elif len(requirements) == 3:
            slotsToAssign = [self.slotC, self.slotB, self.slotA]
            for aType in ResourceType:
                if aType in requirements:
                    slot = slotsToAssign.pop()
                    slot.setTypeAndCount(aType, requirements[aType])
        else:
            raise ValueError("Odd Tray requirements can only be of length 1 or 3")    

    def addToToggler(self, toggler):
        toggler.onIds.add(self.TrayId)
        self.slotA.addToToggler(toggler)
        self.slotB.addToToggler(toggler)
        self.slotC.addToToggler(toggler)

class FourTray:
    TrayId = 'g170'


    NUMBERS_A = {
        5:'text222',
        3:'text215',
        2:'text213',
        1:'text154'
    }

    NUMBERS_B = {
        5:'text230',
        3:'text229',
        2:'text228',
        1:'text226'
    }

    NUMBERS_C = {
        5:'g316',
        3:'g315',
        2:'g313',
        1:'g312'
    }

    NUMBERS_D = {
        5:'g340',
        3:'g332',
        2:'g320',
        1:'g319'
    }

    SLOT_A = RequirementsSlot(
        id='g362', 
        numbers=NUMBERS_A,
        air_id='g24', 
        lotus_id='g26', 
        water_id='g361', 
        earth_id='g54', 
        fire_id='g53'
    )
    
    SLOT_B = RequirementsSlot(
        id='g357', 
        numbers=NUMBERS_B,
        air_id='g32', 
        lotus_id='g34', 
        water_id='g356', 
        earth_id='g30', 
        fire_id='g28'
    )
    
    SLOT_C = RequirementsSlot(
        id='g353', 
        numbers=NUMBERS_C,
        air_id='g42', 
        lotus_id='g44', 
        water_id='g307', 
        earth_id='g39', 
        fire_id='g36'
    )
    
    SLOT_D = RequirementsSlot(
        id='g367', 
        numbers=NUMBERS_D,
        air_id='g56', 
        lotus_id='g58', 
        water_id='g366', 
        earth_id='g54', 
        fire_id='g53'
    )

    def __init__(self, requirements) -> None:
        if len(requirements) != 4:
            raise ValueError("Four Tray requirements can only be of length four")
    
        self.slotA = self.SLOT_A.clone()
        self.slotB = self.SLOT_B.clone()
        self.slotC = self.SLOT_C.clone()
        self.slotD = self.SLOT_D.clone()

        values = list()
        slotsToAssign = [self.slotD, self.slotC, self.slotB, self.slotA]
        for aType in ResourceType:
            if aType in requirements:
                slot = slotsToAssign.pop()
                slot.setTypeAndCount(aType, requirements[aType])
                
       
    def addToToggler(self, toggler):
        self.slotA.addToToggler(toggler)
        self.slotB.addToToggler(toggler)
        self.slotC.addToToggler(toggler)
        self.slotD.addToToggler(toggler)

class TwoTray:
    TrayId = 'g1812'

    NUMBERS_A = {
        7:'text110',
        6:'text109',
        5:'text108',
        4:'text107',
        3:'text106',
        2:'text105',
        1:'text104'
    }

    NUMBERS_B = {
        7:'text93',
        6:'text92',
        5:'text91',
        4:'text90',
        3:'text89',
        2:'text88',
        1:'text87'
    }

    SLOT_A = RequirementsSlot(
        id='g1808', 
        numbers=NUMBERS_A,
        air_id='g6', 
        lotus_id='g9', 
        water_id='g1804', 
        earth_id='g4', 
        fire_id='g3'
    )

    SLOT_B = RequirementsSlot(
        id='g1802', 
        numbers=NUMBERS_B,
        air_id='g14', 
        lotus_id='g16', 
        water_id='g1798', 
        earth_id='g13', 
        fire_id='g10'
    )

    def __init__(self, requirements) -> None:
        if len(requirements) != 2:
            raise ValueError("Two Tray requirements can only be of length two")
        
        self.slotA = self.SLOT_A.clone()
        self.slotB = self.SLOT_B.clone()
    
        for aType in ResourceType:
            if aType in requirements:
                if self.slotA.onType is None:
                    self.slotA.setTypeAndCount(aType, requirements[aType])
                else:
                    self.slotB.setTypeAndCount(aType, requirements[aType])


    def addToToggler(self, toggler):
        toggler.onIds.add(self.TrayId)
        self.slotA.addToToggler(toggler)
        self.slotB.addToToggler(toggler)

class VictoryPoints:

    TopLeft = 'g503'
    BottomLeft = 'g507'
    BottomRight = 'g499'
    TopRight = 'g495'
    Center = 'g482'

    def __init__(self, count) -> None:
        self.count = count

    def addToToggler(self, toggler):
        allIds = {self.TopLeft, self.BottomLeft, self.Center, self.TopRight, self.BottomRight}
        def add(id):
            toggler.onIds.add(id)
            allIds.remove(id)
        
        if self.count == 0:
            pass
        elif self.count == 1:
            add(self.Center)
        elif self.count == 2:
            add(self.TopLeft)
            add(self.BottomRight)
        elif self.count == 3:
            add(self.TopLeft)
            add(self.Center)
            add(self.BottomRight)
        elif self.count == 4:
            add(self.TopLeft)
            add(self.TopRight)
            add(self.BottomLeft)
            add(self.BottomRight)
        elif self.count == 5:
            add(self.Center)
            add(self.TopLeft)
            add(self.TopRight)
            add(self.BottomLeft)
            add(self.BottomRight)
        
        toggler.offIds.update(allIds)

class Border:
    Borders = {
        ResourceType.Earth:'g3089',
        ResourceType.Air:'g2439',
        ResourceType.Fire:'g1773',
        ResourceType.Water:'g1325',
        ResourceType.Lotus:'g1284',
    }

    Backgrounds = {
        ResourceType.Earth:'g83',
        ResourceType.Air:'g84',
        ResourceType.Fire:'g85',
        ResourceType.Water:'g86',
        ResourceType.Lotus:'g87',
    }

    def __init__(self, type) -> None:
        self.type = type
        self.border = self.Borders[type]
        self.background = self.Backgrounds[type]

    def addToToggler(self,toggler):
        toggler.onIds.update([self.border, self.background])

        removeBackgrounds = list(self.Backgrounds.values())
        removeBackgrounds.remove(self.background)
        toggler.offIds.update(removeBackgrounds)

        removeBorders = list(self.Borders.values())
        removeBorders.remove(self.border)
        toggler.offIds.update(removeBorders)

def allTrayIds():
    return {TwoTray.TrayId, FourTray.TrayId, OddTray.TrayId}

def generateResourceCad(outputFile, requirements, victorypoints, type, image, input_svg):
    toggler = Toggler()
    
    escapedPath = str(image).replace(' ', '%20').replace('\\', '/')
    toggler.updateImageHref = f'file:///{escapedPath}' 
    
    if len(requirements) == 1:
        tray = OddTray(requirements)
    elif len(requirements) == 2:
        tray = TwoTray(requirements)
    elif len(requirements) == 3:
        tray = OddTray(requirements)
    elif len(requirements) == 4:
        tray = FourTray(requirements)
    else:
        raise ValueError(f"Invalid requirements length {len(requirements)}")
    
    tray.addToToggler(toggler)
    trayIds = allTrayIds()
    trayIds.remove(tray.TrayId)
    toggler.offIds.update(trayIds)

    border = Border(type)
    border.addToToggler(toggler)

    vp = VictoryPoints(victorypoints)
    vp.addToToggler(toggler)

    
    toggler.execute(input_svg, outputFile)
    logging.info(f'Generated file {outputFile}')



if __name__ == "__main__":
    from pathlib import Path
    level = 1
    produces = ResourceType.Water
    image = ''
    # requirements = {
    #     ResourceType.Water:5,
    #     ResourceType.Lotus:5,
    #     ResourceType.Air:1,
    #     ResourceType.Fire:2,
    # }

    requirements = {
        ResourceType.Air:5,
    }

    # requirements = {
    #     ResourceType.Water:5,
    #     ResourceType.Lotus:5,
    # }

    # requirements = {
    #     ResourceType.Lotus:5,
    #     ResourceType.Air:1,
    #     ResourceType.Fire:2,
    # }

    victoryPoints = 3
    input_svg = r"D:\Dropbox\Eppe's Stuff\Avatar Splenor Assets\Inkscape_SVG\AllCards_v3_Working.svg"
    outputFolder = 'output\\SVGs'
    originRow = 1

    outputFile = Path(outputFolder)/f'Level{level}/{produces}_{(originRow%18) + 1}.svg'
    generateResourceCad(outputFile, requirements, victoryPoints, produces, image, input_svg)