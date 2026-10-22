"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayAlbProtocol``."""

from typing import Literal, TypeAlias, cast

"""<p>The protocol for a gateway's load balancer listener.</p>"""
GatewayAlbProtocol: TypeAlias = Literal[
    "HTTP",
    "HTTPS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayAlbProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GatewayAlbProtocol:
    return cast(GatewayAlbProtocol, data)
