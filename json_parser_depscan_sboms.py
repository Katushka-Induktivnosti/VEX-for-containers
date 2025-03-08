import os
import json
import pandas as pd

def create_df():
    df = pd.DataFrame(columns=['VulnerabilityID','PkgName','Status','Severity','Container'])
    files = [f for f in os.listdir('jsons/DepScan/scout_sbom_vex/')]

    for file in files:
        if ".json" not in file:
            continue
        with open('jsons/DepScan/scout_sbom_vex/'+file) as f:
            try:
                data = []
                for line in f:
                    data.append(json.loads(line))
                for i in data:
                    df.loc[len(df)] = [i['id'],i['package'],i['fix_version'],i['severity'],file.split('_')[0]]
                data.clear()
            except:
                continue
        f.close()
    return df
