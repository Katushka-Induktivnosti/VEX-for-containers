import os
import json
import pandas as pd

def create_df():
    df = pd.DataFrame(columns=['VulnerabilityID','PkgName','Status','Severity','Container'])
    files = [f for f in os.listdir('jsons/DepScan/')]

    for file in files:
        if ".json" not in file:
            continue
        with open('jsons/DepScan/'+file) as f:
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
#    filtered_df1 = filtered_df[filtered_df['Container'].isin(images2)]
#    print(filtered_df1)
