oc login --token=sha256~HYtprWxkl1CbSGFARniZBMMyl0gCF0VNo_i6hkvzzQI --server=https://api.rm3.7wse.p1.openshiftapps.com:6443
oc apply -f pvc.yaml
oc set volume deployment/test_mongo --add --mount-path=/var/lib/mongo --claim-name=fastapi-pvc --name fastapi-pvc
docker buildx build --platform linux/amd64,linux/arm64 -t nbjo460/test_mongo:latest . --push
docker run -d test_mongo
oc new-app --image=docker.io/nbjo460/test_mongo:latest --name=test_mongo
oc get service
oc expose service/fastapi
