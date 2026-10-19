"""Generated from Smithy shape ``com.amazonaws.cloud9#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloud9.types.tag_key
    import capo_cloud9.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_cloud9.types.tag_key.TagKey"
    """<p>The <b>name</b> part of a tag.</p>"""
    value: "capo_cloud9.types.tag_value.TagValue"
    """<p>The <b>value</b> part of a tag.</p>"""


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
