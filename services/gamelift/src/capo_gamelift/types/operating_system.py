"""Generated from Smithy shape ``com.amazonaws.gamelift#OperatingSystem``."""

from typing import Literal, TypeAlias, cast

OperatingSystem: TypeAlias = Literal[
    "WINDOWS_2012",
    "AMAZON_LINUX",
    "AMAZON_LINUX_2",
    "WINDOWS_2016",
    "AMAZON_LINUX_2023",
    "WINDOWS_2022",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperatingSystem) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OperatingSystem:
    return cast(OperatingSystem, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OperatingSystem) -> str:
    return value


def deserialize_cbor(data: str) -> OperatingSystem:
    return cast(OperatingSystem, data)
