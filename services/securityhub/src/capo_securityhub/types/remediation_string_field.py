"""Generated from Smithy shape ``com.amazonaws.securityhub#RemediationStringField``."""

from typing import Literal, TypeAlias, cast

RemediationStringField: TypeAlias = Literal[
    "Resource.Type",
    "Priority",
    "Status",
    "Resource.Id",
    "Resource.ResourceOwnerAccountId",
    "Resource.CloudProvider",
]


# --- restJson1 ser/de ---
def serialize_json(value: RemediationStringField) -> str:
    return value


def deserialize_json(data: str) -> RemediationStringField:
    return cast(RemediationStringField, data)
