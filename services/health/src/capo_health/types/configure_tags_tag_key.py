"""Generated from Smithy shape ``com.amazonaws.health#ConfigureTagsTagKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_health.types.boolean
    import capo_health.types.resource_tag_key2


class ConfigureTagsTagKey(TypedDict, closed=True):
    key: "capo_health.types.resource_tag_key2.ResourceTagKey2"
    """<p>The tag key name.</p>"""
    enabled_for_event_bridge: "capo_health.types.boolean.Boolean"
    """<p>Whether this tag key is enabled for EventBridge notifications.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigureTagsTagKey) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["enabledForEventBridge"] = value.get("enabled_for_event_bridge", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigureTagsTagKey:
    out: ConfigureTagsTagKey = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("enabledForEventBridge") is not None:
        out["enabled_for_event_bridge"] = data["enabledForEventBridge"]
    else:
        out["enabled_for_event_bridge"] = False
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConfigureTagsTagKey) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["enabledForEventBridge"] = value.get("enabled_for_event_bridge", False)
    return out


def deserialize_cbor(data: dict) -> ConfigureTagsTagKey:
    out: ConfigureTagsTagKey = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("enabledForEventBridge") is not None:
        out["enabled_for_event_bridge"] = data["enabledForEventBridge"]
    else:
        out["enabled_for_event_bridge"] = False
    return out
