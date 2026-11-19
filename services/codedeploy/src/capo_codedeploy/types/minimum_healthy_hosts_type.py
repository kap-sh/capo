"""Generated from Smithy shape ``com.amazonaws.codedeploy#MinimumHealthyHostsType``."""

from typing import Literal, TypeAlias, cast

MinimumHealthyHostsType: TypeAlias = Literal[
    "HOST_COUNT",
    "FLEET_PERCENT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MinimumHealthyHostsType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MinimumHealthyHostsType:
    return cast(MinimumHealthyHostsType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MinimumHealthyHostsType) -> str:
    return value


def deserialize_cbor(data: str) -> MinimumHealthyHostsType:
    return cast(MinimumHealthyHostsType, data)
