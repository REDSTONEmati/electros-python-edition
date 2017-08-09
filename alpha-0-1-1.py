print('Welcome to ElectrOS Py Edition, version 0.1.0.1 ALPHA')
devMode = [0]
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
def OS():
  
  print('Type any command. Type .help to show help')
  cmd = input()
  if cmd[0] == '.':
    if cmd == '.help':
      print('==============================' * 2)
      print('.info - displays info about the OS\n.help - displays help\n.bot - launches ChatBot')
      #print(devMode[0])
      if devMode[0] == 1:
        print('.login - Login to an account\n.reg - Registers an account\n.import - imports ElectrOScript app')
        print('.language - Changes language of the OS\n.debug - launches debug screen\n.open - opens app')
      print('==============================' * 2)
    elif cmd == '.info':
      print('==============================' * 2)
      print('ElectrOS ALPHA\nVersion: 0.1.0.1\nEdition: Py (Python/Pi (?)/Raspberry Pi (?))')
      print('Bot Version: 0.1.1\ElectrOScript Version: 0.1.1\n)')
      print('==============================' * 2)
    elif cmd == '.bot':
      print('Enter something, like "Hello"')
      botOutput = "null"
      botAnswers = ["null", "Hello", "Hi", "I'm fine", "I feel fantastic ;)", ""]
      botQuestions = ["null", "Hi", "Hello", "How are you?", "How are you", ""]
      def Bot():
        botInput = input()
        if botInput == "Exit":
          OS()
        else:
          x = 0
          while botInput != botQuestions[x]:
            x = x + 1
          if botInput == botQuestions[x]:
            print(botAnswers[x])
            Bot()
          else:
            print("Sorry, I don\'t have that keyword right now. But I'm trying to learn new phrases each day.")
            print('Remember: your sentences are gramaticly and case sensitive! Remember to start your')
            print('sentence from capital letter")')
            Bot()
      Bot()
    elif cmd == '.language':
      print('Enter the short code of your language. Currenty Supported languages are:')
      print('EN - English\nUA - Україньска')
    elif cmd == '.dev':
     print('Enter developer\'s password')
     devPassword = input()
     if devPassword == "thecakeisalie":
       #print('\n' * 100)
       print('Developer mode was activated. New commands and functions have been added')
       devMode[0] = 1
    elif cmd == "import":
      ElectrOScript()
    else:
      print('ERROR (002) = Unknown command')
    OS()
  else:
      print('ERROR (001) = Commands must start with "."')
      OS()
OS()

    