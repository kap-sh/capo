"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#WaitELBTargetGroupHealthy``."""

from typing import Literal, TypeAlias, cast

WaitELBTargetGroupHealthy: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WaitELBTargetGroupHealthy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WaitELBTargetGroupHealthy:
    return cast(WaitELBTargetGroupHealthy, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WaitELBTargetGroupHealthy) -> str:
    return value


def deserialize_cbor(data: str) -> WaitELBTargetGroupHealthy:
    return cast(WaitELBTargetGroupHealthy, data)
