print()
print("🐍Calculadora em Python🐍".center(35))

print("\n\nOlá, seja bem vindo(a) à calculadora!")
entrada = input("(Enter para continuar😄)\n".center(35))

x=int(input("\nDigite o primeiro valor: "))
y=int(input("\nDigite o segundo valor: "))

escolha = input("\nQual operação matemática você deseja realizar?\n\n(adição, subtração, multiplicação ou divisão?)\n\n")

if escolha.lower() in ["adição"]:
    print("\nA adição entre", x, "e", y, "é", x + y)

elif escolha.lower() in ["subtração"]:
    print("\nA subtração entre", x, "e", y, "é", x - y)

elif escolha.lower() in ["multiplicação"]:
    print("\nA multiplicação entre", x, "e", y, "é", x * y)

elif escolha.lower() in ["divisão"]:
    print("\nA divisão entre", x, "e", y, "é", x / y)