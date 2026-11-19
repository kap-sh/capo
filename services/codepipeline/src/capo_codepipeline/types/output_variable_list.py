"""Generated from Smithy shape ``com.amazonaws.codepipeline#OutputVariableList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.output_variable

OutputVariableList: TypeAlias = list[
    "capo_codepipeline.types.output_variable.OutputVariable"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputVariableList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OutputVariableList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OutputVariableList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> OutputVariableList:
    return [item for item in data if item is not None]
