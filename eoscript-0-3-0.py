def ElectrOScript(mode):
  varNames = ["", "hello", "var1", "d"]
  varData = ["", "Hello World", "test", 'd']
  varTarget = [""]
  varCont = [""]
  importCode = [""]
  x = 1
  if mode == "":
    hhh = 1
    while True:
      line = input()
      if line != "{end}":
          importCode.append(line)
      else:
          importCode.append("{end}")
          break
    x = 2
  else:
    importCode = mode
    hhh = 0
  print(importCode)
  print("================================" * 2)
  if importCode[hhh] == '{start}':
    while importCode[x] != "{end}":
      EScriptLine = list(importCode[x])
      if EScriptLine[0] == "s" and EScriptLine[1] == "a" and EScriptLine[2] == "y":
        if EScriptLine[3] == "(":
          if EScriptLine[4] == '"':
            sayCharCounter = 5
            output = [""]
            while EScriptLine[sayCharCounter] != '"':
              if EScriptLine[sayCharCounter] == "^":
                output.append(" ")
              else:
                output.append(EScriptLine[sayCharCounter])
              sayCharCounter += 1
            print(''.join(output))
            if x <= len(importCode):
              x = x + 1
          else:
            sayCharCounter = 4
            varTarget = [""]
            while EScriptLine[sayCharCounter] != ")":
              varTarget.append(EScriptLine[sayCharCounter])
              sayCharCounter += 1
            varTarget = ''.join(varTarget)
            y = 0
            while varNames[y] != varTarget:
              if y != len(varNames) - 1:
                y += 1
              else:
                break
            print(varData[y])
            if x <= len(importCode):
              x = x + 1
            else:
              break
      elif EScriptLine[0] == "v" and EScriptLine[1] == "a" and EScriptLine[2] == "r":
        sayCharCounter = 4
        varTarget = [""]
        while EScriptLine[sayCharCounter] != ' ' and EScriptLine[sayCharCounter] != ";":
          varTarget.append(EScriptLine[sayCharCounter])
          if EScriptLine[sayCharCounter] != ' ' and EScriptLine != ";":
            sayCharCounter += 1
        print(EScriptLine[sayCharCounter])
        if EScriptLine[sayCharCounter] != ";":
          sayCharCounter += 3
        else:
          if not ''.join(varTarget) in varNames:
            varNames.append(varTarget)
            varData.append("null")
          else:
            print("ERROR")
          print(EScriptLine[sayCharCounter] == '"')
          if EScriptLine[sayCharCounter] == '"':
            print(varData)
            sayCharCounter += 1
            varCont = ['']
            while EScriptLine[sayCharCounter] != '"':
              varCont.append(EScriptLine[sayCharCounter])
              if EScriptLine[sayCharCounter] != '"':
                sayCharCounter += 1
          elif ''.join(EScriptLine[sayCharCounter:sayCharCounter + 7]) == "input()":
            varCont = input()
          else:
            print("ERROR")
          print(varCont)
          varCont = ''.join(varCont)
          varTarget = ''.join(varTarget)
          y = 0
          while varNames[y] != varTarget:
            if y != len(varNames) - 1:
              y += 1
            else:
              break
          varData[y] = varCont
        if x <= len(importCode):
          x = x + 1
      elif EScriptLine[0] == "#":
        if x <= len(importCode):
          x = x + 1
      else:
        #print('ElectrOScript ERROR: No known command was found in the script')
        print("TEST VARIABLE CODE")
        break
