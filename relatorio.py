import csv

# Inicializando as variáveis
total = 0
count = 0
media = 0
maior_valor = 0
menor_valor = float('inf')


arquivo = open("transacoes.csv", "r")
leitor = csv.DictReader(arquivo)


for linha in leitor:
    try:
        valor = float(linha["valor"])
        total += valor
        count += 1
        
  
        if valor > maior_valor:
            maior_valor = valor
        if valor < menor_valor:
            menor_valor = valor
    except KeyError:
        print("Erro: A chave 'valor' não foi encontrada na linha.")
    except ValueError:
        print(f"Erro: O valor '{linha['valor']}' não é um número válido.")


arquivo.close()


if count > 0:
    media = total / count


print(f"Número de transações: {count}")
print(f"Valor total: R$ {total:.2f}")
print(f"Valor médio por transação: R$ {media:.2f}")
print(f"Maior valor de transação: R$ {maior_valor:.2f}")
print(f"Menor valor de transação: R$ {menor_valor:.2f}")

if total > 1000:
    print("O total é maior que 1000.")
else:
    print("O total é menor ou igual a 1000.")
