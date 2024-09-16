from datetime import date
from math import pi

senhaCerta = "soffner"
logado = False

for i in range(3):
    senha = input("Digite sua senha:\n")
    if(senha == senhaCerta):
        logado = True
        break
    elif(senha == "vicentini"):
        print(f"TÁ ERRADO! {2 - i} tentativas restantes")
        continue
    print(f"Senha incorreta, {2 - i} tentativas restantes")
        
if(logado):
    print("Bem-vindo!")
    opcao = 1
    while(opcao != 0):
        opcao = int(input("Escolha um item:"
                      + "\n1. Dia de hoje"
                      + "\n2. Área do círculo"
                      + "\n3. Grade de aulas"
                      + "\n0. Sair\n"))
        if(opcao == 1):
            print(date.today() )
        elif(opcao == 2):
            raio = float(input("Digite o raio:\n"))
            print("Área: %.2f" % (pi*raio**2))
        elif(opcao == 3):
            seg = ["Segunda:", "Redes", "Redes", "Cálculo"]
            ter = [" Terça:", " - ", "Cálculo", "Inglês"]
            qua = [" Quarta:", "DSPTI", "DSPTI", "Programação II"]
            qui = [" Quinta:", " - ", "Programação II", "S.O."]
            sex = [" Sexta:", " - ", "S.O.", "Português II"]
            grade = [seg, ter, qua, qui, sex]
            print('Grade:\n', '\n'.join(' '.join('{:2} /'.format(item) for item in linha) for linha in grade))
        elif(opcao == 0):
            print("Até logo!")
else:
    print("Tentativas esgotadas")
