"""Generated from Smithy shape ``com.amazonaws.fms#ListDiscoveredResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.discovered_resource_list
    import capo_fms.types.pagination_token


class ListDiscoveredResourcesResponse(TypedDict, closed=True):
    items: NotRequired["capo_fms.types.discovered_resource_list.DiscoveredResourceList"]
    """<p>Details of the resources that were discovered.</p>"""
    next_token: NotRequired["capo_fms.types.pagination_token.PaginationToken"]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Firewall Manager returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDiscoveredResourcesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_fms.types.discovered_resource_list

        out["Items"] = capo_fms.types.discovered_resource_list.serialize_aws_json_1_1(
            value["items"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDiscoveredResourcesResponse:
    out: ListDiscoveredResourcesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_fms.types.discovered_resource_list

        out["items"] = capo_fms.types.discovered_resource_list.deserialize_aws_json_1_1(
            data["Items"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListDiscoveredResourcesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_fms.types.discovered_resource_list

        out["Items"] = capo_fms.types.discovered_resource_list.serialize_cbor(
            value["items"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListDiscoveredResourcesResponse:
    out: ListDiscoveredResourcesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_fms.types.discovered_resource_list

        out["items"] = capo_fms.types.discovered_resource_list.deserialize_cbor(
            data["Items"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
