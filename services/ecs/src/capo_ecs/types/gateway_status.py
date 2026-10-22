"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a gateway.</p>"""
GatewayStatus: TypeAlias = Literal[
    "ACTIVE",
    "UPDATE_IN_PROGRESS",
    "UPDATE_COMPLETE",
    "UPDATE_FAILED",
    "DELETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GatewayStatus:
    return cast(GatewayStatus, data)
