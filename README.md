# 🛣️ Análise de Dados de Acidentes - 2025

Este repositório contém duas análises exploratórias da base de dados pública de acidentes de trânsito, realizadas em momentos diferentes do meu processo de aprendizado em Análise de Dados.

---

## 📁 Estrutura do Projeto

```BigData-Senai/
├── Introducao_spark/
├── Importando_arquivo_CSV/
├── Consumindo_Api_test/
├── Analise_com_pyspark/
├── 1-Projeto/
├── 2-Projeto/
├── 3-Projeto/
├── 4-Projeto/
├── 5-Projeto/
├── 6-Projeto/
│   ├── Data/
│   │   └── raw/
│   │       └── Download_base_dados.txt
│   ├── Analise_De_Acidentes_2024_.ipynb      # Primeira análise (Spark)
│   ├── Analise_De_Acidentes_2024_v2.ipynb    # Segunda análise (Pandas)
│   ├── Analise_De_Acidentes_2024_.py         # Script da análise 1
│   └── Analise_De_Acidentes_2024_v2.py       # Script da análise 2
├── notebooks/
└── Script/```


> 🔍 Os projetos finais estão localizados na pasta `6-Projeto`.

---

## 🧠 Sobre as Análises

### 1. Primeira Análise – PySpark (`6-Projeto/notebooks/Analise_De_Acidentes_2024_.ipynb`)

A primeira versão da análise foi feita com PySpark, com o objetivo de treinar conceitos de processamento distribuído e ETL em larga escala. Nesta fase, o foco foi a familiarização com a base e experimentos simples.

**O que foi feito:**

- Leitura do arquivo CSV com Spark
- Verificação do schema
- Contagem de valores nulos
- Análise e construção de gráfico

⚠️ **Nota:** Nesta fase, ainda não possuía uma visão crítica mais aprofundada sobre qualidade de dados.

---

### 2. Segunda Análise – Pandas (`6-Projeto/notebooks/Analise_De_Acidentes_2024_v2.ipynb`)

Após um período estudando mais sobre Análise de Dados, fiz uma nova abordagem com Pandas. Dessa vez, com mais conhecimento técnico e um olhar mais atento à qualidade da base.

**Destaques:**

- Remoção de colunas irrelevantes
- Análise detalhada de valores nulos e duplicações
- Investigações específicas em colunas como `tipo_envolvido`, `tipo_veiculo`, `km` e `id`
- Cálculo de médias e variações por estado
- Verificação de viabilidade da base para análises confiáveis

🧩 **Conclusão:** Apesar de parecer promissora, constatei que a base de dados possui inconsistências e falhas que dificultam análises reais mais precisas e confiáveis. Muitos registros estão duplicados ou incompletos.

---

## 🙏 Considerações Finais

Este projeto foi uma forma prática de consolidar meu aprendizado em ferramentas como **Spark** e **Pandas**, além de me ajudar a desenvolver um olhar crítico sobre dados públicos.  
Ainda estou em processo de evolução, e compartilho este repositório com **humildade e transparência**, para mostrar meu aprendizado.

---

## 📚 Tecnologias Usadas

- Python 3.11
- PySpark
- Pandas
- Seaborn / Matplotlib
- VSCode / Jupyter Notebook

---

## ✍️ Autor

**Lucas Xavier dos Santos Bento**  
📧 lucas.xavier.b7@gmail.com  
🔗 [linkedin.com/in/lucasxavier7](https://www.linkedin.com/in/lucasxavier7)

Aprendendo Análise de Dados com prática, erros e progresso constante.
