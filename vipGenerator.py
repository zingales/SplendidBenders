from toggleSVG import *


slotA = RequirementsSlot('g2', 'g57', 'g1030', 'g1032', 'g1033', 'g1034')
slotB = RequirementsSlot('g18', 'g17', 'g12', 'g10', 'g8', 'g6')
slotC = RequirementsSlot('g32', 'g31', 'g26', 'g24', 'g22', 'g20')


class VIPCounts:

    threeByThree_id = 'g4'
    fourByTwo_id = 'g36'

    def __init__(self, isThreebByThree) -> None:
        if isThreebByThree:
            self.onId = self.threeByThree_id
            self.offId = self.fourByTwo_id
        else:
            self.onId = self.fourByTwo_id
            self.offId = self.threeByThree_id


    def addToToggler(self, toggler):
        toggler.onIds.add(self.onId)
        toggler.offIds.add(self.offId)


def set_vip_requirements(types, toggler):
    if len(types) == 3:
        slotA.setType(types[0])
        slotB.setType(types[1])
        slotC.setType(types[2])
        count = VIPCounts(isThreebByThree=True)
    else:
        slotA.setType(types[0])
        slotB.setType(types[1])
        slotC.turnOff()
        count = VIPCounts(isThreebByThree=False)
    
    count.addToToggler(toggler=toggler)
    slotA.addToToggler(toggler)
    slotB.addToToggler(toggler)
    slotC.addToToggler(toggler)
    


def generateVIPImage(outputFile, types):
    toggler = Toggler()

    set_vip_requirements(types, toggler)

    input_svg = 'VIP_Front.svg'
    toggler.execute(input_svg, outputFile)
    print(f'Generated file {outputFile}')


output = 'output/number1.svg'
generateVIPImage(output, types = [ResourceType.Fire, ResourceType.Lotus])

