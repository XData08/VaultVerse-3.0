import random


def GenerateCode() -> str:
    return "".join([ str(random.randrange(10)) for i in range(6)])
    