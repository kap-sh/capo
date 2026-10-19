"""Generated from Smithy shape ``com.amazonaws.acm#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.tag_key
    import capo_acm.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_acm.types.tag_key.TagKey"
    """<p>The key of the tag.</p>"""
    value: NotRequired["capo_acm.types.tag_value.TagValue"]
    """<p>The value of the tag.</p>"""


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
