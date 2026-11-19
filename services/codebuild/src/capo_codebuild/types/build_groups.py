"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.build_group

BuildGroups: TypeAlias = list["capo_codebuild.types.build_group.BuildGroup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildGroups) -> list:
    import capo_codebuild.types.build_group

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.build_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BuildGroups:
    import capo_codebuild.types.build_group

    out: BuildGroups = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.build_group.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BuildGroups) -> list:
    import capo_codebuild.types.build_group

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.build_group.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> BuildGroups:
    import capo_codebuild.types.build_group

    out: BuildGroups = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.build_group.deserialize_cbor(item))
    return out
