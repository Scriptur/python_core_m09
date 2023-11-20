import sys

NAME_NUM_DICT = dict()


def input_error(func):
    def wrapper(*name_num_input):
        try:
            result = func(*name_num_input)
            return result
        except KeyError:
            return "No user with given name"
        except ValueError:
            return 'Enter name and phone number please: '
        except IndexError:
            return "Give me name and phone please"
    return wrapper

def console_hello(): # Повернення до запитання
    return "How can I help you?"

def console_exit(): # Вихід з консольного бота
    sys.exit()

@input_error
def console_add(name_num_input): # Додавання в словник нового контакта з номером телефону
    parts = name_num_input.split(' ')
    user_name = parts[0]
    user_number = parts[1]
    if user_name not in NAME_NUM_DICT: # Перевірка існування контакта в словнику
        NAME_NUM_DICT[user_name] = user_number
    return f'User {user_name} successfully added'

@input_error
def console_change(name_num_input): # Оновлення в словнику номера телефону зазначеного контакту
    parts = name_num_input.split(' ')
    user_name = parts[0]
    user_number = parts[1]
    NAME_NUM_DICT[user_name] = user_number
    return f'User {user_name} changed number to {user_number}'

@input_error
def console_phone(user_name): # Показати номер телефону зазначеного контакту
    return NAME_NUM_DICT[user_name]

def console_show(): # Виводить всі збережені контакти з номерами телефонів
    return NAME_NUM_DICT

CONTROLLER = {'hello': console_hello,
              'add': console_add,
              'change': console_change,
              'phone': console_phone,
              'show all': console_show,
              'good bye': console_exit,
              'exit': console_exit,
              'close': console_exit,
              }


def main():
    command_console = None
    while True:
        income_message = input("Wait for input: ")
        if command_console is None:
            if income_message.lower() in ['add', 'change', 'phone']:
                command_console = CONTROLLER[income_message.lower()]
                continue
            elif income_message.lower() in ['hello', 'good bye', 'exit', 'close', 'show all']:
                command_console = CONTROLLER[income_message.lower()]
                result = command_console()
                command_console = None
                print(result)
                continue
            else:
                print("Enter valid command: hello, good bye, exit, close, add, change, phone, show all")
                continue
        result = command_console(income_message)
        command_console = None
        print(result)

if __name__ == '__main__':
    main()