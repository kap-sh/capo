"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_metering.types.tag_key
    import capo_marketplace_metering.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_marketplace_metering.types.tag_key.TagKey"
    """<p>One part of a key-value pair that makes up a <code>tag</code>. A <code>key</code> is a label that acts like a category for the specific tag values.</p>"""
    value: "capo_marketplace_metering.types.tag_value.TagValue"
    """<p>One part of a key-value pair that makes up a <code>tag</code>. A <code>value</code> acts as a descriptor within a tag category (key). The value can be empty or null.</p>"""


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
