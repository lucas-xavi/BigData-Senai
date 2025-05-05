# 📊 Curso de Big Data - SENAI  
**Projetos práticos com PySpark, ETL e Análise de Dados**

[![PySpark](https://img.shields.io/badge/Big%20Data-PySpark-blue?logo=apache-spark&logoColor=white)](https://spark.apache.org/)
[![Pandas](https://img.shields.io/badge/Análise-Pandas-yellow?logo=pandas)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Projetos-Concluídos-brightgreen)]()
[![License](https://img.shields.io/badge/Licença-MIT-lightgrey)]()

---

## 🧠 Competências Desenvolvidas  

| Módulo                | Habilidades Principais                              |
|-----------------------|-----------------------------------------------------|
| 🔹 Introdução ao Spark| Processamento distribuído com DataFrames            |
| 📥 Importação de CSV  | Ingestão de grandes volumes com otimizações         |
| 🌐 Consumo de API     | Leitura e tratamento de dados REST/JSON             |
| 📊 Análise com PySpark| Agregações, filtros, joins escaláveis               |
| 🧪 Projetos 1 a 5     | Pipelines ETL, visualizações e refino de dados      |
| ⭐ Projeto Final       | Comparação PySpark × Pandas, análise crítica        |

---

## 🗂️ Estrutura de Projetos  

```bash
BigData-Senai/
├── Introducao_spark/           # Fundamentos do Spark
├── Importando_arquivo_CSV/    # Ingestão de dados massivos
├── Consumindo_Api_test/       # Integração com APIs externas
├── Analise_com_pyspark/       # Processamento com PySpark
├── 1-Projeto/                 # Consumindo dados CSV
├── 2-Projeto/                 # Criação de um dicionário python e ETL
├── 3-Projeto/                 # ETL e Análise de dados com PySpark
├── 4-Projeto/                 # Análise com comandos SQL e PySpark
└── 5-Projeto/                 # Projeto Final
```

---

## ⭐ Projeto Final — Análise de Acidentes

### 📌 Objetivo  
Validar a viabilidade de uma base pública para análises reais de acidentes de trânsito, usando PySpark e Pandas.

---

### 🔄 Comparativo de Abordagens

| 🧪 PySpark (Versão 1)         | 🐼 Pandas (Versão 2)               |
|------------------------------|------------------------------------|
| ✔️ Processamento em cluster   | ✔️ Validação de dados brutos        |
| 📊 Gráficos descritivos       | 🔍 Verificação de inconsistências   |
| 📈 Métricas básicas           | ❓ Questionamento de variáveis       |

---

### 🔍 Principais Descobertas

- **Distorção de IDs**:
  ```python
  contagem_ids.show()  # IDs com até 1.540 repetições → erro de coleta
  ```

- **Erro de interpretação na coluna km**:
  - Interpretação inicial: velocidade média  
  - Correção: marcador geográfico  
  - **Variação**: média de 9.045,89 → análise inviável  

---

## 💬 Lições Aprendidas

- 🔧 **Validação é essencial**: grandes volumes podem conter distorções sérias  
- 🔄 **Ferramentas são meios**: migrar de Spark para Pandas quando necessário  
- 💡 **Pensamento crítico > gráfico bonito**: questionar os dados, não só visualizá-los  

---

## ✅ Diferenciais do Curso

- 🔁 **Hands-on real**: 100% prático, sem foco em "receitas prontas"  
- 🧭 **Erros como aprendizado**: problemas reais discutidos, não mascarados  

---

## 🧭 Preparação para o Mercado

- 🧩 **Domínio do ciclo de dados**: da ingestão à comunicação dos resultados  
- 🧠 **Consciência técnica**: saber quando trocar de ferramenta ou abordagem  

---

## ✍️ Autor

> _"Aprendi que em Big Data, tão importante quanto processar é saber o que processar."_

**👤 Lucas Xavier**  
📎 [GitHub](https://github.com/lucas-xavi)  
🔗 [LinkedIn](https://www.linkedin.com/in/lucasxavier7)
