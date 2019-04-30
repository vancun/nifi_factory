
# Assign root folder for the lab sandbox
$labRoot="C:/Sandbox/NiFiBuilderLab"

# Make sure the lab root folder exists
mkdir -p $labRoot

# Change the current folder to $labRoot
cd $labRoot

# Clone NiFi Builder GitHub repository in the $labRoot folder.
# Once the command completes, NiFi builder will be available
# in the nifi_factory sub-folder.
git clone https://github.com/vancun/nifi_factory

# Test NiFi Builder installation
# Print short usage information
python nifi_factory\bin\nifi-builder.py

# Print detailed usage information
python nifi_factory\bin\nifi-builder.py -h

# Create NiFi docker container
# Once the container is created, navigate your browser to:
#   http://localhost:8080/nifi
docker run --rm -d -p 8080:8080 --name nifibuilderlab apache/nifi:1.8.0

# Explore NiFi Environment Variables
docker exec nifibuilderlab bash -c "env | grep NIFI"

# To open NiFi UI, naviage your browser to:
#    http://localhost:8080/nifi

# Run NiFi Builder
python nifi_factory\bin\nifi-builder.py `
           lab\acquire-random-users.def.nifib.json


# Dump the file from the landing zone
docker exec -ti nifibuilderlab bash `
      -c "cat /tmp/datalake/LANDING/NiFiBuilderLab/RandomUser/INBOX/* | head -n 3"


# Run NiFi Builder, forcing to overwrite existing stream
python nifi_factory\bin\nifi-builder.py -o `
           lab\acquire-random-users.def.nifib.json


# Clean datalake storage
docker exec -ti nifibuilderlab bash -c "rm -rf /tmp/datalake"


# Run NiFi Builder, forcing to overwrite existing stream and
# specifying config file
python nifi_factory\bin\nifi-builder.py -o `
           -c lab\acquire-random-users.conf.nifib.json  `
           lab\acquire-random-users.def.nifib.json        




# Additional commands


# List datalake storage recursively
docker exec -ti nifibuilderlab bash -c "ls -lR /tmp/datalake"
