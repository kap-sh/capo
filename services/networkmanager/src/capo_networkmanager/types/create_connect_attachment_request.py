"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateConnectAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment_id
    import capo_networkmanager.types.client_token
    import capo_networkmanager.types.connect_attachment_options
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.external_region_code
    import capo_networkmanager.types.tag_list


class CreateConnectAttachmentRequest(TypedDict, closed=True):
    core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of a core network where you want to create the attachment. </p>"""
    edge_location: "capo_networkmanager.types.external_region_code.ExternalRegionCode"
    """<p>The Region where the edge is located.</p>"""
    transport_attachment_id: "capo_networkmanager.types.attachment_id.AttachmentId"
    """<p>The ID of the attachment between the two connections.</p>"""
    routing_policy_label: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The routing policy label to apply to the Connect attachment for traffic routing decisions.</p>"""
    options: (
        "capo_networkmanager.types.connect_attachment_options.ConnectAttachmentOptions"
    )
    """<p>Options for creating an attachment.</p>"""
    tags: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>The list of key-value tags associated with the request.</p>"""
    client_token: NotRequired["capo_networkmanager.types.client_token.ClientToken"]
    """<p>The client token associated with the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectAttachmentRequest) -> dict:
    out: dict = {}
    out["CoreNetworkId"] = value["core_network_id"]
    out["EdgeLocation"] = value["edge_location"]
    out["TransportAttachmentId"] = value["transport_attachment_id"]
    if "routing_policy_label" in value:
        out["RoutingPolicyLabel"] = value["routing_policy_label"]
    import capo_networkmanager.types.connect_attachment_options

    out["Options"] = (
        capo_networkmanager.types.connect_attachment_options.serialize_json(
            value["options"]
        )
    )
    if "tags" in value:
        import capo_networkmanager.types.tag_list

        out["Tags"] = capo_networkmanager.types.tag_list.serialize_json(value["tags"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateConnectAttachmentRequest:
    out: CreateConnectAttachmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("CoreNetworkId") is not None:
        out["core_network_id"] = data["CoreNetworkId"]
    else:
        out["core_network_id"] = ""
    if data.get("EdgeLocation") is not None:
        out["edge_location"] = data["EdgeLocation"]
    else:
        out["edge_location"] = ""
    if data.get("TransportAttachmentId") is not None:
        out["transport_attachment_id"] = data["TransportAttachmentId"]
    else:
        out["transport_attachment_id"] = ""
    if data.get("RoutingPolicyLabel") is not None:
        out["routing_policy_label"] = data["RoutingPolicyLabel"]
    if data.get("Options") is not None:
        import capo_networkmanager.types.connect_attachment_options

        out["options"] = (
            capo_networkmanager.types.connect_attachment_options.deserialize_json(
                data["Options"]
            )
        )
    else:
        raise DeserializationError("CreateConnectAttachmentRequest.options required")
    if data.get("Tags") is not None:
        import capo_networkmanager.types.tag_list

        out["tags"] = capo_networkmanager.types.tag_list.deserialize_json(data["Tags"])
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
