import csv
from pathlib import Path
from collections import defaultdict
import logging

from toggleSVG import ResourceType
from ResourceCardGenerator import generateResourceCad
from vipGenerator import generateVIPImage
from inkscapeConversion import svg_to_png

conversionColorToResourceType = {
    'Black': ResourceType.Air,
    'White': ResourceType.Lotus,
    'Blue': ResourceType.Water,
    'Green':ResourceType.Earth,
    'Red':ResourceType.Fire,
}
class BadCSVRow(ValueError):
    def __init__(self, csvRowNumber, rowContents, error):            
        super().__init__(f"Bad CSV Row. Row no.{csvRowNumber}, {error}: row contents {rowContents}")

        self.rowNumber = csvRowNumber
        self.previousError = error
        self.rowContents = rowContents


class VIPCard:

    def __init__(self, requires, victoryPoints, quote, originRow) -> None:
        self.requirements = requires
        self.victoryPoints = victoryPoints
        self.quote = quote
        self.originRow = originRow

    def generateSVG(self, outputFolder, input_svg):
        outputFile = outputFolder/f'VIP/VIP_{self.originRow}.svg'
        generateVIPImage(outputFile, self.requirements, input_svg)
        return outputFile

class ResourceCard:

    def __init__(self,produces,requires, level, victoryPoints,image, originRow) -> None:
        self.produces = produces
        self.requirements = requires
        self.level = level
        self.victoryPoints= victoryPoints
        self.image = image
        self.originRow = originRow

    def generateSVG(self, outputFolder, input_svg):
        outputFile = outputFolder/f'Level{self.level}/{self.produces}_{self.originRow}.svg'
        generateResourceCad(outputFile, self.requirements, self.victoryPoints, self.produces, self.image, input_svg)
        return outputFile

def loadVIPCardsFromCsv(csvFile) -> tuple[list[VIPCard], list[Exception]]:
    with open(csvFile, newline='\n') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar="'")
        cards = list()
        errors = list()
        rowCount = 1
        for row in reader:
            try:
                victoryPoints = int(row['Victor Points']) 
                requirements = dict()
                for ogColor, resourceType in conversionColorToResourceType.items():
                    if row[ogColor] != '':
                        requirements[resourceType] = int(row[ogColor])
                cards.append(VIPCard(requires=requirements, victoryPoints=victoryPoints, quote="", originRow=rowCount))
            except (KeyError,ValueError) as e:
                customError = BadCSVRow(rowCount, f"{row}", e)
                errors.append(customError)
            rowCount+=1

    return cards, errors


def loadResourceCardsFromCsv(csvFile) -> tuple[list[ResourceCard], list[Exception]]:
    with open(csvFile, newline='\n') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar="'")
        cards = list()
        errors = list()
        rowCount = 1
        for row in reader:
            try:
                cardLevel = int(row['Card Level'])
                victoryPoints = 0 if row['VP'] == 0 else int(row['VP']) 
                generates = conversionColorToResourceType[row['Generates']]
                requirements = dict()
                for ogColor, resourceType in conversionColorToResourceType.items():
                    if row[ogColor] != '':
                        requirements[resourceType] = int(row[ogColor])
                cards.append(ResourceCard(produces=generates, requires=requirements,level=cardLevel,victoryPoints=victoryPoints, image='', originRow=rowCount))
            except (KeyError,ValueError) as e:
                customError = BadCSVRow(rowCount, f"{row}", e)
                errors.append(customError)

            rowCount+=1

        return cards, errors

def loadImagePaths(assetsPath):
    ResourceCardFolderName = "Resource Cards Images"    
    AirFolder = "Air Nomads"
    EarthFolder = "Earth Kingdom"
    FireFolder = "Fire Nation"
    WaterFolder = "Water Tribe"
    WhiteLotusFolder = "White Lotus"

    folderNameToResourceType = {
        AirFolder:ResourceType.Air,
        EarthFolder:ResourceType.Earth,
        FireFolder:ResourceType.Fire,
        WaterFolder:ResourceType.Water,
        WhiteLotusFolder:ResourceType.Lotus
    }

    toReturn = defaultdict(list)

    for folderName, resourceType in folderNameToResourceType.items():
        path = assetsPath / ResourceCardFolderName / folderName
        if path.is_dir():
            images = Path(path).glob("*.png")
            toReturn[resourceType] = list(images)
        else:
            logging.debug(f"path {path} doesn't exist")


    return toReturn

def main(outputFolderPath, resourceCardsCSV, vipCardsCSV, vipTemplateSvg, resourceCardTemplateSvg, imagesByType):

    svgsPath = outputFolderPath / "SVGs"


    # Generate Resource Pdf
    resourceCards, errors = loadResourceCardsFromCsv(resourceCardsCSV)
    logging.info(f"number of cards {len(resourceCards)}")
    logging.info(f"number of bad rows {len(errors)}")
    if len(errors) > 0:
        logging.error(f"{errors}")
    for card in resourceCards:
        card.image = imagesByType[card.produces].pop()

     # Genereate VIP Pdf
    vipCards, errors = loadVIPCardsFromCsv(vipCardsCSV)    
    logging.info(f"number of Vip cards {len(vipCards)}")
    logging.info(f"number of bad rows {len(errors)}")
    if len(errors) > 0:
        logging.error(f"{errors}")

    resourceCardSvgs = list()
    for card in resourceCards:
        resourceCardSvgs.append(card.generateSVG(svgsPath, resourceCardTemplateSvg))

    vipCardSvgs = list()
    for card in vipCards:
        vipCardSvgs.append(card.generateSVG(svgsPath, vipTemplateSvg))
    logging.info("Done Generating SVGs")


    logging.info("Generating VIP PNGs")
    for vipPath in vipCardSvgs:
        outputPath = Path(str(vipPath).replace("SVGs", 'PNGs').replace('.svg', '.png'))
        svg_to_png(vipPath, outputPath)

    logging.info("Generating ResourceCard PNGs")
    for resourcePath in resourceCardSvgs:
        outputPath = Path(str(resourcePath).replace("SVGs", 'PNGs').replace('.svg', '.png'))
        svg_to_png(resourcePath, outputPath)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    outputFolderPath = Path("output")

    # assetsPath = Path("assets")
    assetsPath = Path(r"D:\Dropbox\Eppe's Stuff\Avatar Splenor Assets")


    imagesByType = loadImagePaths(assetsPath)

    resourceCardsCSV = assetsPath / "resourceCards.csv"
    vipCardsCSV = assetsPath / "VIPCards.csv"

    vipTemplateSvg = assetsPath/ "Inkscape_SVG" / "VIP_Front.svg"
    resourceCardTemplateSvg = assetsPath/ "Inkscape_SVG" / "AllCards_v3.svg"

    main(outputFolderPath, resourceCardsCSV, vipCardsCSV, vipTemplateSvg, resourceCardTemplateSvg, imagesByType)