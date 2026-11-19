"""Generated from Smithy shape ``com.amazonaws.codepipeline#EnvironmentVariableList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.environment_variable

EnvironmentVariableList: TypeAlias = list[
    "capo_codepipeline.types.environment_variable.EnvironmentVariable"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentVariableList) -> list:
    import capo_codepipeline.types.environment_variable

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.environment_variable.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EnvironmentVariableList:
    import capo_codepipeline.types.environment_variable

    out: EnvironmentVariableList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.environment_variable.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnvironmentVariableList) -> list:
    import capo_codepipeline.types.environment_variable

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.environment_variable.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EnvironmentVariableList:
    import capo_codepipeline.types.environment_variable

    out: EnvironmentVariableList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codepipeline.types.environment_variable.deserialize_cbor(item))
    return out
