def ElectrOScriptN(code):
  import numbers
  from time import sleep
  #variables======================================
  varNames = ["var1"]
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
        if codeLine[charCounter] == "(":
          
          charCounter += 1
          #detects type of content 
          #if string
          if codeLine[charCounter] == '"':
            charCounter += 1
            while ''.join(codeLine[charCounter:charCounter + 3]) != '");':
              cont.append(codeLine[charCounter])
              charCounter += 1
            print(''.join(cont))
          #if integer or variable
          else:
            
            while ''.join(codeLine[charCounter:charCounter + 2]) != ');':
              cont.append(codeLine[charCounter])
              charCounter += 1
            #if integer
            try:
              print(int(''.join(cont)))
            #if variable
            except ValueError:
              varTarget = ''.join(cont)
              #check does variable exist
              if varTarget in varNames:
                y = 0
                #find variable's number in list
                while varNames[y] != varTarget:
                  y += 1
                #print data
                print(varDatas[y])
              else:
                print("ERROR: This variable doesn't exist")
        else:
          print("ERROR: Wrong syntax")
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
        if ''.join(codeLine[charCounter + 1:charCounter + 3]) == "= ":
          charCounter += 3
          cont = []
          #if string
          if codeLine[charCounter] == '"':
            targetType = "str"
            charCounter += 1
            #get content
            while ''.join(codeLine[charCounter:charCounter + 2]) != '";':
              cont.append(codeLine[charCounter])
              charCounter += 1
            cont = ''.join(cont)
          #else int or var
          else:
            #if integer
            try:
              targetType = "int"
              #get content
              while codeLine[charCounter] != ';':
                cont.append(codeLine[charCounter])
                charCounter += 1
              cont = int(''.join(cont))
            except ValueError:
              #get content
              while codeLine[charCounter] != ';':
                cont.append(codeLine[charCounter])
                charCounter += 1
              #check does it exist
              if ''.join(cont) in varNames:
                #find variable's number in list
                while varNames[y] != ''.join(cont):
                  y += 1
                #set cont to variable's data
                cont = varDatas[y]
              else:
                print("ERROR: This variable doesn't exist")
          #check does variable exist
          if varTarget in varNames:
            y = 0
            #find variable's number in list
            while varNames[y] != varTarget:
              y += 1
            #change data
            varDatas[y] = cont
            varTypes[y] = targetType
          else:
            print("ERROR: This variable doesn't exist")
        #if variable is created
        else:
          if not varTarget in varNames:
            varNames.append(varTarget)
            varTypes.append("null")
            varDatas.append('null')
          else:
            print("ERROR: This variable already exists")
        codeLineID += 1
      elif codeLine[charCounter] == '#':
        codeLineID += 1
      elif ''.join(codeLine[charCounter:charCounter + 4]) == "wait":
        charCounter += 4
        if codeLine[charCounter] == "(":
        	cont = []
        	charCounter += 1
        	while ''.join(codeLine[charCounter:charCounter + 2]) != ');':
        	  cont.append(codeLine[charCounter])
        	  charCounter += 1
        	#check type: int or var
        	try:
        	  sleep(int(''.join(cont)))
        	except ValueError:
        	  varTarget = ''.join(cont)
        	  if varTarget in varNames:
        	    y = 0
        	    #find variable's number in list
        	    while varNames[y] != varTarget:
        	      y += 1
        	      #check is variable's data is integer or not
        	    if varTypes[y] == "int":
        	      z = varDatas[y]
        	      sleep(z)
        	    else:
        	      print("ERROR: Only integers are supported for 'wait'")
        	codeLineID += 1
      else:
        print("ERROR: No such command.")
        codeLineID += 1
      #end of executing code
  #================================================
