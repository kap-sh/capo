"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineTriggerDeclarationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.pipeline_trigger_declaration

PipelineTriggerDeclarationList: TypeAlias = list[
    "capo_codepipeline.types.pipeline_trigger_declaration.PipelineTriggerDeclaration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineTriggerDeclarationList) -> list:
    import capo_codepipeline.types.pipeline_trigger_declaration

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.pipeline_trigger_declaration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PipelineTriggerDeclarationList:
    import capo_codepipeline.types.pipeline_trigger_declaration

    out: PipelineTriggerDeclarationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.pipeline_trigger_declaration.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PipelineTriggerDeclarationList) -> list:
    import capo_codepipeline.types.pipeline_trigger_declaration

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.pipeline_trigger_declaration.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> PipelineTriggerDeclarationList:
    import capo_codepipeline.types.pipeline_trigger_declaration

    out: PipelineTriggerDeclarationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.pipeline_trigger_declaration.deserialize_cbor(item)
        )
    return out
