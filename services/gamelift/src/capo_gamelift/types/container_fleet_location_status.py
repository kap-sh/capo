"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerFleetLocationStatus``."""

from typing import Literal, TypeAlias, cast

ContainerFleetLocationStatus: TypeAlias = Literal[
    "PENDING",
    "CREATING",
    "CREATED",
    "ACTIVATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "EXPIRED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerFleetLocationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerFleetLocationStatus:
    return cast(ContainerFleetLocationStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContainerFleetLocationStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ContainerFleetLocationStatus:
    return cast(ContainerFleetLocationStatus, data)
