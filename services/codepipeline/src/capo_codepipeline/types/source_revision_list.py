"""Generated from Smithy shape ``com.amazonaws.codepipeline#SourceRevisionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.source_revision

SourceRevisionList: TypeAlias = list[
    "capo_codepipeline.types.source_revision.SourceRevision"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceRevisionList) -> list:
    import capo_codepipeline.types.source_revision

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.source_revision.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SourceRevisionList:
    import capo_codepipeline.types.source_revision

    out: SourceRevisionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.source_revision.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SourceRevisionList) -> list:
    import capo_codepipeline.types.source_revision

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.source_revision.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> SourceRevisionList:
    import capo_codepipeline.types.source_revision

    out: SourceRevisionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codepipeline.types.source_revision.deserialize_cbor(item))
    return out
