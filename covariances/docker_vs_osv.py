import pandas as pd
from jaccard_index import jaccard_index
import sys
sys.path.insert(0, '/Users/katushka/Documents/VEX_JSON')
from json_parser_docker import create_df as create_docker_df
from json_parser_osv import create_df as create_osv_df

if __name__ == "__main__":
    df_docker = create_docker_df()
    df_osv = create_osv_df()

    result, intersection_df = jaccard_index(df_docker, df_osv)

    #df_docker = df_docker[~df_docker['VulnerabilityID'].str.contains('TEMP', na=False)]
    #df_osv = df_osv[~df_osv['VulnerabilityID'].str.contains('TEMP', na=False)]
    
    print(f"Jaccard Index: {result}")
    print(intersection_df)