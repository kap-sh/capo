"""Generated from Smithy shape ``com.amazonaws.ecrpublic#PutImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr_public.types.image_digest
    import capo_ecr_public.types.image_manifest
    import capo_ecr_public.types.image_tag
    import capo_ecr_public.types.media_type
    import capo_ecr_public.types.registry_id_or_alias
    import capo_ecr_public.types.repository_name


class PutImageRequest(TypedDict, closed=True):
    registry_id: NotRequired[
        "capo_ecr_public.types.registry_id_or_alias.RegistryIdOrAlias"
    ]
    """<p>The Amazon Web Services account ID, or registry alias, that's associated with the public registry that contains the repository where the image is put. If you do not specify a registry, the default public registry is assumed.</p>"""
    repository_name: "capo_ecr_public.types.repository_name.RepositoryName"
    """<p>The name of the repository where the image is put.</p>"""
    image_manifest: "capo_ecr_public.types.image_manifest.ImageManifest"
    """<p>The image manifest that corresponds to the image to be uploaded.</p>"""
    image_manifest_media_type: NotRequired["capo_ecr_public.types.media_type.MediaType"]
    """<p>The media type of the image manifest. If you push an image manifest that doesn't contain the <code>mediaType</code> field, you must specify the <code>imageManifestMediaType</code> in the request.</p>"""
    image_tag: NotRequired["capo_ecr_public.types.image_tag.ImageTag"]
    """<p>The tag to associate with the image. This parameter is required for images that use the Docker Image Manifest V2 Schema 2 or Open Container Initiative (OCI) formats.</p>"""
    image_digest: NotRequired["capo_ecr_public.types.image_digest.ImageDigest"]
    """<p>The image digest of the image manifest that corresponds to the image.</p>"""


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
