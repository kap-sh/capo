"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayRouteStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a gateway route.</p>"""
GatewayRouteStatus: TypeAlias = Literal[
    "ACTIVE",
    "CREATE_IN_PROGRESS",
    "CREATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayRouteStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GatewayRouteStatus:
    return cast(GatewayRouteStatus, data)
