import pandas as pd
from modified_jaccard_4 import modified_jaccard_4
import sys
sys.path.insert(0, '/Users/katushka/Documents/VEX_JSON')
from json_parser_grype_sboms import create_df

if __name__ == "__main__":

    df_depscan, df_docker, df_syft, df_trivy = create_df()

    result, intersection_df = modified_jaccard_4(df_syft, df_trivy, df_depscan, df_docker)

    
    print(f"Jaccard Index: {result}")
    print(intersection_df)