"""Generated from Smithy shape ``com.amazonaws.directconnect#AllocateHostedConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_direct_connect.types.bandwidth
    import capo_direct_connect.types.connection_id
    import capo_direct_connect.types.connection_name
    import capo_direct_connect.types.owner_account
    import capo_direct_connect.types.tag_list
    import capo_direct_connect.types.vlan


class AllocateHostedConnectionRequest(TypedDict, closed=True):
    connection_id: "capo_direct_connect.types.connection_id.ConnectionId"
    """<p>The ID of the interconnect or LAG.</p>"""
    owner_account: "capo_direct_connect.types.owner_account.OwnerAccount"
    """<p>The ID of the Amazon Web Services account ID of the customer for the connection.</p>"""
    bandwidth: "capo_direct_connect.types.bandwidth.Bandwidth"
    """<p>The bandwidth of the connection. The possible values are 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, 500Mbps, 1Gbps, 2Gbps, 5Gbps, 10Gbps, and 25Gbps. Note that only those Direct Connect Partners who have met specific requirements are allowed to create a 1Gbps, 2Gbps, 5Gbps, 10Gbps, or 25Gbps hosted connection. </p>"""
    connection_name: "capo_direct_connect.types.connection_name.ConnectionName"
    """<p>The name of the hosted connection.</p>"""
    vlan: "capo_direct_connect.types.vlan.VLAN"
    """<p>The dedicated VLAN provisioned to the hosted connection.</p>"""
    tags: NotRequired["capo_direct_connect.types.tag_list.TagList"]
    """<p>The tags associated with the connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllocateHostedConnectionRequest) -> dict:
    out: dict = {}
    out["connectionId"] = value["connection_id"]
    out["ownerAccount"] = value["owner_account"]
    out["bandwidth"] = value["bandwidth"]
    out["connectionName"] = value["connection_name"]
    out["vlan"] = value["vlan"]
    if "tags" in value:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AllocateHostedConnectionRequest:
    out: AllocateHostedConnectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    else:
        raise DeserializationError(
            "AllocateHostedConnectionRequest.connection_id required"
        )
    if data.get("ownerAccount") is not None:
        out["owner_account"] = data["ownerAccount"]
    else:
        raise DeserializationError(
            "AllocateHostedConnectionRequest.owner_account required"
        )
    if data.get("bandwidth") is not None:
        out["bandwidth"] = data["bandwidth"]
    else:
        raise DeserializationError("AllocateHostedConnectionRequest.bandwidth required")
    if data.get("connectionName") is not None:
        out["connection_name"] = data["connectionName"]
    else:
        raise DeserializationError(
            "AllocateHostedConnectionRequest.connection_name required"
        )
    if data.get("vlan") is not None:
        out["vlan"] = data["vlan"]
    else:
        raise DeserializationError("AllocateHostedConnectionRequest.vlan required")
    if data.get("tags") is not None:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
