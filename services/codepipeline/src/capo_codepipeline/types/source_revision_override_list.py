"""Generated from Smithy shape ``com.amazonaws.codepipeline#SourceRevisionOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.source_revision_override

SourceRevisionOverrideList: TypeAlias = list[
    "capo_codepipeline.types.source_revision_override.SourceRevisionOverride"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceRevisionOverrideList) -> list:
    import capo_codepipeline.types.source_revision_override

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.source_revision_override.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SourceRevisionOverrideList:
    import capo_codepipeline.types.source_revision_override

    out: SourceRevisionOverrideList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.source_revision_override.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SourceRevisionOverrideList) -> list:
    import capo_codepipeline.types.source_revision_override

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.source_revision_override.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> SourceRevisionOverrideList:
    import capo_codepipeline.types.source_revision_override

    out: SourceRevisionOverrideList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.source_revision_override.deserialize_cbor(item)
        )
    return out
