"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayAlbDesyncMitigationMode``."""

from typing import Literal, TypeAlias, cast

"""<p>The desync mitigation mode for a gateway's load balancers, which determines how the load balancers handle requests that might pose a security risk.</p>"""
GatewayAlbDesyncMitigationMode: TypeAlias = Literal[
    "monitor",
    "defensive",
    "strictest",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayAlbDesyncMitigationMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GatewayAlbDesyncMitigationMode:
    return cast(GatewayAlbDesyncMitigationMode, data)
