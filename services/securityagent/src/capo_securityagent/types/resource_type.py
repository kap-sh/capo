"""Generated from Smithy shape ``com.amazonaws.securityagent#ResourceType``."""

from typing import Literal, TypeAlias, cast

"""<p>Type of resource.</p>"""
ResourceType: TypeAlias = Literal[
    "CODE_REPOSITORY",
    "DOCUMENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    return cast(ResourceType, data)
