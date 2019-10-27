from .cliMsg import ynOptionError

def ynCliOption(questionMessage):
     while True:
        choice = input(questionMessage)
        if choice.lower() == '' or choice.lower() == 's':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print(ynOptionError)
