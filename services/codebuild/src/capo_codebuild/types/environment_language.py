"""Generated from Smithy shape ``com.amazonaws.codebuild#EnvironmentLanguage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.environment_images
    import capo_codebuild.types.language_type


class EnvironmentLanguage(TypedDict, closed=True):
    language: NotRequired["capo_codebuild.types.language_type.LanguageType"]
    """<p>The programming language for the Docker images.</p>"""
    images: NotRequired["capo_codebuild.types.environment_images.EnvironmentImages"]
    """<p>The list of Docker images that are related by the specified programming language.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentLanguage) -> dict:
    out: dict = {}
    if "language" in value:
        import capo_codebuild.types.language_type

        out["language"] = capo_codebuild.types.language_type.serialize_aws_json_1_1(
            value["language"]
        )
    if "images" in value:
        import capo_codebuild.types.environment_images

        out["images"] = capo_codebuild.types.environment_images.serialize_aws_json_1_1(
            value["images"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnvironmentLanguage:
    out: EnvironmentLanguage = {}  # type: ignore[typeddict-item]
    if data.get("language") is not None:
        import capo_codebuild.types.language_type

        out["language"] = capo_codebuild.types.language_type.deserialize_aws_json_1_1(
            data["language"]
        )
    if data.get("images") is not None:
        import capo_codebuild.types.environment_images

        out["images"] = (
            capo_codebuild.types.environment_images.deserialize_aws_json_1_1(
                data["images"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnvironmentLanguage) -> dict:
    out: dict = {}
    if "language" in value:
        import capo_codebuild.types.language_type

        out["language"] = capo_codebuild.types.language_type.serialize_cbor(
            value["language"]
        )
    if "images" in value:
        import capo_codebuild.types.environment_images

        out["images"] = capo_codebuild.types.environment_images.serialize_cbor(
            value["images"]
        )
    return out


def deserialize_cbor(data: dict) -> EnvironmentLanguage:
    out: EnvironmentLanguage = {}  # type: ignore[typeddict-item]
    if data.get("language") is not None:
        import capo_codebuild.types.language_type

        out["language"] = capo_codebuild.types.language_type.deserialize_cbor(
            data["language"]
        )
    if data.get("images") is not None:
        import capo_codebuild.types.environment_images

        out["images"] = capo_codebuild.types.environment_images.deserialize_cbor(
            data["images"]
        )
    return out
