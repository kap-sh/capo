"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#WorkflowTargetAction``."""

from typing import Literal, TypeAlias, cast

WorkflowTargetAction: TypeAlias = Literal[
    "activate",
    "deactivate",
    "postRecovery",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowTargetAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WorkflowTargetAction:
    return cast(WorkflowTargetAction, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkflowTargetAction) -> str:
    return value


def deserialize_cbor(data: str) -> WorkflowTargetAction:
    return cast(WorkflowTargetAction, data)
