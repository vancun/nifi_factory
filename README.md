# NiFi Factory

NiFi Factory is a set of tools for automated NiFi flow generation and flow management. 



## NiFi Shell - Interactive Command Line Client

NiFi Shell provides a way to interact with and explore the NiFi REST API. 

To start NiFi Shell

```bash
python .\bin\nifi-cli.py shell
```

Above command will start NiFi Shell, trying to connect to NiFi on http://localhost:8080

The general syntax for starting the NiFi Shell is as follows:

```
Usage: nifi-cli.py shell [OPTIONS] [NIFI_URL]

  Interactive nifi shell

Options:
  --help  Show this message and exit.
```



## NiFi Builder - Automated Data Pipeline Build in NiFi

NiFi Builder provides a command line interface for building and updating NiFi data pipelines, defined using a pipeline descriptor in JSON.

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



More information could be found in the [NiFi builder documentation](docs/NiFi-Builder.md).