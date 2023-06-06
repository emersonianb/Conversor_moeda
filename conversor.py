import requests
import json

cotacoes = (requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")).json()
cotacao_dolar = float(cotacoes["USDBRL"]["bid"])
cotacao_euro = float(cotacoes["EURBRL"]["bid"])
cotacao_bitcoin = float(cotacoes["BTCBRL"]["bid"])

print("Você gostaria de converter para (1) Dolar, (2) Euro ou (3) Bitcoin?")
resposta = input()
valor = float(input("Digite o valor a ser convertido: "))

if resposta == "1":
    print(valor*cotacao_dolar)
elif resposta == "2":
    print(valor*cotacao_euro)
elif resposta == "3":
    print(valor*cotacao_bitcoin)