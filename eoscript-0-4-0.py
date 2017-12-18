def ElectrOScriptN(code):
  import numbers
  #variables======================================
  varNames = ["test"]
  varDatas = ["TEST"]
  varTypes = ["str"]
  importCode = []
  #===============================================
  #getting the code===============================
  if code == "":
    while True:
      line = input()
      if line != "{end}":
          importCode.append(line)
      else:
          importCode.append("{end}")
          break
  else:
    importCode = code
  codeLineID = 0
  #===============================================
  #executing code=================================
  if importCode[codeLineID] == "{start}":
    codeLineID += 1
    charCounter = 0
    #while not checking last line
    while importCode[codeLineID] != "{end}":
      
      codeLine = list(importCode[codeLineID])
      charCounter = 0
      
      #checks which command it is
      if ''.join(codeLine[charCounter:charCounter + 3]) == "say":
        
        cont = []
        charCounter += 3
        
        #checks if content of command is present
        if ''.join(codeLine[charCounter:charCounter + 3]) == " = ":
          
          charCounter += 3
          
          #detects type of content 
          #if string
          if codeLine[charCounter] == '"':
            charCounter += 1
            while ''.join(codeLine[charCounter:charCounter + 2]) != '";':
              cont.append(codeLine[charCounter])
              charCounter += 1
            print(''.join(cont))
          #if integer or variable
          else:
            while codeLine[charCounter] != ';':
              cont.append(codeLine[charCounter])
              charCounter += 1
            #if integer
            try:
              print(int(''.join(cont)))
            #if variable
            except ValueError:
              print("var")
        else:
          print("ERROR")
        codeLineID += 1
      elif ''.join(codeLine[charCounter:charCounter + 3]) == "var":
        
        charCounter += 4
        varTarget = []
        
        #gets variables name
        while codeLine[charCounter] != ' ' and codeLine[charCounter] != ";":
          varTarget.append(codeLine[charCounter])
          charCounter += 1
        varTarget = ''.join(varTarget)
        #if variable is edited
        if codeLine[charCounter] == " ":
          print("old")
        #if variable is created
        else:
          if not varTarget in varNames:
            varNames.append(varTarget)
            varTypes.append("null")
            varDatas.append('null')
          else:
            print("ERROR: This variable alredy exists")
        codeLineID += 1
      elif codeLine[charCounter] == '#':
        codeLineID += 1
      else:
        print("ERROR: No such command.")
        codeLineID += 1
      #end of executing code
  #================================================
      
