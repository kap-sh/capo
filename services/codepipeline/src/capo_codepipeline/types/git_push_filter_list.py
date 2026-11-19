"""Generated from Smithy shape ``com.amazonaws.codepipeline#GitPushFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.git_push_filter

GitPushFilterList: TypeAlias = list[
    "capo_codepipeline.types.git_push_filter.GitPushFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GitPushFilterList) -> list:
    import capo_codepipeline.types.git_push_filter

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.git_push_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GitPushFilterList:
    import capo_codepipeline.types.git_push_filter

    out: GitPushFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.git_push_filter.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GitPushFilterList) -> list:
    import capo_codepipeline.types.git_push_filter

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.git_push_filter.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> GitPushFilterList:
    import capo_codepipeline.types.git_push_filter

    out: GitPushFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codepipeline.types.git_push_filter.deserialize_cbor(item))
    return out
