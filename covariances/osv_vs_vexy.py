import pandas as pd
from jaccard_index import jaccard_index
import sys
sys.path.insert(0, '/Users/katushka/Documents/VEX_JSON')
from json_parser_vexy import create_df as create_vexy_df
from json_parser_osv import create_df as create_osv_df

if __name__ == "__main__":
    df_vexy = create_vexy_df()
    df_osv = create_osv_df()

    #df_osv = df_osv[~df_osv['VulnerabilityID'].str.contains('TEMP', na=False)]
    #df_vexy = df_vexy[~df_vexy['VulnerabilityID'].str.contains('TEMP', na=False)]

    result, intersection_df = jaccard_index(df_vexy, df_osv)
    
    print(f"Jaccard Index: {result}")
    print(intersection_df)