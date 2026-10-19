"""Generated from Smithy shape ``com.amazonaws.storagegateway#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.tag_key
    import capo_storage_gateway.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_storage_gateway.types.tag_key.TagKey"
    """<p>Tag key. The key can't start with aws:.</p>"""
    value: "capo_storage_gateway.types.tag_value.TagValue"
    """<p>Value of the tag key.</p>"""


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
