from datetime import datetime
from pathlib import Path


def decorators(old_function):
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open('logs.txt', 'w') as file:
            log = f'{datetime.datetime.today()} вызвали функцию {old_function} с аргументами {args} результат которой {result}'
            file.write(log)
        return result 
    return new_function 


def decorators2(old_function):
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open('logs.txt','a') as file:
            log = f'{datetime.today()} вызвали функцию {old_function} с аргументами {args} результат которой {result}\n'
            file.write(log)
        dir_path = Path.cwd()
        path = Path(dir_path, 'logs.txt')
        print(f'Был записан лог файл по адресу {path}')   
        return result 
    return new_function