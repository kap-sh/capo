"""Generated from Smithy shape ``com.amazonaws.vpclattice#UpdateResourceGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.resource_config_dns_resolution
    import capo_vpc_lattice.types.resource_gateway_identifier
    import capo_vpc_lattice.types.security_group_list


class UpdateResourceGatewayRequest(TypedDict, closed=True):
    resource_gateway_identifier: (
        "capo_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier"
    )
    """<p>The ID or ARN of the resource gateway.</p>"""
    security_group_ids: NotRequired[
        "capo_vpc_lattice.types.security_group_list.SecurityGroupList"
    ]
    """<p>The IDs of the security groups associated with the resource gateway.</p>"""
    resource_config_dns_resolution: NotRequired[
        "capo_vpc_lattice.types.resource_config_dns_resolution.ResourceConfigDnsResolution"
    ]
    """<p>Indicates how DNS is resolved for resource configurations associated with this resource gateway.</p> <ul> <li> <p> <code>IN_VPC</code> - DNS resolution occurs privately within the resource gateway's VPC. Use this when your resource domain names are hosted in private Route 53 hosted zones or on-premises DNS servers reachable from the VPC.</p> </li> <li> <p> <code>PUBLIC</code> - DNS resolution occurs against public DNS resolvers. Use this when your resource domain names are publicly resolvable.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResourceGatewayRequest) -> dict:
    out: dict = {}
    if "security_group_ids" in value:
        import capo_vpc_lattice.types.security_group_list

        out["securityGroupIds"] = (
            capo_vpc_lattice.types.security_group_list.serialize_json(
                value["security_group_ids"]
            )
        )
    if "resource_config_dns_resolution" in value:
        out["resourceConfigDnsResolution"] = value["resource_config_dns_resolution"]
    return out


def deserialize_json(data: dict) -> UpdateResourceGatewayRequest:
    out: UpdateResourceGatewayRequest = {}  # type: ignore[typeddict-item]
    if data.get("securityGroupIds") is not None:
        import capo_vpc_lattice.types.security_group_list

        out["security_group_ids"] = (
            capo_vpc_lattice.types.security_group_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if data.get("resourceConfigDnsResolution") is not None:
        out["resource_config_dns_resolution"] = data["resourceConfigDnsResolution"]
    return out
