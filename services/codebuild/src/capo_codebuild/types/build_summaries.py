"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.build_summary

BuildSummaries: TypeAlias = list["capo_codebuild.types.build_summary.BuildSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildSummaries) -> list:
    import capo_codebuild.types.build_summary

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.build_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BuildSummaries:
    import capo_codebuild.types.build_summary

    out: BuildSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.build_summary.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BuildSummaries) -> list:
    import capo_codebuild.types.build_summary

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.build_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> BuildSummaries:
    import capo_codebuild.types.build_summary

    out: BuildSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.build_summary.deserialize_cbor(item))
    return out
