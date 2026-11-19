"""Generated from Smithy shape ``com.amazonaws.codebuild#Projects``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.project

Projects: TypeAlias = list["capo_codebuild.types.project.Project"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Projects) -> list:
    import capo_codebuild.types.project

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.project.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Projects:
    import capo_codebuild.types.project

    out: Projects = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.project.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Projects) -> list:
    import capo_codebuild.types.project

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.project.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Projects:
    import capo_codebuild.types.project

    out: Projects = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.project.deserialize_cbor(item))
    return out
