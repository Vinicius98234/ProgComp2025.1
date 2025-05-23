print("Programa que conta o número de dias decorridos entre duas datas dentro do mesmo ano")

di = int(input("Dia inical = "))
mi = int(input("Mês inical = "))
df = int(input("Dia final = "))
mf = int(input("Mês final = "))

quantdias = 0

janeiro = 31
fevereiro = 28
marco = 31
abril = 30
maio = 31
junho = 30
julho = 31
agosto = 31
setembro = 30
outubro = 31
novembro = 30
dezembro = 31

if mf < mi or (mf == mi and df < di):
    print("A data final deve ser posterior à data inicial!")
else:
    if mi == mf:
        totaldias = df - di
        

