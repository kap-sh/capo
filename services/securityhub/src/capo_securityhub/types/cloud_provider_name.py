"""Generated from Smithy shape ``com.amazonaws.securityhub#CloudProviderName``."""

from typing import Literal, TypeAlias, cast

CloudProviderName: TypeAlias = Literal[
    "Azure",
    "AWS",
    "GCP",
]


# --- restJson1 ser/de ---
def serialize_json(value: CloudProviderName) -> str:
    return value


def deserialize_json(data: str) -> CloudProviderName:
    return cast(CloudProviderName, data)
