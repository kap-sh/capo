"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerOperatingSystem``."""

from typing import Literal, TypeAlias, cast

ContainerOperatingSystem: TypeAlias = Literal["AMAZON_LINUX_2023",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerOperatingSystem) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerOperatingSystem:
    return cast(ContainerOperatingSystem, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContainerOperatingSystem) -> str:
    return value


def deserialize_cbor(data: str) -> ContainerOperatingSystem:
    return cast(ContainerOperatingSystem, data)
