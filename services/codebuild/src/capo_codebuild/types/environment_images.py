"""Generated from Smithy shape ``com.amazonaws.codebuild#EnvironmentImages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.environment_image

EnvironmentImages: TypeAlias = list[
    "capo_codebuild.types.environment_image.EnvironmentImage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentImages) -> list:
    import capo_codebuild.types.environment_image

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.environment_image.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EnvironmentImages:
    import capo_codebuild.types.environment_image

    out: EnvironmentImages = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codebuild.types.environment_image.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnvironmentImages) -> list:
    import capo_codebuild.types.environment_image

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.environment_image.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EnvironmentImages:
    import capo_codebuild.types.environment_image

    out: EnvironmentImages = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.environment_image.deserialize_cbor(item))
    return out
