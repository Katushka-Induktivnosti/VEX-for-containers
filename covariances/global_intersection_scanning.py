import pandas as pd
from modified_jaccard_4 import modified_jaccard_4
from jaccard_index import jaccard_index
import sys
sys.path.insert(0, '/Users/katushka/Documents/VEX_JSON')
from json_parser_grype import create_df as create_grype_df
from json_parser_snyk import create_df as create_snyk_df
from json_parser_trivy import create_df as create_trivy_df
from json_parser_depscan import create_df as create_depscan_df
from json_parser_docker import create_df as create_docker_df
from json_parser_osv import create_df as create_osv_df
from json_parser_vexy import create_df as create_vexy_df

if __name__ == "__main__":

    images1 = ["storm", "rocket.chat", "friendica", "ghost", "xwiki", "mysql", "silverpeas", "plone"]

    images2 = ["almalinux", "eggdrop", "teamspeak", "nats", "busybox", "photon", "sl", "traefik"]

    images3 = ["redis", "memcached", "node", "httpd", "rabbitmq", "mariadb", "nginx", "tomcat", "neo4j", 
           "gradle", "consul:1.15.4", "ruby", "flink", "elasticsearch:8.12.2", "kibana:8.12.2", "composer", "telegraf", 
           "sapmachine", "joomla", "groovy", "aerospike:ee-7.0.0.4", "kapacitor", "lightstreamer", "elixir", 
           "erlang", "mediawiki", "monica", "jetty", "odoo", "bonita", "irssi", "gazebo"]

    df_grype = create_grype_df()
    df_snyk = create_snyk_df()
    df_trivy = create_trivy_df()
    df_depscan = create_depscan_df()
    df_docker = create_docker_df()
    df_osv = create_osv_df()
    df_vexy = create_vexy_df()
    

    df_grype = df_grype.loc[df_grype['Container'].isin(images3)]
    df_snyk = df_snyk.loc[df_snyk['Container'].isin(images3)]
    df_trivy = df_trivy.loc[df_trivy['Container'].isin(images3)]
    df_depscan = df_depscan.loc[df_depscan['Container'].isin(images3)]
    df_docker = df_docker.loc[df_docker['Container'].isin(images3)]
    df_osv = df_osv.loc[df_osv['Container'].isin(images3)]
    df_vexy = df_vexy.loc[df_vexy['Container'].isin(images3)]


    result, intersection_df = modified_jaccard_4(df_grype, df_trivy, df_docker, df_snyk)
    
    print(f"Jaccard Index: {result}")
    print(intersection_df)

    """set = set(df_trivy['VulnerabilityID'].astype(str) + "/" + df_trivy['Container'].astype(str))
    gt_df = pd.DataFrame(list(set), columns=['Vulnerability'])
    gt_df['Vulnerability'].replace('', "NaN", inplace=True)
    print(gt_df)
    gt_df[['VulnerabilityID', 'Container']] = gt_df['Vulnerability'].str.split('/', expand=True)
    gt_df.drop(columns=['Vulnerability'], inplace=True)
    print(gt_df)

    

    result_2, tool_eval_df = jaccard_index(intersection_df, gt_df)

    print(result)
    #print((f"Ground_truth_Jaccard: {result_2}"))"""