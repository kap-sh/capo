"""Generated from Smithy shape ``com.amazonaws.codepipeline#ArtifactDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.artifact_detail

ArtifactDetailList: TypeAlias = list[
    "capo_codepipeline.types.artifact_detail.ArtifactDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactDetailList) -> list:
    import capo_codepipeline.types.artifact_detail

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.artifact_detail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ArtifactDetailList:
    import capo_codepipeline.types.artifact_detail

    out: ArtifactDetailList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.artifact_detail.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ArtifactDetailList) -> list:
    import capo_codepipeline.types.artifact_detail

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.artifact_detail.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ArtifactDetailList:
    import capo_codepipeline.types.artifact_detail

    out: ArtifactDetailList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codepipeline.types.artifact_detail.deserialize_cbor(item))
    return out
