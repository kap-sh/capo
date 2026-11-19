"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#UsageAllocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_metering.types.allocated_usage_quantity
    import capo_marketplace_metering.types.allocated_usage_quantity_as_decimal_string
    import capo_marketplace_metering.types.tag_list


class UsageAllocation(TypedDict, closed=True):
    allocated_usage_quantity: "capo_marketplace_metering.types.allocated_usage_quantity.AllocatedUsageQuantity"
    """<p>The total quantity allocated to this bucket of usage, as a whole number.</p> <p>Use <code>AllocatedUsageQuantityAsDecimal</code> instead. Each allocation must specify exactly one of <code>AllocatedUsageQuantity</code> or <code>AllocatedUsageQuantityAsDecimal</code>.</p>"""
    allocated_usage_quantity_as_decimal: NotRequired[
        "capo_marketplace_metering.types.allocated_usage_quantity_as_decimal_string.AllocatedUsageQuantityAsDecimalString"
    ]
    """<p>The total quantity allocated to this bucket of usage, as a decimal string. Use this when the usage quantity of the request or usage record is specified as a decimal (<code>UsageQuantityAsDecimal</code> or <code>QuantityAsDecimal</code>).</p> <p>A non-negative decimal number, for example <code>17.42</code>.</p> <p>Each allocation must specify exactly one of <code>AllocatedUsageQuantity</code> or <code>AllocatedUsageQuantityAsDecimal</code>.</p>"""
    tags: NotRequired["capo_marketplace_metering.types.tag_list.TagList"]
    """<p>The set of tags that define the bucket of usage. For the bucket of items with no tags, this parameter can be left out.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsageAllocation) -> dict:
    out: dict = {}
    out["AllocatedUsageQuantity"] = value.get("allocated_usage_quantity", 0)
    if "allocated_usage_quantity_as_decimal" in value:
        out["AllocatedUsageQuantityAsDecimal"] = value[
            "allocated_usage_quantity_as_decimal"
        ]
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
    if data.get("AllocatedUsageQuantityAsDecimal") is not None:
        out["allocated_usage_quantity_as_decimal"] = data[
            "AllocatedUsageQuantityAsDecimal"
        ]
    if data.get("Tags") is not None:
        import capo_marketplace_metering.types.tag_list

        out["tags"] = capo_marketplace_metering.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
