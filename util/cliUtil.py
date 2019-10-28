'''
    Este modulo sirve de utilidad para las preguntas que se puedan hacer por consola
'''
from .cliMsg import ynOptionError

def ynCliOption(questionMessage):
     '''
        Le pregunta al usuario "si" o "no" y valida la respuesta

        Parametros:
           :param str questionMessage: la pregunta que se le hará al usuario (debe contener [s/n])

        :return: None
     '''
     while True:
        choice = input(questionMessage)
        if choice.lower() == '' or choice.lower() == 's':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print(ynOptionError)
