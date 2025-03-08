import os
import json
import pandas as pd

def create_df():
    df1 = pd.DataFrame(columns=['VulnerabilityID','PkgName','Status','Severity','Container','tool'])
    df2 = pd.DataFrame(columns=['VulnerabilityID','PkgName','Status','Severity','Container'])
    df3 = pd.DataFrame(columns=['VulnerabilityID','PkgName','Status','Severity','Container'])
    df4 = pd.DataFrame(columns=['VulnerabilityID','PkgName','Status','Severity','Container'])
    files1 = [f for f in os.listdir('jsons/Trivy/trivy_sbom_vex')]
    files2 = [f for f in os.listdir('jsons/Trivy/syft_sbom_vex')]
    files3 = [f for f in os.listdir('jsons/Trivy/docker_sbom_vex')]
    files4 = [f for f in os.listdir('jsons/Trivy/depscan_sbom_vex')]

    for file in files1:
        if "_vex.json" not in file:
            continue
        f = open('jsons/trivy/trivy_sbom_vex/'+file)
        data = json.load(f)
        try:
            for i in data['Results']:
                try:
                    for j in i["Vulnerabilities"]:
                        df1.loc[len(df1)] = [j['VulnerabilityID'],j['PkgName'],j['Status'],j['Severity'],data["ArtifactName"][18:-10],'trivy']
                except:
                    RuntimeError
        except:
            continue

        f.close()

    for file in files2:
        if "_vex.json" not in file:
            continue
        f = open('jsons/trivy/syft_sbom_vex/'+file)
        data = json.load(f)
        try:
            for i in data['Results']:
                try:
                    for j in i["Vulnerabilities"]:
                        df2.loc[len(df2)] = [j['VulnerabilityID'],j['PkgName'],j['Status'],j['Severity'],data["ArtifactName"][18:-10]]
                except:
                    RuntimeError
        except:
            continue

        f.close()

    for file in files3:
        if "_vex.json" not in file:
            continue
        f = open('jsons/trivy/docker_sbom_vex/'+file)
        data = json.load(f)
        try:
            for i in data['Results']:
                try:
                    for j in i["Vulnerabilities"]:
                        df3.loc[len(df3)] = [j['VulnerabilityID'],j['PkgName'],j['Status'],j['Severity'],data["ArtifactName"][25:-10]]
                except:
                    RuntimeError
        except:
            continue

        f.close()


    for file in files4:
        if "_vex.json" not in file:
            continue
        f = open('jsons/trivy/depscan_sbom_vex/'+file)
        data = json.load(f)
        try:
            for i in data['Results']:
                try:
                    for j in i["Vulnerabilities"]:
                        df4.loc[len(df4)] = [j['VulnerabilityID'],j['PkgName'],j['Status'],j['Severity'],data["ArtifactName"][20:-10]]
                except:
                    RuntimeError
        except:
            continue

        f.close()

    return df3



  