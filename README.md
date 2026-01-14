# Titanic Survival Prediction 🚢
Este projeto utiliza técnicas de Machine Learning para prever a probabilidade de sobrevivência dos passageiros do Titanic. O objetivo principal é responder à pergunta: "Quais tipos de pessoas tinham maior probabilidade de sobreviver?" utilizando dados históricos como idade, sexo, classe social,

## Tecnologias e Bibliotecas
O projeto foi desenvolvido em Python, utilizando as seguintes bibliotecas:

- Manipulação de Dados: pandas, os
- Visualização: matplotlib, yellowbrick
- Machine Learning: scikit-learn, xgboost
- Métricas e Avaliação: Matriz de Confusão, Curva ROC (AUC), Learning Curves e Validação Cruzada (StratifiedKFold).

![alt text](/images/image.png)

## Modelos Testados
Para encontrar o melhor desempenho, o projeto explora diversos algoritmos de classificação:
- Regressão Logística (LogisticRegression)
- Árvores de Decisão (DecisionTreeClassifier)
- Random Forest (RandomForestClassifier)
- K-Nearest Neighbors (KNeighborsClassifier)
- Support Vector Machine (SVC)
- Naive Bayes (GaussianNB)
- XGBoost (XGBClassifier)

## Avaliação de Desempenho
O projeto utiliza a biblioteca Yellowbrick para visualizações avançadas de diagnóstico de modelo, incluindo:
- Confusion Matrix: Para visualizar erros de falso positivo e falso negativo.
- ROC/AUC Curve: Para medir a capacidade de separação das classes do modelo.
- Learning Curve: Para detectar problemas de overfitting ou underfitting.

## Fluxograma: Preparação do Ambiente
```mermaid
flowchart TD
    A[uv init] 
    H{Dentro uma pasta}
    G2[uv venv]
    G3[source ./.venv/bin/activate]
    B[uv init NOMEDAPASTA]
    C{não precisa de um 'mkdir}
    D[uv pip install ipykernel]
    E[uv add ipykernel]
    I[uv add jupyter-core]
    F[uv run ipython kernel install --user --name='my_project_kernel']
    G[jupyter kernelspec list]
    Z1[Python]
    G1[uv add AAAAA]
    

    A --> H
    A -->|OU| B
    B --> C
    B -->G2
    G2 --> G3
    G3--> D
    D -->|OU| E
    E -->I
    I-->F
    F--> G
    G-->G1
    G1 -->|o antônimo| Z4(uv remove AAAA)
    G1 -->|Instalar| Z1{Python já vem no venv init}
    G1-->|Instalar| P[matplotlib]--> Z2
    G1 -->|Instalar| Q[Pandas]-->Z2
    G1 -->|Instalar| K[seaborn]-->Z2
    G1 -->|Instalar| L[numpy]-->Z2
    G1 -->|Instalar| M[scikit-learn]-->Z2
    G1 -->|Instalar| O[seaborn]-->Z2
    Z1 -->Z2[uv sync]
    Z2 --> Z3{Ambiente implementado}

%% Individual node styling. Try the visual editor toolbar
%%style C color:#FFFFFF, fill:#AA0OFF, stroke: #AA@OFF
style C color:#FFFFFF, stroke: #00C853, fill:#00C853
style Z1 color:#FFFFFF, stroke: #2962FF, fill:#2962FF

```

## A ideia bruta do nosso projeto
 ```mermaid
 flowchart TD
    A[Início] --> R(Estudar o problema)
    R --> |Criar projeto| B(Estruturar pastas)
    B --> |Download| G(Data)
    G --> H[Raw]
    H -->|Cortar| W[30% Dados de Validação]
    H -->|Cortar| Z[70% Dados de Treinamento]
    Z --> I[processed]
    G --> J[Post-prosseced]
    I --> |tratamento tipo:| M[Valores nulos]
    I --> |tratamento tipo:| S[Limpeza]
    I --> |tratamento tipo:| T[Missing data]
    I --> |tratamento tipo:| U[normalização]
    I --> |tratamento tipo:| V[codificando variáveis categôricas]
```
## A ideia do nosso machine learning
```mermaid
 flowchart TD
    A[Faça uma pergunta]
    B[Colete os dados]
    C[Crie os atributos]
    D[Limpe os dados]
    E[Normalize os dados]
    F[Dados das amostras]
    G[Dados de treinamento]
    H[Crie o modelo]
    K[Avalie o modelo]
    L[Mude a pergunta]
    M[Implante o modelo]
    N[Dados de teste]

    A-->B
    B-->C
    B-->D
    C-->E
    D-->E
    E-->F
    F-->N
    F-->G
    G-->H
    H-->K
    K-->M
    K-->L
    L-->A
    K-->A
    N-->K
```

## Resultados

