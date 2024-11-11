# BASICS OF PYTHON (DATA SCIENCE)
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import scipy
warnings.filterwarnings("ignore")
data = pd.read_csv(r"C:\Users\G Rishika\Downloads\auto_mpg.csv")
#print(data)

print(data.describe())
