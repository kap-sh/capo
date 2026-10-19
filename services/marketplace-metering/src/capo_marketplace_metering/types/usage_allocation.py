"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#UsageAllocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_metering.types.allocated_usage_quantity
    import capo_marketplace_metering.types.tag_list


class UsageAllocation(TypedDict, closed=True):
    allocated_usage_quantity: "capo_marketplace_metering.types.allocated_usage_quantity.AllocatedUsageQuantity"
    """<p>The total quantity allocated to this bucket of usage.</p>"""
    tags: NotRequired["capo_marketplace_metering.types.tag_list.TagList"]
    """<p>The set of tags that define the bucket of usage. For the bucket of items with no tags, this parameter can be left out.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsageAllocation) -> dict:
    out: dict = {}
    out["AllocatedUsageQuantity"] = value["allocated_usage_quantity"]
    if "tags" in value:
        import capo_marketplace_metering.types.tag_list

        out["Tags"] = capo_marketplace_metering.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UsageAllocation:
    out: UsageAllocation = {}  # type: ignore[typeddict-item]
    if data.get("AllocatedUsageQuantity") is not None:
        out["allocated_usage_quantity"] = data["AllocatedUsageQuantity"]
    else:
        out["allocated_usage_quantity"] = 0
    if data.get("Tags") is not None:
        import capo_marketplace_metering.types.tag_list

        out["tags"] = capo_marketplace_metering.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
