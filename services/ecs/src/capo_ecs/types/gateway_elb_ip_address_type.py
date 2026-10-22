"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayElbIpAddressType``."""

from typing import Literal, TypeAlias, cast

"""<p>The IP address type for the load balancers that a gateway manages.</p>"""
GatewayElbIpAddressType: TypeAlias = Literal[
    "ipv4",
    "dualstack",
    "dualstack-without-public-ipv4",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayElbIpAddressType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GatewayElbIpAddressType:
    return cast(GatewayElbIpAddressType, data)
