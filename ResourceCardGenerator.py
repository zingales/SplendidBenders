from toggleSVG import Toggler, RequirementsSlot, ResourceType


class FourTray:
    TrayId = 'g170'

            # RequirementsSlot(id, air, lotus, water, earth, fire)
    SlotA = RequirementsSlot('g362', 'g24', 'g26', 'g361', 'g54', 'g53')
    SlotB = RequirementsSlot('g357', 'g32', 'g34', 'g356', 'g30', 'g28')
    SlotC = RequirementsSlot('g353', 'g42', 'g44', 'g307', 'g39', 'g36')
    SlotD = RequirementsSlot('g367', 'g56', 'g58', 'g366', 'g54', 'g53')

    FiveThreeThreeThree = 'g5'
    ThreeFiveThreeThree = 'g2'
    ThreeThreeFiveThree = 'g161'
    ThreeThreeThreeFive = 'g177'

    TwoOneOneOne = 'g183'
    OneTwoOneOne = 'g189'
    OneOneTwoOne = 'g198'
    OneOneOneTwo = 'g206'
    OneOneOneOne = 'g167'

    def __init__(self, requirements) -> None:
        if len(requirements) != 4:
            raise ValueError("Four Tray requirements can only be of length four")
    
        values = list()
        slotsToAssign = [self.SlotD, self.SlotC, self.SlotB, self.SlotA]
        for aType in ResourceType:
            if aType in requirements:
                slot = slotsToAssign.pop()
                slot.setType(aType)
                values.append(requirements[aType])
                
        self.numsId = self.allNumsTree()[values[0]][values[1]][values[2]][values[3]]

    def allNums(self):
        return {
            self.FiveThreeThreeThree, 
            self.ThreeFiveThreeThree, 
            self.ThreeThreeFiveThree, 
            self.ThreeThreeThreeFive,
            self.TwoOneOneOne,
            self.OneTwoOneOne,
            self.OneOneTwoOne,
            self.OneOneOneTwo,
            self.OneOneOneOne
            }
    
    def allNumsTree(self):
        return { 
                5: {3:{3:{3:self.FiveThreeThreeThree}}}, 
                3: {3:{3:{5:self.ThreeThreeThreeFive}, 5:{3:self.ThreeThreeFiveThree}}}, 
                2: {1:{1:{1:self.TwoOneOneOne}}},
                1: {1:{1:{1:self.OneOneOneOne, 2:self.OneOneOneTwo},2: {1:self.OneOneTwoOne}}, 2:{1:{1:self.OneTwoOneOne},},}
            }
    

    def addToToggler(self, toggler):
        print(f'Slot A is {self.SlotA.onType}')
        print(f'Slot B is {self.SlotB.onType}')
        print(f'Slot C is {self.SlotC.onType}')
        print(f'Slot D is {self.SlotD.onType}')
        print(f'Nums on {self.numsId}')

        otherNums = self.allNums()
        otherNums.remove(self.numsId)
        toggler.offIds.update(otherNums)
        toggler.onIds.update([self.TrayId, self.numsId])
        self.SlotA.addToToggler(toggler)
        self.SlotB.addToToggler(toggler)
        self.SlotC.addToToggler(toggler)
        self.SlotD.addToToggler(toggler)

class TwoTray:
    TrayId = 'g1812'
    SlotA = RequirementsSlot('g1808', 'g6', 'g9', 'g1804', 'g4', 'g3')
    SlotB = RequirementsSlot('g1802', 'g14', 'g16', 'g1798', 'g13', 'g10')

    SevenThree = 'g341'
    ThreeSeven = 'g339'
    FiveThree = 'g338'
    ThreeFive = 'g343'
    TwoTwo = 'g345'
    TwoOne = 'g347'
    OneTwo = 'g349'

    def allNums(self):
        return {
            self.SevenThree, 
            self.ThreeSeven, 
            self.FiveThree, 
            self.ThreeFive,
            self.TwoTwo,
            self.TwoOne,
            self.OneTwo
            }
    
    def allNumsTree(self):
        return { 
                7: {3:self.SevenThree}, 
                3: {7:self.ThreeSeven, 5:self.ThreeFive}, 
                5: {3:self.FiveThree},
                2: {2:self.TwoTwo, 1:self.TwoOne},
                1: {2:self.OneTwo}
            }
    
    def __init__(self, requirements) -> None:
        if len(requirements) != 2:
            raise ValueError("Two Tray requirements can only be of length two")
    
        value_a = 0
        value_b = 0    
        for aType in ResourceType:
            if aType in requirements:
                if self.SlotA.onType is None:
                    self.SlotA.setType(aType)
                    value_a = requirements[aType]
                else:
                    self.SlotB.setType(aType)
                    value_b = requirements[aType]
        
        self.numsId = self.allNumsTree()[value_a][value_b]


    def addToToggler(self, toggler):
        print(f'Slot A is {self.SlotA.onType}')
        print(f'Slot B is {self.SlotB.onType}')
        otherNums = self.allNums()
        otherNums.remove(self.numsId)
        toggler.offIds.update(otherNums)
        toggler.onIds.update([self.TrayId, self.numsId])
        print(f'Nums on {self.numsId}')
        self.SlotA.addToToggler(toggler)
        self.SlotB.addToToggler(toggler)

def allTrayIds():
    return {TwoTray.TrayId, FourTray.TrayId}

def generateResourceCad(outputFile, requirements, victorypoints, type, image):
    toggler = Toggler()
    
    
    if len(requirements) == 2:
        tray = TwoTray(requirements)
    elif len(requirements) == 4:
        tray = FourTray(requirements)
    
    tray.addToToggler(toggler)
    trayIds = allTrayIds()
    trayIds.remove(tray.TrayId)
    toggler.offIds.update(trayIds)
    

    print(f'On ids {toggler.onIds}')
    print(f'Off ids {toggler.offIds}')

    input_svg = 'AllCards_v3.svg'
    toggler.execute(input_svg, outputFile)
    print(f'Generated file {outputFile}')


# requirements = {ResourceType.Air:7, ResourceType.Water:3}
requirements = {ResourceType.Fire:1, ResourceType.Lotus:1, ResourceType.Water:1, ResourceType.Air:1}
generateResourceCad('output/FourTray.svg', requirements, 5, ResourceType.Air, image='')
