import subprocess

images1 = ["storm", "rocket.chat", "friendica", "ghost", "xwiki", "mysql", "silverpeas", "plone"]

images2 = ["almalinux", "eggdrop", "teamspeak", "nats", "busybox", "photon", "sl", "traefik"]

images3 = ["redis", "memcached", "node", "httpd", "rabbitmq", "mariadb", "nginx", "tomcat", "neo4j", 
           "gradle", "consul:1.15.4", "ruby", "flink", "docker.elastic.co/elasticsearch/elasticsearch:8.12.2", "kibana:8.12.2", "composer", "telegraf", 
           "sapmachine", "joomla", "groovy", "aerospike:ee-7.0.0.4_1", "kapacitor", "lightstreamer", "elixir", 
           "erlang", "mediawiki", "monica", "jetty", "odoo", "bonita", "irssi", "gazebo"]

for image in images3:
    try:
        subprocess.call(["docker", "image", "save",  "-o", "/Users/katushka/oci_tars/"+image+".tar", image])
        subprocess.call(["docker", "image", "import", "/Users/katushka/oci_tars/"+image+".tar", "oci-"+image])
    except:
        RuntimeError