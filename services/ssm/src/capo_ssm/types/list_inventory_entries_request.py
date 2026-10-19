"""Generated from Smithy shape ``com.amazonaws.ssm#ListInventoryEntriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.instance_id
    import capo_ssm.types.inventory_filter_list
    import capo_ssm.types.inventory_item_type_name
    import capo_ssm.types.max_results
    import capo_ssm.types.next_token


class ListInventoryEntriesRequest(TypedDict, closed=True):
    instance_id: "capo_ssm.types.instance_id.InstanceId"
    """<p>The managed node ID for which you want inventory information.</p>"""
    type_name: "capo_ssm.types.inventory_item_type_name.InventoryItemTypeName"
    """<p>The type of inventory item for which you want information.</p>"""
    filters: NotRequired["capo_ssm.types.inventory_filter_list.InventoryFilterList"]
    """<p>One or more filters. Use a filter to return a more specific list of results.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_results: NotRequired["capo_ssm.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInventoryEntriesRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["TypeName"] = value["type_name"]
    if "filters" in value:
        import capo_ssm.types.inventory_filter_list

        out["Filters"] = capo_ssm.types.inventory_filter_list.serialize_aws_json_1_1(
            value["filters"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInventoryEntriesRequest:
    out: ListInventoryEntriesRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        out["instance_id"] = ""
    if data.get("TypeName") is not None:
        out["type_name"] = data["TypeName"]
    else:
        out["type_name"] = ""
    if data.get("Filters") is not None:
        import capo_ssm.types.inventory_filter_list

        out["filters"] = capo_ssm.types.inventory_filter_list.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
