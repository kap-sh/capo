"""Generated from Smithy shape ``com.amazonaws.inspector2#ConnectorCloudProvider``."""

from typing import Literal, TypeAlias, cast

ConnectorCloudProvider: TypeAlias = Literal[
    "AZURE",
    "GCP",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorCloudProvider) -> str:
    return value


def deserialize_json(data: str) -> ConnectorCloudProvider:
    return cast(ConnectorCloudProvider, data)
