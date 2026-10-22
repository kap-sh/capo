"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayClusterAssociationStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of an association between a gateway and a cluster.</p>"""
GatewayClusterAssociationStatus: TypeAlias = Literal[
    "ACTIVE",
    "DISASSOCIATING",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayClusterAssociationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GatewayClusterAssociationStatus:
    return cast(GatewayClusterAssociationStatus, data)
