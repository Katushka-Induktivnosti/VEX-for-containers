import nvdlib
import os
from json_parser_grype import create_df as create_grype_df
from json_parser_depscan import create_df as create_depscan_df
import sys
sys.path.insert(0, '/Users/katushka/Documents/VEX_JSON/covariances/')
from jaccard_index import jaccard_index

api_key = os.getenv("NVD_API_KEY")

def filter_by_nvd_existence(df):
    """
    Filter a DataFrame to only include vulnerabilities that exist in the NVD database.
    
    Args:
        df: pandas DataFrame with a 'VulnerabilityID' column
        
    Returns:
        Filtered DataFrame containing only rows where VulnerabilityID exists in NVD
    """
    if not api_key:
        raise ValueError("NVD_API_KEY environment variable not set")
    
    # Create a copy to avoid modifying the original
    filtered_df = df.copy()
    
    # Get list of rows to drop
    rows_to_drop = []
    
    # Iterate through each row
    for index, row in filtered_df.iterrows():
        vuln_id = row['VulnerabilityID']
        
        # Skip non-CVE IDs if needed
        if not vuln_id.startswith('CVE-'):
            rows_to_drop.append(index)
            continue
            
        try:
            # Search for the CVE in NVD
            result = nvdlib.searchCVE(cveId=vuln_id, key=api_key, delay=0.61)
            
            # If no results or empty results, drop the row
            if not result:
                rows_to_drop.append(index)
                
        except Exception as e:
            # If any exception occurs, the CVE likely doesn't exist
            rows_to_drop.append(index)
    
    # Drop all rows that need to be removed
    filtered_df = filtered_df.drop(rows_to_drop)
    
    return filtered_df

def search_cve(vulnerabilities_df):
    """
    Legacy function - use filter_by_nvd_existence instead.
    This function has issues with iterating over the DataFrame.
    """
    #registered_vulnerabilities = []

    for vuln in vulnerabilities_df:
        try:
            r = nvdlib.searchCVE(cveId=vuln['VulnerabilityID'], key=api_key, verbose=True, delay=0.61)[0]
            #print(r.id)
            #registered_vulnerabilities.append(r.id)
            #vulnerabilities_df.drop()

        except:
            #print("Exception occured")
            vulnerabilities_df = vulnerabilities_df[vulnerabilities_df["VulnerabilityID"] != vuln['VulnerabilityID']]

    return vulnerabilities_df


if __name__ == "__main__":

    df_grype = create_grype_df()
    df_depscan = create_depscan_df()

    df_grype = df_grype[df_grype['VulnerabilityID'].str.contains(r'^CVE', na=False)]
    df_depscan = df_depscan[df_depscan['VulnerabilityID'].str.contains(r'^CVE', na=False)]

    # Filter DataFrames to only include vulnerabilities that exist in NVD
    found_vulns_grype = filter_by_nvd_existence(df_grype)
    found_vulns_depscan = filter_by_nvd_existence(df_depscan)

    print("Grype vulnerabilities before filtering:", len(df_grype))
    print("Grype vulnerabilities after filtering:", len(found_vulns_grype))
    print("DepScan vulnerabilities before filtering:", len(df_depscan))
    print("DepScan vulnerabilities after filtering:", len(found_vulns_depscan))

    result, intersection_df = jaccard_index(found_vulns_grype, found_vulns_depscan)

    print(f"Jaccard Index: {result}")
    #print(intersection_df)
