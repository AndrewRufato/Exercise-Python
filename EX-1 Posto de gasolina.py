postos_de_gasolina = [22]
combustivel_em_litros = 2
consumo_de_combustivel_por_km = 8
postos_de_gasolina_consegue_chegar = list()
postos_de_gasolina.sort(reverse = True)
km_rodados = (combustivel_em_litros * consumo_de_combustivel_por_km)
for i in postos_de_gasolina:  
    if km_rodados > i:
      postos_de_gasolina_consegue_chegar.append(i)
if len(postos_de_gasolina_consegue_chegar) == 0:
        postos_de_gasolina_consegue_chegar.append(-1)
print(postos_de_gasolina_consegue_chegar)
print('teste')
  


#def ultima_parada(combustivel,consumo,postos_de_gasolina):>< len(lista_desejada) == 0
    
    #pass

#Combustivel (em litros): 2
#Consumo médio (km/l): 8
#Postos de Gasolina (km): [2, 15, 22, 10.2]