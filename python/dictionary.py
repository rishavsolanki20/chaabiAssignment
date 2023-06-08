def fileType(extensionTypeStr, fileList):
    
    extensionDictionary = {}
    for item in extensionTypeStr.split(';'):
        extension, fileType = item.split(',')
        extensionDictionary[extension] = fileType

    result = {}
    for file in fileList:
        
        splitFile = file.split('.')
        if len(splitFile) == 2:
            filename, extension = splitFile
            
            if extension in extensionDictionary:
                result[file] = extensionDictionary[extension]
            else:
                result[file] = 'unknown'
        else:
            result[file] = 'unknown'

    return result


extensionTypeStr = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
fileList = ["abc.jpg", "xyz.xls", "text.csv", "123"]
result = fileType(extensionTypeStr, fileList)
print(result)
