"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#SavingsEstimationMode``."""

from typing import Literal, TypeAlias, cast

SavingsEstimationMode: TypeAlias = Literal[
    "BeforeDiscount",
    "AfterDiscount",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SavingsEstimationMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SavingsEstimationMode:
    return cast(SavingsEstimationMode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SavingsEstimationMode) -> str:
    return value


def deserialize_cbor(data: str) -> SavingsEstimationMode:
    return cast(SavingsEstimationMode, data)
