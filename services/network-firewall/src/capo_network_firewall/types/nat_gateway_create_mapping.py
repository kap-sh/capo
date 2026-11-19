"""Generated from Smithy shape ``com.amazonaws.networkfirewall#NatGatewayCreateMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.collection_member_string
    import capo_network_firewall.types.nat_gateway_allocation_id_list
    import capo_network_firewall.types.nat_gateway_private_ip_list


class NatGatewayCreateMapping(TypedDict, closed=True):
    subnet_id: (
        "capo_network_firewall.types.collection_member_string.CollectionMember_String"
    )
    """<p>The ID of the subnet where Network Firewall creates the NAT gateway. The subnet must be in the firewall's VPC and can't be one of the firewall endpoint subnets. Each mapping must be in a different Availability Zone.</p>"""
    allocation_ids: NotRequired[
        "capo_network_firewall.types.nat_gateway_allocation_id_list.NatGatewayAllocationIdList"
    ]
    """<p>The allocation IDs of the Elastic IP addresses for a public NAT gateway, from 1 to 8. For each allocation ID, specify one address in <code>PrivateIps</code>. If you don't specify this, Network Firewall creates a private NAT gateway.</p>"""
    private_ips: NotRequired[
        "capo_network_firewall.types.nat_gateway_private_ip_list.NatGatewayPrivateIpList"
    ]
    """<p>The private IPv4 addresses of the NAT gateway. The addresses must be in the subnet that you specify and can't be the subnet's reserved addresses.</p> <p>For a public NAT gateway, you must specify exactly one address for each Elastic IP address in <code>AllocationIds</code>, even if you specify only one. For a private NAT gateway, specify from 1 to 8 addresses. The first address is the primary address.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NatGatewayCreateMapping) -> dict:
    out: dict = {}
    out["SubnetId"] = value["subnet_id"]
    if "allocation_ids" in value:
        import capo_network_firewall.types.nat_gateway_allocation_id_list

        out["AllocationIds"] = (
            capo_network_firewall.types.nat_gateway_allocation_id_list.serialize_aws_json_1_0(
                value["allocation_ids"]
            )
        )
    if "private_ips" in value:
        import capo_network_firewall.types.nat_gateway_private_ip_list

        out["PrivateIps"] = (
            capo_network_firewall.types.nat_gateway_private_ip_list.serialize_aws_json_1_0(
                value["private_ips"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> NatGatewayCreateMapping:
    out: NatGatewayCreateMapping = {}  # type: ignore[typeddict-item]
    if data.get("SubnetId") is not None:
        out["subnet_id"] = data["SubnetId"]
    else:
        out["subnet_id"] = ""
    if data.get("AllocationIds") is not None:
        import capo_network_firewall.types.nat_gateway_allocation_id_list

        out["allocation_ids"] = (
            capo_network_firewall.types.nat_gateway_allocation_id_list.deserialize_aws_json_1_0(
                data["AllocationIds"]
            )
        )
    if data.get("PrivateIps") is not None:
        import capo_network_firewall.types.nat_gateway_private_ip_list

        out["private_ips"] = (
            capo_network_firewall.types.nat_gateway_private_ip_list.deserialize_aws_json_1_0(
                data["PrivateIps"]
            )
        )
    return out
