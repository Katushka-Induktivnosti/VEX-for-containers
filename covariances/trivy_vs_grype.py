import pandas as pd
from jaccard_index import jaccard_index
import sys
sys.path.insert(0, '/Users/katushka/Documents/VEX_JSON')
from json_parser_trivy import create_df as create_trivy_df
from json_parser_grype import create_df as create_grype_df

if __name__ == "__main__":
    df_trivy = create_trivy_df()
    df_grype = create_grype_df()

    df_trivy = df_trivy[~df_trivy['VulnerabilityID'].str.contains('TEMP', na=False)]
    df_grype = df_grype[~df_grype['VulnerabilityID'].str.contains('TEMP', na=False)]

    result, intersection_df = jaccard_index(df_trivy, df_grype)

    print(f"Jaccard Index: {result}")
    print(intersection_df)
