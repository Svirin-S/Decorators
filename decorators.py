from datetime import datetime



def decorators(old_function):
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open('logs.txt', 'w') as file:
            log = f'{datetime.datetime.today()} вызвали функцию {old_function} с аргументами {args} результат которой {result}'
            file.write(log)
        return result 
    return new_function 


def decorators2(params):
    def _decorators2(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open('logs.txt','a') as file:
                log = f'{datetime.today()} вызвали функцию {old_function} с аргументами {args} результат которой {result}\n'
                file.write(log)
            print(f'Был записан лог файл по адресу {params}')   
            return result 
        return new_function
    return _decorators2    