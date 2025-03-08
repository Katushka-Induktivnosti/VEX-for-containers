import os
import json
import pandas as pd

def create_df():
    df = pd.DataFrame(columns=['VulnerabilityID','PkgName','Status','Severity','Container'])
    files = [f for f in os.listdir('jsons/Grype')]

    for file in files:
        if "_vex.json" not in file:
            continue
        f = open('jsons/grype/'+file)
        data = json.load(f)
        try:
            for i in data['matches']:
                df.loc[len(df)] = [i['vulnerability']['id'],i['vulnerability']['namespace'],i['vulnerability']['fix']['state'],i['vulnerability']['severity'],file.split('_')[0]]

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
#    filtered_df1 = filtered_df[filtered_df['Container'].isin(images4)]
#    print(filtered_df1)
