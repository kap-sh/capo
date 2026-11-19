"""Generated from Smithy shape ``com.amazonaws.directconnect#ResiliencyModel``."""

from typing import Literal, TypeAlias, cast

ResiliencyModel: TypeAlias = Literal[
    "maximum-resiliency",
    "high-resiliency",
    "basic-resiliency",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResiliencyModel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResiliencyModel:
    return cast(ResiliencyModel, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResiliencyModel) -> str:
    return value


def deserialize_cbor(data: str) -> ResiliencyModel:
    return cast(ResiliencyModel, data)
