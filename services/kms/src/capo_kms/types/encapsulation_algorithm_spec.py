"""Generated from Smithy shape ``com.amazonaws.kms#EncapsulationAlgorithmSpec``."""

from typing import Literal, TypeAlias, cast

EncapsulationAlgorithmSpec: TypeAlias = Literal["ML_KEM",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncapsulationAlgorithmSpec) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EncapsulationAlgorithmSpec:
    return cast(EncapsulationAlgorithmSpec, data)
