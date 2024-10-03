from toggleSVG import Toggler, RequirementsSlot, ResourceType

class OddTray:
    TrayId = 'g1763'

            # RequirementsSlot(id, air, lotus, water, earth, fire)
    SlotA = RequirementsSlot('g1762', 'g66', 'g64', 'g62', 'g60', 'g1757')
    SlotB = RequirementsSlot('g1755', 'g74', 'g72', 'g70', 'g68', 'g1751')
    SlotC = RequirementsSlot('g1749', 'g82', 'g80', 'g78', 'g76', 'g1745')
    

    def threeNumTree(self):
        return {
            1:{
                1:{
                    2:self.OneOneTwo,
                    3:self.OneOneThree,
                }, 2: {
                    2:self.OneTwoTwo
                }, 3: {
                    1:self.OneThreeOne,
                }, 4: {
                    2:self.OneFourTwo
                }
            }, 
            2:{
                1:{
                    2:self.TwoOneTwo,
                    4:self.TwoOneFour
                }, 
                2:{
                    1:self.TwoTwoOne,
                    3:self.TwoTwoThree
                },
                3: {
                    2:self.TwoThreeTwo,
                    3:self.TwoThreeThree
                },
                
            }, 
            3:{
                1: {
                    1:self.ThreeOneOne,
                },
                2: {
                    2:self.ThreeTwoTwo,
                    3:self.ThreeTwoThree,
                },
                3: {
                    2:self.ThreeThreeTwo,
                    6:self.ThreeThreeSix
                },
                6: {
                    3:self.ThreeSixThree,
                }
            }, 
            6: {
                2: {
                    1:self.SixTwoOne,
                },
                3: {
                    3:self.SixThreeThree
                }
            }
        }


    OneOneTwo = 'g294'

    OneTwoTwo = 'g317'
    TwoOneTwo = 'g266'
    TwoTwoOne = 'g280'

    OneOneThree = 'g305'
    OneThreeOne = 'g299'
    ThreeOneOne = 'g254'

    TwoTwoThree = 'g270'
    TwoThreeTwo = 'g274'
    ThreeTwoTwo = 'g248'

    TwoThreeThree = 'g227'
    ThreeTwoThree = 'g241'
    ThreeThreeTwo = 'g236'

    OneFourTwo = 'g259'
    TwoOneFour = 'g287'

    SixTwoOne = 'g210'

    ThreeThreeSix = 'g216'
    ThreeSixThree = 'g221'
    SixThreeThree = 'g212'

    Seven = 'g336'
    Six = 'g335'
    Five = 'g334'
    Four = 'g333'
    Three = 'g331'


    def allNums(self):
        return {
            self.OneOneTwo,
            self.OneTwoTwo,
            self.TwoOneTwo,
            self.TwoTwoOne,
            self.OneOneThree,
            self.OneThreeOne,
            self.ThreeOneOne,
            self.TwoTwoThree,
            self.TwoThreeTwo,
            self.ThreeTwoTwo,
            self.TwoThreeThree,
            self.ThreeTwoThree,
            self.ThreeThreeTwo,
            self.OneFourTwo,
            self.TwoOneFour,
            self.SixTwoOne,
            self.ThreeThreeSix,
            self.ThreeSixThree,
            self.SixThreeThree,
            self.Seven, 
            self.Six, 
            self.Five, 
            self.Four,
            self.Three
            }

    
    def __init__(self, requirements) -> None:
        
        if len(requirements) == 1:
            
            self.SlotC.turnOff()
            self.SlotA.turnOff()
            aType = list(requirements.keys())[0]
            self.SlotB.setType(aType)
            self.numsId = self.oneNumTree()[requirements[aType]]



        elif len(requirements) == 3:
            values = list()
            slotsToAssign = [self.SlotC, self.SlotB, self.SlotA]
            for aType in ResourceType:
                if aType in requirements:
                    slot = slotsToAssign.pop()
                    slot.setType(aType)
                    values.append(requirements[aType])
                    
            self.numsId = self.threeNumTree()[values[0]][values[1]][values[2]]
        else:
            raise ValueError("Odd Tray requirements can only be of length 1 or 3")    
    
    

    def oneNumTree(self):
        return {7:self.Seven, 6:self.Six, 5:self.Five, 4:self.Four, 3:self.Three}

    def addToToggler(self, toggler):
        otherNums = self.allNums()
        otherNums.remove(self.numsId)
        toggler.offIds.update(otherNums)
        toggler.onIds.update([self.TrayId, self.numsId])
        self.SlotA.addToToggler(toggler)
        self.SlotB.addToToggler(toggler)
        self.SlotC.addToToggler(toggler)

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
        otherNums = self.allNums()
        otherNums.remove(self.numsId)
        toggler.offIds.update(otherNums)
        toggler.onIds.update([self.TrayId, self.numsId])
        self.SlotA.addToToggler(toggler)
        self.SlotB.addToToggler(toggler)

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
        self.border = self.Borders[type]
        self.background = self.Backgrounds[type]

    def addToToggler(self,toggler):
        toggler.onIds.update([self.border, self.background])

        removeBackgrounds = list(self.Backgrounds.values())
        removeBackgrounds.remove(self.background)
        toggler.offIds.update(removeBackgrounds)

        removeBorders = list(self.Borders.values())
        removeBorders.remove(self.border)

def allTrayIds():
    return {TwoTray.TrayId, FourTray.TrayId, OddTray.TrayId}

def generateResourceCad(outputFile, requirements, victorypoints, type, image):
    toggler = Toggler()
    
    
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

    input_svg = 'AllCards_v3.svg'
    toggler.execute(input_svg, outputFile)
    print(f'Generated file {outputFile}')


