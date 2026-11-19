"""Generated from Smithy shape ``com.amazonaws.codedeploy#MinimumHealthyHostsPerZoneType``."""

from typing import Literal, TypeAlias, cast

MinimumHealthyHostsPerZoneType: TypeAlias = Literal[
    "HOST_COUNT",
    "FLEET_PERCENT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MinimumHealthyHostsPerZoneType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MinimumHealthyHostsPerZoneType:
    return cast(MinimumHealthyHostsPerZoneType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MinimumHealthyHostsPerZoneType) -> str:
    return value


def deserialize_cbor(data: str) -> MinimumHealthyHostsPerZoneType:
    return cast(MinimumHealthyHostsPerZoneType, data)
