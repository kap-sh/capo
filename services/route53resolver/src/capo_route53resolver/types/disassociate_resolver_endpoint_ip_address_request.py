"""Generated from Smithy shape ``com.amazonaws.route53resolver#DisassociateResolverEndpointIpAddressRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53resolver.types.ip_address_update
    import capo_route53resolver.types.resource_id


class DisassociateResolverEndpointIpAddressRequest(TypedDict, closed=True):
    resolver_endpoint_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the Resolver endpoint that you want to disassociate an IP address from.</p>"""
    ip_address: "capo_route53resolver.types.ip_address_update.IpAddressUpdate"
    """<p>The IPv4 address that you want to remove from a Resolver endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateResolverEndpointIpAddressRequest) -> dict:
    out: dict = {}
    out["ResolverEndpointId"] = value["resolver_endpoint_id"]
    import capo_route53resolver.types.ip_address_update

    out["IpAddress"] = (
        capo_route53resolver.types.ip_address_update.serialize_aws_json_1_1(
            value["ip_address"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DisassociateResolverEndpointIpAddressRequest:
    out: DisassociateResolverEndpointIpAddressRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResolverEndpointId") is not None:
        out["resolver_endpoint_id"] = data["ResolverEndpointId"]
    else:
        out["resolver_endpoint_id"] = ""
    if data.get("IpAddress") is not None:
        import capo_route53resolver.types.ip_address_update

        out["ip_address"] = (
            capo_route53resolver.types.ip_address_update.deserialize_aws_json_1_1(
                data["IpAddress"]
            )
        )
    else:
        raise DeserializationError(
            "DisassociateResolverEndpointIpAddressRequest.ip_address required"
        )
    return out
