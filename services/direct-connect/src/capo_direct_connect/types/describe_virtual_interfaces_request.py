"""Generated from Smithy shape ``com.amazonaws.directconnect#DescribeVirtualInterfacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.connection_id
    import capo_direct_connect.types.max_result_set_size
    import capo_direct_connect.types.pagination_token
    import capo_direct_connect.types.virtual_interface_id


class DescribeVirtualInterfacesRequest(TypedDict, closed=True):
    connection_id: NotRequired["capo_direct_connect.types.connection_id.ConnectionId"]
    """<p>The ID of the connection.</p>"""
    virtual_interface_id: NotRequired[
        "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
    ]
    """<p>The ID of the virtual interface.</p>"""
    max_results: NotRequired[
        "capo_direct_connect.types.max_result_set_size.MaxResultSetSize"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>"""
    next_token: NotRequired[
        "capo_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeVirtualInterfacesRequest) -> dict:
    out: dict = {}
    if "connection_id" in value:
        out["connectionId"] = value["connection_id"]
    if "virtual_interface_id" in value:
        out["virtualInterfaceId"] = value["virtual_interface_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeVirtualInterfacesRequest:
    out: DescribeVirtualInterfacesRequest = {}  # type: ignore[typeddict-item]
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    if data.get("virtualInterfaceId") is not None:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeVirtualInterfacesRequest) -> dict:
    out: dict = {}
    if "connection_id" in value:
        out["connectionId"] = value["connection_id"]
    if "virtual_interface_id" in value:
        out["virtualInterfaceId"] = value["virtual_interface_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeVirtualInterfacesRequest:
    out: DescribeVirtualInterfacesRequest = {}  # type: ignore[typeddict-item]
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    if data.get("virtualInterfaceId") is not None:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
