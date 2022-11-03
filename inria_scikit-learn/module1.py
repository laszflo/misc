# %% open data from csv

import pandas as pd
data = pd.read_csv('/home/ubuntu/test_FL/software_pdf/prod_stat.csv')

# %% data quick visualization

data.head()

# %% to see the repartition of one column

data['Producer'].value_counts()

# %% differentiation between numerical and categorical data

numerical_columns = "nb_of_use"
categorical_columns = "Producer"
target_column = "perc_of_fake (%)"

all_columns = numerical_columns + categorical_columns + target_column

print("the data set contains {} samples and {} features".format(data.shape[0], data.shape[1]-2))

# %% visualization of the data before building a model

_ = data.hist(figsize=(20, 14))
# _ = is used to avoid the output of the function

# %% pay attention to the imbalance of the data
# for instance there is a lot more females than males in a data
# can raise a problem of fairness fairlearn.org

# we can also have correlated features 
pd.crosstab(index=data["nb_of_use"], columns=data["perc_of_fake (%)"])

# for every entry, if we have only one value in this array, this means that the two features are correlated

# data can be inspected with seaborn

# if target column is imbalanced we can have a problem 
# correlated features are a problem
# linear models can only capture linear relationships contrary to decision trees

# %%

