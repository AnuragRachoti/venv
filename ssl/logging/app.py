import logging

##logging config file
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    handlers= [
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger= logging.getLogger('ArithmeticApp')

def add(a,b):
    result = a+b
    logger.debug(f'adding {a}+{b} = {result}')
    return result

def sub(a,b):
    result = a-b
    logger.debug(f'subracting {a}-{b} = {result}')
    return result

def mul(a,b):
    result = a*b
    logger.debug(f'multiplication {a}*{b} = {result}')
    return result

def div(a,b):
    try:
        result = a/b
        logger.debug(f'division {a}/{b} = {result}')
        return result
    except ZeroDivisionError:
        logger.error(f'division by zero error')
        return None
    


add(10,15)
sub(10,15)
mul(10,15)
div(10,15)
