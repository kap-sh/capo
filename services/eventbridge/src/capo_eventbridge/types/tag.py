"""Generated from Smithy shape ``com.amazonaws.eventbridge#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.tag_key
    import capo_eventbridge.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_eventbridge.types.tag_key.TagKey"
    """<p>A string you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.</p>"""
    value: "capo_eventbridge.types.tag_value.TagValue"
    """<p>The value for the specified tag key.</p>"""


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
