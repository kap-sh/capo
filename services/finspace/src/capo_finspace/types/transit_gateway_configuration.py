"""Generated from Smithy shape ``com.amazonaws.finspace#TransitGatewayConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_finspace.errors import DeserializationError

if TYPE_CHECKING:
    import capo_finspace.types.network_acl_configuration
    import capo_finspace.types.transit_gateway_id
    import capo_finspace.types.valid_cidr_space


class TransitGatewayConfiguration(TypedDict, closed=True):
    transit_gateway_id: "capo_finspace.types.transit_gateway_id.TransitGatewayID"
    """<p>The identifier of the transit gateway created by the customer to connect outbound traffics from kdb network to your internal network.</p>"""
    routable_cidr_space: "capo_finspace.types.valid_cidr_space.ValidCIDRSpace"
    """<p>The routing CIDR on behalf of kdb environment. It could be any "/26 range in the 100.64.0.0 CIDR space. After providing, it will be added to the customer's transit gateway routing table so that the traffics could be routed to kdb network.</p>"""
    attachment_network_acl_configuration: NotRequired[
        "capo_finspace.types.network_acl_configuration.NetworkACLConfiguration"
    ]
    """<p> The rules that define how you manage the outbound traffic from kdb network to your internal network. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransitGatewayConfiguration) -> dict:
    out: dict = {}
    out["transitGatewayID"] = value["transit_gateway_id"]
    out["routableCIDRSpace"] = value["routable_cidr_space"]
    if "attachment_network_acl_configuration" in value:
        import capo_finspace.types.network_acl_configuration

        out["attachmentNetworkAclConfiguration"] = (
            capo_finspace.types.network_acl_configuration.serialize_json(
                value["attachment_network_acl_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> TransitGatewayConfiguration:
    out: TransitGatewayConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("transitGatewayID") is not None:
        out["transit_gateway_id"] = data["transitGatewayID"]
    else:
        raise DeserializationError(
            "TransitGatewayConfiguration.transit_gateway_id required"
        )
    if data.get("routableCIDRSpace") is not None:
        out["routable_cidr_space"] = data["routableCIDRSpace"]
    else:
        raise DeserializationError(
            "TransitGatewayConfiguration.routable_cidr_space required"
        )
    if data.get("attachmentNetworkAclConfiguration") is not None:
        import capo_finspace.types.network_acl_configuration

        out["attachment_network_acl_configuration"] = (
            capo_finspace.types.network_acl_configuration.deserialize_json(
                data["attachmentNetworkAclConfiguration"]
            )
        )
    return out
