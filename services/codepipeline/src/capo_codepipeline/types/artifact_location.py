"""Generated from Smithy shape ``com.amazonaws.codepipeline#ArtifactLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.artifact_location_type
    import capo_codepipeline.types.s3_artifact_location


class ArtifactLocation(TypedDict, closed=True):
    type: NotRequired[
        "capo_codepipeline.types.artifact_location_type.ArtifactLocationType"
    ]
    """<p>The type of artifact in the location.</p>"""
    s3_location: NotRequired[
        "capo_codepipeline.types.s3_artifact_location.S3ArtifactLocation"
    ]
    """<p>The S3 bucket that contains the artifact.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactLocation) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_codepipeline.types.artifact_location_type

        out["type"] = (
            capo_codepipeline.types.artifact_location_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "s3_location" in value:
        import capo_codepipeline.types.s3_artifact_location

        out["s3Location"] = (
            capo_codepipeline.types.s3_artifact_location.serialize_aws_json_1_1(
                value["s3_location"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ArtifactLocation:
    out: ArtifactLocation = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_codepipeline.types.artifact_location_type

        out["type"] = (
            capo_codepipeline.types.artifact_location_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    if data.get("s3Location") is not None:
        import capo_codepipeline.types.s3_artifact_location

        out["s3_location"] = (
            capo_codepipeline.types.s3_artifact_location.deserialize_aws_json_1_1(
                data["s3Location"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ArtifactLocation) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_codepipeline.types.artifact_location_type

        out["type"] = capo_codepipeline.types.artifact_location_type.serialize_cbor(
            value["type"]
        )
    if "s3_location" in value:
        import capo_codepipeline.types.s3_artifact_location

        out["s3Location"] = capo_codepipeline.types.s3_artifact_location.serialize_cbor(
            value["s3_location"]
        )
    return out


def deserialize_cbor(data: dict) -> ArtifactLocation:
    out: ArtifactLocation = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_codepipeline.types.artifact_location_type

        out["type"] = capo_codepipeline.types.artifact_location_type.deserialize_cbor(
            data["type"]
        )
    if data.get("s3Location") is not None:
        import capo_codepipeline.types.s3_artifact_location

        out["s3_location"] = (
            capo_codepipeline.types.s3_artifact_location.deserialize_cbor(
                data["s3Location"]
            )
        )
    return out
