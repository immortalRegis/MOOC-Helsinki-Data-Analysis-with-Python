#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    df = pd.DataFrame({'State':['United Kingdom', 'Finland', 'USA', 'Sweden', 'Germany','Russia'],'Year of independence':[np.nan, 1917,1776,1523,np.nan,1992],'President':[None, 'Niinistö','Trump',None,'Steinmeier','Putin']})
    df = df.set_index('State')
    return df



def main():
    missing_value_types()

if __name__ == "__main__":
    main()
