import math
import locale


def exercicio01():
    num = int(input("Digite um número inteiro: "))
    print(num)


def exercicio02():
    num = float(input("Digite um número real: "))
    print(num)


def exercicio03():
    num1 = int(input("Digite o 1º número inteiro: "))
    num2 = int(input("Digite o 2º número inteiros: "))
    num3 = int(input("Digite o 3º número inteiros: "))
    print(f'A soma dos três números digitados é: {num1 + num2 + num3}')


def exercicio04():
    num = float(input("Digite um número real: "))
    print(f'O quadrado do número é: {num ** 2}')


def exercicio05():
    num = float(input("Digite um número real: "))
    print(f'A quinta parte do número é: {num / 5}')


def exercicio06():
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celsius * (9 / 5) + 32
    print(f'{celsius}º graus Celsius corresponde a {fahrenheit:.2f} º Fahrenheit')


def exercicio07():
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = 5 * (fahrenheit - 32) / 9
    print(f'{fahrenheit}º Fahrenheit corresponde a {celsius:.2f}º Celsius')
    # print(f'{fahrenheit}º Fahrenheit corresponde a {celsius:.{num}f}º Celsius')
    # print("{:.2f}".format(celsius))
    # print("{:.{}f}".format(celsius, 2))


def exercicio08():
    kelvin = float(input("Digite a temperatura em Kelvin: "))
    celsius = kelvin - 273.15
    print(f'{kelvin} Kelvin corresponde a {celsius:.2f}º graus Celsius')


def exercicio09():
    celsius = float(input("Digite a temperatura em Celsius: "))
    kelvin = celsius + 273.15
    print(f'{celsius}º graus Celsius corresponde a {kelvin:.2f} Kelvin')


def exercicio10():
    kmh = float(input("Digite a velocidade em km/h: "))
    ms = kmh / 3.6
    print(f'A velocidade convertida para m/s é: {ms:.2f}')


def exercicio11():
    ms = float(input("Digite a velocidade em m/s: "))
    kmh = ms * 3.6
    print(f'A velocidade convertida para km/h é: {kmh:.2f}')


def exercicio12():
    milha = float(input("Digite a distância em milhas: "))
    km = milha * 1.61
    print(f'A distância convertida para quilômetro é: {km:.2f}')


def exercicio13():
    km = float(input("Digite a distância em quilômetro: "))
    milha = km / 1.61
    print(f'A distância convertida para milhas é: {milha:.2f}')


def exercicio14():
    grau = float(input("Digite o ângulo em graus: "))
    radiano = grau * math.pi / 180
    print(f'O ângulo convertido para radiano é: {radiano:.2f}')


def exercicio15():
    radiano = float(input("Digite o ângulo em radianos: "))
    grau = radiano * 180 / math.pi
    print(f'O ângulo convertido para grau é: {grau:.2f}')


def exercicio16():
    polegada = float(input("Digite o comprimento em polegadas: "))
    centimetro = polegada * 2.54
    print(f'O comprimento convertido para centimetro é: {centimetro:.2f}')


def exercicio17():
    centimetro = float(input("Digite o comprimento em centimetro: "))
    polegada = centimetro / 2.54
    print(f'O comprimento convertido para polegadas é: {polegada:.2f}')


def exercicio18():
    metro_cubico = float(input("Digite o volume em metro cúbicos: "))
    litro = metro_cubico * 1000
    print(f'O volume convertido para litros é: {litro:.3f}')


def exercicio19():
    litro = float(input("Digite o volume em litros: "))
    metro_cubico = litro / 1000
    print(f'O volume convertido para metro cúbicos é: {metro_cubico:.3f}')


def exercicio20():
    quilogramas = float(input("Digite a massa em quilogramas: "))
    libras = quilogramas / 0.45
    print(f'A massa convertida para libras é: {libras:.3f}')


def exercicio21():
    libras = float(input("Digite a massa em libras: "))
    quilogramas = libras * 0.45
    print(f'A massa convertida para quilogramas é: {quilogramas:.3f}')


