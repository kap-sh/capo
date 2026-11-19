"""Generated from Smithy shape ``com.amazonaws.codebuild#EnvironmentPlatform``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.environment_languages
    import capo_codebuild.types.platform_type


class EnvironmentPlatform(TypedDict, closed=True):
    platform: NotRequired["capo_codebuild.types.platform_type.PlatformType"]
    """<p>The platform's name.</p>"""
    languages: NotRequired[
        "capo_codebuild.types.environment_languages.EnvironmentLanguages"
    ]
    """<p>The list of programming languages that are available for the specified platform.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentPlatform) -> dict:
    out: dict = {}
    if "platform" in value:
        import capo_codebuild.types.platform_type

        out["platform"] = capo_codebuild.types.platform_type.serialize_aws_json_1_1(
            value["platform"]
        )
    if "languages" in value:
        import capo_codebuild.types.environment_languages

        out["languages"] = (
            capo_codebuild.types.environment_languages.serialize_aws_json_1_1(
                value["languages"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnvironmentPlatform:
    out: EnvironmentPlatform = {}  # type: ignore[typeddict-item]
    if data.get("platform") is not None:
        import capo_codebuild.types.platform_type

        out["platform"] = capo_codebuild.types.platform_type.deserialize_aws_json_1_1(
            data["platform"]
        )
    if data.get("languages") is not None:
        import capo_codebuild.types.environment_languages

        out["languages"] = (
            capo_codebuild.types.environment_languages.deserialize_aws_json_1_1(
                data["languages"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnvironmentPlatform) -> dict:
    out: dict = {}
    if "platform" in value:
        import capo_codebuild.types.platform_type

        out["platform"] = capo_codebuild.types.platform_type.serialize_cbor(
            value["platform"]
        )
    if "languages" in value:
        import capo_codebuild.types.environment_languages

        out["languages"] = capo_codebuild.types.environment_languages.serialize_cbor(
            value["languages"]
        )
    return out


def deserialize_cbor(data: dict) -> EnvironmentPlatform:
    out: EnvironmentPlatform = {}  # type: ignore[typeddict-item]
    if data.get("platform") is not None:
        import capo_codebuild.types.platform_type

        out["platform"] = capo_codebuild.types.platform_type.deserialize_cbor(
            data["platform"]
        )
    if data.get("languages") is not None:
        import capo_codebuild.types.environment_languages

        out["languages"] = capo_codebuild.types.environment_languages.deserialize_cbor(
            data["languages"]
        )
    return out
