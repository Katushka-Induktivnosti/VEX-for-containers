import os
import json
import pandas as pd

def create_df():
    df1 = pd.DataFrame(columns=['VulnerabilityID','PkgName','Status','Severity','Container'])
    df2 = pd.DataFrame(columns=['VulnerabilityID','PkgName','Status','Severity','Container'])
    df3 = pd.DataFrame(columns=['VulnerabilityID','PkgName','Status','Severity','Container'])
    df4 = pd.DataFrame(columns=['VulnerabilityID','PkgName','Status','Severity','Container'])

    files1 = [f for f in os.listdir('jsons/OSV/syft_sbom_vex/')]
    files2 = [f for f in os.listdir('jsons/OSV/trivy_sbom_vex/')]
    files3 = [f for f in os.listdir('jsons/OSV/docker_sbom_vex/')]
    files4 = [f for f in os.listdir('jsons/OSV/depscan_sbom_vex/')]

    for file in files1:
        if "_vex.json" not in file:
            continue
        try:
            f = open('jsons/OSV/syft_sbom_vex/'+file)
            data = json.load(f)
            for package in data['results'][0]['packages']:
                for vuln in package['vulnerabilities']:
                    try:
                        id_name = vuln['aliases'][0]
                    except:
                        id_name = vuln['id']
                    pkgname = package['package']['name']
                    status = ''
                    try:
                        severity = vuln['database_specific']['severity']
                    except:
                        severity = ''
                    container_name = file.split('_')[0]
                    df1.loc[len(df1)] = [id_name, pkgname, status, severity, container_name]
        except:
            continue
        f.close()

    for file in files2:
        if "_vex.json" not in file:
            continue
        try:
            f = open('jsons/OSV/trivy_sbom_vex/'+file)
            data = json.load(f)
            for package in data['results'][0]['packages']:
                for vuln in package['vulnerabilities']:
                    try:
                        id_name = vuln['aliases'][0]
                    except:
                        id_name = vuln['id']
                    pkgname = package['package']['name']
                    status = ''
                    try:
                        severity = vuln['database_specific']['severity']
                    except:
                        severity = ''
                    container_name = file.split('_')[0]
                    df2.loc[len(df2)] = [id_name, pkgname, status, severity, container_name]
        except:
            continue
        f.close()

    for file in files3:
        if "_vex.json" not in file:
            continue
        try:
            f = open('jsons/OSV/docker_sbom_vex/'+file)
            data = json.load(f)
            for package in data['results'][0]['packages']:
                for vuln in package['vulnerabilities']:
                    try:
                        id_name = vuln['aliases'][0]
                    except:
                        id_name = vuln['id']
                    pkgname = package['package']['name']
                    status = ''
                    try:
                        severity = vuln['database_specific']['severity']
                    except:
                        severity = ''
                    container_name = file.split('_')[0]
                    df3.loc[len(df3)] = [id_name, pkgname, status, severity, container_name]
        except:
            continue
        f.close()

    for file in files4:
        if "_vex.json" not in file:
            continue
        try:
            f = open('jsons/OSV/depscan_sbom_vex/'+file)
            data = json.load(f)
            for package in data['results'][0]['packages']:
                for vuln in package['vulnerabilities']:
                    try:
                        id_name = vuln['aliases'][0]
                    except:
                        id_name = vuln['id']
                    pkgname = package['package']['name']
                    status = ''
                    try:
                        severity = vuln['database_specific']['severity']
                    except:
                        severity = ''
                    container_name = file.split('_')[0]
                    df4.loc[len(df4)] = [id_name, pkgname, status, severity, container_name]
        except:
            continue
        f.close()

    return df3
