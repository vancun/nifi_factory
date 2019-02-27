import json

from .client import NiFiClient
from .datapipeline import DataPipelineFactory
from .nififlow import NiFiProcessGroup, NiFiProcessGroupFlow

__version__ = '0.0.1'


# https://github.com/AzureAD/azure-activedirectory-library-for-python
# https://github.com/Azure-Samples/active-directory-python-webapp-graphapi/blob/master/app.py
# https://github.com/pallets/jinja

__all__ = [
    'NiFiClient',
    'NiFiProcessGroup', 'NiFiProcessGroupFlow',
    'DataPipelineFactory'
]
