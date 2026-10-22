"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayElbScheme``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies whether the load balancers that a gateway manages are internet-facing or internal.</p>"""
GatewayElbScheme: TypeAlias = Literal[
    "internet-facing",
    "internal",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayElbScheme) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GatewayElbScheme:
    return cast(GatewayElbScheme, data)
