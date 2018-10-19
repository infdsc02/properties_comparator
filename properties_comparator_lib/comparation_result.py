class ComparationResult(object):

    def __init__(self, fileOnePath, fileTwoPath, uniqueKeysInFileOne=[], uniqueKeysInFileTwo=[],
                 keysWithDifferentValues=[]):
        self.fileOnePath = fileOnePath
        self.fileTwoPath = fileTwoPath
        self.uniqueKeysInFileOne = uniqueKeysInFileOne
        self.uniqueKeysInFileTwo = uniqueKeysInFileTwo
        self.keysWithDifferentValues = keysWithDifferentValues