"""Generated from Smithy shape ``com.amazonaws.backupgateway#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.tag_key
    import capo_backup_gateway.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_backup_gateway.types.tag_key.TagKey"
    """<p>The key part of a tag's key-value pair. The key can't start with <code>aws:</code>.</p>"""
    value: "capo_backup_gateway.types.tag_value.TagValue"
    """<p>The value part of a tag's key-value pair.</p>"""


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