def exercicio22():
    jarda = float(input("Digite o comprimento em jardas: "))
    metro = jarda * 0.91
    print(f'O comprimento convertido para metros é: {metro:.3f}')


def exercicio23():
    metro = float(input("Digite o comprimento em metros: "))
    jarda = metro / 0.91
    print(f'O comprimento convertido para jardas é: {jarda:.3f}')


def exercicio24():
    metro_quadrado = float(input("Digite a área em metros quadrados: "))
    acre = metro_quadrado * 0.000247
    print(f'A área convertida para acres é: {acre}')


def exercicio25():
    acre = float(input("Digite a área em acre: "))
    metro_quadrado = acre * 4048.58
    print(f'A área convertida para metros quadrados é: {metro_quadrado}')


def exercicio26():
    metro_quadrado = float(input("Digite a área em metros quadrados: "))
    hectare = metro_quadrado * 0.0001
    print(f'A área convertida para hectares é: {hectare}')


def exercicio27():
    hectare = float(input("Digite a área em hectares: "))
    metro_quadrado = hectare * 10000
    print(f'A área convertida para metros quadrados é: {metro_quadrado}')


def exercicio28():
    num1 = float(input("Digite o 1º valor: "))
    num2 = float(input("Digite o 2º valor: "))
    num3 = float(input("Digite o 3º valor: "))

    soma_quadrados = num1 ** 2 + num2 ** 2 + num3 ** 2
    print(f'A soma dos quadrados dos três números digitados é: {soma_quadrados}')


def exercicio29():
    num1 = float(input("Digite a 1ª nota: "))
    num2 = float(input("Digite a 2ª nota: "))
    num3 = float(input("Digite a 3ª nota: "))
    num4 = float(input("Digite a 4ª nota: "))

    media_aritmetica = (num1 + num2 + num3 + num4) / 4
    print(f'A media aritmética dos quatro números digitados é: {media_aritmetica}')


def exercicio30():
    real = float(input("Digite um valor em real (R$): "))
    cotacao_dolar = float(input("Digite a cotação do dólar ($): "))

    dolar = real / cotacao_dolar
    print(f'R$ {real:.2f} corresponde a $ {dolar:.2f}')


def exercicio31():
    num = int(input("Digite um número: "))
    antecessor, sucessor = num - 1, num + 1
    print(f'O antecessor e sucessor do número {num} é, respectivamente: {antecessor} e {sucessor}')


def exercicio32():
    num = int(input("Digite um número: "))
    resultado = (num * 3 + 1) + (num * 2 - 1)
    print(f'O resultado da soma do sucessor do triplo de {num} com o antecessor de seu dobro é: {resultado}')


def exercicio33():
    lado_quadrado = float(input("Digite o tamanho do lado do quadrado: "))
    area_quadrado = lado_quadrado * lado_quadrado
    print(f'A área do quadrado é: {area_quadrado:.2f}')


def exercicio34():
    raio = float(input("Digite o valor do raio do círculo: "))
    area_circulo = math.pi * raio ** 2
    print(f'A área do círculo é: {area_circulo:.2f}')


def exercicio35():
    cateto_a = float(input("Digite o tamanho do cateto A de um triângulo: "))
    cateto_b = float(input("Digite o tamanho do cateto B de um triângulo: "))
    hipotenusa = math.sqrt(cateto_a ** 2 + cateto_b ** 2)
    # hipotenusa = (cateto_a ** 2 + cateto_b ** 2) ** 0.5
    print(f'A hipotenusa do triângulo é: {hipotenusa:.2f}')


def exercicio36():
    altura, raio = float(input("Digite a altura do cilindro: ")), \
                   float(input("Digite o raio do cilindro: "))
    volume_cilindro = math.pi * raio ** 2 * altura
    print(f'O volume do cilindro é: {volume_cilindro:.2f}')


def exercicio37():
    valor_produto = float(input("Digite o valor do produto: "))
    total = valor_produto * 0.88
    print(f'O valor do produto com desconto de 12% é de: {total}')


