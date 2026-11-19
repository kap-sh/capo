"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#UpdatePlanExecutionAction``."""

from typing import Literal, TypeAlias, cast

UpdatePlanExecutionAction: TypeAlias = Literal[
    "switchToGraceful",
    "switchToUngraceful",
    "pause",
    "resume",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdatePlanExecutionAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> UpdatePlanExecutionAction:
    return cast(UpdatePlanExecutionAction, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdatePlanExecutionAction) -> str:
    return value


def deserialize_cbor(data: str) -> UpdatePlanExecutionAction:
    return cast(UpdatePlanExecutionAction, data)
