"""Generated from Smithy shape ``com.amazonaws.codebuild#EnvironmentLanguages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.environment_language

EnvironmentLanguages: TypeAlias = list[
    "capo_codebuild.types.environment_language.EnvironmentLanguage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentLanguages) -> list:
    import capo_codebuild.types.environment_language

    out: list = []
    for item in value:
        out.append(
            capo_codebuild.types.environment_language.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EnvironmentLanguages:
    import capo_codebuild.types.environment_language

    out: EnvironmentLanguages = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codebuild.types.environment_language.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnvironmentLanguages) -> list:
    import capo_codebuild.types.environment_language

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.environment_language.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EnvironmentLanguages:
    import capo_codebuild.types.environment_language

    out: EnvironmentLanguages = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.environment_language.deserialize_cbor(item))
    return out
