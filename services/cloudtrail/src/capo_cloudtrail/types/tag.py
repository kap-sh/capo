"""Generated from Smithy shape ``com.amazonaws.cloudtrail#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.tag_key
    import capo_cloudtrail.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_cloudtrail.types.tag_key.TagKey"
    """<p>The key in a key-value pair. The key must be must be no longer than 128 Unicode characters. The key must be unique for the resource to which it applies.</p>"""
    value: NotRequired["capo_cloudtrail.types.tag_value.TagValue"]
    """<p>The value in a key-value pair of a tag. The value must be no longer than 256 Unicode characters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
