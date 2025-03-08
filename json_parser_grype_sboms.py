import os
import json
import pandas as pd

def create_df():
    df1 = pd.DataFrame(columns=['VulnerabilityID','PkgName','Status','Severity','Container'])
    df2 = pd.DataFrame(columns=['VulnerabilityID','PkgName','Status','Severity','Container'])
    df3 = pd.DataFrame(columns=['VulnerabilityID','PkgName','Status','Severity','Container'])
    df4 = pd.DataFrame(columns=['VulnerabilityID','PkgName','Status','Severity','Container'])
    files1 = [f for f in os.listdir('jsons/Grype/depscan_sbom_vex/')]
    files2 = [f for f in os.listdir('jsons/Grype/docker_sbom_vex/')]
    files3 = [f for f in os.listdir('jsons/Grype/syft_sbom_vex/')]
    files4 = [f for f in os.listdir('jsons/Grype/trivy_sbom_vex/')]

    for file in files1:
        if "_vex.json" not in file:
            continue
        f = open('jsons/grype/depscan_sbom_vex/'+file)
        try:
            data = json.load(f)
            try:
                for i in data['matches']:
                    df1.loc[len(df1)] = [i['vulnerability']['id'],i['vulnerability']['namespace'],i['vulnerability']['fix']['state'],i['vulnerability']['severity'],file.split('_')[0]]

            except:
                continue
        except:
                continue

        f.close()

    for file in files2:
        if "_vex.json" not in file:
            continue
        f = open('jsons/grype/docker_sbom_vex/'+file)
        data = json.load(f)
        try:
            for i in data['matches']:
                df2.loc[len(df2)] = [i['vulnerability']['id'],i['vulnerability']['namespace'],i['vulnerability']['fix']['state'],i['vulnerability']['severity'],file.split('_')[0]]

        except:
            continue

        f.close()

    for file in files3:
        if "_vex.json" not in file:
            continue
        f = open('jsons/grype/syft_sbom_vex/'+file)
        data = json.load(f)
        try:
            for i in data['matches']:
                df3.loc[len(df3)] = [i['vulnerability']['id'],i['vulnerability']['namespace'],i['vulnerability']['fix']['state'],i['vulnerability']['severity'],file.split('_')[0]]

        except:
            continue

        f.close()

    for file in files4:
        if "_vex.json" not in file:
            continue
        f = open('jsons/grype/trivy_sbom_vex/'+file)
        data = json.load(f)
        try:
            for i in data['matches']:
                df4.loc[len(df4)] = [i['vulnerability']['id'],i['vulnerability']['namespace'],i['vulnerability']['fix']['state'],i['vulnerability']['severity'],file.split('_')[0]]

        except:
            continue

        f.close()
    
    
    return df2
