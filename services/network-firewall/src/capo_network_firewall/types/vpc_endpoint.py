"""Generated from Smithy shape ``com.amazonaws.networkfirewall#VpcEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.subnet_mappings
    import capo_network_firewall.types.vpc_id


class VpcEndpoint(TypedDict, closed=True):
    vpc_id: "capo_network_firewall.types.vpc_id.VpcId"
    """<p>The unique identifier of the VPC where Network Firewall creates the proxy mode firewall endpoint. </p>"""
    subnet_mappings: "capo_network_firewall.types.subnet_mappings.SubnetMappings"
    """<p>The subnets in which Network Firewall creates the firewall endpoint for a proxy mode firewall. Each subnet must belong to a different Availability Zone in the VPC. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcEndpoint) -> dict:
    out: dict = {}
    out["VpcId"] = value["vpc_id"]
    import capo_network_firewall.types.subnet_mappings

    out["SubnetMappings"] = (
        capo_network_firewall.types.subnet_mappings.serialize_aws_json_1_0(
            value["subnet_mappings"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> VpcEndpoint:
    out: VpcEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    else:
        out["vpc_id"] = ""
    if data.get("SubnetMappings") is not None:
        import capo_network_firewall.types.subnet_mappings

        out["subnet_mappings"] = (
            capo_network_firewall.types.subnet_mappings.deserialize_aws_json_1_0(
                data["SubnetMappings"]
            )
        )
    else:
        out["subnet_mappings"] = []
    return out
