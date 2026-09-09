# FarmTech Solutions - Machine Learning

## Integrante

- Angelina Nogueira da Silva

---

# Entrega 1 - Machine Learning

## Sobre o projeto

Este projeto foi desenvolvido para a FarmTech Solutions com o objetivo de utilizar técnicas de Machine Learning para analisar dados agrícolas, identificar padrões de produtividade e realizar previsões de rendimento das culturas.

A solução utiliza informações relacionadas às condições climáticas e ao tipo de cultura para explorar os dados e construir modelos capazes de prever o rendimento agrícola.

O desenvolvimento completo da solução está disponível no Jupyter Notebook, que apresenta o passo a passo da análise, desde a exploração dos dados até a avaliação e comparação dos modelos preditivos.

## Base de dados

A base utilizada no projeto é composta por 156 registros e apresenta informações sobre quatro culturas agrícolas:

- Cocoa, beans
- Oil palm fruit
- Rice, paddy
- Rubber, natural

As variáveis utilizadas são:

- Precipitation (mm day-1)
- Specific Humidity at 2 Meters (g/kg)
- Relative Humidity at 2 Meters (%)
- Temperature at 2 Meters (C)
- Yield

## Metodologia

A solução foi desenvolvida em etapas, envolvendo:

- Análise exploratória dos dados;
- Estatísticas descritivas;
- Análise do rendimento por cultura;
- Identificação de possíveis outliers;
- Análise de correlação entre as variáveis;
- Clusterização utilizando K-Means;
- Avaliação dos clusters por meio do Silhouette Score;
- Desenvolvimento de cinco modelos de regressão;
- Avaliação utilizando MAE, RMSE e R²;
- Validação cruzada com 5 folds;
- Seleção do modelo de melhor desempenho;
- Realização de uma previsão utilizando o modelo final.

## Clusterização

Foi utilizado o algoritmo K-Means para identificar diferentes padrões nos dados.

Foram avaliadas configurações de 2 a 6 clusters utilizando o Silhouette Score. O melhor resultado foi obtido com 5 clusters.

A análise permitiu identificar grupos com diferentes padrões de condições ambientais e rendimento.

É importante destacar que o rendimento foi utilizado juntamente com as variáveis climáticas na formação dos clusters. Portanto, os resultados não devem ser interpretados como evidência de uma relação causal entre as condições climáticas e a produtividade.

## Modelos preditivos

Foram desenvolvidos cinco modelos de regressão:

1. Regressão Linear
2. Árvore de Decisão
3. Random Forest
4. KNN
5. SVR

Os modelos foram avaliados utilizando as métricas:

- MAE (Mean Absolute Error);
- RMSE (Root Mean Squared Error);
- R² (Coeficiente de Determinação).

Para tornar a avaliação mais robusta, também foi utilizada validação cruzada com 5 folds.

## Resultados

Após a validação cruzada, o Random Forest apresentou o melhor desempenho geral entre os modelos avaliados.

| Modelo | MAE médio | RMSE médio | R² médio |
|---|---:|---:|---:|
| Regressão Linear | 5.087,74 | 7.874,35 | 0,9870 |
| Árvore de Decisão | 4.988,17 | 8.585,00 | 0,9843 |
| Random Forest | **4.291,63** | **7.548,43** | **0,9878** |
| KNN | 5.413,41 | 10.249,49 | 0,9774 |
| SVR | 48.092,20 | 79.664,62 | -0,3082 |

Considerando as três métricas, o Random Forest foi selecionado como o modelo de melhor desempenho.

## Previsão prática

Após a seleção do Random Forest, foi realizada uma previsão utilizando uma nova condição de cultivo para a cultura Rice, paddy.

Para as condições utilizadas no teste, o modelo apresentou:

**Rendimento previsto: 28.760**

Essa etapa demonstra uma aplicação prática do modelo, permitindo estimar o rendimento esperado a partir das condições fornecidas.

## Pontos fortes

- Avaliação de cinco algoritmos diferentes de Machine Learning;
- Utilização de métricas complementares;
- Aplicação de validação cruzada com 5 folds;
- Comparação objetiva entre os modelos;
- Utilização de técnicas de aprendizado supervisionado e não supervisionado;
- Realização de uma previsão prática utilizando o modelo selecionado.

## Limitações

- A base de dados possui apenas 156 registros;
- Existem diferenças significativas de rendimento entre as culturas;
- A clusterização utilizou o rendimento juntamente com as variáveis climáticas;
- A base possui uma quantidade limitada de variáveis para explicar o rendimento agrícola;
- Os valores de rendimento devem ser interpretados de acordo com a unidade e escala fornecidas na base de dados.

## Jupyter Notebook

O Jupyter Notebook contém o desenvolvimento completo da solução, incluindo o tratamento e exploração dos dados, clusterização, treinamento dos modelos, avaliação, validação cruzada e previsão.

**Acessar o Jupyter Notebook:**

https://colab.research.google.com/drive/1hi-Y8iwaQCnhd8NgY5ifkIPS3zO6Lqa2?usp=sharing


