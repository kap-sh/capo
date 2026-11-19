"""Generated from Smithy shape ``com.amazonaws.inspector2#AccountAggregation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_sort_by
    import capo_inspector2.types.aggregation_finding_type
    import capo_inspector2.types.aggregation_resource_type
    import capo_inspector2.types.sort_order


class AccountAggregation(TypedDict, closed=True):
    finding_type: NotRequired[
        "capo_inspector2.types.aggregation_finding_type.AggregationFindingType"
    ]
    """<p>The type of finding.</p>"""
    resource_type: NotRequired[
        "capo_inspector2.types.aggregation_resource_type.AggregationResourceType"
    ]
    """<p>The type of resource. For Google Cloud Platform (GCP) resources, the resource type is <code>compute.googleapis.com/Instance</code>, <code>cloudfunctions.googleapis.com/Function</code>, or <code>artifactregistry.googleapis.com/DockerImage</code>.</p>"""
    sort_order: NotRequired["capo_inspector2.types.sort_order.SortOrder"]
    """<p>The sort order (ascending or descending).</p>"""
    sort_by: NotRequired["capo_inspector2.types.account_sort_by.AccountSortBy"]
    """<p>The value to sort by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountAggregation) -> dict:
    out: dict = {}
    if "finding_type" in value:
        out["findingType"] = value["finding_type"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "sort_order" in value:
        out["sortOrder"] = value["sort_order"]
    if "sort_by" in value:
        out["sortBy"] = value["sort_by"]
    return out


def deserialize_json(data: dict) -> AccountAggregation:
    out: AccountAggregation = {}  # type: ignore[typeddict-item]
    if data.get("findingType") is not None:
        out["finding_type"] = data["findingType"]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    if data.get("sortOrder") is not None:
        out["sort_order"] = data["sortOrder"]
    if data.get("sortBy") is not None:
        out["sort_by"] = data["sortBy"]
    return out
