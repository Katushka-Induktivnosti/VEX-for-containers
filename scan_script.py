import subprocess

'''
reps = ["reddit-archive/reddit", "zalandoresearch/fashion-mnist", "NVIDIA/vid2vid", "miguelgrinberg/flasky",
        "seemoo-lab/opendrop", "rbgirshick/py-faster-rcnn", "EleutherAI/gpt-neo", "the-paperless-project/paperless",
        "/openai/universe", "schollz/howmanypeoplearearound"
        ]
'''

images1 = ["storm", "rocket.chat", "friendica", "ghost", "xwiki", "mysql", "silverpeas", "plone"]

images2 = ["almalinux", "eggdrop", "teamspeak", "nats", "busybox", "photon", "sl", "traefik"]

images3 = ["redis", "memcached", "node", "httpd", "rabbitmq", "mariadb", "nginx", "tomcat", "neo4j", 
           "gradle", "consul", "ruby", "flink", "elasticsearch", "kibana", "composer", "telegraf", 
           "sapmachine", "joomla", "groovy", "aerospike:ee", "kapacitor", "lightstreamer", "elixir", 
           "erlang", "mediawiki", "monica", "jetty", "odoo", "bonita", "irssi", "gazebo"]


'''
for rep in reps:
    try:
        subprocess.call(["trivy", "repo", "-f", "json", "--scanners", "vuln,config,secret,license", "-o", 
                 "jsons/"+rep.replace("/", "_")+"_vex.json", "https://github.com/"+rep])
        
    except:
        RuntimeError
'''

for image in images3:
    try:
        #subprocess.call(["trivy", "image", "-f", "cyclonedx",  "-o", "jsons/trivy/cyclone/"+image+"_vex.json", image])
        #f = open("jsons/grype/depscan_sbom_vex/"+image+"_vex.json", "w")
        #subprocess.call(["grype", "sbom:jsons/DepScan/sboms/"+image+"_sbom.json", "-o", "json"], stdout=f)
        #f.close
        #f = open("jsons/OSV/depscan_sbom_vex/"+image+"_vex.json", "w")
        #subprocess.call(["osv-scanner", "--format", "json", "--sbom=jsons/DepScan/sboms/"+image+"_sbom.json"], stdout=f)
        #f.close
        #f = open("jsons/grype/sboms/"+image+"_sbom.json", "w")
        #subprocess.call(["syft", image, "-o", "cyclonedx-json"], stdout=f)
        #f.close

        #subprocess.call(["trivy", "image", "-f", "cyclonedx",  "-o", "jsons/trivy/cyclone/"+image+"_cycl_sbom.json", image])
        #subprocess.call(["trivy", "sbom", "-f", "json", "-o", "jsons/trivy/depscan_sbom_vex/"+image+"_vex.json", "jsons/DepScan/sboms/"+image+"_sbom.json"])

        #subprocess.call(["vexy", "--in-file", "jsons/Docker_scout/sboms_cyclonedx/"+image+"_sbom.json", "--format", "json", "-c", "jsons/vexy/vexy.yml", "-o", "jsons/vexy/scout_sbom_vex/"+image+"_vex.json"])
        #subprocess.call(["docker", "scout", "sbom", "--format", "cyclonedx", "-o", "jsons/Docker_scout/sboms_cyclonedx/"+image+"_sbom.json", image])
        #subprocess.call(['./clair-scanner','--reportAll=true', f'--report={image}.json', '--ip', '192.168.8.181',  image])
        #f = open("jsons/Snyk/"+image+"_vex.json", "w")
        #subprocess.call(['snyk', 'container', 'test', '--platform=linux/amd64', '--json', '--docker', image], stdout=f)
        #f.close

        #subprocess.call(["depscan", "--cache", "--src", image, "-t", "docker", "-o", "jsons/DepScan/"+image+"_vex.json"])
        #subprocess.call(["cdxgen", "-t", "docker", image, "-o", "jsons/DepScan/sboms/"+image+"_sbom.json", "--spec-version", "1.5"])
        #subprocess.call(["depscan", "--bom", "jsons/Docker_scout/sboms_cyclonedx/"+image+"_sbom.json", "-o", "jsons/DepScan/scout_sbom_vex/"+image+"_vex.json"])


    except:
        RuntimeError