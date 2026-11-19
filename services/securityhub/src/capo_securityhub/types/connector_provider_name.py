"""Generated from Smithy shape ``com.amazonaws.securityhub#ConnectorProviderName``."""

from typing import Literal, TypeAlias, cast

ConnectorProviderName: TypeAlias = Literal[
    "JIRA_CLOUD",
    "SERVICENOW",
    "AZURE",
    "GCP",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorProviderName) -> str:
    return value


def deserialize_json(data: str) -> ConnectorProviderName:
    return cast(ConnectorProviderName, data)
