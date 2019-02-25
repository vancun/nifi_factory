## Get Process Group
curl "http://localhost:8080/nifi-api/process-groups/e14e46d8-0168-1000-60f4-cbbacbd0a23c"


## Update PG Configuration
curl "http://localhost:8080/nifi-api/process-groups/11acb31a-0169-1000-638d-7e3901e1b63c" --data-binary "^{^\^"revision^\^":^{^\^"clientId^\^":^\^"0f4cd134-0169-1000-8eaa-0d976b2fde93^\^",^\^"version^\^":1^},^\^"disconnectedNodeAcknowledged^\^":false,^\^"component^\^":^{^\^"id^\^":^\^"11acb31a-0169-1000-638d-7e3901e1b63c^\^",^\^"name^\^":^\^"Demo CSV Ingest^\^",^\^"comments^\^":^\^"Descr^\^"^}^}" --compressed

## Get Variables
curl "http://localhost:8080/nifi-api/process-groups/11d765a4-0169-1000-c177-0d9e711f9756/variable-registry"

## Update Variables
curl "http://localhost:8080/nifi-api/process-groups/11c005c7-0169-1000-3353-f24170bfefcb/variable-registry/update-requests" --data-binary "^{^\^"processGroupRevision^\^":^{^\^"clientId^\^":^\^"0f4cd134-0169-1000-8eaa-0d976b2fde93^\^",^\^"version^\^":2^},^\^"disconnectedNodeAcknowledged^\^":false,^\^"variableRegistry^\^":^{^\^"processGroupId^\^":^\^"11c005c7-0169-1000-3353-f24170bfefcb^\^",^\^"variables^\^":^[^{^\^"variable^\^":^{^\^"name^\^":^\^"A^\^",^\^"value^\^":^\^"1^\^"^}^}^]^}^}" --compressed

## List Templates
curl "http://localhost:8080/nifi-api/flow/templates" 

## Instantiate Template
curl "http://localhost:8080/nifi-api/process-groups/10b32e39-0169-1000-e650-6a39523f411c/template-instance" --data-binary "^{^\^"templateId^\^":^\^"f842c312-b7e1-416f-ad3a-c3cb019e1d85^\^",^\^"originX^\^":242.00002506933936,^\^"originY^\^":79.00002490682732,^\^"disconnectedNodeAcknowledged^\^":false^}" --compressed


## Create Connection
curl "http://localhost:8080/nifi-api/process-groups/11051aab-0169-1000-3078-67b545e2af6d/connections" --data-binary "^{^\^"revision^\^":^{^\^"clientId^\^":^\^"0f4cd134-0169-1000-8eaa-0d976b2fde93^\^",^\^"version^\^":0^},^\^"disconnectedNodeAcknowledged^\^":false,^\^"component^\^":^{^\^"name^\^":^\^"^\^",^\^"source^\^":^{^\^"id^\^":^\^"cf9ff17e-de15-3f8d-b230-235a16959b59^\^",^\^"groupId^\^":^\^"0574f873-97d7-3a8b-3f56-7a39564fd6f1^\^",^\^"type^\^":^\^"OUTPUT_PORT^\^"^},^\^"destination^\^":^{^\^"id^\^":^\^"fdd5bbc1-39d3-335b-1bff-338187665c9f^\^",^\^"groupId^\^":^\^"84861771-eec4-33f4-7125-a63455b00f1f^\^",^\^"type^\^":^\^"INPUT_PORT^\^"^},^\^"flowFileExpiration^\^":^\^"0 sec^\^",^\^"backPressureDataSizeThreshold^\^":^\^"1 GB^\^",^\^"backPressureObjectThreshold^\^":^\^"10000^\^",^\^"bends^\^":^[^],^\^"prioritizers^\^":^[^],^\^"loadBalanceStrategy^\^":^\^"DO_NOT_LOAD_BALANCE^\^",^\^"loadBalancePartitionAttribute^\^":^\^"^\^",^\^"loadBalanceCompression^\^":^\^"DO_NOT_COMPRESS^\^"^}^}" --compressed



# Data for Demo

https://randomuser.me/api/?format=csv&inc=gender,name,nat&seed=ivan1&results=200

