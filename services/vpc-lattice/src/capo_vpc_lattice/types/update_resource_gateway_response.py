"""Generated from Smithy shape ``com.amazonaws.vpclattice#UpdateResourceGatewayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.ip_address_type
    import capo_vpc_lattice.types.resource_config_dns_resolution
    import capo_vpc_lattice.types.resource_gateway_arn
    import capo_vpc_lattice.types.resource_gateway_id
    import capo_vpc_lattice.types.resource_gateway_name
    import capo_vpc_lattice.types.resource_gateway_status
    import capo_vpc_lattice.types.security_group_list
    import capo_vpc_lattice.types.subnet_list
    import capo_vpc_lattice.types.vpc_id


class UpdateResourceGatewayResponse(TypedDict, closed=True):
    name: NotRequired[
        "capo_vpc_lattice.types.resource_gateway_name.ResourceGatewayName"
    ]
    """<p>The name of the resource gateway.</p>"""
    id: NotRequired["capo_vpc_lattice.types.resource_gateway_id.ResourceGatewayId"]
    """<p>The ID of the resource gateway.</p>"""
    arn: NotRequired["capo_vpc_lattice.types.resource_gateway_arn.ResourceGatewayArn"]
    """<p>The Amazon Resource Name (ARN) of the resource gateway.</p>"""
    status: NotRequired[
        "capo_vpc_lattice.types.resource_gateway_status.ResourceGatewayStatus"
    ]
    """<p>The status of the resource gateway.</p>"""
    vpc_id: NotRequired["capo_vpc_lattice.types.vpc_id.VpcId"]
    """<p>The ID of the VPC for the resource gateway.</p>"""
    subnet_ids: NotRequired["capo_vpc_lattice.types.subnet_list.SubnetList"]
    """<p>The IDs of the VPC subnets for the resource gateway.</p>"""
    security_group_ids: NotRequired[
        "capo_vpc_lattice.types.security_group_list.SecurityGroupList"
    ]
    """<p>The IDs of the security groups associated with the resource gateway.</p>"""
    ip_address_type: NotRequired["capo_vpc_lattice.types.ip_address_type.IpAddressType"]
    """<p>The type of IP address used by the resource gateway.</p>"""
    resource_config_dns_resolution: NotRequired[
        "capo_vpc_lattice.types.resource_config_dns_resolution.ResourceConfigDnsResolution"
    ]
    """<p>The DNS resolution type for resource configurations that are associated with this resource gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResourceGatewayResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "subnet_ids" in value:
        import capo_vpc_lattice.types.subnet_list

        out["subnetIds"] = capo_vpc_lattice.types.subnet_list.serialize_json(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import capo_vpc_lattice.types.security_group_list

        out["securityGroupIds"] = (
            capo_vpc_lattice.types.security_group_list.serialize_json(
                value["security_group_ids"]
            )
        )
    if "ip_address_type" in value:
        out["ipAddressType"] = value["ip_address_type"]
    if "resource_config_dns_resolution" in value:
        out["resourceConfigDnsResolution"] = value["resource_config_dns_resolution"]
    return out


def deserialize_json(data: dict) -> UpdateResourceGatewayResponse:
    out: UpdateResourceGatewayResponse = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    if data.get("subnetIds") is not None:
        import capo_vpc_lattice.types.subnet_list

        out["subnet_ids"] = capo_vpc_lattice.types.subnet_list.deserialize_json(
            data["subnetIds"]
        )
    if data.get("securityGroupIds") is not None:
        import capo_vpc_lattice.types.security_group_list

        out["security_group_ids"] = (
            capo_vpc_lattice.types.security_group_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if data.get("ipAddressType") is not None:
        out["ip_address_type"] = data["ipAddressType"]
    if data.get("resourceConfigDnsResolution") is not None:
        out["resource_config_dns_resolution"] = data["resourceConfigDnsResolution"]
    return out
