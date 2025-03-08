import pandas as pd
import numpy as np

def modified_jaccard_4(df1, df2, df3, df4):
    set1 = set(df1['VulnerabilityID'].astype(str) + "/" + df1['Container'].astype(str))  #+ "/" + df1['Severity'].astype(str).str.upper())
    set2 = set(df2['VulnerabilityID'].astype(str) + "/" +  df2['Container'].astype(str)) #+ "/" + df2['Severity'].astype(str).str.upper())
    set3 = set(df3['VulnerabilityID'].astype(str) + "/" +  df3['Container'].astype(str)) #+ "/" + df3['Severity'].astype(str).str.upper())
    set4 = set(df4['VulnerabilityID'].astype(str) + "/" +  df4['Container'].astype(str)) #+ "/" + df4['Severity'].astype(str).str.upper())


    intersection = set1.intersection(set2).intersection(set3).intersection(set4)
    union = set1.union(set2).union(set3).union(set4)
    
    jaccard_index = len(intersection)/len(union)

    intersection_df = pd.DataFrame(list(intersection), columns=['Vulnerability'])
    intersection_df[['VulnerabilityID', 'Container']] = intersection_df['Vulnerability'].str.split('/', expand=True)
    intersection_df.drop(columns=['Vulnerability'], inplace=True)
    
    return jaccard_index, intersection_df

