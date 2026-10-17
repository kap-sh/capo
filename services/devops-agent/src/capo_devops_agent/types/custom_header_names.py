"""Generated from Smithy shape ``com.amazonaws.devopsagent#CustomHeaderNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.custom_header_name

CustomHeaderNames: TypeAlias = list[
    "capo_devops_agent.types.custom_header_name.CustomHeaderName"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomHeaderNames) -> list:
    return list(value)


def deserialize_json(data: list) -> CustomHeaderNames:
    return [item for item in data if item is not None]
