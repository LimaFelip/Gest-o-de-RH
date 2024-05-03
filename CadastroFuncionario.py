# cadastro de funcionarios
print()
print('============== RELATORIO DO FUNCIONARIO ==============  ''\n')

# Dados da empresa

NOME_EM, CNPJ = "   Tavares Industrias LTDA", "00.215.000/0001.21"
print(NOME_EM, ', CNPJ', CNPJ)

EMDERECO_EMPRESA, CIDADE_EM, ESTADO_EM = "          Rua Tavares Nº 000", "São Gonçalo", "RJ"
print(EMDERECO_EMPRESA, CIDADE_EM, ESTADO_EM, "\n")

# informaçoes pessoais do funcionario

# nome = str(input('Nome: '))
# dataNasci = str(input('Data de Nascimento: '))
# idade = int(input('Idade: '))
# cpf = str(input('CPF: '))

# cidade = str(input('Cidade: '))
# estado = str(input('Estado: '))
# endereco = str(input('Rua: '))
# num_endereco = int(input('N°: '))

# quantidade_dependentes = int(input('Quantos dependentes? '))
# cargo = str(input('Cargo: '))
salario_base = float(input('Salario: '))
# data_admicao = str(input('Data de Admição: '))

# Informações Administrativas de pagamentos

# adiantamento = float(input('Adiantamento de: '))
# comissao = float(input('Valor da Comissão: '))
# vr = float(input('Vale refeição: '))
# gratificacao = float(input('Gratificação: '))
# horas_extras = float(input('Horas Extras: '))

# Instituto Nacional do Seguro Social - INSS

aliquata_7_5 = salario_base * 7.5/100
aliquata_9 = salario_base * 9/100
aliquata_12 = salario_base * 12/100
aliquata_14 = salario_base * 14/100

deducao_7_5 = 'INSETO'
deducao_9 = 21.18
deducao_12 = 101.18
deducao_14 = 181.18

if salario_base >= 0.0 and salario_base <= 1412.00:
    print(f"Salario Base = R$ {salario_base:.2f}")
    print(f"Salario liquido = R$ {salario_base - aliquata_7_5:.2f}")
    print(f"Valor da Alíquota 7,5% = R$ {aliquata_7_5:.2f}")
    print(f"Valor da parcela a Deduzir = R$ {deducao_7_5} ")
elif salario_base >= 1412.01:
    print(f"Salario Base = R$ {salario_base:.2f}")
    print(f"Salario lilíquota 7,5% = R$ {aliquata_9:.2f}")
    print(f"Valor da parcela a Deduzir = R$ {deducao_9} ")
elif salario_base >= 2666.69:
    print(f"Salario Base = R$ {salario_base:.2f}")
    print(f"Salario liquido = R$ {salario_base - aliquata_9:.2f}")
    print(f"Valor da Aquido = R$ {salario_base - aliquata_12:.2f}")
    print(f"Valor da Alíquota 7,5% = R$ {aliquata_12:.2f}")
    print(f"Valor da parcela a Deduzir = R$ {deducao_12} ")
elif salario_base >= 4000.04 and salario_base <= 7786.02:
    print(f"Salario Base = R$ {salario_base:.2f}")
    print(f"Salario liquido = R$ {salario_base - aliquata_14:.2f}")
    print(f"Valor da Alíquota 7,5% = R$ {aliquata_14:.2f}")
    print(f"Valor da parcela a Deduzir = R$ {deducao_14} ")

else:
    print("ERRO: Você não digitou nada")


# Imposto de Renda - IRRF
# if salrio_base <=
# FGTS
# Ferias
#  = (salario_base/3)+salario_base
# salario_13 =

# print(f'Salario R${salario_base:.2f}')
# print(f'Ferias R${ferias:.2f}')