def exercicio38():
    salario = float(input("Digite o salário do funcionário: "))
    aumento = salario * 1.25
    print(f'O novo salário do funcionário é de: {aumento}')


def exercicio39():
    importancia = 780_000.00
    primeiro_lugar = importancia * 0.46
    segundo_lugar = importancia * 0.32
    terceiro_lugar = importancia * 0.22

    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
    print(f'O valor recebido por cada ganhador do sorteio é de: \n'
          f'1º ganhador: {locale.currency(primeiro_lugar, grouping=True)} \n'
          f'2º ganhador: {locale.currency(segundo_lugar, grouping=True)} \n'
          f'3º ganhador: {locale.currency(terceiro_lugar, grouping=True)}')


def exercicio40():
    dias_trabalhados = float(input(f'Digite o número de dias trabalhados pelo encanador: '))
    pagamento = (dias_trabalhados * 30) * 0.92
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

    print(f'O valor líquido a ser pago para o encanador é: {locale.currency(pagamento, grouping=True)}')


def exercicio41():
    valor_hora_trabalho, horas_trabalhadas = float(input(f'Digite o valor da hora de trabalho do funcionário: ')), \
                                             int(input(f'Digite o valor de horas trabalhadas no mês: '))
    pagamento = valor_hora_trabalho * horas_trabalhadas * 1.10
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

    print(f'O valor a ser pago para o trabalhador é: {locale.currency(pagamento, grouping=True)}')


def exercicio42():
    salario_base = float(input(f'Digite o valor do salário base do funcionário: '))
    pagamento = (salario_base * 1.05) - (salario_base * 0.07)
    locale.setlocale(locale.LC_MONETARY, 'pt-br.UTF-8')

    print(f'O valor a ser pago para o funcionário é de: {locale.currency(pagamento, grouping=True)}')


def exercicio43():
    valor = float(input(f'Digite o valor da compra: '))
    total_desconto = valor * 0.90
    total_parcela = valor / 3
    comissao_vista = total_desconto * 0.05
    comissao_parcelado = valor * 0.05

    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
    print(f'Sobre a compra: \n'
          f'Valor pago á vista com desconto de 10%: {locale.currency(total_desconto, grouping=True)} \n'
          f'Comissão do vendedor na compra á vista onde fora aplicado o desconto de 10%: {locale.currency(comissao_vista, grouping=True)} \n '
          f'Valor parcelado de 3x (sem juros): {locale.currency(total_parcela, grouping=True)} \n'
          f'Comissão do vendedor em compras parceladas: {locale.currency(comissao_parcelado, grouping=True)}')


def exercicio44():
    altura_degrau, altura_desejada = float(input(f'Digite a altura em cm do degrau: ')), \
                                     float(input(f'Digite a altura em cm desejada: '))
    num_degraus = int(altura_desejada / altura_degrau)
    print(f'O usuário precisa subir {num_degraus} para alcançar a altura de {altura_desejada} cm')


def exercicio45():
    """
    Retorna o código ASCII do caractere - ord('a')
    Retorna o caractere referente aquele ao código - chr(97)
    """

    caractere = input(f'Digite uma letra minuscula do alfabeto para ser convertida em maiusculo: ')[0]
    maiusculo = chr(ord(caractere) - 32)
    # maiusculo = caractere.upper()

    print(f'O caractere informado foi: {caractere} - conversão do caractere para maiusculo: {maiusculo}')


def exercicio46():
    num = abs(int(input("Digite um número inteiro, positivo de três dígitos de 100 a 999: ")[0:3]))
    print(f'O número criado a partir da inversão do número digitado é: {str(num)[::-1]}')


def exercicio47():
    num = abs(int(input("Digite um número inteiro, positivo e de quatro dígitos de 1000 a 9999: ")[0:4]))
    print(f'1º Dígito: {str(num)[0:1:]} \n'
          f'2º Dígito: {str(num)[1:2:]} \n'
          f'3º Dígito: {str(num)[2:3:]} \n'
          f'4º Dígito: {str(num)[3:4:]} \n')


