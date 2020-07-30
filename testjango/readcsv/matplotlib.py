import numpy as np
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt
from .models import CsvData

def matplotlib_graph(request):
    df = pd.DataFrame(list(CsvData.objects.all().values()))
    df.drop(['Unnamed: 0'],axis='columns', inplace=True)
    delete_rownum = [0,1]
    df = df.drop(delete_rownum)
    df = df.reset_index(drop=True)
    plt.figure(figsize=(15,10))
    plt.scatter(x='UTC', y='Master Offset', data=df)
    plt.xticks(np.arange(0,310,step=10), ["{:0<2d}".format(x) for x in np.arange(0,310, step=10)],
              fontsize=10,
              rotation=45)
    plt.ylim(-6000,8000)
    plt.xlabel('Running Time (sec)', labelpad=30, fontsize=15)
    plt.ylabel('Offset', labelpad=30, fontsize=15)
    plt.title('Offset during 5min', pad=30, fontsize=20)
    plt.savefig('/home/rtst15/a.png')