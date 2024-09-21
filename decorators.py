def my_decorade(total):
    def wrapper(*args, **kwargs):
        print("inicio da funcao")
        total()
        print("fim da funcao")



@my_decorade
def juntar_conta(num1, num2):
    valor_conta = num1 + num2
    total = valor_conta
    return str(valor_conta)

