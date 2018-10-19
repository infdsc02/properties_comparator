import tableprint as tp
import os.path

def __calculateColumnsMaxWidth__(headers, data):

    columns_max_width = list(map(lambda header: len(header), headers))
    for item in data:
        for i in range(len(columns_max_width)):
            columns_max_width[i] = len(item[i]) if len(item[i]) > columns_max_width[i] else columns_max_width[i]
    return columns_max_width


def __printTable__(title, data, headers):

    tp.banner(title)
    columns_max_width = __calculateColumnsMaxWidth__(headers, data)
    tp.table(data=data, headers=headers, width=columns_max_width, style='fancy_grid')


def printResults(comparationResult):

    headers = ['Keys', os.path.split(comparationResult.fileOnePath)[1], os.path.split(comparationResult.fileTwoPath)[1]]

    result = list(map(lambda x: (x, ''), comparationResult.uniqueKeysInFileOne))
    result.extend(list(map(lambda x: ('', x), comparationResult.uniqueKeysInFileTwo)))
    __printTable__(title='Keys that are in one file but not in the other', headers=headers[1:], data=result)

    if (len(comparationResult.keysWithDifferentValues) >  0):
        data = list(map(lambda item: (item.key, item.value1, item.value2), comparationResult.keysWithDifferentValues))
        __printTable__(title='Keys that are in the two files but with different values', headers=headers,
                            data=data)