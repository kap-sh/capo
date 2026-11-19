"""Generated from Smithy shape ``com.amazonaws.health#ResourceTagKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.boolean
    import capo_health.types.resource_tag_key2
    import capo_health.types.tag_key_status


class ResourceTagKey(TypedDict, closed=True):
    key: NotRequired["capo_health.types.resource_tag_key2.ResourceTagKey2"]
    """<p>The tag key name.</p>"""
    enabled_for_event_bridge: "capo_health.types.boolean.Boolean"
    """<p>Whether this tag key is enabled for EventBridge notifications.</p>"""
    status: NotRequired["capo_health.types.tag_key_status.TagKeyStatus"]
    """<p>The current status of the tag key configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceTagKey) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    out["enabledForEventBridge"] = value.get("enabled_for_event_bridge", False)
    if "status" in value:
        import capo_health.types.tag_key_status

        out["status"] = capo_health.types.tag_key_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceTagKey:
    out: ResourceTagKey = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    if data.get("enabledForEventBridge") is not None:
        out["enabled_for_event_bridge"] = data["enabledForEventBridge"]
    else:
        out["enabled_for_event_bridge"] = False
    if data.get("status") is not None:
        import capo_health.types.tag_key_status

        out["status"] = capo_health.types.tag_key_status.deserialize_aws_json_1_1(
            data["status"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceTagKey) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    out["enabledForEventBridge"] = value.get("enabled_for_event_bridge", False)
    if "status" in value:
        import capo_health.types.tag_key_status

        out["status"] = capo_health.types.tag_key_status.serialize_cbor(value["status"])
    return out


def deserialize_cbor(data: dict) -> ResourceTagKey:
    out: ResourceTagKey = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    if data.get("enabledForEventBridge") is not None:
        out["enabled_for_event_bridge"] = data["enabledForEventBridge"]
    else:
        out["enabled_for_event_bridge"] = False
    if data.get("status") is not None:
        import capo_health.types.tag_key_status

        out["status"] = capo_health.types.tag_key_status.deserialize_cbor(
            data["status"]
        )
    return out
