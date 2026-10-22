"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayConnectorHealthCheckProtocol``."""

from typing import Literal, TypeAlias, cast

"""<p>The protocol that a gateway uses to perform health checks on connector targets.</p>"""
GatewayConnectorHealthCheckProtocol: TypeAlias = Literal[
    "HTTP",
    "HTTPS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayConnectorHealthCheckProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GatewayConnectorHealthCheckProtocol:
    return cast(GatewayConnectorHealthCheckProtocol, data)
