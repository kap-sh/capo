"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.tag_key
    import capo_resource_groups_tagging_api.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_resource_groups_tagging_api.types.tag_key.TagKey"
    """<p>One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.</p>"""
    value: "capo_resource_groups_tagging_api.types.tag_value.TagValue"
    """<p>One part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key). The value can be empty or null.</p>"""


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
