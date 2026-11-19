"""Generated from Smithy shape ``com.amazonaws.codebuild#Builds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.build

Builds: TypeAlias = list["capo_codebuild.types.build.Build"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Builds) -> list:
    import capo_codebuild.types.build

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.build.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Builds:
    import capo_codebuild.types.build

    out: Builds = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.build.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Builds) -> list:
    import capo_codebuild.types.build

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.build.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Builds:
    import capo_codebuild.types.build

    out: Builds = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.build.deserialize_cbor(item))
    return out
