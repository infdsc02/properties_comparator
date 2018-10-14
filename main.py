import argparse

from properties_comparator import PropertiesComparator

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Properties files compare tool.')
    requiredNamed = parser.add_argument_group('Required arguments')
    requiredNamed.add_argument('-f1', dest='fileOnePath', help='File one path', required=True)
    requiredNamed.add_argument('-f2', dest='fileTwoPath', help='File two path', required=True)
    args = parser.parse_args()

    propertiesComparator = PropertiesComparator(args.fileOnePath, args.fileTwoPath)
    propertiesComparator.compareFiles()