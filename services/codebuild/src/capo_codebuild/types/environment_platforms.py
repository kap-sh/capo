"""Generated from Smithy shape ``com.amazonaws.codebuild#EnvironmentPlatforms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.environment_platform

EnvironmentPlatforms: TypeAlias = list[
    "capo_codebuild.types.environment_platform.EnvironmentPlatform"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentPlatforms) -> list:
    import capo_codebuild.types.environment_platform

    out: list = []
    for item in value:
        out.append(
            capo_codebuild.types.environment_platform.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EnvironmentPlatforms:
    import capo_codebuild.types.environment_platform

    out: EnvironmentPlatforms = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codebuild.types.environment_platform.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnvironmentPlatforms) -> list:
    import capo_codebuild.types.environment_platform

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.environment_platform.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EnvironmentPlatforms:
    import capo_codebuild.types.environment_platform

    out: EnvironmentPlatforms = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.environment_platform.deserialize_cbor(item))
    return out
