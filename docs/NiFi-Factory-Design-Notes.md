



## Configuration Driven NiFi Flow Generation

Flow description is provided. Based on the description, a flow is generated. Flow is identified by its name. 

Flow is wrapped into a NiFi Process Group. Flow name is assigned to the Process Group.

If flow already exists, the behavior is controlled through configuration option:

* Overwrite - Existing flow is recreated. 
  * If there are running processors or queued flow files, process is aborted.
  * If upstream or downstream processors are running, process is aborted.
* Abort (Default) - Generation stops with error code.
* Append - A new flow is created with generated name.



# Notes



## Original Stories

EPIC: Define, Design and Implement Data Acquisition Automation

* Provide the API calls to build a NiFi flow to read data CSV from a local fileserver and ingest them in Azure DLS (API-NiFi-CSV-ADLS)
* Provide the API calls to de-identify fields in CSV using the SecuPi processor
* Provide the API calls to build a NiFi to read data JSON from a local fileserver and ingest them in Azure Blob
* Provide the API calls to de-identify fields in JSON using the SecuPi processor
* Provide the API calls to build a NiFi to read data XML from a local fileserver and ingest them in Azure Blob
* Provide the API calls to de-identify fields in XML using the SecuPi processor
* Provide the API calls to deploy a NiFi flow to an environment using the NiFi CI/CD
* Provide the API calls to commit the curate a CSV
  * API call to commit the code in BitBucket
  * API call to build the artefact in Nexus via Jenkins
  * API call to build deploy the artefact from Nexus to HDI or HDP environment via Jenkins
* Provide the API calls to commit the curate a JSON
  * API call to commit the code in BitBucket
  * API call to build the artefact in Nexus via Jenkins
  * API call to build deploy the artefact from Nexus to HDI or HDP environment via Jenkins
* Provide the API calls to commit the curate a XML
  *  API call to commit the code in BitBucket
  * API call to build the artefact in Nexus via Jenkins
  * API call to build deploy the artefact from Nexus to HDI or HDP environment via Jenkins
* Etc.





* http://localhost:8080/nifi-api/flow/current-user

  * curl 'http://localhost:8080/nifi-api/flow/current-user' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.9,bg-BG;q=0.8,bg;q=0.7' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: http://localhost:8080/nifi/' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --compressed

* http://localhost:8080/nifi-api/flow/client-id

  * ```bash
    curl 'http://localhost:8080/nifi-api/flow/client-id' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.9,bg-BG;q=0.8,bg;q=0.7' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' -H 'Accept: */*' -H 'Referer: http://localhost:8080/nifi/' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --compressed
    ```

  * 

* http://localhost:8080/nifi-api/flow/config

* http://localhost:8080/nifi-api/flow/banners

* http://localhost:8080/nifi-api/flow/processor-types

  * ```bash 
    curl 'http://localhost:8080/nifi-api/flow/processor-types' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.9,bg-BG;q=0.8,bg;q=0.7' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: http://localhost:8080/nifi/' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --compressed
    ```

* http://localhost:8080/nifi-api/flow/about

  * ```bash
    curl 'http://localhost:8080/nifi-api/access/config' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.9,bg-BG;q=0.8,bg;q=0.7' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: http://localhost:8080/nifi/' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --compressed
    ```

* http://localhost:8080/nifi-api/flow/controller-service-types

* http://localhost:8080/nifi-api/flow/reporting-task-types

* http://localhost:8080/nifi-api/flow/prioritizers

