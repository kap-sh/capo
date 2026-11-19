"""Generated from Smithy shape ``com.amazonaws.codedeploy#StopStatus``."""

from typing import Literal, TypeAlias, cast

StopStatus: TypeAlias = Literal[
    "Pending",
    "Succeeded",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StopStatus:
    return cast(StopStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StopStatus) -> str:
    return value


def deserialize_cbor(data: str) -> StopStatus:
    return cast(StopStatus, data)
