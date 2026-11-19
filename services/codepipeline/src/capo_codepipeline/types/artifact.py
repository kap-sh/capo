"""Generated from Smithy shape ``com.amazonaws.codepipeline#Artifact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.artifact_location
    import capo_codepipeline.types.artifact_name
    import capo_codepipeline.types.revision


class Artifact(TypedDict, closed=True):
    name: NotRequired["capo_codepipeline.types.artifact_name.ArtifactName"]
    """<p>The artifact's name.</p>"""
    revision: NotRequired["capo_codepipeline.types.revision.Revision"]
    """<p>The artifact's revision ID. Depending on the type of object, this could be a commit ID (GitHub) or a revision ID (Amazon S3).</p>"""
    location: NotRequired["capo_codepipeline.types.artifact_location.ArtifactLocation"]
    """<p>The location of an artifact.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Artifact) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "revision" in value:
        out["revision"] = value["revision"]
    if "location" in value:
        import capo_codepipeline.types.artifact_location

        out["location"] = (
            capo_codepipeline.types.artifact_location.serialize_aws_json_1_1(
                value["location"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Artifact:
    out: Artifact = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    if data.get("location") is not None:
        import capo_codepipeline.types.artifact_location

        out["location"] = (
            capo_codepipeline.types.artifact_location.deserialize_aws_json_1_1(
                data["location"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Artifact) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "revision" in value:
        out["revision"] = value["revision"]
    if "location" in value:
        import capo_codepipeline.types.artifact_location

        out["location"] = capo_codepipeline.types.artifact_location.serialize_cbor(
            value["location"]
        )
    return out


def deserialize_cbor(data: dict) -> Artifact:
    out: Artifact = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    if data.get("location") is not None:
        import capo_codepipeline.types.artifact_location

        out["location"] = capo_codepipeline.types.artifact_location.deserialize_cbor(
            data["location"]
        )
    return out
