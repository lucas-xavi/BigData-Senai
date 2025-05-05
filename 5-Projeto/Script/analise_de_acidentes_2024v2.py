# Importando algumas das bibliotecas necessárias para a análise e criação dos gráficos
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Caminho para o arquivo da análise
path = 'data/acidentes2025_todas_causas_tipos.csv'

# Criado a função createDataFrame para usar o DataFrame.
def createDataFrame() -> pd.DataFrame:
    data = pd.read_csv(path, delimiter=';', low_memory=False, encoding='UTF-8', dtype=str)
    df = pd.DataFrame(data)
    
    #Removi as colunas latitude, longitude, regional, delegacia, uop, pois não considero importante para minha análise.
    df.drop(columns=['latitude','longitude','regional','delegacia','uop'],inplace=True) 
    
    return df

def main():
    # Armazenando a função createDataFrame na váriavel df.
    df = createDataFrame()

    # Código para ver o schema do DataFrame.
    #df.info()

    # Visualização dos 5 primeiros registros.
    df.head()

    # Pesquisando por tipo_envolvido, para se ter uma visão mais amplas sobre os dados nullos.
    df[df['tipo_envolvido'].isna()].sample(5)

    # Filtrei por alguns Ids, pois a cada vez que verificava, tinha-se muitos ids com multiplos registros.
    df[df['id']== '661121']

    # Selecionei a coluna tipo_envolvido, para saber os valores que nela continha e qual a relação com o tipo_veiculo, após a análise superficial acima.
    df['tipo_envolvido'].unique()

    # Tive uma dúvida em relação a tipo_envolvido e tipo_veiculo = Semireboque, então usei os códigos abaixos para saber se todo tipo_veiculo = Semireboque tinha o valor NaN.
    df[df['tipo_veiculo'] == 'Semireboque']['tipo_envolvido'].isna().all()

    #Mostra quantos registros em cada coluna, tem o valor Null
    df.isnull().sum()

    #Média em porcentagem, para saber quantos valores são nullos
    df.isnull().mean() * 100

    # Verificação da coluna KM, pois mesmo com análise interior, não fazia sentido alguns dados nesse arquivo, como KM = 424,6 
    df[['km']]
    df['km'].unique()
    #Ao verificar e pesquisar um pouco, descobri que a coluna KM se trata do kilometro e não da velocidade ao qual o(s) condutor(es) estavam.

    # Média de acidentes por estado (com todos os dados)
    media_completa = df.groupby('uf').size().mean()
    print(media_completa)

    # Convertendo KM para tipo númerico, para fazer a média
    df['km'] = pd.to_numeric(df['km'], errors='coerce') # coerce é para que se a conversão não for bem sucedida, ele retornarar NaN
    df_validos = df[df['km'].notnull()]

    # Média por estado com dados válidos
    media_filtrada = df_validos.groupby('uf').size().mean()

    # Cálculando a variancia, para saber se a tabela está usável depois das dúvidas
    variancia = media_completa - media_filtrada
    print(f"Variação entre as médias: {variancia:.2f}")

    # Além da variação extremamente alta, há muitos registros em um único id
    df['id'].value_counts().head(10)

if __name__ == "__main__":
    main()