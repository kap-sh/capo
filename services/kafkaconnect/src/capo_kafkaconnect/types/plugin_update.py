"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#PluginUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kafkaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kafkaconnect.types.custom_plugin_update


class PluginUpdate(TypedDict, closed=True):
    custom_plugin: "capo_kafkaconnect.types.custom_plugin_update.CustomPluginUpdate"
    """<p>The custom plugin to use for the connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PluginUpdate) -> dict:
    out: dict = {}
    import capo_kafkaconnect.types.custom_plugin_update

    out["customPlugin"] = capo_kafkaconnect.types.custom_plugin_update.serialize_json(
        value["custom_plugin"]
    )
    return out


def deserialize_json(data: dict) -> PluginUpdate:
    out: PluginUpdate = {}  # type: ignore[typeddict-item]
    if data.get("customPlugin") is not None:
        import capo_kafkaconnect.types.custom_plugin_update

        out["custom_plugin"] = (
            capo_kafkaconnect.types.custom_plugin_update.deserialize_json(
                data["customPlugin"]
            )
        )
    else:
        raise DeserializationError("PluginUpdate.custom_plugin required")
    return out
