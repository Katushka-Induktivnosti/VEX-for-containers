import os
import json
import pandas as pd

def create_df():
    df = pd.DataFrame(columns=['VulnerabilityID','PkgName','Status','Severity','Container'])
    files = [f for f in os.listdir('jsons/vexy/syft_sbom_vex/')]

    for file in files:
        if "_vex.json" not in file:
            continue
        f = open('jsons/vexy/syft_sbom_vex/'+file)
        data = json.load(f)
        try:
            for vuln in data['vulnerabilities']:
                id_name = vuln['references'][0]['id']
                pkgname = ""
                status = vuln['affects'][0]['versions'][0]['status']
                severity = vuln['ratings'][0]['severity']
                container_name = file.split('_')[0]
                df.loc[len(df)] = [id_name, pkgname, status, severity, container_name]
            f.close()
        except:
            continue
    return df

#if __name__=="__main__":
#    images1 = ["storm", "rocket.chat", "friendica", "ghost", "xwiki", "mysql", "silverpeas", "plone"]

#    images2 = ["almalinux", "eggdrop", "teamspeak", "nats", "busybox", "photon", "sl", "traefik"]

#    images3 = ["redis", "memcached", "node", "httpd", "rabbitmq", "mariadb", "nginx", "tomcat", "neo4j", 
#           "gradle", "consul:1.15.4", "ruby", "flink", "docker.elastic.co/elasticsearch/elasticsearch:8.12.2", "kibana:8.12.2", "composer", "telegraf", 
#           "sapmachine", "joomla", "groovy", "aerospike:ee-7.0.0.4_1", "kapacitor", "lightstreamer", "elixir", 
#           "erlang", "mediawiki", "monica", "jetty", "odoo", "bonita", "irssi", "gazebo"]
#    images4 = ["elasticsearch:8.12.2"]
#    df = create_df()
#    filtered_df = df[df["VulnerabilityID"].str.contains(r'^CVE', regex=True)]
#    filtered_df1 = filtered_df[filtered_df['Container'].isin(images1)]
#    print(filtered_df1)
