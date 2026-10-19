"""Generated from Smithy shape ``com.amazonaws.iotwireless#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.amazon_resource_name
    import capo_iot_wireless.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_iot_wireless.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the resource to add tags to.</p>"""
    tags: "capo_iot_wireless.types.tag_list.TagList"
    """<p>Adds to or modifies the tags of the given resource. Tags are metadata that you can use to manage a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_iot_wireless.types.tag_list

    out["Tags"] = capo_iot_wireless.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_iot_wireless.types.tag_list

        out["tags"] = capo_iot_wireless.types.tag_list.deserialize_json(data["Tags"])
    else:
        out["tags"] = []
    return out
