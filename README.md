# ⚡ Simulador de Consumo Energético

Este projeto é um simulador interativo desenvolvido em Python para calcular faturas de energia, identificar bandeiras tarifárias e gerar relatórios visuais e estruturados.

## 🚀 Funcionalidades
- **Validação de Inputs:** Sistema que impede entradas inválidas usando blocos `try/except`.
- **Cálculo Inteligente:** Aplicação automática de tarifas baseadas nas bandeiras Verde, Amarela e Vermelha.
- **Data Visualization:** Gráfico de barras com cores dinâmicas e linha de média para análise rápida.
- **Exportação de Dados:** Geração de arquivo `.xlsx` (Excel) com os dados processados.

## 🛠️ Tecnologias Utilizadas
- **Python 3**
- **Pandas**: Manipulação de DataFrames.
- **Numpy**: Processamento lógico e matemático.
- **Matplotlib**: Criação de gráficos.
- **Openpyxl**: Engine para exportação para Excel.

## 📊 Resultados do Projeto

### Interface e Código
O código foi estruturado de forma modular para facilitar a manutenção e garantir a segurança dos dados.

### Análise Visual
O gráfico abaixo mostra a relação entre o consumo e o valor da fatura, destacando os meses de maior gasto.
![Gráfico de Consumo](https://github.com/user-attachments/assets/0cc50941-bb56-4343-8640-39cd17876905)

### Relatório Estruturado
Saída automática em Excel para gestão de dados.

![Planilha Gerada](https://github.com/user-attachments/assets/56fc08d8-3e8f-4ab9-a1cf-db982cee0033) 

## 📝 Como executar
1. Certifique-se de ter o Python instalado.
2. Instale as bibliotecas necessárias:
   ```bash
   pip install pandas numpy matplotlib openpyxl
