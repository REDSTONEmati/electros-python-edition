print('Welcome to ElectrOS Py Edition, version 0.1.2 ALPHA')
devMode = [0]
language = ["EN"]
def ElectrOScript():
  importCode = "null"
  x = 1
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
        if EScriptLine[3] == "(" and EScriptLine[4] == '"':
          sayCharCounter = 5
          output = [""]
          while EScriptLine[sayCharCounter] != '"':
            if EScriptLine[sayCharCounter] == "^":
              output.append(" ")
            else:
              output.append(EScriptLine[sayCharCounter])
            sayCharCounter += 1
          print(''.join(output))
          break
        else:
          print('ElectrOScript ERROR: string must start with ""')
      else:
        print('ElectrOScript ERROR: No known command was found in the script')
    x = x + 1
def OS():
  if language[0] == "EN":
    print('Type any command. Type .help to show help')
  elif language[0] == "UA":
    print('Напишіть яку завгодно команду. Щоб побачити повний список команд, напишіть .help')
  cmd = input()
  if cmd[0] == '.':
    if cmd == '.help':
      print('==============================' * 2)
      if language[0] == "EN":
        print('.info - displays info about the OS\n.help - displays help\n.bot - launches ChatBot')
        print('.import - imports ElectrOScript app\n.language - changes the language of the OS')
      elif language[0] == "UA":
        print('.info - показує інформацію о системі\n.help - показує список команд\n.bot - вмикає ЧатБота')
        print('.import - імпортує програму написану в ElectrOScript\n.language - Змінює мову')
      #print(devMode[0])
      if devMode[0] == 1:
        print('.login - Login to an account\n.reg - Registers an account')
        print('.debug - launches debug screen\n.open - opens app')
      print('==============================' * 2)
    elif cmd == '.info':
      print('==============================' * 2)
      print('ElectrOS ALPHA\nVersion: 0.1.2\nEdition: Py (Python/Pi (?)/Raspberry Pi (?))')
      print('Bot Version: 0.1.1\nElectrOScript Version: 0.2.0)')
      print('==============================' * 2)
    elif cmd == '.bot':
      print('Enter something, like "Hello"')
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
      language[0] = input()
      OS()
    elif cmd == '.dev':
     print('Enter developer\'s password')
     devPassword = input()
     if devPassword == "thecakeisalie":
       #print('\n' * 100)
       print('Developer mode was activated. New commands and functions have been added')
       devMode[0] = 1
    elif cmd == ".import" or cmd == ".code":
      ElectrOScript()
    else:
      print('ERROR (002) = Unknown command')
    OS()
  else:
      print('ERROR (001) = Commands must start with "."')
      OS()
OS()

    