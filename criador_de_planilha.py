import pandas as pd
import random
from datetime import datetime, timedelta
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# Função para gerar datas a partir de uma data inicial
def generate_dates(start_date, num_days):
    return [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(num_days)]

# Data inicial
start_date = datetime.strptime('2024-01-01', '%Y-%m-%d')

# Geração dos dados fictícios
num_rows = 100
data = {
    'Data': generate_dates(start_date, num_rows),
    'Vendas Totais (R$)': [round(random.uniform(1000, 3000), 2) for _ in range(num_rows)],
    'Clientes Atendidos': [random.randint(40, 100) for _ in range(num_rows)],
    'Itens Vendidos': [random.randint(200, 500) for _ in range(num_rows)],
    'Custo Operacional (R$)': [round(random.uniform(400, 800), 2) for _ in range(num_rows)],
    'Lucro Bruto (R$)': [round(random.uniform(600, 2200), 2) for _ in range(num_rows)]
}

# Criação do DataFrame
df = pd.DataFrame(data)

# Adicionar coluna de Porcentagem de Lucro
df['Porcentagem de Lucro (%)'] = (df['Lucro Bruto (R$)'] / df['Vendas Totais (R$)']) * 100

# Salvar o DataFrame em uma planilha Excel sem ajuste de formatação
df.to_excel('administracao_loja_temp.xlsx', index=False)

# Ajustar a formatação usando openpyxl
wb = load_workbook('administracao_loja_temp.xlsx')
ws = wb.active

# Ajustar o tamanho das colunas
for col in ws.columns:
    max_length = 0
    column = col[0].column_letter  # Get the column name
    for cell in col:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(str(cell.value))
        except:
            pass
    adjusted_width = (max_length + 2)
    ws.column_dimensions[column].width = adjusted_width

# Salvar a planilha formatada com o nome final
wb.save('administracao_loja.xlsx')

print("Planilha 'administracao_loja.xlsx' criada com sucesso!")
