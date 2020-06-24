import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def open_file(path):
    df = pd.read_csv(path)
    return df

def get_cols(df):
    return list(df.columns)
    
def get_mean(df, col):
    try:
        mean = df[col].mean()
    except: 
        mean = None
    return mean

def get_plot(df, num_var1, num_var2, cat_var):
    plot = sns.scatterplot(x = num_var1, 
                           y = num_var2,
                           hue = cat_var,
                           data = df)
    plt.savefig("0.png")
    return plot