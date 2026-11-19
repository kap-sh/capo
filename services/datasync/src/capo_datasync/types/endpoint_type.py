"""Generated from Smithy shape ``com.amazonaws.datasync#EndpointType``."""

from typing import Literal, TypeAlias, cast

EndpointType: TypeAlias = Literal[
    "PUBLIC",
    "PRIVATE_LINK",
    "FIPS",
    "FIPS_PRIVATE_LINK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EndpointType:
    return cast(EndpointType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EndpointType) -> str:
    return value


def deserialize_cbor(data: str) -> EndpointType:
    return cast(EndpointType, data)
