import csv
import ftplib

sourceServerAddress = input("Please Enter the Source Server Address: ")
sourcePortNumber = input("Please Enter the Source Port Number: ")
sourceLoginUsername = input("Please Enter the Source Login Username: ")
sourceLoginPassword = input("Please Enter the Source Login Password: ")
sourceServer = ftplib.FTP()
sourceServer.connect(sourceServerAddress, sourcePortNumber)
sourceServer.login(sourceLoginUsername, sourceLoginPassword)

if sourceServer is None:
    print("Not able to connect to Source Server. Please check the details provided")
else:
    sourceFilePath = input("Please Enter the Source Folder with fileName: ")
    with open(sourceFilePath, 'r') as sourceFile:
        sourceReader = csv.reader(sourceFile)
        sourceData = list(sourceReader)
        sourceRowCount = len(sourceData)
        print(sourceRowCount)

destinationServerAddress = input("Please Enter the Destination Server Address: ")
destinationPortNumber = input("Please Enter the Destination Port Number: ")
destinationLoginUsername = input("Please Enter the Destination Login Username: ")
destinationLoginPassword = input("Please Enter the Destination Login Password: ")
destinationServer = ftplib.FTP()
destinationServer.connect(destinationServerAddress, destinationPortNumber)
destinationServer.login(destinationLoginUsername, destinationLoginPassword)

if destinationServer is None:
    print("Not able to connect to Destination Server. Please check the details provided")
else:
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
    else:
        print("Source File Count is matching with Destination File Count")
