from toggleSVG import VIPCardRequirement, ResourceType, Toggler
import logging

QuoteIds = [
    "g1277",
    "g1278",
    "g1279",
    "g1280",
    "g1281",
    "g1282",
    "g1283",
    "g1284",
    "g1285",
    "g1286",
]

slotA = VIPCardRequirement('g28','g4','g1268', 'g1269','g1270')
slotB = VIPCardRequirement('g31', 'g5','g1271', 'g1272','g1273')
slotC = VIPCardRequirement('g34','g6','g1274', 'g1275','g1276')

def generateVIPImage(outputFile, types, input_svg, quoteNumber):
    toggler = Toggler()


    quoteId = QuoteIds[quoteNumber]
    otherQuoteIds = list(QuoteIds)
    otherQuoteIds.remove(quoteId)

    typeKeys = list(types.keys())
    if len(typeKeys) == 3:
        isThree = True
        slotA.setTypeAndCount(typeKeys[0], isThree)
        slotB.setTypeAndCount(typeKeys[1], isThree)
        slotC.setTypeAndCount(typeKeys[2], isThree)
    else:
        isThree = False
        slotA.setTypeAndCount(typeKeys[0], isThree)
        slotB.setTypeAndCount(typeKeys[1], isThree)
        slotC.turnOff()
    
    slotA.addToToggler(toggler)
    slotB.addToToggler(toggler)
    slotC.addToToggler(toggler)

    toggler.onIds.add(quoteId)
    toggler.offIds.update(otherQuoteIds)
    

    toggler.execute(input_svg, outputFile)
    logging.info(f'Generated file {outputFile}')


if __name__ == "__main__":
    output = 'output/number1.svg'
    input_svg = r"D:\Dropbox\Eppe's Stuff\Avatar Splenor Assets\Inkscape_SVG\Vip Front All.svg"
    generateVIPImage(
        outputFile = output, 
        types = {ResourceType.Fire:4, ResourceType.Lotus:4, ResourceType.Water:3}, 
        input_svg=input_svg, 
        quoteNumber=0)

