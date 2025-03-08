import pandas as pd
from jaccard_index import jaccard_index
import sys
sys.path.insert(0, '/Users/katushka/Documents/VEX_JSON')
from json_parser_depscan import create_df as create_depscan_df
from json_parser_snyk import create_df as create_snyk_df

if __name__ == "__main__":
    df_depscan = create_depscan_df()
    df_snyk = create_snyk_df()

    df_snyk = df_snyk[~df_snyk['VulnerabilityID'].str.contains('TEMP', na=False)]
    df_depscan = df_depscan[~df_depscan['VulnerabilityID'].str.contains('TEMP', na=False)]

    result, intersection_df = jaccard_index(df_depscan, df_snyk)

    print(f"Jaccard Index: {result}")
    print(intersection_df)