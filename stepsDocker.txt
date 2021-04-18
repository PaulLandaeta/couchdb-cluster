

docker run -itd -p 5984:5984 -p 5986:5986 --name=couchdb0 \
-e NODENAME='couchdb-0.local.com' \
--mount 'source=volume-0,target=/opt/couchdb/data' \
-e COUCHDB_USER=admin -e COUCHDB_PASSWORD=123456 \
couchdb:latest


docker run -itd -p 15984:5984 -p 15986:5986 --name=couchdb1 \
-e NODENAME='couchdb-1.local.com' \
--mount 'source=volume-1,target=/opt/couchdb/data' \
-e COUCHDB_USER=admin -e COUCHDB_PASSWORD=123456 \
couchdb:latest

docker run -itd -p 25984:5984 -p 25986:5986 --name=couchdb2 \
-e NODENAME='couchdb-2.local.com' \
--mount 'source=volume-2,target=/opt/couchdb/data' \
-e COUCHDB_USER=admin -e COUCHDB_PASSWORD=123456 \
couchdb:latest

create the bridge 

docker network create -d bridge --subnet 172.25.0.0/16 isolated_nw


docker network connect --alias couchdb-0.local.com \
isolated_nw couchdb0


docker network connect --alias couchdb-1.local.com \
isolated_nw couchdb1



