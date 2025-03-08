import pandas as pd
from jaccard_index import jaccard_index
import sys
sys.path.insert(0, '/Users/katushka/Documents/VEX_JSON')
#from json_parser_grype_sboms import create_df as create_grype_s_df
from json_parser_trivy_sboms import create_df as create_trivy_s_df

if __name__ == "__main__":
    df_trivy_s1, df_trivy_s2 = create_trivy_s_df()
    
    df_trivy_s1 = df_trivy_s1[df_trivy_s1['VulnerabilityID'].str.contains('CVE', na=False)]
    df_trivy_s2 = df_trivy_s2[df_trivy_s2['VulnerabilityID'].str.contains('CVE', na=False)]

    result, intersection_df = jaccard_index(df_trivy_s2, df_trivy_s1)

    print(f"Jaccard Index: {result}")
    print(intersection_df)