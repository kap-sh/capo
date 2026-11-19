"""Generated from Smithy shape ``com.amazonaws.codepipeline#OutputVariablesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.output_variables_key
    import capo_codepipeline.types.output_variables_value

OutputVariablesMap: TypeAlias = dict[
    "capo_codepipeline.types.output_variables_key.OutputVariablesKey",
    "capo_codepipeline.types.output_variables_value.OutputVariablesValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: OutputVariablesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> OutputVariablesMap:
    out: OutputVariablesMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: OutputVariablesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> OutputVariablesMap:
    out: OutputVariablesMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
