import copy

from properties_comparator_lib.key_with_different_values import KeyWithDifferentValues
from properties_comparator_lib.properties_dict import PropertiesDict

from properties_comparator_lib.comparation_result import ComparationResult


class PropertiesComparator:

    def __init__(self, fileOnePath, fileTwoPath):

        self.fileOnePath = fileOnePath
        self.fileTwoPath = fileTwoPath


    def compareFiles(self, compareKeyValues=True):
        valuesDifferents = []
        dictFileOne = PropertiesDict(self.fileOnePath)
        dictFileTwo = PropertiesDict(self.fileTwoPath)
        tempDict = copy.deepcopy(dictFileOne)

        for key, value in tempDict.items():

            if key in dictFileTwo:
                if compareKeyValues and value != dictFileTwo[key]:
                    valuesDifferents.append(KeyWithDifferentValues(key, self.fileOnePath, value, self.fileTwoPath,
                                                                dictFileTwo[key]))
                del dictFileOne[key]
                del dictFileTwo[key]

        return ComparationResult(fileOnePath=self.fileOnePath, fileTwoPath=self.fileTwoPath,
                                 uniqueKeysInFileOne=dictFileOne.keys(), uniqueKeysInFileTwo=dictFileTwo.keys(),
                                 keysWithDifferentValues=valuesDifferents)


