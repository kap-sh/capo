"""Generated from Smithy shape ``com.amazonaws.codepipeline#StageTransitionType``."""

from typing import Literal, TypeAlias, cast

StageTransitionType: TypeAlias = Literal[
    "Inbound",
    "Outbound",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StageTransitionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StageTransitionType:
    return cast(StageTransitionType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StageTransitionType) -> str:
    return value


def deserialize_cbor(data: str) -> StageTransitionType:
    return cast(StageTransitionType, data)
