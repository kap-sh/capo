"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#ResourceTagsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_agent_registry_control.types.tag_key
    import capo_agent_registry_control.types.tag_value

ResourceTagsMap: TypeAlias = dict[
    "capo_agent_registry_control.types.tag_key.TagKey",
    "capo_agent_registry_control.types.tag_value.TagValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ResourceTagsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ResourceTagsMap:
    out: ResourceTagsMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
