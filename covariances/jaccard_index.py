import pandas as pd

def jaccard_index(df1:pd.core.frame.DataFrame, df2:pd.core.frame.DataFrame):
    set1 = set(df1['VulnerabilityID'].astype(str) + "/" + df1['Container'].astype(str)) #+ "/" + df1['Severity'].astype(str).str.upper())
    set2 = set(df2['VulnerabilityID'].astype(str) + "/" +  df2['Container'].astype(str)) #+ "/" + df1['Severity'].astype(str).str.upper())

    intersection = set1.intersection(set2)
    union = set1.union(set2)
    
    jaccard_index = len(intersection) / len(union)
    intersection_df = pd.DataFrame(list(intersection), columns=['Vulnerability'])
    intersection_df[['VulnerabilityID', 'Container']] = intersection_df['Vulnerability'].str.split('/', expand=True)
    intersection_df.drop(columns=['Vulnerability'], inplace=True)
    
    return jaccard_index, intersection_df