* http://localhost:8080/nifi-api/flow/process-groups/root

  * ```bash
    curl 'http://localhost:8080/nifi-api/flow/process-groups/root' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.9,bg-BG;q=0.8,bg;q=0.7' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: http://localhost:8080/nifi/' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --compressed
    ```

  * ```json
    {
        "permissions": {
            "canRead": true,
            "canWrite": true
        },
        "processGroupFlow": {
            "id": "cc6f6e50-0168-1000-0261-75adc2c330e5",
            "uri": "http://localhost:8080/nifi-api/flow/process-groups/cc6f6e50-0168-1000-0261-75adc2c330e5",
            "breadcrumb": {
                "id": "cc6f6e50-0168-1000-0261-75adc2c330e5",
                "permissions": {
                    "canRead": true,
                    "canWrite": true
                },
                "breadcrumb": {
                    "id": "cc6f6e50-0168-1000-0261-75adc2c330e5",
                    "name": "NiFi Flow"
                }
            },
            "flow": {
                "processGroups": [
                    {
                        "revision": {
                            "clientId": "ccb75313-0168-1000-ded8-065f68728627",
                            "version": 1
                        },
                        "id": "ccc69044-0168-1000-93ed-04661d1fdc08",
                        "uri": "http://localhost:8080/nifi-api/process-groups/ccc69044-0168-1000-93ed-04661d1fdc08",
                        "position": {
                            "x": 365,
                            "y": 204
                        },
                        "permissions": {
                            "canRead": true,
                            "canWrite": true
                        },
                        "bulletins": [
                        ],
                        "component": {
                            "id": "ccc69044-0168-1000-93ed-04661d1fdc08",
                            "parentGroupId": "cc6f6e50-0168-1000-0261-75adc2c330e5",
                            "position": {
                                "x": 365,
                                "y": 204
                            },
                            "name": "AMSLOG_Ingest",
                            "comments": "",
                            "variables": {
                            },
                            "runningCount": 0,
                            "stoppedCount": 0,
                            "invalidCount": 0,
                            "disabledCount": 0,
                            "activeRemotePortCount": 0,
                            "inactiveRemotePortCount": 0,
                            "upToDateCount": 0,
                            "locallyModifiedCount": 0,
                            "staleCount": 0,
                            "locallyModifiedAndStaleCount": 0,
                            "syncFailureCount": 0,
                            "inputPortCount": 0,
                            "outputPortCount": 0
                        },
                        "status": {
                            "id": "ccc69044-0168-1000-93ed-04661d1fdc08",
                            "name": "AMSLOG_Ingest",
                            "statsLastRefreshed": "12:05:58 CET",
                            "aggregateSnapshot": {
                                "id": "ccc69044-0168-1000-93ed-04661d1fdc08",
                                "name": "AMSLOG_Ingest",
                                "flowFilesIn": 0,
                                "bytesIn": 0,
                                "input": "0 (0 bytes)",
                                "flowFilesQueued": 0,
                                "bytesQueued": 0,
                                "queued": "0 (0 bytes)",
                                "queuedCount": "0",
                                "queuedSize": "0 bytes",
                                "bytesRead": 0,
                                "read": "0 bytes",
                                "bytesWritten": 0,
                                "written": "0 bytes",
                                "flowFilesOut": 0,
                                "bytesOut": 0,
                                "output": "0 (0 bytes)",
                                "flowFilesTransferred": 0,
                                "bytesTransferred": 0,
                                "transferred": "0 (0 bytes)",
                                "bytesReceived": 0,
                                "flowFilesReceived": 0,
                                "received": "0 (0 bytes)",
                                "bytesSent": 0,
                                "flowFilesSent": 0,
                                "sent": "0 (0 bytes)",
                                "activeThreadCount": 0,
                                "terminatedThreadCount": 0
                            }
                        },
                        "runningCount": 0,
                        "stoppedCount": 0,
                        "invalidCount": 0,
                        "disabledCount": 0,
                        "activeRemotePortCount": 0,
                        "inactiveRemotePortCount": 0,
                        "upToDateCount": 0,
                        "locallyModifiedCount": 0,
                        "staleCount": 0,
                        "locallyModifiedAndStaleCount": 0,
                        "syncFailureCount": 0,
                        "inputPortCount": 0,
                        "outputPortCount": 0
                    }
                ],
                "remoteProcessGroups": [
                ],
                "processors": [
                ],
                "inputPorts": [
                ],
                "outputPorts": [
                ],
                "connections": [
                ],
                "labels": [
                ],
                "funnels": [
                ]
            },
            "lastRefreshed": "12:05:58 CET"
        }
    }
    ```

  * 

* http://localhost:8080/nifi-api/flow/status

* http://localhost:8080/nifi-api/flow/controller/bulletins

  * ```bash
    curl 'http://localhost:8080/nifi-api/flow/controller/bulletins' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.9,bg-BG;q=0.8,bg;q=0.7' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: http://localhost:8080/nifi/' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --compressed
    ```

  * 





#### Create Process Group

```bash
curl 'http://localhost:8080/nifi-api/process-groups/cc6f6e50-0168-1000-0261-75adc2c330e5/process-groups' -H 'Origin: http://localhost:8080' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.9,bg-BG;q=0.8,bg;q=0.7' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' -H 'Content-Type: application/json' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: http://localhost:8080/nifi/' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --data-binary '{"revision":{"clientId":"ccb75313-0168-1000-ded8-065f68728627","version":0},"disconnectedNodeAcknowledged":false,"component":{"name":"AMSLOG_Ingest","position":{"x":365,"y":204}}}' --compressed
```

Process group dimensions: 380x172







## Resources

* Python CLI - https://docs.python-guide.org/scenarios/cli/
* Python CLI - https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df
  * Click Documentation - https://click.palletsprojects.com/en/7.x/
* CMD
  * https://coderwall.com/p/w78iva/give-your-python-program-a-shell-with-the-cmd-module
  * https://docs.python.org/3/library/cmd.html