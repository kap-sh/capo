"""Generated from Smithy shape ``com.amazonaws.devicefarm#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.tag_key
    import capo_device_farm.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_device_farm.types.tag_key.TagKey"
    """<p>One part of a key-value pair that makes up a tag. A <code>key</code> is a general label that acts like a category for more specific tag values.</p>"""
    value: "capo_device_farm.types.tag_value.TagValue"
    """<p>The optional part of a key-value pair that makes up a tag. A <code>value</code> acts as a descriptor in a tag category (key).</p>"""


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
