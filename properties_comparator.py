import copy
import tableprint as tp
import os.path

class PropertiesComparator:

    def __init__(self, fileOnePath, fileTwoPath):

        self.fileOnePath = fileOnePath
        self.fileTwoPath = fileTwoPath
        self.dictFileOne = {}
        self.dictFileTwo = {}
        self.valuesDifferents = []
        self.keysDifferents = []


    def compareFiles(self):

        self.dictFileOne = self.__readFile__(self.fileOnePath)
        self.dictFileTwo = self.__readFile__(self.fileTwoPath)
        tempDict = copy.deepcopy(self.dictFileOne)

        for key, value in tempDict.iteritems():

            if self.dictFileTwo.has_key(key):
                if value != self.dictFileTwo[key]:
                    self.valuesDifferents.append(__FileKeyValue__(key, self.fileOnePath, value, self.fileTwoPath,
                                                                  self.dictFileTwo[key]))
                del self.dictFileOne[key]
                del self.dictFileTwo[key]
        self.__printResults__()


    def __readFile__(self, fileName):

        dictFile = {}
        with open(fileName, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if "=" in line:
                    splitted_line = line.split("=")
                    dictFile[splitted_line[0].strip()] = splitted_line[1].strip()

        return dictFile


    def __calculateColumnsMaxWidth__(self, headers, data):

        max_width = map(lambda header: len(header), headers)
        for item in data:
            for i in range(len(max_width)):
                max_width[i] = len(item[i]) if len(item[i]) > max_width[i] else max_width[i]
        return max_width


    def __printTable__(self, title, data, headers):

        tp.banner(title)
        max_width = self.__calculateColumnsMaxWidth__(headers, data)
        tp.table(data=data, headers=headers, width=max_width, style='fancy_grid')


    def __printResults__(self):

        headers = ['Keys', os.path.split(self.fileOnePath)[1], os.path.split(self.fileTwoPath)[1]]
        result = map(lambda x: (x, ''), self.dictFileOne.keys())
        result.extend(map(lambda x: ('', x), self.dictFileTwo.keys()))
        self.__printTable__(title='Keys that are in one file but not in the other', headers=headers[1:], data=result)
        data = map(lambda item: (item.key, item.value1, item.value2), self.valuesDifferents)
        self.__printTable__(title='Keys that are in the two files but with different values', headers=headers,
                            data=data)


class __FileKeyValue__:

    def __init__(self, key, fileName1, value1, fileName2, value2):

        self.fileName1 = fileName1
        self.fileName2 = fileName2
        self.key = key
        self.value1 = value1
        self.value2 = value2
