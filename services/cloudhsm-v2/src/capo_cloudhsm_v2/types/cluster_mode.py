"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#ClusterMode``."""

from typing import Literal, TypeAlias, cast

ClusterMode: TypeAlias = Literal[
    "FIPS",
    "NON_FIPS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterMode:
    return cast(ClusterMode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ClusterMode) -> str:
    return value


def deserialize_cbor(data: str) -> ClusterMode:
    return cast(ClusterMode, data)
