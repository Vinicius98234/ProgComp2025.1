print("Programa que leia o número de minutos que um veículo permaneceu no estacionamento e exiba o valor a ser pago pelo responsável.")

permanencia = int(input("Quanto tempo em minutos seu carro passou no estacionamento? "))
horas = permanencia/60

tarifa1 = 8
tarifa2 = 5
tarifa3 = 3
tarifafix = 30

if horas <= 2:
    valpago = tarifa1 * horas
    print("Você passou", permanencia, "minutos no estacionamento. O valor a ser pago é de R$", valpago)
else:
    if horas <= 4:
        valpago = (2 * tarifa1) + ((horas-2) * tarifa2)
        print("Você passou", permanencia, "minutos no estacionamento. O valor a ser pago é de R$", valpago)
    else:
        if horas < 12:
            valpago = (2 * tarifa1) + (2 * tarifa2) + ((horas - 4) * tarifa3)
            print("Você passou", permanencia, "minutos no estacionamento. O valor a ser pago é de R$", valpago)
        else:
            valpago = tarifafix
            print("Você passou", permanencia, "minutos no estacionamento, que é equivalente a mais de 12 horas, então, O valor a ser pago é de R$", valpago)
    
    

