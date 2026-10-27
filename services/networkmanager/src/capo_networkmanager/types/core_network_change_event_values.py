"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkChangeEventValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment_id
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.external_region_code
    import capo_networkmanager.types.routing_policy_association_details_list
    import capo_networkmanager.types.routing_policy_direction


class CoreNetworkChangeEventValues(TypedDict, closed=True):
    edge_location: NotRequired[
        "capo_networkmanager.types.external_region_code.ExternalRegionCode"
    ]
    """<p>The edge location for the core network change event.</p>"""
    peer_edge_location: NotRequired[
        "capo_networkmanager.types.external_region_code.ExternalRegionCode"
    ]
    """<p>The edge location of the peer in a core network change event.</p>"""
    routing_policy_direction: NotRequired[
        "capo_networkmanager.types.routing_policy_direction.RoutingPolicyDirection"
    ]
    """<p>The routing policy direction (inbound/outbound) in a core network change event.</p>"""
    segment_name: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The segment name if the change event is associated with a segment.</p>"""
    network_function_group_name: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The changed network function group name.</p>"""
    attachment_id: NotRequired["capo_networkmanager.types.attachment_id.AttachmentId"]
    """<p>The ID of the attachment if the change event is associated with an attachment. </p>"""
    cidr: NotRequired["capo_networkmanager.types.constrained_string.ConstrainedString"]
    """<p>For a <code>STATIC_ROUTE</code> event, this is the IP address.</p>"""
    routing_policy_association_details: NotRequired[
        "capo_networkmanager.types.routing_policy_association_details_list.RoutingPolicyAssociationDetailsList"
    ]
    """<p>The names of the routing policies and other association details in a core network change event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkChangeEventValues) -> dict:
    out: dict = {}
    if "edge_location" in value:
        out["EdgeLocation"] = value["edge_location"]
    if "peer_edge_location" in value:
        out["PeerEdgeLocation"] = value["peer_edge_location"]
    if "routing_policy_direction" in value:
        import capo_networkmanager.types.routing_policy_direction

        out["RoutingPolicyDirection"] = (
            capo_networkmanager.types.routing_policy_direction.serialize_json(
                value["routing_policy_direction"]
            )
        )
    if "segment_name" in value:
        out["SegmentName"] = value["segment_name"]
    if "network_function_group_name" in value:
        out["NetworkFunctionGroupName"] = value["network_function_group_name"]
    if "attachment_id" in value:
        out["AttachmentId"] = value["attachment_id"]
    if "cidr" in value:
        out["Cidr"] = value["cidr"]
    if "routing_policy_association_details" in value:
        import capo_networkmanager.types.routing_policy_association_details_list

        out["RoutingPolicyAssociationDetails"] = (
            capo_networkmanager.types.routing_policy_association_details_list.serialize_json(
                value["routing_policy_association_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> CoreNetworkChangeEventValues:
    out: CoreNetworkChangeEventValues = {}  # type: ignore[typeddict-item]
    if data.get("EdgeLocation") is not None:
        out["edge_location"] = data["EdgeLocation"]
    if data.get("PeerEdgeLocation") is not None:
        out["peer_edge_location"] = data["PeerEdgeLocation"]
    if data.get("RoutingPolicyDirection") is not None:
        import capo_networkmanager.types.routing_policy_direction

        out["routing_policy_direction"] = (
            capo_networkmanager.types.routing_policy_direction.deserialize_json(
                data["RoutingPolicyDirection"]
            )
        )
    if data.get("SegmentName") is not None:
        out["segment_name"] = data["SegmentName"]
    if data.get("NetworkFunctionGroupName") is not None:
        out["network_function_group_name"] = data["NetworkFunctionGroupName"]
    if data.get("AttachmentId") is not None:
        out["attachment_id"] = data["AttachmentId"]
    if data.get("Cidr") is not None:
        out["cidr"] = data["Cidr"]
    if data.get("RoutingPolicyAssociationDetails") is not None:
        import capo_networkmanager.types.routing_policy_association_details_list

        out["routing_policy_association_details"] = (
            capo_networkmanager.types.routing_policy_association_details_list.deserialize_json(
                data["RoutingPolicyAssociationDetails"]
            )
        )
    return out
