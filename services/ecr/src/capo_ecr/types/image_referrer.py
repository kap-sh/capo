"""Generated from Smithy shape ``com.amazonaws.ecr#ImageReferrer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.annotations
    import capo_ecr.types.artifact_status
    import capo_ecr.types.artifact_type
    import capo_ecr.types.image_digest
    import capo_ecr.types.image_size_in_bytes
    import capo_ecr.types.media_type


class ImageReferrer(TypedDict, closed=True):
    digest: "capo_ecr.types.image_digest.ImageDigest"
    """<p>The digest of the artifact manifest.</p>"""
    media_type: "capo_ecr.types.media_type.MediaType"
    """<p>The media type of the artifact manifest.</p>"""
    artifact_type: NotRequired["capo_ecr.types.artifact_type.ArtifactType"]
    """<p>A string identifying the type of artifact.</p>"""
    size: "capo_ecr.types.image_size_in_bytes.ImageSizeInBytes"
    """<p>The size, in bytes, of the artifact.</p>"""
    annotations: NotRequired["capo_ecr.types.annotations.Annotations"]
    """<p>A map of annotations associated with the artifact.</p>"""
    artifact_status: NotRequired["capo_ecr.types.artifact_status.ArtifactStatus"]
    """<p>The status of the artifact. Valid values are <code>ACTIVE</code>, <code>ARCHIVED</code>, or <code>ACTIVATING</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageReferrer) -> dict:
    out: dict = {}
    out["digest"] = value["digest"]
    out["mediaType"] = value["media_type"]
    if "artifact_type" in value:
        out["artifactType"] = value["artifact_type"]
    out["size"] = value["size"]
    if "annotations" in value:
        import capo_ecr.types.annotations

        out["annotations"] = capo_ecr.types.annotations.serialize_aws_json_1_1(
            value["annotations"]
        )
    if "artifact_status" in value:
        import capo_ecr.types.artifact_status

        out["artifactStatus"] = capo_ecr.types.artifact_status.serialize_aws_json_1_1(
            value["artifact_status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageReferrer:
    out: ImageReferrer = {}  # type: ignore[typeddict-item]
    if data.get("digest") is not None:
        out["digest"] = data["digest"]
    else:
        out["digest"] = ""
    if data.get("mediaType") is not None:
        out["media_type"] = data["mediaType"]
    else:
        out["media_type"] = ""
    if data.get("artifactType") is not None:
        out["artifact_type"] = data["artifactType"]
    if data.get("size") is not None:
        out["size"] = data["size"]
    else:
        out["size"] = 0
    if data.get("annotations") is not None:
        import capo_ecr.types.annotations

        out["annotations"] = capo_ecr.types.annotations.deserialize_aws_json_1_1(
            data["annotations"]
        )
    if data.get("artifactStatus") is not None:
        import capo_ecr.types.artifact_status

        out["artifact_status"] = (
            capo_ecr.types.artifact_status.deserialize_aws_json_1_1(
                data["artifactStatus"]
            )
        )
    return out
