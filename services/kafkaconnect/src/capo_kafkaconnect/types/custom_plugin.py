"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#CustomPlugin``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__long_min1
    import capo_kafkaconnect.types.__string


class CustomPlugin(TypedDict, closed=True):
    custom_plugin_arn: "capo_kafkaconnect.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the custom plugin.</p>"""
    revision: "capo_kafkaconnect.types.__long_min1.__longMin1"
    """<p>The revision of the custom plugin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomPlugin) -> dict:
    out: dict = {}
    out["customPluginArn"] = value["custom_plugin_arn"]
    out["revision"] = value.get("revision", 0)
    return out


def deserialize_json(data: dict) -> CustomPlugin:
    out: CustomPlugin = {}  # type: ignore[typeddict-item]
    if data.get("customPluginArn") is not None:
        out["custom_plugin_arn"] = data["customPluginArn"]
    else:
        out["custom_plugin_arn"] = ""
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    else:
        out["revision"] = 0
    return out
