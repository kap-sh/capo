"""Generated from Smithy shape ``com.amazonaws.directconnect#StartBgpFailoverTestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.bgp_peer_id_list
    import capo_direct_connect.types.test_duration
    import capo_direct_connect.types.virtual_interface_id


class StartBgpFailoverTestRequest(TypedDict, closed=True):
    virtual_interface_id: (
        "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
    )
    """<p>The ID of the virtual interface you want to test.</p>"""
    bgp_peers: NotRequired["capo_direct_connect.types.bgp_peer_id_list.BGPPeerIdList"]
    """<p>The BGP peers to place in the DOWN state.</p>"""
    test_duration_in_minutes: NotRequired[
        "capo_direct_connect.types.test_duration.TestDuration"
    ]
    """<p>The time in minutes that the virtual interface failover test will last.</p> <p>Maximum value: 4,320 minutes (72 hours).</p> <p>Default: 180 minutes (3 hours).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartBgpFailoverTestRequest) -> dict:
    out: dict = {}
    out["virtualInterfaceId"] = value["virtual_interface_id"]
    if "bgp_peers" in value:
        import capo_direct_connect.types.bgp_peer_id_list

        out["bgpPeers"] = (
            capo_direct_connect.types.bgp_peer_id_list.serialize_aws_json_1_1(
                value["bgp_peers"]
            )
        )
    if "test_duration_in_minutes" in value:
        out["testDurationInMinutes"] = value["test_duration_in_minutes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartBgpFailoverTestRequest:
    out: StartBgpFailoverTestRequest = {}  # type: ignore[typeddict-item]
    if data.get("virtualInterfaceId") is not None:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    else:
        out["virtual_interface_id"] = ""
    if data.get("bgpPeers") is not None:
        import capo_direct_connect.types.bgp_peer_id_list

        out["bgp_peers"] = (
            capo_direct_connect.types.bgp_peer_id_list.deserialize_aws_json_1_1(
                data["bgpPeers"]
            )
        )
    if data.get("testDurationInMinutes") is not None:
        out["test_duration_in_minutes"] = data["testDurationInMinutes"]
    return out
