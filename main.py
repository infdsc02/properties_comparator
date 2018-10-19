import argparse
import logging

from logging_conf import setup_logging
from properties_comparator_lib.properties_comparator import PropertiesComparator
from print_results import printResults

if __name__ == "__main__":

    setup_logging(default_path='./data/logging.yaml', default_level=logging.INFO)

    parser = argparse.ArgumentParser(description='Properties files compare tool.')

    requiredNamed = parser.add_argument_group('Required arguments')
    requiredNamed.add_argument('-f1', dest='fileOnePath', help='File one path', required=True)
    requiredNamed.add_argument('-f2', dest='fileTwoPath', help='File two path', required=True)

    optionalNamed = parser.add_argument_group('Optional arguments')
    optionalNamed.add_argument('-ck', dest='compareKeyValues', action='store_true', help='Compare key values.')
    optionalNamed.set_defaults(compareKeyValues=False)

    args = parser.parse_args()

    propertiesComparator = PropertiesComparator(args.fileOnePath, args.fileTwoPath)
    compareResult = propertiesComparator.compareFiles(args.compareKeyValues)
    printResults(compareResult)