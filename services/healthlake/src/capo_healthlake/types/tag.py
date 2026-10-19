"""Generated from Smithy shape ``com.amazonaws.healthlake#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.tag_key
    import capo_healthlake.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_healthlake.types.tag_key.TagKey"
    """<p>The key portion of a tag. Tag keys are case sensitive. </p>"""
    value: "capo_healthlake.types.tag_value.TagValue"
    """<p> The value portion of a tag. Tag values are case-sensitive.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Tag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Tag:
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
