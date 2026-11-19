"""Generated from Smithy shape ``com.amazonaws.codepipeline#StageExecutionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.stage_execution

StageExecutionList: TypeAlias = list[
    "capo_codepipeline.types.stage_execution.StageExecution"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StageExecutionList) -> list:
    import capo_codepipeline.types.stage_execution

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.stage_execution.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StageExecutionList:
    import capo_codepipeline.types.stage_execution

    out: StageExecutionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.stage_execution.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StageExecutionList) -> list:
    import capo_codepipeline.types.stage_execution

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.stage_execution.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> StageExecutionList:
    import capo_codepipeline.types.stage_execution

    out: StageExecutionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codepipeline.types.stage_execution.deserialize_cbor(item))
    return out
