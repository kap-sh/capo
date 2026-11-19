"""Generated from Smithy shape ``com.amazonaws.codebuild#ResolvedArtifact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.artifacts_type
    import capo_codebuild.types.string


class ResolvedArtifact(TypedDict, closed=True):
    type: NotRequired["capo_codebuild.types.artifacts_type.ArtifactsType"]
    """<p>Specifies the type of artifact.</p>"""
    location: NotRequired["capo_codebuild.types.string.String"]
    """<p>The location of the artifact.</p>"""
    identifier: NotRequired["capo_codebuild.types.string.String"]
    """<p>The identifier of the artifact.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolvedArtifact) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_codebuild.types.artifacts_type

        out["type"] = capo_codebuild.types.artifacts_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "location" in value:
        out["location"] = value["location"]
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolvedArtifact:
    out: ResolvedArtifact = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_codebuild.types.artifacts_type

        out["type"] = capo_codebuild.types.artifacts_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if data.get("location") is not None:
        out["location"] = data["location"]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResolvedArtifact) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_codebuild.types.artifacts_type

        out["type"] = capo_codebuild.types.artifacts_type.serialize_cbor(value["type"])
    if "location" in value:
        out["location"] = value["location"]
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    return out


def deserialize_cbor(data: dict) -> ResolvedArtifact:
    out: ResolvedArtifact = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_codebuild.types.artifacts_type

        out["type"] = capo_codebuild.types.artifacts_type.deserialize_cbor(data["type"])
    if data.get("location") is not None:
        out["location"] = data["location"]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    return out