def exercicio48():
    segundo = abs(int(input("Digite um valor de tempo em segundos: ")))
    hora = segundo // 3_600
    minuto = (segundo % 3_600) // 60
    segundo = (segundo % 3_600) % 60
    print(f'O valor em hora:minuto:segundo é: {hora}:{minuto}:{segundo}')


def exercicio49():
    hora_inicio, duracao = str(input("Digite a hora:minuto:segundo de início do experimento: ")), \
                    abs(int(input("Digite a duração do experimento com o valor de tempo em segundos: ")))

    hora_inicio = hora_inicio.split(':')
    duracao += (int(hora_inicio[0]) * 3_600) + (int(hora_inicio[1]) * 60) + int(hora_inicio[2])

    hora_final = duracao // 3_600
    minuto_final = (duracao % 3_600) // 60
    segundo_final = (duracao % 3_600) % 60

    print(f'O valor em hora:minuto:segundo é: {hora_final}:{minuto_final}:{segundo_final}')


def exercicio50():
    idade, ano = abs(int(input("Informe sua idade: "))), abs(int(input("Informe o ano vigente: ")))
    print(f'Seu ano de nascimento foi {ano - idade}')


def exercicio51():
    cordenada_x, cordenada_y = int(input("Informe a cordenada x: ")), int(input("Informe a cordenada y: "))
    distancia_pontos = math.sqrt((cordenada_x - 0) ** 2 + (cordenada_y - 0) ** 2)
    print(f'A distancia entre os ponto ({cordenada_x}, {cordenada_y}) e (0,0) é: {distancia_pontos:.2f}')


def exercicio52():
    valor_premio, aposta1, aposta2, aposta3 = float(input("Informe o valor do prêmio da loteria: ")), \
                                              float(input("Informe o valor investido pelo 1º apostador: ")), \
                                              float(input("Informe o valor investido pelo 2º apostador: ")), \
                                              float(input("Informe o valor investido pelo 3º apostador: "))
    aposta_total = aposta1 + aposta2 + aposta3
    premio1 = (aposta1 / aposta_total) * valor_premio
    premio2 = (aposta2 / aposta_total) * valor_premio
    premio3 = (aposta3 / aposta_total) * valor_premio
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

    print(f'O prêmio do 1º apostador é: {locale.currency(premio1, grouping=True)} \n' 
          f'O prêmio do 2º apostador é: {locale.currency(premio2, grouping=True)} \n' 
          f'O prêmio do 3º apostador é: {locale.currency(premio3, grouping=True)}')


def exercicio53():
    comprimento, largura, preco_metro = float(input("Informe o comprimento o terreno: ")), \
                                        float(input("Informe a largura do terreno: ")), \
                                        float(input("Informe o preço do metro da tela: "))

    custo = (comprimento * 2 + largura * 2) * preco_metro
    print(f'O custo para cercar o terreno é {custo:.2f}')


exercicio01()
exercicio02()
exercicio03()
exercicio04()
exercicio05()
exercicio06()
exercicio07()
exercicio08()
exercicio09()
exercicio10()
exercicio11()
exercicio12()
exercicio13()
exercicio14()
exercicio15()
exercicio16()
exercicio17()
exercicio18()
exercicio19()
exercicio20()
exercicio21()
exercicio22()
exercicio23()
exercicio24()
exercicio25()
exercicio26()
exercicio27()
exercicio28()
exercicio29()
exercicio30()
exercicio31()
exercicio32()
exercicio33()
exercicio34()
exercicio35()
exercicio36()
exercicio37()
exercicio38()
exercicio39()
exercicio40()
exercicio41()
exercicio42()
exercicio43()
exercicio44()
exercicio45()
exercicio46()
exercicio47()
exercicio48()
exercicio49()
exercicio50()
exercicio51()
exercicio52()
exercicio53()
