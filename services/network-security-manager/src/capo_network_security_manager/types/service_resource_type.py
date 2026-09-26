"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ServiceResourceType``."""

from typing import Literal, TypeAlias, cast

ServiceResourceType: TypeAlias = Literal[
    "Rule",
    "Template",
    "Policy",
    "Deployment",
    "Scope",
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceResourceType) -> str:
    return value


def deserialize_json(data: str) -> ServiceResourceType:
    return cast(ServiceResourceType, data)
