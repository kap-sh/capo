"""Generated from Smithy shape ``com.amazonaws.ecr#PutImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.image_digest
    import capo_ecr.types.image_manifest
    import capo_ecr.types.image_tag
    import capo_ecr.types.media_type
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name


class PutImageRequest(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry that contains the repository in which to put the image. If you do not specify a registry, the default registry is assumed.</p>"""
    repository_name: "capo_ecr.types.repository_name.RepositoryName"
    """<p>The name of the repository in which to put the image.</p>"""
    image_manifest: "capo_ecr.types.image_manifest.ImageManifest"
    """<p>The image manifest corresponding to the image to be uploaded.</p>"""
    image_manifest_media_type: NotRequired["capo_ecr.types.media_type.MediaType"]
    """<p>The media type of the image manifest. If you push an image manifest that does not contain the <code>mediaType</code> field, you must specify the <code>imageManifestMediaType</code> in the request.</p>"""
    image_tag: NotRequired["capo_ecr.types.image_tag.ImageTag"]
    """<p>The tag to associate with the image. This parameter is optional.</p>"""
    image_digest: NotRequired["capo_ecr.types.image_digest.ImageDigest"]
    """<p>The image digest of the image manifest corresponding to the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutImageRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    out["imageManifest"] = value["image_manifest"]
    if "image_manifest_media_type" in value:
        out["imageManifestMediaType"] = value["image_manifest_media_type"]
    if "image_tag" in value:
        out["imageTag"] = value["image_tag"]
    if "image_digest" in value:
        out["imageDigest"] = value["image_digest"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutImageRequest:
    out: PutImageRequest = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("imageManifest") is not None:
        out["image_manifest"] = data["imageManifest"]
    else:
        out["image_manifest"] = ""
    if data.get("imageManifestMediaType") is not None:
        out["image_manifest_media_type"] = data["imageManifestMediaType"]
    if data.get("imageTag") is not None:
        out["image_tag"] = data["imageTag"]
    if data.get("imageDigest") is not None:
        out["image_digest"] = data["imageDigest"]
    return out
