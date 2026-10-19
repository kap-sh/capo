"""Generated from Smithy shape ``com.amazonaws.ssm#GetInventorySchemaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.aggregator_schema_only
    import capo_ssm.types.get_inventory_schema_max_results
    import capo_ssm.types.inventory_item_type_name_filter
    import capo_ssm.types.is_sub_type_schema
    import capo_ssm.types.next_token


class GetInventorySchemaRequest(TypedDict, closed=True):
    type_name: NotRequired[
        "capo_ssm.types.inventory_item_type_name_filter.InventoryItemTypeNameFilter"
    ]
    """<p>The type of inventory item to return.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_results: NotRequired[
        "capo_ssm.types.get_inventory_schema_max_results.GetInventorySchemaMaxResults"
    ]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    aggregator: NotRequired[
        "capo_ssm.types.aggregator_schema_only.AggregatorSchemaOnly"
    ]
    """<p>Returns inventory schemas that support aggregation. For example, this call returns the <code>AWS:InstanceInformation</code> type, because it supports aggregation based on the <code>PlatformName</code>, <code>PlatformType</code>, and <code>PlatformVersion</code> attributes.</p>"""
    sub_type: NotRequired["capo_ssm.types.is_sub_type_schema.IsSubTypeSchema"]
    """<p>Returns the sub-type schema for a specified inventory type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInventorySchemaRequest) -> dict:
    out: dict = {}
    if "type_name" in value:
        out["TypeName"] = value["type_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "aggregator" in value:
        out["Aggregator"] = value["aggregator"]
    if "sub_type" in value:
        out["SubType"] = value["sub_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInventorySchemaRequest:
    out: GetInventorySchemaRequest = {}  # type: ignore[typeddict-item]
    if data.get("TypeName") is not None:
        out["type_name"] = data["TypeName"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Aggregator") is not None:
        out["aggregator"] = data["Aggregator"]
    if data.get("SubType") is not None:
        out["sub_type"] = data["SubType"]
    return out
