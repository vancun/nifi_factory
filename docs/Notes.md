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





## Processors

### Get Processor

```bash
curl 'http://localhost:8080/nifi-api/processors/3a743c7a-6a73-3611-d91b-ab2478edfb5f' --compressed
```



```json
{
	"revision": {
		"version": 0
	},
	"id": "3a743c7a-6a73-3611-d91b-ab2478edfb5f",
	"uri": "http://localhost:8080/nifi-api/processors/3a743c7a-6a73-3611-d91b-ab2478edfb5f",
	"position": {
		"x": 354.99999536407995,
		"y": 89.99998894099326
	},
	"permissions": {
		"canRead": true,
		"canWrite": true
	},
	"bulletins": [],
	"component": {
		"id": "3a743c7a-6a73-3611-d91b-ab2478edfb5f",
		"parentGroupId": "0574f873-97d7-3a8b-3a86-550f2a775aa1",
		"position": {
			"x": 354.99999536407995,
			"y": 89.99998894099326
		},
		"name": "ListFile",
		"type": "org.apache.nifi.processors.standard.ListFile",
		"bundle": {
			"group": "org.apache.nifi",
			"artifact": "nifi-standard-nar",
			"version": "1.8.0"
		},
		"state": "STOPPED",
		"style": {},
		"relationships": [{
				"name": "success",
				"description": "All FlowFiles that are received are routed to success",
				"autoTerminate": false
			}
		],
		"supportsParallelProcessing": false,
		"supportsEventDriven": false,
		"supportsBatching": false,
		"persistsState": true,
		"restricted": false,
		"deprecated": false,
		"executionNodeRestricted": false,
		"multipleVersionsAvailable": false,
		"inputRequirement": "INPUT_FORBIDDEN",
		"config": {
			"properties": {
				"listing-strategy": "timestamps",
				"Input Directory": "${sdp_input_dir}",
				"Recurse Subdirectories": "true",
				"Input Directory Location": "Local",
				"File Filter": "[^\\.].*",
				"Path Filter": null,
				"Include File Attributes": "true",
				"Minimum File Age": "0 sec",
				"Maximum File Age": null,
				"Minimum File Size": "0 B",
				"Maximum File Size": null,
				"Ignore Hidden Files": "true",
				"target-system-timestamp-precision": "auto-detect",
				"et-state-cache": null,
				"et-time-window": "3 hours",
				"et-initial-listing-target": "all",
				"et-node-identifier": "${hostname()}"
			},
			"descriptors": {
				"listing-strategy": {
					"name": "listing-strategy",
					"displayName": "Listing Strategy",
					"description": "Specify how to determine new/updated entities. See each strategy descriptions for detail.",
					"defaultValue": "timestamps",
					"allowableValues": [{
							"allowableValue": {
								"displayName": "Tracking Timestamps",
								"value": "timestamps",
								"description": "This strategy tracks the latest timestamp of listed entity to determine new/updated entities. Since it only tracks few timestamps, it can manage listing state efficiently. However, any newly added, or updated entity having timestamp older than the tracked latest timestamp can not be picked by this strategy. For example, such situation can happen in a file system if a file with old timestamp is copied or moved into the target directory without its last modified timestamp being updated."
							},
							"canRead": true
						}, {
							"allowableValue": {
								"displayName": "Tracking Entities",
								"value": "entities",
								"description": "This strategy tracks information of all the listed entities within the latest 'Entity Tracking Time Window' to determine new/updated entities. This strategy can pick entities having old timestamp that can be missed with 'Tracing Timestamps'. However additional DistributedMapCache controller service is required and more JVM heap memory is used. See the description of 'Entity Tracking Time Window' property for further details on how it works."
							},
							"canRead": true
						}
					],
					"required": true,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"Input Directory": {
					"name": "Input Directory",
					"displayName": "Input Directory",
					"description": "The input directory from which files to pull files",
					"required": true,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": true,
					"expressionLanguageScope": "Variable Registry Only"
				},
				"Recurse Subdirectories": {
					"name": "Recurse Subdirectories",
					"displayName": "Recurse Subdirectories",
					"description": "Indicates whether to list files from subdirectories of the directory",
					"defaultValue": "true",
					"allowableValues": [{
							"allowableValue": {
								"displayName": "true",
								"value": "true"
							},
							"canRead": true
						}, {
							"allowableValue": {
								"displayName": "false",
								"value": "false"
							},
							"canRead": true
						}
					],
					"required": true,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"Input Directory Location": {
					"name": "Input Directory Location",
					"displayName": "Input Directory Location",
					"description": "Specifies where the Input Directory is located. This is used to determine whether state should be stored locally or across the cluster.",
					"defaultValue": "Local",
					"allowableValues": [{
							"allowableValue": {
								"displayName": "Local",
								"value": "Local",
								"description": "Input Directory is located on a local disk. State will be stored locally on each node in the cluster."
							},
							"canRead": true
						}, {
							"allowableValue": {
								"displayName": "Remote",
								"value": "Remote",
								"description": "Input Directory is located on a remote system. State will be stored across the cluster so that the listing can be performed on Primary Node Only and another node can pick up where the last node left off, if the Primary Node changes"
							},
							"canRead": true
						}
					],
					"required": true,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"File Filter": {
					"name": "File Filter",
					"displayName": "File Filter",
					"description": "Only files whose names match the given regular expression will be picked up",
					"defaultValue": "[^\\.].*",
					"required": true,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"Path Filter": {
					"name": "Path Filter",
					"displayName": "Path Filter",
					"description": "When Recurse Subdirectories is true, then only subdirectories whose path matches the given regular expression will be scanned",
					"required": false,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"Include File Attributes": {
					"name": "Include File Attributes",
					"displayName": "Include File Attributes",
					"description": "Whether or not to include information such as the file's Last Modified Time and Owner as FlowFile Attributes. Depending on the File System being used, gathering this information can be expensive and as a result should be disabled. This is especially true of remote file shares.",
					"defaultValue": "true",
					"allowableValues": [{
							"allowableValue": {
								"displayName": "true",
								"value": "true"
							},
							"canRead": true
						}, {
							"allowableValue": {
								"displayName": "false",
								"value": "false"
							},
							"canRead": true
						}
					],
					"required": true,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"Minimum File Age": {
					"name": "Minimum File Age",
					"displayName": "Minimum File Age",
					"description": "The minimum age that a file must be in order to be pulled; any file younger than this amount of time (according to last modification date) will be ignored",
					"defaultValue": "0 sec",
					"required": true,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"Maximum File Age": {
					"name": "Maximum File Age",
					"displayName": "Maximum File Age",
					"description": "The maximum age that a file must be in order to be pulled; any file older than this amount of time (according to last modification date) will be ignored",
					"required": false,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"Minimum File Size": {
					"name": "Minimum File Size",
					"displayName": "Minimum File Size",
					"description": "The minimum size that a file must be in order to be pulled",
					"defaultValue": "0 B",
					"required": true,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"Maximum File Size": {
					"name": "Maximum File Size",
					"displayName": "Maximum File Size",
					"description": "The maximum size that a file can be in order to be pulled",
					"required": false,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"Ignore Hidden Files": {
					"name": "Ignore Hidden Files",
					"displayName": "Ignore Hidden Files",
					"description": "Indicates whether or not hidden files should be ignored",
					"defaultValue": "true",
					"allowableValues": [{
							"allowableValue": {
								"displayName": "true",
								"value": "true"
							},
							"canRead": true
						}, {
							"allowableValue": {
								"displayName": "false",
								"value": "false"
							},
							"canRead": true
						}
					],
					"required": true,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"target-system-timestamp-precision": {
					"name": "target-system-timestamp-precision",
					"displayName": "Target System Timestamp Precision",
					"description": "Specify timestamp precision at the target system. Since this processor uses timestamp of entities to decide which should be listed, it is crucial to use the right timestamp precision.",
					"defaultValue": "auto-detect",
					"allowableValues": [{
							"allowableValue": {
								"displayName": "Auto Detect",
								"value": "auto-detect",
								"description": "Automatically detect time unit deterministically based on candidate entries timestamp. Please note that this option may take longer to list entities unnecessarily, if none of entries has a precise precision timestamp. E.g. even if a target system supports millis, if all entries only have timestamps without millis, such as '2017-06-16 09:06:34.000', then its precision is determined as 'seconds'."
							},
							"canRead": true
						}, {
							"allowableValue": {
								"displayName": "Milliseconds",
								"value": "millis",
								"description": "This option provides the minimum latency for an entry from being available to being listed if target system supports millis, if not, use other options."
							},
							"canRead": true
						}, {
							"allowableValue": {
								"displayName": "Seconds",
								"value": "seconds",
								"description": "For a target system that does not have millis precision, but has in seconds."
							},
							"canRead": true
						}, {
							"allowableValue": {
								"displayName": "Minutes",
								"value": "minutes",
								"description": "For a target system that only supports precision in minutes."
							},
							"canRead": true
						}
					],
					"required": true,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"et-state-cache": {
					"name": "et-state-cache",
					"displayName": "Entity Tracking State Cache",
					"description": "Listed entities are stored in the specified cache storage so that this processor can resume listing across NiFi restart or in case of primary node change. 'Tracking Entities' strategy require tracking information of all listed entities within the last 'Tracking Time Window'. To support large number of entities, the strategy uses DistributedMapCache instead of managed state. Cache key format is 'ListedEntities::{processorId}(::{nodeId})'. If it tracks per node listed entities, then the optional '::{nodeId}' part is added to manage state separately. E.g. cluster wide cache key = 'ListedEntities::8dda2321-0164-1000-50fa-3042fe7d6a7b', per node cache key = 'ListedEntities::8dda2321-0164-1000-50fa-3042fe7d6a7b::nifi-node3' The stored cache content is Gzipped JSON string. The cache key will be deleted when target listing configuration is changed. Used by 'Tracking Entities' strategy.",
					"allowableValues": [],
					"required": false,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported",
					"identifiesControllerService": "org.apache.nifi.distributed.cache.client.DistributedMapCacheClient",
					"identifiesControllerServiceBundle": {
						"group": "org.apache.nifi",
						"artifact": "nifi-standard-services-api-nar",
						"version": "1.8.0"
					}
				},
				"et-time-window": {
					"name": "et-time-window",
					"displayName": "Entity Tracking Time Window",
					"description": "Specify how long this processor should track already-listed entities. 'Tracking Entities' strategy can pick any entity whose timestamp is inside the specified time window. For example, if set to '30 minutes', any entity having timestamp in recent 30 minutes will be the listing target when this processor runs. A listed entity is considered 'new/updated' and a FlowFile is emitted if one of following condition meets: 1. does not exist in the already-listed entities, 2. has newer timestamp than the cached entity, 3. has different size than the cached entity. If a cached entity's timestamp becomes older than specified time window, that entity will be removed from the cached already-listed entities. Used by 'Tracking Entities' strategy.",
					"defaultValue": "3 hours",
					"required": false,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": true,
					"expressionLanguageScope": "Variable Registry Only"
				},
				"et-initial-listing-target": {
					"name": "et-initial-listing-target",
					"displayName": "Entity Tracking Initial Listing Target",
					"description": "Specify how initial listing should be handled. Used by 'Tracking Entities' strategy.",
					"defaultValue": "all",
					"allowableValues": [{
							"allowableValue": {
								"displayName": "Tracking Time Window",
								"value": "window",
								"description": "Ignore entities having timestamp older than the specified 'Tracking Time Window' at the initial listing activity."
							},
							"canRead": true
						}, {
							"allowableValue": {
								"displayName": "All Available",
								"value": "all",
								"description": "Regardless of entities timestamp, all existing entities will be listed at the initial listing activity."
							},
							"canRead": true
						}
					],
					"required": false,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"et-node-identifier": {
					"name": "et-node-identifier",
					"displayName": "Entity Tracking Node Identifier",
					"description": "The configured value will be appended to the cache key so that listing state can be tracked per NiFi node rather than cluster wide when tracking state is scoped to LOCAL. Used by 'Tracking Entities' strategy.",
					"defaultValue": "${hostname()}",
					"required": false,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": true,
					"expressionLanguageScope": "Variable Registry Only"
				}
			},
			"schedulingPeriod": "0 s",
			"schedulingStrategy": "TIMER_DRIVEN",
			"executionNode": "PRIMARY",
			"penaltyDuration": "30 sec",
			"yieldDuration": "1 sec",
			"bulletinLevel": "WARN",
			"runDurationMillis": 0,
			"concurrentlySchedulableTaskCount": 1,
			"comments": "",
			"lossTolerant": false,
			"defaultConcurrentTasks": {
				"TIMER_DRIVEN": "1",
				"EVENT_DRIVEN": "0",
				"CRON_DRIVEN": "1"
			},
			"defaultSchedulingPeriod": {
				"TIMER_DRIVEN": "0 sec",
				"CRON_DRIVEN": "* * * * * ?"
			}
		},
		"validationStatus": "VALID",
		"extensionMissing": false
	},
	"inputRequirement": "INPUT_FORBIDDEN",
	"status": {
		"groupId": "0574f873-97d7-3a8b-3a86-550f2a775aa1",
		"id": "3a743c7a-6a73-3611-d91b-ab2478edfb5f",
		"name": "ListFile",
		"runStatus": "Stopped",
		"statsLastRefreshed": "21:07:29 CET",
		"aggregateSnapshot": {
			"id": "3a743c7a-6a73-3611-d91b-ab2478edfb5f",
			"groupId": "0574f873-97d7-3a8b-3a86-550f2a775aa1",
			"name": "ListFile",
			"type": "ListFile",
			"runStatus": "Stopped",
			"executionNode": "PRIMARY",
			"bytesRead": 0,
			"bytesWritten": 0,
			"read": "0 bytes",
			"written": "0 bytes",
			"flowFilesIn": 0,
			"bytesIn": 0,
			"input": "0 (0 bytes)",
			"flowFilesOut": 0,
			"bytesOut": 0,
			"output": "0 (0 bytes)",
			"taskCount": 0,
			"tasksDurationNanos": 0,
			"tasks": "0",
			"tasksDuration": "00:00:00.000",
			"activeThreadCount": 0,
			"terminatedThreadCount": 0
		}
	},
	"operatePermissions": {
		"canRead": true,
		"canWrite": true
	}
}
```



