"""Generated from Smithy shape ``com.amazonaws.directconnect#ListVirtualInterfaceRoutesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.max_result_set_size
    import capo_direct_connect.types.pagination_token
    import capo_direct_connect.types.route_filters
    import capo_direct_connect.types.virtual_interface_id


class ListVirtualInterfaceRoutesRequest(TypedDict, closed=True):
    virtual_interface_id: NotRequired[
        "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
    ]
    """<p>The ID of the virtual interface.</p>"""
    filters: NotRequired["capo_direct_connect.types.route_filters.RouteFilters"]
    """<p>The filters to apply to the routes returned.</p>"""
    max_results: NotRequired[
        "capo_direct_connect.types.max_result_set_size.MaxResultSetSize"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>"""
    next_token: NotRequired[
        "capo_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListVirtualInterfaceRoutesRequest) -> dict:
    out: dict = {}
    if "virtual_interface_id" in value:
        out["virtualInterfaceId"] = value["virtual_interface_id"]
    if "filters" in value:
        import capo_direct_connect.types.route_filters

        out["filters"] = capo_direct_connect.types.route_filters.serialize_aws_json_1_1(
            value["filters"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListVirtualInterfaceRoutesRequest:
    out: ListVirtualInterfaceRoutesRequest = {}  # type: ignore[typeddict-item]
    if data.get("virtualInterfaceId") is not None:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    if data.get("filters") is not None:
        import capo_direct_connect.types.route_filters

        out["filters"] = (
            capo_direct_connect.types.route_filters.deserialize_aws_json_1_1(
                data["filters"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListVirtualInterfaceRoutesRequest) -> dict:
    out: dict = {}
    if "virtual_interface_id" in value:
        out["virtualInterfaceId"] = value["virtual_interface_id"]
    if "filters" in value:
        import capo_direct_connect.types.route_filters

        out["filters"] = capo_direct_connect.types.route_filters.serialize_cbor(
            value["filters"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListVirtualInterfaceRoutesRequest:
    out: ListVirtualInterfaceRoutesRequest = {}  # type: ignore[typeddict-item]
    if data.get("virtualInterfaceId") is not None:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    if data.get("filters") is not None:
        import capo_direct_connect.types.route_filters

        out["filters"] = capo_direct_connect.types.route_filters.deserialize_cbor(
            data["filters"]
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
