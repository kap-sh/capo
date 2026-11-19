"""Generated from Smithy shape ``com.amazonaws.comprehend#EndpointStatus``."""

from typing import Literal, TypeAlias, cast

EndpointStatus: TypeAlias = Literal[
    "CREATING",
    "DELETING",
    "FAILED",
    "IN_SERVICE",
    "UPDATING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EndpointStatus:
    return cast(EndpointStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EndpointStatus) -> str:
    return value


def deserialize_cbor(data: str) -> EndpointStatus:
    return cast(EndpointStatus, data)
