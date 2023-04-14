import xml.etree.ElementTree as ET

def main(junit_xml_file):
    tree = ET.parse(junit_xml_file)
    root = tree.getroot()

    passed = 0
    failed = 0
    skipped = 0
    error = 0

    for testcase in root.iter('testcase'):
        if testcase.find('failure') is not None:
            failed += 1
        elif testcase.find('skipped') is not None:
            skipped += 1
        elif testcase.find('error') is not None:
            error += 1
        else:
            passed += 1

    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Skipped: {skipped}")
    print(f"Error: {error}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python parse_junit_xml.py <junit_xml_file>")
        sys.exit(1)

    junit_xml_file = sys.argv[1]
    main(junit_xml_file)