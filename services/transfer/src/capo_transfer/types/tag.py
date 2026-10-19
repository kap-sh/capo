"""Generated from Smithy shape ``com.amazonaws.transfer#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.tag_key
    import capo_transfer.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_transfer.types.tag_key.TagKey"
    """<p>The name assigned to the tag that you create.</p>"""
    value: "capo_transfer.types.tag_value.TagValue"
    """<p>Contains one or more values that you assigned to the key name you create.</p>"""


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
