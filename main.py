from properties_comparator import PropertiesComparator

if __name__ == "__main__":
    propertiesComparator = PropertiesComparator('./test_files/uno.properties', './test_files/dos.properties')
    propertiesComparator.compareFiles()