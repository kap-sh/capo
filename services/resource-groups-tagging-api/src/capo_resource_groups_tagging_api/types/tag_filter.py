"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#TagFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.tag_key
    import capo_resource_groups_tagging_api.types.tag_value_list


class TagFilter(TypedDict, closed=True):
    key: NotRequired["capo_resource_groups_tagging_api.types.tag_key.TagKey"]
    """<p>One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.</p>"""
    values: NotRequired[
        "capo_resource_groups_tagging_api.types.tag_value_list.TagValueList"
    ]
    """<p>One part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key). The value can be empty or null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagFilter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "values" in value:
        import capo_resource_groups_tagging_api.types.tag_value_list

        out["Values"] = (
            capo_resource_groups_tagging_api.types.tag_value_list.serialize_aws_json_1_1(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagFilter:
    out: TagFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Values") is not None:
        import capo_resource_groups_tagging_api.types.tag_value_list

        out["values"] = (
            capo_resource_groups_tagging_api.types.tag_value_list.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TagFilter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "values" in value:
        import capo_resource_groups_tagging_api.types.tag_value_list

        out["Values"] = (
            capo_resource_groups_tagging_api.types.tag_value_list.serialize_cbor(
                value["values"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> TagFilter:
    out: TagFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Values") is not None:
        import capo_resource_groups_tagging_api.types.tag_value_list

        out["values"] = (
            capo_resource_groups_tagging_api.types.tag_value_list.deserialize_cbor(
                data["Values"]
            )
        )
    return out
