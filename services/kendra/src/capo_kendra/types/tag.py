"""Generated from Smithy shape ``com.amazonaws.kendra#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.tag_key
    import capo_kendra.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_kendra.types.tag_key.TagKey"
    """<p>The key for the tag. Keys are not case sensitive and must be unique for the index, FAQ, data source, or other resource.</p>"""
    value: "capo_kendra.types.tag_value.TagValue"
    """<p>The value associated with the tag. The value may be an empty string but it can't be null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
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
    else:
        out["value"] = ""
    return out
