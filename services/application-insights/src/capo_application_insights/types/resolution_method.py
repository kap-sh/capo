"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ResolutionMethod``."""

from typing import Literal, TypeAlias, cast

ResolutionMethod: TypeAlias = Literal[
    "MANUAL",
    "AUTOMATIC",
    "UNRESOLVED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolutionMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResolutionMethod:
    return cast(ResolutionMethod, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResolutionMethod) -> str:
    return value


def deserialize_cbor(data: str) -> ResolutionMethod:
    return cast(ResolutionMethod, data)
