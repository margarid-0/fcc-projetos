import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1: Carregar os dados a partir do arquivo CSV
df = pd.read_csv('medical_examination.csv')

# 2: Adicionar uma coluna "overweight" com valor 1 se o IMC > 25, caso contrário 0
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3: Normalizar os dados para as colunas 'cholesterol' e 'gluc'
df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0)
df['gluc'] = df['gluc'].apply(lambda x: 1 if x > 1 else 0)

# 4: Função para desenhar o gráfico categórico
def draw_cat_plot():
    # Criar DataFrame para o gráfico categórico
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Agrupar os dados por categoria e contar o total de cada valor
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size()

    # Ajustar o nome da coluna para "total" em vez de "size"
    df_cat.rename(columns={'size': 'total'}, inplace=True)

    # Desenhar o gráfico categórico com seaborn
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').fig

    # Salvar a figura em um arquivo
    fig.savefig('catplot.png')
    return fig


# 10: Função para desenhar o mapa de calor
def draw_heat_map():
    # 11: Limpar os dados
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12: Calcular a correlação
    corr = df_heat.corr()

    # 13: Gerar uma máscara para o triângulo superior da matriz de correlação
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14: Desenhar o mapa de calor com seaborn
    fig, ax = plt.subplots(figsize=(12, 12))
    sns.heatmap(corr, annot=True, fmt='.1f', mask=mask, square=True, linewidths=1, ax=ax)

    # 15: Salvar a figura em um arquivo
    fig.savefig('heatmap.png')
    return fig