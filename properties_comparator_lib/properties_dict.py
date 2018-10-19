import logging
from copy import deepcopy

class PropertiesDict(dict):

    def __init__(self, filePath):
        dict.__init__(self)
        self.logger = logging.getLogger(__name__)
        self.__readFile__(filePath)

    def __readFile__(self, filePath):

        propDict = {}
        try:
            with open(filePath, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if "=" in line:
                        splitted_line = line.split("=")
                        self[splitted_line[0].strip()] = splitted_line[1].strip()
        except Exception:
            self.logger.error('', exc_info=True)
        finally:
            return propDict


    def __deepcopy__(self, memo):

        return deepcopy(dict(self))