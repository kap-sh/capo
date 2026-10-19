"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateConnectPeerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment_id
    import capo_networkmanager.types.bgp_options
    import capo_networkmanager.types.client_token
    import capo_networkmanager.types.constrained_string_list
    import capo_networkmanager.types.ip_address
    import capo_networkmanager.types.subnet_arn
    import capo_networkmanager.types.tag_list


class CreateConnectPeerRequest(TypedDict, closed=True):
    connect_attachment_id: "capo_networkmanager.types.attachment_id.AttachmentId"
    """<p>The ID of the connection attachment.</p>"""
    core_network_address: NotRequired["capo_networkmanager.types.ip_address.IPAddress"]
    """<p>A Connect peer core network address. This only applies only when the protocol is <code>GRE</code>.</p>"""
    peer_address: "capo_networkmanager.types.ip_address.IPAddress"
    """<p>The Connect peer address.</p>"""
    bgp_options: NotRequired["capo_networkmanager.types.bgp_options.BgpOptions"]
    """<p>The Connect peer BGP options. This only applies only when the protocol is <code>GRE</code>.</p>"""
    inside_cidr_blocks: NotRequired[
        "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>The inside IP addresses used for BGP peering.</p>"""
    tags: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>The tags associated with the peer request.</p>"""
    client_token: NotRequired["capo_networkmanager.types.client_token.ClientToken"]
    """<p>The client token associated with the request.</p>"""
    subnet_arn: NotRequired["capo_networkmanager.types.subnet_arn.SubnetArn"]
    """<p>The subnet ARN for the Connect peer. This only applies only when the protocol is NO_ENCAP.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectPeerRequest) -> dict:
    out: dict = {}
    out["ConnectAttachmentId"] = value["connect_attachment_id"]
    if "core_network_address" in value:
        out["CoreNetworkAddress"] = value["core_network_address"]
    out["PeerAddress"] = value["peer_address"]
    if "bgp_options" in value:
        import capo_networkmanager.types.bgp_options

        out["BgpOptions"] = capo_networkmanager.types.bgp_options.serialize_json(
            value["bgp_options"]
        )
    if "inside_cidr_blocks" in value:
        import capo_networkmanager.types.constrained_string_list

        out["InsideCidrBlocks"] = (
            capo_networkmanager.types.constrained_string_list.serialize_json(
                value["inside_cidr_blocks"]
            )
        )
    if "tags" in value:
        import capo_networkmanager.types.tag_list

        out["Tags"] = capo_networkmanager.types.tag_list.serialize_json(value["tags"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "subnet_arn" in value:
        out["SubnetArn"] = value["subnet_arn"]
    return out


def deserialize_json(data: dict) -> CreateConnectPeerRequest:
    out: CreateConnectPeerRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConnectAttachmentId") is not None:
        out["connect_attachment_id"] = data["ConnectAttachmentId"]
    else:
        out["connect_attachment_id"] = ""
    if data.get("CoreNetworkAddress") is not None:
        out["core_network_address"] = data["CoreNetworkAddress"]
    if data.get("PeerAddress") is not None:
        out["peer_address"] = data["PeerAddress"]
    else:
        out["peer_address"] = ""
    if data.get("BgpOptions") is not None:
        import capo_networkmanager.types.bgp_options

        out["bgp_options"] = capo_networkmanager.types.bgp_options.deserialize_json(
            data["BgpOptions"]
        )
    if data.get("InsideCidrBlocks") is not None:
        import capo_networkmanager.types.constrained_string_list

        out["inside_cidr_blocks"] = (
            capo_networkmanager.types.constrained_string_list.deserialize_json(
                data["InsideCidrBlocks"]
            )
        )
    if data.get("Tags") is not None:
        import capo_networkmanager.types.tag_list

        out["tags"] = capo_networkmanager.types.tag_list.deserialize_json(data["Tags"])
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("SubnetArn") is not None:
        out["subnet_arn"] = data["SubnetArn"]
    return out
