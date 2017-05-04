"""Function that imports a csv_file to a pandas dataframe"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs

def csv_to_dataframe(filepath):

    df = pd.read_csv(filepath)

    print "Head {}".format(df.head())
    print "=============================="
    print "Columns {}".format(df.columns)
    print "=============================="
    print "Short Summary {}".format(df.describe().T)
    print "=============================="
    print "Info {}".format(df.info())

    return df

def hist_plot(arr, bins=40):
    pass



if __name__ == '__main__':
    main()
