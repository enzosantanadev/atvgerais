def contar_letras(palavra, contagem):
    for letra in palavra:
        if letra in contagem:
            contagem[letra] += 1
        else:
            contagem[letra] = 1

    return contagem
contagem = {}
while True:
     palavra = input("fale uma palavra")
     if palavra.lower()== 'sair':
         break
     contar_letras(palavra, contagem)
     print("contagem atual:", contagem)

print("contagem final", contagem)
