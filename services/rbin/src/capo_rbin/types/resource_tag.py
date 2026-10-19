"""Generated from Smithy shape ``com.amazonaws.rbin#ResourceTag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rbin.types.resource_tag_key
    import capo_rbin.types.resource_tag_value


class ResourceTag(TypedDict, closed=True):
    resource_tag_key: "capo_rbin.types.resource_tag_key.ResourceTagKey"
    """<p>The tag key.</p>"""
    resource_tag_value: NotRequired[
        "capo_rbin.types.resource_tag_value.ResourceTagValue"
    ]
    """<p>The tag value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTag) -> dict:
    out: dict = {}
    out["ResourceTagKey"] = value["resource_tag_key"]
    if "resource_tag_value" in value:
        out["ResourceTagValue"] = value["resource_tag_value"]
    return out


def deserialize_json(data: dict) -> ResourceTag:
    out: ResourceTag = {}  # type: ignore[typeddict-item]
    if data.get("ResourceTagKey") is not None:
        out["resource_tag_key"] = data["ResourceTagKey"]
    else:
        out["resource_tag_key"] = ""
    if data.get("ResourceTagValue") is not None:
        out["resource_tag_value"] = data["ResourceTagValue"]
    return out
