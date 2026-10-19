"""Generated from Smithy shape ``com.amazonaws.iotevents#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.amazon_resource_name
    import capo_iot_events.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_iot_events.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the resource.</p>"""
    tags: "capo_iot_events.types.tags.Tags"
    """<p>The new or modified tags for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_iot_events.types.tags

    out["tags"] = capo_iot_events.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_iot_events.types.tags

        out["tags"] = capo_iot_events.types.tags.deserialize_json(data["tags"])
    else:
        out["tags"] = []
    return out
