def ElectrOScript():
  importCode = "null"
  x = 1
  plines = []
  importCode.split('\n')
  lines = []
  while True:
    line = input()
    if line != "{end}":
        lines.append(line)
    else:
        break
  text = '\n'.join(lines)
  importCode = text.split()
  if importCode[0] == "{start}":
  while importCode[x] != "{end}":
    if "say" in importCode[x]:
      EScriptLine = list(importCode[x])
      sayChars = [":)"]
      if EScriptLine[3] == "(":
        sayCharCounter = 4
        output = [""]
        while EScriptLine[sayCharCounter] != ")":
          output.append(EScriptLine[sayCharCounter])
          sayCharCounter += 1
        print(''.join(output))
        break
  x = x + 1