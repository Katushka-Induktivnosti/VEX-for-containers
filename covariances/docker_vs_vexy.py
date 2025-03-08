import pandas as pd
from jaccard_index import jaccard_index
import sys
sys.path.insert(0, '/Users/katushka/Documents/VEX_JSON')
from json_parser_docker import create_df as create_docker_df
from json_parser_vexy import create_df as create_vexy_df

if __name__ == "__main__":
    df_docker = create_docker_df()
    df_vexy = create_vexy_df()
    
    #df_docker = df_docker[~df_docker['VulnerabilityID'].str.contains('TEMP', na=False)]
    #df_vexy = df_vexy[~df_vexy['VulnerabilityID'].str.contains('TEMP', na=False)]
    

    result, intersection_df = jaccard_index(df_docker, df_vexy)
    
    print(f"Jaccard Index: {result}")
    print(intersection_df)