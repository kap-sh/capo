"""Generated from Smithy shape ``com.amazonaws.codepipeline#OutputArtifactList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.output_artifact

OutputArtifactList: TypeAlias = list[
    "capo_codepipeline.types.output_artifact.OutputArtifact"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputArtifactList) -> list:
    import capo_codepipeline.types.output_artifact

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.output_artifact.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OutputArtifactList:
    import capo_codepipeline.types.output_artifact

    out: OutputArtifactList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.output_artifact.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OutputArtifactList) -> list:
    import capo_codepipeline.types.output_artifact

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.output_artifact.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> OutputArtifactList:
    import capo_codepipeline.types.output_artifact

    out: OutputArtifactList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codepipeline.types.output_artifact.deserialize_cbor(item))
    return out
