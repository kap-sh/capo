"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#__listOfPluginUpdate``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafkaconnect.types.plugin_update

__listOfPluginUpdate: TypeAlias = list[
    "capo_kafkaconnect.types.plugin_update.PluginUpdate"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfPluginUpdate) -> list:
    import capo_kafkaconnect.types.plugin_update

    out: list = []
    for item in value:
        out.append(capo_kafkaconnect.types.plugin_update.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfPluginUpdate:
    import capo_kafkaconnect.types.plugin_update

    out: __listOfPluginUpdate = []
    for item in data:
        if item is None:
            continue
        out.append(capo_kafkaconnect.types.plugin_update.deserialize_json(item))
    return out
