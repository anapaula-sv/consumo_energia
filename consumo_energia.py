import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl
import os

def obter_consumo(mes):
    while True:
        try:
            valor = float(input(f"Consumo em {mes} (kWh): "))
            if valor < 0: raise ValueError
            return valor
        except ValueError:
            print("❌ Por favor, digite um número válido e positivo.")

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
consumos = [obter_consumo(mes) for mes in meses]
df = pd.DataFrame({'Mês': meses, 'Consumo': consumos})

def calcular_fatura(linha):
    if linha['Consumo'] > 250:
        return linha['Consumo'] * 0.90, '#e74c3c', 'Vermelha'
    elif linha['Consumo'] > 150:
        return linha['Consumo'] * 0.75, '#f1c40f', 'Amarela'
    else:
        return linha['Consumo'] * 0.60, '#2ecc71', 'Verde'

df[['Valor_Fatura', 'Cor', 'Bandeira']] = df.apply(
    lambda row: pd.Series(calcular_fatura(row)), axis=1
)

print("\n--- Relatório Semestral ---")
print(df[['Mês', 'Consumo', 'Valor_Fatura', 'Bandeira']])

plt.style.use('ggplot') 
fig, ax = plt.subplots(figsize=(10, 6))

barras = ax.bar(df['Mês'], df['Valor_Fatura'], color=df['Cor'], edgecolor='black', alpha=0.8)

media_gasto = df['Valor_Fatura'].mean()
ax.axhline(media_gasto, color='blue', linestyle='--', label=f'Média: R$ {media_gasto:.2f}')

ax.set_title('Simulador de análise de Gastos com Energia', fontsize=14)
ax.set_ylabel('Valor da Conta (R$)')
ax.legend()

for barra in barras:
    height = barra.get_height()
    ax.annotate(f'R$ {height:.2f}',
                xy=(barra.get_x() + barra.get_width() / 2, height),
                xytext=(0, 3), 
                textcoords="offset points",
                ha='center', va='bottom')

plt.tight_layout()
plt.show()

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_final = os.path.join(diretorio_atual, "relatorio_energia.xlsx")

try:
    df.drop(columns=['Cor']).to_excel(caminho_final, index=False)
    print(f"\n Planilha criada/atualizada com sucesso!")
    print(f"📍 Local: {caminho_final}")
except PermissionError:
    print("\n Erro: Feche o arquivo Excel antes de rodar o código.")
except Exception as e:
    print(f"\n Erro ao salvar: {e}")