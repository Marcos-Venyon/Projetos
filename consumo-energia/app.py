nome = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho (em watts): "))
horasDia = float(input("Digite o número de horas de uso por dia: "))

consumoMensal = (potencia * horasDia * 30) / 1000

custoMensal = consumoMensal * 0.75  # Supondo um custo de R$ 0,75 por kWh

print(f"O consumo mensal do aparelho {nome} é de {consumoMensal:.2f} kWh.")
print(f"O custo mensal do aparelho {nome} é de R$ {custoMensal:.2f}.") 