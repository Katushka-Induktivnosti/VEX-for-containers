import pandas as pd
from jaccard_index import jaccard_index
import sys
sys.path.insert(0, '/Users/katushka/Documents/VEX_JSON')
from json_parser_depscan import create_df as create_depscan_df
from json_parser_depscan_sboms import create_df as create_depscan_s_df

if __name__ == "__main__":
    df_depscan = create_depscan_df()
    df_depscan_s = create_depscan_s_df()

    result, intersection_df = jaccard_index(df_depscan, df_depscan_s)

    print(f"Jaccard Index: {result}")
    print(intersection_df)