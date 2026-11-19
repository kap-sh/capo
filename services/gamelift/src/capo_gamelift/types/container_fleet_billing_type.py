"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerFleetBillingType``."""

from typing import Literal, TypeAlias, cast

ContainerFleetBillingType: TypeAlias = Literal[
    "ON_DEMAND",
    "SPOT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerFleetBillingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerFleetBillingType:
    return cast(ContainerFleetBillingType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContainerFleetBillingType) -> str:
    return value


def deserialize_cbor(data: str) -> ContainerFleetBillingType:
    return cast(ContainerFleetBillingType, data)
