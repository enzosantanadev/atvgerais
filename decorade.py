def func(f):
    def wrapper():
        print("Iniciada")
        f()
        print("Finalizada")
    return wrapper
def f1():
    print("Função f1() chamada!")
def f2():
    print("Função f2() chamada")