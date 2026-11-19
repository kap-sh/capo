"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#PreferredResourceName``."""

from typing import Literal, TypeAlias, cast

PreferredResourceName: TypeAlias = Literal["Ec2InstanceTypes",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PreferredResourceName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PreferredResourceName:
    return cast(PreferredResourceName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PreferredResourceName) -> str:
    return value


def deserialize_cbor(data: str) -> PreferredResourceName:
    return cast(PreferredResourceName, data)
