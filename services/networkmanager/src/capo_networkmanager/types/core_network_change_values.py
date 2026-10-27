"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkChangeValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.boolean
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.constrained_string_list
    import capo_networkmanager.types.core_network_policy_document
    import capo_networkmanager.types.external_region_code_list
    import capo_networkmanager.types.long
    import capo_networkmanager.types.routing_policy_association_details_list
    import capo_networkmanager.types.routing_policy_direction
    import capo_networkmanager.types.service_insertion_action_list


class CoreNetworkChangeValues(TypedDict, closed=True):
    segment_name: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The names of the segments in a core network.</p>"""
    network_function_group_name: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The network function group name if the change event is associated with a network function group.</p>"""
    edge_locations: NotRequired[
        "capo_networkmanager.types.external_region_code_list.ExternalRegionCodeList"
    ]
    """<p>The Regions where edges are located in a core network. </p>"""
    asn: NotRequired["capo_networkmanager.types.long.Long"]
    """<p>The ASN of a core network.</p>"""
    cidr: NotRequired["capo_networkmanager.types.constrained_string.ConstrainedString"]
    """<p>The IP addresses used for a core network.</p>"""
    destination_identifier: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The ID of the destination.</p>"""
    inside_cidr_blocks: NotRequired[
        "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>The inside IP addresses used for core network change values.</p>"""
    shared_segments: NotRequired[
        "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>The shared segments for a core network change value. </p>"""
    service_insertion_actions: NotRequired[
        "capo_networkmanager.types.service_insertion_action_list.ServiceInsertionActionList"
    ]
    """<p>Describes the service insertion action. </p>"""
    vpn_ecmp_support: "capo_networkmanager.types.boolean.Boolean"
    """<p>Indicates whether Equal Cost Multipath (ECMP) is enabled for the core network.</p>"""
    dns_support: "capo_networkmanager.types.boolean.Boolean"
    """<p>Indicates whether public DNS support is supported. The default is <code>true</code>. </p>"""
    security_group_referencing_support: "capo_networkmanager.types.boolean.Boolean"
    """<p>Indicates whether security group referencing is enabled for the core network.</p>"""
    routing_policy_direction: NotRequired[
        "capo_networkmanager.types.routing_policy_direction.RoutingPolicyDirection"
    ]
    """<p>The routing policy direction (inbound/outbound) in the core network change values.</p>"""
    routing_policy: NotRequired[
        "capo_networkmanager.types.core_network_policy_document.CoreNetworkPolicyDocument"
    ]
    """<p>The routing policy configuration in the core network change values.</p>"""
    peer_edge_locations: NotRequired[
        "capo_networkmanager.types.external_region_code_list.ExternalRegionCodeList"
    ]
    """<p>The edge locations of peers in the core network change values.</p>"""
    attachment_id: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The attachment identifier in the core network change values.</p>"""
    routing_policy_association_details: NotRequired[
        "capo_networkmanager.types.routing_policy_association_details_list.RoutingPolicyAssociationDetailsList"
    ]
    """<p>The names of the routing policies and other association details in the core network change values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkChangeValues) -> dict:
    out: dict = {}
    if "segment_name" in value:
        out["SegmentName"] = value["segment_name"]
    if "network_function_group_name" in value:
        out["NetworkFunctionGroupName"] = value["network_function_group_name"]
    if "edge_locations" in value:
        import capo_networkmanager.types.external_region_code_list

        out["EdgeLocations"] = (
            capo_networkmanager.types.external_region_code_list.serialize_json(
                value["edge_locations"]
            )
        )
    if "asn" in value:
        out["Asn"] = value["asn"]
    if "cidr" in value:
        out["Cidr"] = value["cidr"]
    if "destination_identifier" in value:
        out["DestinationIdentifier"] = value["destination_identifier"]
    if "inside_cidr_blocks" in value:
        import capo_networkmanager.types.constrained_string_list

        out["InsideCidrBlocks"] = (
            capo_networkmanager.types.constrained_string_list.serialize_json(
                value["inside_cidr_blocks"]
            )
        )
    if "shared_segments" in value:
        import capo_networkmanager.types.constrained_string_list

        out["SharedSegments"] = (
            capo_networkmanager.types.constrained_string_list.serialize_json(
                value["shared_segments"]
            )
        )
    if "service_insertion_actions" in value:
        import capo_networkmanager.types.service_insertion_action_list

        out["ServiceInsertionActions"] = (
            capo_networkmanager.types.service_insertion_action_list.serialize_json(
                value["service_insertion_actions"]
            )
        )
    out["VpnEcmpSupport"] = value.get("vpn_ecmp_support", False)
    out["DnsSupport"] = value.get("dns_support", False)
    out["SecurityGroupReferencingSupport"] = value.get(
        "security_group_referencing_support", False
    )
    if "routing_policy_direction" in value:
        import capo_networkmanager.types.routing_policy_direction

        out["RoutingPolicyDirection"] = (
            capo_networkmanager.types.routing_policy_direction.serialize_json(
                value["routing_policy_direction"]
            )
        )
    if "routing_policy" in value:
        out["RoutingPolicy"] = value["routing_policy"]
    if "peer_edge_locations" in value:
        import capo_networkmanager.types.external_region_code_list

        out["PeerEdgeLocations"] = (
            capo_networkmanager.types.external_region_code_list.serialize_json(
                value["peer_edge_locations"]
            )
        )
    if "attachment_id" in value:
        out["AttachmentId"] = value["attachment_id"]
    if "routing_policy_association_details" in value:
        import capo_networkmanager.types.routing_policy_association_details_list

        out["RoutingPolicyAssociationDetails"] = (
            capo_networkmanager.types.routing_policy_association_details_list.serialize_json(
                value["routing_policy_association_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> CoreNetworkChangeValues:
    out: CoreNetworkChangeValues = {}  # type: ignore[typeddict-item]
    if data.get("SegmentName") is not None:
        out["segment_name"] = data["SegmentName"]
    if data.get("NetworkFunctionGroupName") is not None:
        out["network_function_group_name"] = data["NetworkFunctionGroupName"]
    if data.get("EdgeLocations") is not None:
        import capo_networkmanager.types.external_region_code_list

        out["edge_locations"] = (
            capo_networkmanager.types.external_region_code_list.deserialize_json(
                data["EdgeLocations"]
            )
        )
    if data.get("Asn") is not None:
        out["asn"] = data["Asn"]
    if data.get("Cidr") is not None:
        out["cidr"] = data["Cidr"]
    if data.get("DestinationIdentifier") is not None:
        out["destination_identifier"] = data["DestinationIdentifier"]
    if data.get("InsideCidrBlocks") is not None:
        import capo_networkmanager.types.constrained_string_list

        out["inside_cidr_blocks"] = (
            capo_networkmanager.types.constrained_string_list.deserialize_json(
                data["InsideCidrBlocks"]
            )
        )
    if data.get("SharedSegments") is not None:
        import capo_networkmanager.types.constrained_string_list

        out["shared_segments"] = (
            capo_networkmanager.types.constrained_string_list.deserialize_json(
                data["SharedSegments"]
            )
        )
    if data.get("ServiceInsertionActions") is not None:
        import capo_networkmanager.types.service_insertion_action_list

        out["service_insertion_actions"] = (
            capo_networkmanager.types.service_insertion_action_list.deserialize_json(
                data["ServiceInsertionActions"]
            )
        )
    if data.get("VpnEcmpSupport") is not None:
        out["vpn_ecmp_support"] = data["VpnEcmpSupport"]
    else:
        out["vpn_ecmp_support"] = False
    if data.get("DnsSupport") is not None:
        out["dns_support"] = data["DnsSupport"]
    else:
        out["dns_support"] = False
    if data.get("SecurityGroupReferencingSupport") is not None:
        out["security_group_referencing_support"] = data[
            "SecurityGroupReferencingSupport"
        ]
    else:
        out["security_group_referencing_support"] = False
    if data.get("RoutingPolicyDirection") is not None:
        import capo_networkmanager.types.routing_policy_direction

        out["routing_policy_direction"] = (
            capo_networkmanager.types.routing_policy_direction.deserialize_json(
                data["RoutingPolicyDirection"]
            )
        )
    if data.get("RoutingPolicy") is not None:
        out["routing_policy"] = data["RoutingPolicy"]
    if data.get("PeerEdgeLocations") is not None:
        import capo_networkmanager.types.external_region_code_list

        out["peer_edge_locations"] = (
            capo_networkmanager.types.external_region_code_list.deserialize_json(
                data["PeerEdgeLocations"]
            )
        )
    if data.get("AttachmentId") is not None:
        out["attachment_id"] = data["AttachmentId"]
    if data.get("RoutingPolicyAssociationDetails") is not None:
        import capo_networkmanager.types.routing_policy_association_details_list

        out["routing_policy_association_details"] = (
            capo_networkmanager.types.routing_policy_association_details_list.deserialize_json(
                data["RoutingPolicyAssociationDetails"]
            )
        )
    return out
