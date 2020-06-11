#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[4]:


black_friday.head()


# In[5]:


resp1= black_friday.shape 
resp1


# In[6]:


black_friday.Age.value_counts()


# In[7]:


black_friday.Age =='26-35'


# In[8]:


q2= black_friday[black_friday.Age=='26-35']
q2.columns


# In[9]:


resp21= q2.groupby('Gender')['User_ID'].nunique()[0]
resp2= int(resp21)
resp2


# In[10]:


resp22 = black_friday.loc[(black_friday.Gender == "F") & (black_friday.Age == '26-35'), :].shape[0]
resp2c = int(resp22)
resp2c


# In[11]:


q3=black_friday.User_ID
resp3= q3.nunique()
resp3


# In[12]:


resp4=black_friday.dtypes.nunique()


# In[13]:


q5 = black_friday.isna().sum()/black_friday.shape[0]
resp5 =float(q5.Product_Category_3)
resp5


# In[14]:


resp6 = black_friday.isna().sum().max()
resp6


# In[15]:


resp7 = black_friday.Product_Category_3.value_counts().index[0]
resp7


# In[16]:


resp81 = (black_friday.Purchase - min(black_friday.Purchase))/(max(black_friday.Purchase)-min(black_friday.Purchase))
resp8= resp81.mean()
resp8


# In[17]:


pad= (black_friday.Purchase-black_friday.Purchase.mean())/(black_friday.Purchase.std())
resp91 = ((pad >=-1) & (pad <=1)).sum()
resp9 = int(resp91)
resp9


# In[28]:


boolean = black_friday['Product_Category_2'].isna().isin(black_friday['Product_Category_3'].isna())   
resp10= bool([boolean])
resp10


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[19]:


def q1():
    
    return resp1


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[286]:


def q2():
    
    return resp2c


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[287]:


def q3():
   
    return  resp3


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[288]:


def q4():
   
    return  resp4


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[289]:


def q5():
    
    return resp5


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[290]:


def q6():
    
    return resp6


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[291]:


def q7():
   
    return  resp7


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[292]:


def q8():
    
    return resp8


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[293]:


def q9():
    
    return resp9


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[29]:


def q10():
   
 return resp10

