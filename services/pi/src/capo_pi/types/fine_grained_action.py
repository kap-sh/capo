"""Generated from Smithy shape ``com.amazonaws.pi#FineGrainedAction``."""

from typing import Literal, TypeAlias, cast

FineGrainedAction: TypeAlias = Literal[
    "DescribeDimensionKeys",
    "GetDimensionKeyDetails",
    "GetResourceMetrics",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FineGrainedAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FineGrainedAction:
    return cast(FineGrainedAction, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FineGrainedAction) -> str:
    return value


def deserialize_cbor(data: str) -> FineGrainedAction:
    return cast(FineGrainedAction, data)
