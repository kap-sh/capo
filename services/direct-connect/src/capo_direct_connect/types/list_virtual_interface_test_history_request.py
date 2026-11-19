"""Generated from Smithy shape ``com.amazonaws.directconnect#ListVirtualInterfaceTestHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.bgp_peer_id_list
    import capo_direct_connect.types.failure_test_history_status
    import capo_direct_connect.types.max_result_set_size
    import capo_direct_connect.types.pagination_token
    import capo_direct_connect.types.test_id
    import capo_direct_connect.types.virtual_interface_id


class ListVirtualInterfaceTestHistoryRequest(TypedDict, closed=True):
    test_id: NotRequired["capo_direct_connect.types.test_id.TestId"]
    """<p>The ID of the virtual interface failover test.</p>"""
    virtual_interface_id: NotRequired[
        "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
    ]
    """<p>The ID of the virtual interface that was tested.</p>"""
    bgp_peers: NotRequired["capo_direct_connect.types.bgp_peer_id_list.BGPPeerIdList"]
    """<p>The BGP peers that were placed in the DOWN state during the virtual interface failover test.</p>"""
    status: NotRequired[
        "capo_direct_connect.types.failure_test_history_status.FailureTestHistoryStatus"
    ]
    """<p>The status of the virtual interface failover test.</p>"""
    max_results: NotRequired[
        "capo_direct_connect.types.max_result_set_size.MaxResultSetSize"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>"""
    next_token: NotRequired[
        "capo_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListVirtualInterfaceTestHistoryRequest) -> dict:
    out: dict = {}
    if "test_id" in value:
        out["testId"] = value["test_id"]
    if "virtual_interface_id" in value:
        out["virtualInterfaceId"] = value["virtual_interface_id"]
    if "bgp_peers" in value:
        import capo_direct_connect.types.bgp_peer_id_list

        out["bgpPeers"] = (
            capo_direct_connect.types.bgp_peer_id_list.serialize_aws_json_1_1(
                value["bgp_peers"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListVirtualInterfaceTestHistoryRequest:
    out: ListVirtualInterfaceTestHistoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("testId") is not None:
        out["test_id"] = data["testId"]
    if data.get("virtualInterfaceId") is not None:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    if data.get("bgpPeers") is not None:
        import capo_direct_connect.types.bgp_peer_id_list

        out["bgp_peers"] = (
            capo_direct_connect.types.bgp_peer_id_list.deserialize_aws_json_1_1(
                data["bgpPeers"]
            )
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListVirtualInterfaceTestHistoryRequest) -> dict:
    out: dict = {}
    if "test_id" in value:
        out["testId"] = value["test_id"]
    if "virtual_interface_id" in value:
        out["virtualInterfaceId"] = value["virtual_interface_id"]
    if "bgp_peers" in value:
        import capo_direct_connect.types.bgp_peer_id_list

        out["bgpPeers"] = capo_direct_connect.types.bgp_peer_id_list.serialize_cbor(
            value["bgp_peers"]
        )
    if "status" in value:
        out["status"] = value["status"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListVirtualInterfaceTestHistoryRequest:
    out: ListVirtualInterfaceTestHistoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("testId") is not None:
        out["test_id"] = data["testId"]
    if data.get("virtualInterfaceId") is not None:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    if data.get("bgpPeers") is not None:
        import capo_direct_connect.types.bgp_peer_id_list

        out["bgp_peers"] = capo_direct_connect.types.bgp_peer_id_list.deserialize_cbor(
            data["bgpPeers"]
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
