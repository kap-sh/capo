"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayElbNetworkConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.gateway_elb_ip_address_type
    import capo_ecs.types.string
    import capo_ecs.types.string_list


class GatewayElbNetworkConfiguration(TypedDict, closed=True):
    inbound_security_group: NotRequired["capo_ecs.types.string.String"]
    """<p>The ID of a security group that you provide to control inbound traffic to the load balancers that the gateway manages. When you specify a security group, the gateway doesn't create inbound rules on the security group it manages.</p>"""
    subnets: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The subnets for the load balancers that the gateway manages. The default is the subnets in the default VPC.</p>"""
    ip_address_type: NotRequired[
        "capo_ecs.types.gateway_elb_ip_address_type.GatewayElbIpAddressType"
    ]
    """<p>The IP address type for the load balancers that the gateway manages. The default is <code>dualstack</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayElbNetworkConfiguration) -> dict:
    out: dict = {}
    if "inbound_security_group" in value:
        out["inboundSecurityGroup"] = value["inbound_security_group"]
    if "subnets" in value:
        import capo_ecs.types.string_list

        out["subnets"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["subnets"]
        )
    if "ip_address_type" in value:
        import capo_ecs.types.gateway_elb_ip_address_type

        out["ipAddressType"] = (
            capo_ecs.types.gateway_elb_ip_address_type.serialize_aws_json_1_1(
                value["ip_address_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GatewayElbNetworkConfiguration:
    out: GatewayElbNetworkConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("inboundSecurityGroup") is not None:
        out["inbound_security_group"] = data["inboundSecurityGroup"]
    if data.get("subnets") is not None:
        import capo_ecs.types.string_list

        out["subnets"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["subnets"]
        )
    if data.get("ipAddressType") is not None:
        import capo_ecs.types.gateway_elb_ip_address_type

        out["ip_address_type"] = (
            capo_ecs.types.gateway_elb_ip_address_type.deserialize_aws_json_1_1(
                data["ipAddressType"]
            )
        )
    return out
