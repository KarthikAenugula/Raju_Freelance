import csv

sourceFilePath = input("Please Enter the Source Folder with fileName: ")
with open(sourceFilePath, 'r') as sourceFile:
    sourceReader = csv.reader(sourceFile)
    sourceData = list(sourceReader)
    sourceRowCount = len(sourceData)
    print(sourceRowCount)

destinationFilePath = input("Please Enter the Destination Folder with fileName: ")
with open(destinationFilePath, 'r') as destinationFile:
    destinationReader = csv.reader(destinationFile)
    destinationData = list(destinationReader)
    destinationRowCount = len(destinationData)
    print(destinationRowCount)

if sourceRowCount != destinationRowCount:
    print("Source File Count is not matching with Destination File Count")
elif sourceRowCount > destinationRowCount:
    print("Source File Count is greater than Destination File Count")
elif sourceRowCount < destinationRowCount:
    print("Source File Count is lesser than Destination File Count")
else :
    print("Source File Count is matching with Destination File Count")
