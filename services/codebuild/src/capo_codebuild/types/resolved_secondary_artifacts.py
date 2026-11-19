"""Generated from Smithy shape ``com.amazonaws.codebuild#ResolvedSecondaryArtifacts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.resolved_artifact

ResolvedSecondaryArtifacts: TypeAlias = list[
    "capo_codebuild.types.resolved_artifact.ResolvedArtifact"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolvedSecondaryArtifacts) -> list:
    import capo_codebuild.types.resolved_artifact

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.resolved_artifact.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResolvedSecondaryArtifacts:
    import capo_codebuild.types.resolved_artifact

    out: ResolvedSecondaryArtifacts = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codebuild.types.resolved_artifact.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResolvedSecondaryArtifacts) -> list:
    import capo_codebuild.types.resolved_artifact

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.resolved_artifact.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ResolvedSecondaryArtifacts:
    import capo_codebuild.types.resolved_artifact

    out: ResolvedSecondaryArtifacts = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.resolved_artifact.deserialize_cbor(item))
    return out