### Update Processor

```bash
curl 'http://localhost:8080/nifi-api/processors/3a743c7a-6a73-3611-d91b-ab2478edfb5f' -X PUT --data-binary '{"component":{"id":"3a743c7a-6a73-3611-d91b-ab2478edfb5f","name":"ListFile","config":{"schedulingPeriod":"0 s","executionNode":"PRIMARY","penaltyDuration":"30 sec","yieldDuration":"1 sec","bulletinLevel":"WARN","schedulingStrategy":"TIMER_DRIVEN","comments":"","autoTerminatedRelationships":[],"properties":{"Path Filter":"for"}},"state":"STOPPED"},"revision":{"clientId":"2b49939b-0169-1000-3b8d-100c0336546f","version":0},"disconnectedNodeAcknowledged":false}' --compressed
```



```json
{
	"revision": {
		"clientId": "2b49939b-0169-1000-3b8d-100c0336546f",
		"version": 1,
		"lastModifier": "anonymous"
	},
	"id": "3a743c7a-6a73-3611-d91b-ab2478edfb5f",
	"uri": "http://localhost:8080/nifi-api/processors/3a743c7a-6a73-3611-d91b-ab2478edfb5f",
	"position": {
		"x": 354.99999536407995,
		"y": 89.99998894099326
	},
	"permissions": {
		"canRead": true,
		"canWrite": true
	},
	"bulletins": [],
	"component": {
		"id": "3a743c7a-6a73-3611-d91b-ab2478edfb5f",
		"parentGroupId": "0574f873-97d7-3a8b-3a86-550f2a775aa1",
		"position": {
			"x": 354.99999536407995,
			"y": 89.99998894099326
		},
		"name": "ListFile",
		"type": "org.apache.nifi.processors.standard.ListFile",
		"bundle": {
			"group": "org.apache.nifi",
			"artifact": "nifi-standard-nar",
			"version": "1.8.0"
		},
		"state": "STOPPED",
		"style": {},
		"relationships": [{
				"name": "success",
				"description": "All FlowFiles that are received are routed to success",
				"autoTerminate": false
			}
		],
		"supportsParallelProcessing": false,
		"supportsEventDriven": false,
		"supportsBatching": false,
		"persistsState": true,
		"restricted": false,
		"deprecated": false,
		"executionNodeRestricted": false,
		"multipleVersionsAvailable": false,
		"inputRequirement": "INPUT_FORBIDDEN",
		"config": {
			"properties": {
				"listing-strategy": "timestamps",
				"Input Directory": "${sdp_input_dir}",
				"Recurse Subdirectories": "true",
				"Input Directory Location": "Local",
				"File Filter": "[^\\.].*",
				"Path Filter": "for",
				"Include File Attributes": "true",
				"Minimum File Age": "0 sec",
				"Maximum File Age": null,
				"Minimum File Size": "0 B",
				"Maximum File Size": null,
				"Ignore Hidden Files": "true",
				"target-system-timestamp-precision": "auto-detect",
				"et-state-cache": null,
				"et-time-window": "3 hours",
				"et-initial-listing-target": "all",
				"et-node-identifier": "${hostname()}"
			},
			"descriptors": {
				"listing-strategy": {
					"name": "listing-strategy",
					"displayName": "Listing Strategy",
					"description": "Specify how to determine new/updated entities. See each strategy descriptions for detail.",
					"defaultValue": "timestamps",
					"allowableValues": [{
							"allowableValue": {
								"displayName": "Tracking Timestamps",
								"value": "timestamps",
								"description": "This strategy tracks the latest timestamp of listed entity to determine new/updated entities. Since it only tracks few timestamps, it can manage listing state efficiently. However, any newly added, or updated entity having timestamp older than the tracked latest timestamp can not be picked by this strategy. For example, such situation can happen in a file system if a file with old timestamp is copied or moved into the target directory without its last modified timestamp being updated."
							},
							"canRead": true
						}, {
							"allowableValue": {
								"displayName": "Tracking Entities",
								"value": "entities",
								"description": "This strategy tracks information of all the listed entities within the latest 'Entity Tracking Time Window' to determine new/updated entities. This strategy can pick entities having old timestamp that can be missed with 'Tracing Timestamps'. However additional DistributedMapCache controller service is required and more JVM heap memory is used. See the description of 'Entity Tracking Time Window' property for further details on how it works."
							},
							"canRead": true
						}
					],
					"required": true,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"Input Directory": {
					"name": "Input Directory",
					"displayName": "Input Directory",
					"description": "The input directory from which files to pull files",
					"required": true,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": true,
					"expressionLanguageScope": "Variable Registry Only"
				},
				"Recurse Subdirectories": {
					"name": "Recurse Subdirectories",
					"displayName": "Recurse Subdirectories",
					"description": "Indicates whether to list files from subdirectories of the directory",
					"defaultValue": "true",
					"allowableValues": [{
							"allowableValue": {
								"displayName": "true",
								"value": "true"
							},
							"canRead": true
						}, {
							"allowableValue": {
								"displayName": "false",
								"value": "false"
							},
							"canRead": true
						}
					],
					"required": true,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"Input Directory Location": {
					"name": "Input Directory Location",
					"displayName": "Input Directory Location",
					"description": "Specifies where the Input Directory is located. This is used to determine whether state should be stored locally or across the cluster.",
					"defaultValue": "Local",
					"allowableValues": [{
							"allowableValue": {
								"displayName": "Local",
								"value": "Local",
								"description": "Input Directory is located on a local disk. State will be stored locally on each node in the cluster."
							},
							"canRead": true
						}, {
							"allowableValue": {
								"displayName": "Remote",
								"value": "Remote",
								"description": "Input Directory is located on a remote system. State will be stored across the cluster so that the listing can be performed on Primary Node Only and another node can pick up where the last node left off, if the Primary Node changes"
							},
							"canRead": true
						}
					],
					"required": true,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"File Filter": {
					"name": "File Filter",
					"displayName": "File Filter",
					"description": "Only files whose names match the given regular expression will be picked up",
					"defaultValue": "[^\\.].*",
					"required": true,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"Path Filter": {
					"name": "Path Filter",
					"displayName": "Path Filter",
					"description": "When Recurse Subdirectories is true, then only subdirectories whose path matches the given regular expression will be scanned",
					"required": false,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"Include File Attributes": {
					"name": "Include File Attributes",
					"displayName": "Include File Attributes",
					"description": "Whether or not to include information such as the file's Last Modified Time and Owner as FlowFile Attributes. Depending on the File System being used, gathering this information can be expensive and as a result should be disabled. This is especially true of remote file shares.",
					"defaultValue": "true",
					"allowableValues": [{
							"allowableValue": {
								"displayName": "true",
								"value": "true"
							},
							"canRead": true
						}, {
							"allowableValue": {
								"displayName": "false",
								"value": "false"
							},
							"canRead": true
						}
					],
					"required": true,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"Minimum File Age": {
					"name": "Minimum File Age",
					"displayName": "Minimum File Age",
					"description": "The minimum age that a file must be in order to be pulled; any file younger than this amount of time (according to last modification date) will be ignored",
					"defaultValue": "0 sec",
					"required": true,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"Maximum File Age": {
					"name": "Maximum File Age",
					"displayName": "Maximum File Age",
					"description": "The maximum age that a file must be in order to be pulled; any file older than this amount of time (according to last modification date) will be ignored",
					"required": false,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"Minimum File Size": {
					"name": "Minimum File Size",
					"displayName": "Minimum File Size",
					"description": "The minimum size that a file must be in order to be pulled",
					"defaultValue": "0 B",
					"required": true,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"Maximum File Size": {
					"name": "Maximum File Size",
					"displayName": "Maximum File Size",
					"description": "The maximum size that a file can be in order to be pulled",
					"required": false,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"Ignore Hidden Files": {
					"name": "Ignore Hidden Files",
					"displayName": "Ignore Hidden Files",
					"description": "Indicates whether or not hidden files should be ignored",
					"defaultValue": "true",
					"allowableValues": [{
							"allowableValue": {
								"displayName": "true",
								"value": "true"
							},
							"canRead": true
						}, {
							"allowableValue": {
								"displayName": "false",
								"value": "false"
							},
							"canRead": true
						}
					],
					"required": true,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"target-system-timestamp-precision": {
					"name": "target-system-timestamp-precision",
					"displayName": "Target System Timestamp Precision",
					"description": "Specify timestamp precision at the target system. Since this processor uses timestamp of entities to decide which should be listed, it is crucial to use the right timestamp precision.",
					"defaultValue": "auto-detect",
					"allowableValues": [{
							"allowableValue": {
								"displayName": "Auto Detect",
								"value": "auto-detect",
								"description": "Automatically detect time unit deterministically based on candidate entries timestamp. Please note that this option may take longer to list entities unnecessarily, if none of entries has a precise precision timestamp. E.g. even if a target system supports millis, if all entries only have timestamps without millis, such as '2017-06-16 09:06:34.000', then its precision is determined as 'seconds'."
							},
							"canRead": true
						}, {
							"allowableValue": {
								"displayName": "Milliseconds",
								"value": "millis",
								"description": "This option provides the minimum latency for an entry from being available to being listed if target system supports millis, if not, use other options."
							},
							"canRead": true
						}, {
							"allowableValue": {
								"displayName": "Seconds",
								"value": "seconds",
								"description": "For a target system that does not have millis precision, but has in seconds."
							},
							"canRead": true
						}, {
							"allowableValue": {
								"displayName": "Minutes",
								"value": "minutes",
								"description": "For a target system that only supports precision in minutes."
							},
							"canRead": true
						}
					],
					"required": true,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"et-state-cache": {
					"name": "et-state-cache",
					"displayName": "Entity Tracking State Cache",
					"description": "Listed entities are stored in the specified cache storage so that this processor can resume listing across NiFi restart or in case of primary node change. 'Tracking Entities' strategy require tracking information of all listed entities within the last 'Tracking Time Window'. To support large number of entities, the strategy uses DistributedMapCache instead of managed state. Cache key format is 'ListedEntities::{processorId}(::{nodeId})'. If it tracks per node listed entities, then the optional '::{nodeId}' part is added to manage state separately. E.g. cluster wide cache key = 'ListedEntities::8dda2321-0164-1000-50fa-3042fe7d6a7b', per node cache key = 'ListedEntities::8dda2321-0164-1000-50fa-3042fe7d6a7b::nifi-node3' The stored cache content is Gzipped JSON string. The cache key will be deleted when target listing configuration is changed. Used by 'Tracking Entities' strategy.",
					"allowableValues": [],
					"required": false,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported",
					"identifiesControllerService": "org.apache.nifi.distributed.cache.client.DistributedMapCacheClient",
					"identifiesControllerServiceBundle": {
						"group": "org.apache.nifi",
						"artifact": "nifi-standard-services-api-nar",
						"version": "1.8.0"
					}
				},
				"et-time-window": {
					"name": "et-time-window",
					"displayName": "Entity Tracking Time Window",
					"description": "Specify how long this processor should track already-listed entities. 'Tracking Entities' strategy can pick any entity whose timestamp is inside the specified time window. For example, if set to '30 minutes', any entity having timestamp in recent 30 minutes will be the listing target when this processor runs. A listed entity is considered 'new/updated' and a FlowFile is emitted if one of following condition meets: 1. does not exist in the already-listed entities, 2. has newer timestamp than the cached entity, 3. has different size than the cached entity. If a cached entity's timestamp becomes older than specified time window, that entity will be removed from the cached already-listed entities. Used by 'Tracking Entities' strategy.",
					"defaultValue": "3 hours",
					"required": false,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": true,
					"expressionLanguageScope": "Variable Registry Only"
				},
				"et-initial-listing-target": {
					"name": "et-initial-listing-target",
					"displayName": "Entity Tracking Initial Listing Target",
					"description": "Specify how initial listing should be handled. Used by 'Tracking Entities' strategy.",
					"defaultValue": "all",
					"allowableValues": [{
							"allowableValue": {
								"displayName": "Tracking Time Window",
								"value": "window",
								"description": "Ignore entities having timestamp older than the specified 'Tracking Time Window' at the initial listing activity."
							},
							"canRead": true
						}, {
							"allowableValue": {
								"displayName": "All Available",
								"value": "all",
								"description": "Regardless of entities timestamp, all existing entities will be listed at the initial listing activity."
							},
							"canRead": true
						}
					],
					"required": false,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": false,
					"expressionLanguageScope": "Not Supported"
				},
				"et-node-identifier": {
					"name": "et-node-identifier",
					"displayName": "Entity Tracking Node Identifier",
					"description": "The configured value will be appended to the cache key so that listing state can be tracked per NiFi node rather than cluster wide when tracking state is scoped to LOCAL. Used by 'Tracking Entities' strategy.",
					"defaultValue": "${hostname()}",
					"required": false,
					"sensitive": false,
					"dynamic": false,
					"supportsEl": true,
					"expressionLanguageScope": "Variable Registry Only"
				}
			},
			"schedulingPeriod": "0 s",
			"schedulingStrategy": "TIMER_DRIVEN",
			"executionNode": "PRIMARY",
			"penaltyDuration": "30 sec",
			"yieldDuration": "1 sec",
			"bulletinLevel": "WARN",
			"runDurationMillis": 0,
			"concurrentlySchedulableTaskCount": 1,
			"comments": "",
			"lossTolerant": false,
			"defaultConcurrentTasks": {
				"TIMER_DRIVEN": "1",
				"EVENT_DRIVEN": "0",
				"CRON_DRIVEN": "1"
			},
			"defaultSchedulingPeriod": {
				"TIMER_DRIVEN": "0 sec",
				"CRON_DRIVEN": "* * * * * ?"
			}
		},
		"validationStatus": "VALID",
		"extensionMissing": false
	},
	"inputRequirement": "INPUT_FORBIDDEN",
	"status": {
		"groupId": "0574f873-97d7-3a8b-3a86-550f2a775aa1",
		"id": "3a743c7a-6a73-3611-d91b-ab2478edfb5f",
		"name": "ListFile",
		"runStatus": "Stopped",
		"statsLastRefreshed": "21:10:49 CET",
		"aggregateSnapshot": {
			"id": "3a743c7a-6a73-3611-d91b-ab2478edfb5f",
			"groupId": "0574f873-97d7-3a8b-3a86-550f2a775aa1",
			"name": "ListFile",
			"type": "ListFile",
			"runStatus": "Stopped",
			"executionNode": "PRIMARY",
			"bytesRead": 0,
			"bytesWritten": 0,
			"read": "0 bytes",
			"written": "0 bytes",
			"flowFilesIn": 0,
			"bytesIn": 0,
			"input": "0 (0 bytes)",
			"flowFilesOut": 0,
			"bytesOut": 0,
			"output": "0 (0 bytes)",
			"taskCount": 0,
			"tasksDurationNanos": 0,
			"tasks": "0",
			"tasksDuration": "00:00:00.000",
			"activeThreadCount": 0,
			"terminatedThreadCount": 0
		}
	},
	"operatePermissions": {
		"canRead": true,
		"canWrite": true
	}
}

```



# Data for Demo

https://randomuser.me/api/?format=csv&inc=gender,name,nat&seed=ivan1&results=200

