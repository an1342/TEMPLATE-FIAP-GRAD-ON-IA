
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

**Acesse o Jupyter Notebook:**
https://colab.research.google.com/drive/1hi-Y8iwaQCnhd8NgY5ifkIPS3zO6Lqa2?usp=sharing


---

# Entrega 2 - Computação em Nuvem com AWS

## Estimativa de custos

Para hospedar a API responsável por receber os dados dos sensores e executar o modelo de Machine Learning, foi realizada uma estimativa utilizando a AWS Pricing Calculator.

A configuração considerada foi:

- Sistema operacional: Linux;
- Processadores: 2 vCPUs;
- Memória: 1 GiB;
- Rede: até 5 Gbps;
- Armazenamento: 50 GB;
- Modelo de cobrança: On-Demand;
- Utilização: 730 horas por mês;
- Quantidade: 1 instância.

A instância utilizada na estimativa foi a **t3.micro**.

## Comparação entre as regiões

Foram comparadas as regiões **South America (São Paulo)** e **US East (N. Virginia)**.

| Região | EC2 On-Demand | EBS - 50 GB | Custo mensal total |
|---|---:|---:|---:|
| São Paulo | US$ 12,26 | US$ 7,60 | **US$ 19,86** |
| Norte da Virgínia | US$ 7,59 | US$ 4,00 | **US$ 11,59** |

A região Norte da Virgínia apresentou o menor custo mensal, com aproximadamente **US$ 11,59**, enquanto São Paulo apresentou custo mensal de **US$ 19,86**.

Portanto, considerando exclusivamente o preço, a região Norte da Virgínia seria a opção mais barata.

## Justificativa da escolha

Apesar de a região Norte da Virgínia apresentar menor custo, a solução escolhida para este projeto seria a região de **São Paulo**.

Essa escolha ocorre devido à restrição legal apresentada no enunciado em relação ao armazenamento de dados no exterior.

Como a aplicação receberá dados provenientes dos sensores da fazenda, manter os recursos na região de São Paulo permite que os dados permaneçam armazenados no Brasil, atendendo à restrição apresentada.

Além disso, manter a infraestrutura mais próxima da origem dos dados pode contribuir para reduzir a distância entre os sensores e a aplicação, favorecendo o acesso aos dados.

Dessa forma, mesmo apresentando um custo mensal maior, **São Paulo é a opção mais adequada para o cenário proposto**, considerando os requisitos legais e operacionais.

## Imagens da AWS Pricing Calculator

Nesta seção serão apresentadas as imagens utilizadas para demonstrar as configurações e os resultados da AWS Pricing Calculator.

### Configuração - São Paulo
<img width="934" height="749" alt="Captura de tela 2026-09-08 233621" src="https://github.com/user-attachments/assets/4c15319d-cfef-4b86-a2df-43ee3b5a425f" />
<img width="942" height="790" alt="Captura de tela 2026-09-08 233659" src="https://github.com/user-attachments/assets/ab0bfc7b-146c-4ec1-b11f-b68879c37156" />
<img width="922" height="783" alt="Captura de tela 2026-09-08 233713" src="https://github.com/user-attachments/assets/c2ab65a9-87b8-49f6-894a-467f0a5fc782" />
<img width="935" height="785" alt="Captura de tela 2026-09-08 233737" src="https://github.com/user-attachments/assets/6aac81e3-26fb-4164-941e-38050b01b10e" />
<img width="943" height="853" alt="Captura de tela 2026-09-08 233805" src="https://github.com/user-attachments/assets/fddc5b49-ffb4-4838-b025-136c0ef6a52e" />

### Configuração - Norte da Virgínia
<img width="1853" height="681" alt="Captura de tela 2026-09-08 232427" src="https://github.com/user-attachments/assets/50afdff6-3ec5-4df2-a0a6-38a083bedef9" />

<img width="1855" height="741" alt="Captura de tela 2026-09-08 232450" src="https://github.com/user-attachments/assets/dfc53f98-d11f-4d0c-812c-d8e9e019f7ea" />
<img width="1854" height="742" alt="Captura de tela 2026-09-08 232503" src="https://github.com/user-attachments/assets/01d21a79-bed6-4863-9b53-61aef2fab314" />
<img width="1813" height="169" alt="Captura de tela 2026-09-08 232602" src="https://github.com/user-attachments/assets/75946fbb-554f-401e-bb95-65fa86e2a0ec" />
<img width="1833" height="720" alt="Captura de tela 2026-09-08 232625" src="https://github.com/user-attachments/assets/11000352-c915-40da-9290-f8f4bc1f8ce3" />
<img width="1453" height="799" alt="Captura de tela 2026-09-08 232640" src="https://github.com/user-attachments/assets/886ab847-5779-40be-bde1-66d41e7706a8" />




### Comparação dos custos

<img width="1780" height="283" alt="image" src="https://github.com/user-attachments/assets/065845f9-ed9e-4ffb-baa2-cffdeaecaabc" />


---

# Tecnologias utilizadas

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- AWS Pricing Calculator
- GitHub




