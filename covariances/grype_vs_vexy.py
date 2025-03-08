import pandas as pd
from jaccard_index import jaccard_index
import sys
sys.path.insert(0, '/Users/katushka/Documents/VEX_JSON')
from json_parser_grype import create_df as create_grype_df
from json_parser_vexy import create_df as create_vexy_df

if __name__ == "__main__":
    df_grype = create_grype_df()
    df_vexy = create_vexy_df()

    #df_vexy = df_vexy[~df_vexy['VulnerabilityID'].str.contains('TEMP', na=False)]
    #df_grype = df_grype[~df_grype['VulnerabilityID'].str.contains('TEMP', na=False)]

    result, intersection_df = jaccard_index(df_grype, df_vexy)
    
    print(f"Jaccard Index: {result}")
    print(intersection_df)