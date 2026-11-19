"""Generated from Smithy shape ``com.amazonaws.fms#DependentServiceName``."""

from typing import Literal, TypeAlias, cast

DependentServiceName: TypeAlias = Literal[
    "AWSCONFIG",
    "AWSWAF",
    "AWSSHIELD_ADVANCED",
    "AWSVPC",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DependentServiceName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DependentServiceName:
    return cast(DependentServiceName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DependentServiceName) -> str:
    return value


def deserialize_cbor(data: str) -> DependentServiceName:
    return cast(DependentServiceName, data)
