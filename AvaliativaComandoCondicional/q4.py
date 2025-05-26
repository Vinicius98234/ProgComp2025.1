# Lê dia e mês inicial!
dia_ini = int(input("Digite o dia inicial: "))
mes_ini = int(input("De qual mês: "))
# Transformando a data inicial em dias julianos!
if mes_ini == 1:
    dia_ju_ini = 334 + dia_ini  
if mes_ini == 2:
    dia_ju_ini = 304 + dia_ini   
if mes_ini == 3:
    dia_ju_ini = 273 + dia_ini   
if mes_ini == 4:
    dia_ju_ini = 243 + dia_ini   
if mes_ini == 5:
    dia_ju_ini = 212 + dia_ini   
if mes_ini == 6:
    dia_ju_ini = 181 + dia_ini   
if mes_ini == 7:
    dia_ju_ini = 151 + dia_ini   
if mes_ini == 8:
    dia_ju_ini = 120 + dia_ini   
if mes_ini == 9:
    dia_ju_ini = 90 + dia_ini    
if mes_ini == 10:
    dia_ju_ini = 59 + dia_ini    
if mes_ini == 11:
    dia_ju_ini = 31 + dia_ini    
if mes_ini == 12:
    dia_ju_ini = dia_ini         

# Lê dia e mês final!
dia_fin = int(input("Digite o dia final: "))
mes_fin = int(input("De qual mês: "))
# Transformando a data final em dias julianos!
if mes_fin == 1:
    dia_ju_fin = 334 + dia_fin
if mes_fin == 2:
    dia_ju_fin = 304 + dia_fin
if mes_fin == 3:
    dia_ju_fin = 273 + dia_fin
if mes_fin == 4:
    dia_ju_fin = 243 + dia_fin
if mes_fin == 5:
    dia_ju_fin = 212 + dia_fin
if mes_fin == 6:
    dia_ju_fin = 181 + dia_fin
if mes_fin == 7:
    dia_ju_fin = 151 + dia_fin
if mes_fin == 8:
    dia_ju_fin = 120 + dia_fin
if mes_fin == 9:
    dia_ju_fin = 90 + dia_fin
if mes_fin == 10:
    dia_ju_fin = 59 + dia_fin
if mes_fin == 11:
    dia_ju_fin = 31 + dia_fin
if mes_fin == 12:
    dia_ju_fin = dia_fin

# Exibe o resultado!
print("Passaram-se", abs(dia_ju_fin - dia_ju_ini), "dias, entre", dia_ini, "do", mes_ini, "até", dia_fin, "do", mes_fin)