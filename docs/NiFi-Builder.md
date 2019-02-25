---
typora-root-url: ./
---

# NiFi Builder

NiFi Builder provides a command line interface for building and updating NiFi data pipelines, defined using a pipeline descriptor in JSON.

* Abstract NiFi API complexity and encapsulate into a NiFi client.
* Enable multi-target and multi-platform pipeline generation with support for a variety of platforms.
* Enable fast development and maintenance by avoiding developer copy/paste.

## NiFi Builder Design Overview

To build a NiFi pipeline the NiFi Builder reads a NiFi Pipeline Descriptor and executes it against the NiFi REST API.

![NiFi-Builder-Drawings.drawio-NiFiBuilder](/img/NiFi-Builder-Drawings.drawio-NiFiBuilder.png)

The Pipeline Descriptor is a JSON document which describes the different steps of acquiring the data and parameters to be set. The steps are mapped to NiFi templates.

### NiFi Pipeline Descriptor Example

Below is presented a sample pipeline descriptor for fetching files from a `source` folder on the local file system (in Windows system), unzipping the files and storing them into a `landing` folder.

```json
{
    "name": "Demo CSV Ingest",
    "description": "Ingest CSV file from local filesystem.",
    "parameters": {
        "sdp_input_dir": "C:\\Sandbox\\notebooks\\repo\\nifi_factory\\data\\source",
        "sdp_output_dir": "C:\\Sandbox\\notebooks\\repo\\nifi_factory\\data\\landing"
    },
    "pipeline": {
        "steps": [
            {
                "name": "AcquireLocal",
                "type": "sdp_tpl_AcquireLocalFiles",
                "description": "Acquire files from local directory",
                "variables": {
                    "sdp_input_dir": "{sdp_input_dir}"
                }
            },
            {
                "name": "Unzip",
                "type": "sdp_tpl_UnzipFiles",
                "description": "Unzip Files"
            },
            {
                "name": "StoreLocal",
                "type": "sdp_tpl_PutLocalFiles",
                "variables": {
                    "sdp_output_dir": "{sdp_output_dir}"
                }
            }
        ]
    }
}
```



## Multi-target and Multi-Platform Generation Approach

![NiFi-Builder-Drawings.drawio-IntegratedApproach](/img/NiFi-Builder-Drawings.drawio-IntegratedApproach.png)

## Features

* Create NiFi Process Group to wrap the data pipeline.
  * Support `name`  - Process Group Name is updated
  * Support `description` (optional) - Process Group `Comments` updated with the description.
* Enable existing pipeline overwriting through command line parameter.
* Arbitrary templated steps could be specified
  * Support `name` - Step (Process Group) Name is updated
  * Support `description` (optional) - Step Process Group Description is updated
  * Support `variables` (optional) - Step variables are updated
* Automatic connection discovery ( `out` --> `in`) between steps.
* Parameters could be defined
  * String formatting (template replacement) for variable string expressions (See https://docs.python.org/3.4/library/string.html#format-string-syntax on Python string formatting)

## Not-implemented

* Passing parameters for expression formatting from command line - for reuse of parameters across pipelines.
* Passing parameters for expression formatting from .properties file - for reuse of parameters across pipelines.
* Define variables on Pipeline level  - useful to inherit variables from Pipeline level or global. (+)
* Remove variables from steps - useful to inherit variables from Pipeline level or global. (+)
* Update processor properties - useful for sensitive properties which are removed during template instantiation. Useful for fine-tuning of pipelines. (+)
  * Apply property update, specified in the template - to link variables with the processor instances.
* Define connections in the pipeline descriptor. - to support arbitrary complexity and steps with multiple inputs/outputs.  (-)
* Define pipeline outbound/inbound connections (from/to external pipelines/processors) (+)
* Read Pipeline Descriptor from STDIN - useful for Multi-target/platform generation. (-)
* Instantiate steps from NiFi Registry (-)
* Commit to NiFi Registry (-)

## Starting the NiFi Builder

To Start NiFi Builder:

```bash
python .\bin\nifi-builder.py <filename>
```

Where `<filename>` points to a JSON pipeline descriptor.

The general NiFi Builder command-line syntax is as follows:

```
usage: nifi-builder.py [-h] [-u NIFI_URL] [-o] filename

NiFi Flow Builder

positional arguments:
  filename

optional arguments:
  -h, --help            show this help message and exit
  -u NIFI_URL, --nifi-url NIFI_URL
                        URL for the NiFi server. Default URL:
                        http://localhost:8080
  -o, --overwrite       Overwrite existing pipeline.
```





## Pipeline Descriptor Template



```json
{
    "name": "/* Data Flow Name */",
    "description": "/* Description for the data flow. */",
    "parameters": {
        "/* parameter name */": "/* parameter value */"
    },
    "pipeline": {
        "steps": [
            {
                "name": "/* Step Name */",
                "type": "/* NiFi Template Name */",
                "description": "/* Step Description */",
                "variables": {
                    "/* variable name */": "/* string expression */"
                }
            }
        ]
    }
}
```
