"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionExecutionStatus``."""

from typing import Literal, TypeAlias, cast

ActionExecutionStatus: TypeAlias = Literal[
    "InProgress",
    "Abandoned",
    "Succeeded",
    "Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActionExecutionStatus:
    return cast(ActionExecutionStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ActionExecutionStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ActionExecutionStatus:
    return cast(ActionExecutionStatus, data)
