from os import path

def createStatement(onlyCreate):
    clearStoredFile()

    file = open("import.txt", "r")
    
    lines = file.readlines()
    for i in range(len(lines)):
        if "table=" in lines[i]:
            tableName = lines[i][6:]
        elif "ID" in lines[i]:
            fields = lines[i].split()
            generateCreate(tableName, fields)
        elif not len(lines[i].strip()) == 0  and onlyCreate == 1:
            generateInsertInto(tableName,fields,lines[i])
    
    input("Done.\nPress Enter to continue...")



def generateCreate(name, fieldNames):
    
    parsedNameAndType = ""

    for i in range(len(fieldNames)):
        seperated = fieldNames[i].split("=")
        if seperated[1] == "varchar2":
            length = "200"
        elif seperated[1] == "number":
            length = "10"
        else:
            length = "50"
        parsedNameAndType = parsedNameAndType + seperated[0] + " " + seperated[1] + "(" + length + ")" + " NOT NULL" +",\n"

    query = "CREATE TABLE " + name  + "(\n" + parsedNameAndType[:-2] + "\n);"
    
    storeFile = "queries.txt"
    mode = 'a' if path.exists(storeFile) else 'w'
    with open(storeFile, mode) as f:
        f.write(query + "\n\n")



def  generateInsertInto(name, fieldNames, line):

    values = line.split("\t")
    
    parsedValues = ""
    parsedNames = ""

    for i in range(len(values)):
        if "varchar" in fieldNames[i]:
            parsedValues = parsedValues + "\'" + values[i] + "\',"
        else:
            parsedValues = parsedValues + values[i] + ","
    parsedValues = parsedValues[:-1]
    
    for i in range(len(fieldNames)):
        seperated = fieldNames[i].split("=")
        parsedNames = parsedNames + seperated[0] + ","
    parsedNames = parsedNames[:-1]

    query = "INSERT INTO " + name + "(" + parsedNames + ")\n" + "VALUES (" + parsedValues + ");"

    print(query)

    storeFile = "queries.txt"
    mode = 'a' if path.exists(storeFile) else 'w'
    with open(storeFile, mode) as f:
        f.write(query + "\n\n")



def clearStoredFile():
    storeFile = "queries.txt"
    mode = "w"
    with open(storeFile, mode) as f:
        f.write("")