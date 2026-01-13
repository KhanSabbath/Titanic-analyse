import pandas as pd

# Create a sample DataFrame
data = {'Color': ['Red', 'Green', 'Blue', 'Green', 'Red'],
        'Size': ['S', 'M', 'L', 'M', 'S']}
df = pd.DataFrame(data)
print(df.dtypes)

# Convert categorical columns to dummy variables
df_encoded = pd.get_dummies(df)

#print(df_encoded)

if 'Name' in df.columns:
	name = df['Name']
	print(f'a cabeça do nosso objeto names: {name.head(3)}')
elif 'orig_df' in globals() and 'Name' in orig_df.columns:
	name = orig_df['Name']
	print("Coluna 'Name' não está em df atual; obtendo 'Name' de orig_df.")
	print(f'a cabeça do nosso objeto names: {name.head(3)}')

	
# IterativeImputer está em sklearn.impute — não é necessário (nem existe) 'enable_iterative_import'
from sklearn.impute import IterativeImputer

# Colunas numéricas a imputar (use nomes como strings)
num_cols = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']

# verificar quais colunas realmente existem nos dataframes (evita KeyError)
num_cols = [c for c in num_cols if c in X_train.columns]

imputer = IterativeImputer(random_state=0)
X_train.loc[:, num_cols] = imputer.fit_transform(X_train[num_cols])
X_test.loc[:, num_cols] = imputer.transform(X_test[num_cols])

# preencher possíveis NaNs restantes com a mediana do conjunto de treino (aplicado às colunas numéricas)
meds = X_train[num_cols].median()
X_train.loc[:, num_cols] = X_train[num_cols].fillna(meds)
X_test.loc[:, num_cols] = X_test[num_cols].fillna(meds)