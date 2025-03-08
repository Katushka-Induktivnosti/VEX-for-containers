import os
import json
import pandas as pd

def create_df():
    df = pd.DataFrame(columns=['VulnerabilityID','Package','Status','Severity','Container'])
    files = [f for f in os.listdir('jsons/snyk/')]

    for file in files:
        f = open('jsons/snyk/'+file)
        data = json.load(f)
        for i in data['vulnerabilities']:
            try:
                df.loc[len(df)] = [i['identifiers']['CVE'][0],i['packageName']+i['version'],i['relativeImportance'],i['nvdSeverity'],file.split('_')[0]]
            except:
                continue
        f.close()
    return df

#if __name__=="__main__":
#    df = create_df()
#    filtered_df = df[df["VulnerabilityID"].str.contains(r'^CVE', regex=True)]
#    print(df)
#    print(filtered_df)