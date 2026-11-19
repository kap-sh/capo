"""Generated from Smithy shape ``com.amazonaws.codebuild#EnvironmentImage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.image_versions
    import capo_codebuild.types.string


class EnvironmentImage(TypedDict, closed=True):
    name: NotRequired["capo_codebuild.types.string.String"]
    """<p>The name of the Docker image.</p>"""
    description: NotRequired["capo_codebuild.types.string.String"]
    """<p>The description of the Docker image.</p>"""
    versions: NotRequired["capo_codebuild.types.image_versions.ImageVersions"]
    """<p>A list of environment image versions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentImage) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "versions" in value:
        import capo_codebuild.types.image_versions

        out["versions"] = capo_codebuild.types.image_versions.serialize_aws_json_1_1(
            value["versions"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnvironmentImage:
    out: EnvironmentImage = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("versions") is not None:
        import capo_codebuild.types.image_versions

        out["versions"] = capo_codebuild.types.image_versions.deserialize_aws_json_1_1(
            data["versions"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnvironmentImage) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "versions" in value:
        import capo_codebuild.types.image_versions

        out["versions"] = capo_codebuild.types.image_versions.serialize_cbor(
            value["versions"]
        )
    return out


def deserialize_cbor(data: dict) -> EnvironmentImage:
    out: EnvironmentImage = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("versions") is not None:
        import capo_codebuild.types.image_versions

        out["versions"] = capo_codebuild.types.image_versions.deserialize_cbor(
            data["versions"]
        )
    return out
