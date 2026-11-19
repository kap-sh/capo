"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerGroupType``."""

from typing import Literal, TypeAlias, cast

ContainerGroupType: TypeAlias = Literal[
    "GAME_SERVER",
    "PER_INSTANCE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerGroupType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerGroupType:
    return cast(ContainerGroupType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContainerGroupType) -> str:
    return value


def deserialize_cbor(data: str) -> ContainerGroupType:
    return cast(ContainerGroupType, data)
