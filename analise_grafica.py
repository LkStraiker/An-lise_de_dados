import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Carregar os dados do Excel
df = pd.read_excel('administracao_loja.xlsx')

# Criar o aplicativo Dash
app = dash.Dash(__name__)

# Definir cores personalizadas
cor_primaria = '#FF5733'  # Laranja neon
cor_secundaria = '#FFFF00'  # Amarelo neon
cor_texto = '#FFFFFF'  # Branco

# Layout do aplicativo
app.layout = html.Div(style={'backgroundColor': '#000000', 'padding': '20px'}, children=[
    html.H1("Dashboard de Análise de Dados da Loja de Mercado", style={'color': cor_primaria, 'text-align': 'center', 'margin-bottom': '30px'}),

    html.Div(className='row', children=[
        html.Div(className='six columns', children=[
            dcc.Graph(
                id='vendas-totais',
                figure=px.line(df, x='Data', y='Vendas Totais (R$)', title='Vendas Totais ao Longo do Tempo')
                          .update_traces(line_color=cor_primaria)
                          .update_layout(margin=dict(l=20, r=20, t=50, b=20), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
                          .update_layout(height=400)
            ),
            html.P("Este gráfico mostra a evolução das vendas totais ao longo do tempo, permitindo identificar tendências e padrões de comportamento.", style={'color': cor_texto})
        ]),

        html.Div(className='six columns', children=[
            dcc.Graph(
                id='clientes-atendidos',
                figure=px.bar(df, x='Data', y='Clientes Atendidos', title='Clientes Atendidos por Dia', color_discrete_sequence=[cor_primaria])
                          .update_layout(margin=dict(l=20, r=20, t=50, b=20), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
                          .update_layout(height=400)
            ),
            html.P("Este gráfico exibe o número de clientes atendidos por dia, ajudando a avaliar o volume de demanda ao longo do tempo.", style={'color': cor_texto})
        ])
    ], style={'margin-bottom': '30px'}),

    html.Div(className='row', children=[
        html.Div(className='six columns', children=[
            dcc.Graph(
                id='itens-vendidos',
                figure=px.scatter(df, x='Clientes Atendidos', y='Itens Vendidos', title='Itens Vendidos vs. Clientes Atendidos', color='Itens Vendidos', color_continuous_scale=px.colors.sequential.Viridis)
                          .update_traces(marker=dict(color=cor_primaria))
                          .update_layout(margin=dict(l=20, r=20, t=50, b=20), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
                          .update_layout(height=400)
            ),
            html.P("Este gráfico analisa a relação entre o número de clientes atendidos e o volume de itens vendidos, identificando possíveis correlações.", style={'color': cor_texto})
        ]),

        html.Div(className='six columns', children=[
            dcc.Graph(
                id='lucro-por-dia',
                figure=px.line(df, x='Data', y='Lucro Bruto (R$)', title='Lucro Bruto ao Longo do Tempo')
                          .update_traces(line_color=cor_primaria)
                          .update_layout(margin=dict(l=20, r=20, t=50, b=20), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
                          .update_layout(height=400)
            ),
            html.P("Este gráfico exibe a evolução do lucro bruto ao longo do tempo, permitindo avaliar o desempenho financeiro da empresa.", style={'color': cor_texto})
        ])
    ])
])

# Executar o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
