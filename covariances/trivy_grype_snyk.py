import pandas as pd
from modified_jaccard import modified_jaccard
import sys
sys.path.insert(0, '/Users/katushka/Documents/VEX_JSON')
from json_parser_trivy import create_df as create_trivy_df
from json_parser_grype import create_df as create_grype_df
from json_parser_snyk import create_df as create_snyk_df


if __name__ == "__main__":
    df_trivy = create_trivy_df()
    df_grype = create_grype_df()
    df_snyk = create_snyk_df()

    result, intersection_df = modified_jaccard(df_trivy, df_grype, df_snyk)

    print(f"Modified Jaccard Index: {result}")
    print(intersection_df)