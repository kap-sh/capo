"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostAllocationTag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.cost_allocation_tag_status
    import capo_cost_explorer.types.cost_allocation_tag_type
    import capo_cost_explorer.types.tag_key
    import capo_cost_explorer.types.zoned_date_time


class CostAllocationTag(TypedDict, closed=True):
    tag_key: "capo_cost_explorer.types.tag_key.TagKey"
    """<p>The key for the cost allocation tag. </p>"""
    type: "capo_cost_explorer.types.cost_allocation_tag_type.CostAllocationTagType"
    """<p>The type of cost allocation tag. You can use <code>AWSGenerated</code> or <code>UserDefined</code> type tags. <code>AWSGenerated</code> type tags are tags that Amazon Web Services defines and applies to support Amazon Web Services resources for cost allocation purposes. <code>UserDefined</code> type tags are tags that you define, create, and apply to resources. </p>"""
    status: (
        "capo_cost_explorer.types.cost_allocation_tag_status.CostAllocationTagStatus"
    )
    """<p>The status of a cost allocation tag. </p>"""
    last_updated_date: NotRequired[
        "capo_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    """<p>The last date that the tag was either activated or deactivated.</p>"""
    last_used_date: NotRequired[
        "capo_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    """<p>The last month that the tag was used on an Amazon Web Services resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostAllocationTag) -> dict:
    out: dict = {}
    out["TagKey"] = value["tag_key"]
    import capo_cost_explorer.types.cost_allocation_tag_type

    out["Type"] = (
        capo_cost_explorer.types.cost_allocation_tag_type.serialize_aws_json_1_1(
            value["type"]
        )
    )
    import capo_cost_explorer.types.cost_allocation_tag_status

    out["Status"] = (
        capo_cost_explorer.types.cost_allocation_tag_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "last_updated_date" in value:
        out["LastUpdatedDate"] = value["last_updated_date"]
    if "last_used_date" in value:
        out["LastUsedDate"] = value["last_used_date"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CostAllocationTag:
    out: CostAllocationTag = {}  # type: ignore[typeddict-item]
    if data.get("TagKey") is not None:
        out["tag_key"] = data["TagKey"]
    else:
        out["tag_key"] = ""
    if data.get("Type") is not None:
        import capo_cost_explorer.types.cost_allocation_tag_type

        out["type"] = (
            capo_cost_explorer.types.cost_allocation_tag_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_cost_explorer.types.cost_allocation_tag_type.CostAllocationTagType",
            "",
        )
    if data.get("Status") is not None:
        import capo_cost_explorer.types.cost_allocation_tag_status

        out["status"] = (
            capo_cost_explorer.types.cost_allocation_tag_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_cost_explorer.types.cost_allocation_tag_status.CostAllocationTagStatus",
            "",
        )
    if data.get("LastUpdatedDate") is not None:
        out["last_updated_date"] = data["LastUpdatedDate"]
    if data.get("LastUsedDate") is not None:
        out["last_used_date"] = data["LastUsedDate"]
    return out
