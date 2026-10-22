"""Generated from Smithy shape ``com.amazonaws.devopsagent#Service``."""

from typing import Literal, TypeAlias, cast

"""<p>Enumeration of all supported service types, combining OAuth 3-legged, client credentials, and simple token authentication methods.</p>"""
Service: TypeAlias = Literal[
    "github",
    "slack",
    "azure",
    "azuredevops",
    "msteams",
    "dynatrace",
    "servicenow",
    "pagerduty",
    "gitlab",
    "eventChannel",
    "mcpservernewrelic",
    "mcpservergrafana",
    "mcpserverdatadog",
    "mcpserver",
    "mcpserversplunk",
    "azureidentity",
    "mcpserversigv4",
    "remoteagent",
    "remoteagentsigv4",
]


# --- restJson1 ser/de ---
def serialize_json(value: Service) -> str:
    return value


def deserialize_json(data: str) -> Service:
    return cast(Service, data)
