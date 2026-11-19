"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#UpdatePlanExecutionStepAction``."""

from typing import Literal, TypeAlias, cast

UpdatePlanExecutionStepAction: TypeAlias = Literal[
    "switchToUngraceful",
    "skip",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdatePlanExecutionStepAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> UpdatePlanExecutionStepAction:
    return cast(UpdatePlanExecutionStepAction, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdatePlanExecutionStepAction) -> str:
    return value


def deserialize_cbor(data: str) -> UpdatePlanExecutionStepAction:
    return cast(UpdatePlanExecutionStepAction, data)
