"""Generated from Smithy shape ``com.amazonaws.inspector#ResourceGroupTag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.tag_key
    import capo_inspector.types.tag_value


class ResourceGroupTag(TypedDict, closed=True):
    key: "capo_inspector.types.tag_key.TagKey"
    """<p>A tag key.</p>"""
    value: NotRequired["capo_inspector.types.tag_value.TagValue"]
    """<p>The value assigned to a tag key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceGroupTag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceGroupTag:
    out: ResourceGroupTag = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    return out
