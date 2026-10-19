"""Generated from Smithy shape ``com.amazonaws.directconnect#AllocateConnectionOnInterconnectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_direct_connect.types.bandwidth
    import capo_direct_connect.types.connection_name
    import capo_direct_connect.types.interconnect_id
    import capo_direct_connect.types.owner_account
    import capo_direct_connect.types.vlan


class AllocateConnectionOnInterconnectRequest(TypedDict, closed=True):
    bandwidth: "capo_direct_connect.types.bandwidth.Bandwidth"
    """<p>The bandwidth of the connection. The possible values are 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, 500Mbps, 1Gbps, 2Gbps, 5Gbps, and 10Gbps. Note that only those Direct Connect Partners who have met specific requirements are allowed to create a 1Gbps, 2Gbps, 5Gbps or 10Gbps hosted connection.</p>"""
    connection_name: "capo_direct_connect.types.connection_name.ConnectionName"
    """<p>The name of the provisioned connection.</p>"""
    owner_account: "capo_direct_connect.types.owner_account.OwnerAccount"
    """<p>The ID of the Amazon Web Services account of the customer for whom the connection will be provisioned.</p>"""
    interconnect_id: "capo_direct_connect.types.interconnect_id.InterconnectId"
    """<p>The ID of the interconnect on which the connection will be provisioned.</p>"""
    vlan: "capo_direct_connect.types.vlan.VLAN"
    """<p>The dedicated VLAN provisioned to the connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllocateConnectionOnInterconnectRequest) -> dict:
    out: dict = {}
    out["bandwidth"] = value["bandwidth"]
    out["connectionName"] = value["connection_name"]
    out["ownerAccount"] = value["owner_account"]
    out["interconnectId"] = value["interconnect_id"]
    out["vlan"] = value["vlan"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AllocateConnectionOnInterconnectRequest:
    out: AllocateConnectionOnInterconnectRequest = {}  # type: ignore[typeddict-item]
    if data.get("bandwidth") is not None:
        out["bandwidth"] = data["bandwidth"]
    else:
        raise DeserializationError(
            "AllocateConnectionOnInterconnectRequest.bandwidth required"
        )
    if data.get("connectionName") is not None:
        out["connection_name"] = data["connectionName"]
    else:
        raise DeserializationError(
            "AllocateConnectionOnInterconnectRequest.connection_name required"
        )
    if data.get("ownerAccount") is not None:
        out["owner_account"] = data["ownerAccount"]
    else:
        raise DeserializationError(
            "AllocateConnectionOnInterconnectRequest.owner_account required"
        )
    if data.get("interconnectId") is not None:
        out["interconnect_id"] = data["interconnectId"]
    else:
        raise DeserializationError(
            "AllocateConnectionOnInterconnectRequest.interconnect_id required"
        )
    if data.get("vlan") is not None:
        out["vlan"] = data["vlan"]
    else:
        raise DeserializationError(
            "AllocateConnectionOnInterconnectRequest.vlan required"
        )
    return out
