"""Generated from Smithy shape ``com.amazonaws.ecr#GetDownloadUrlForLayerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.layer_digest
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name


class GetDownloadUrlForLayerRequest(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry that contains the image layer to download. If you do not specify a registry, the default registry is assumed.</p>"""
    repository_name: "capo_ecr.types.repository_name.RepositoryName"
    """<p>The name of the repository that is associated with the image layer to download.</p>"""
    layer_digest: "capo_ecr.types.layer_digest.LayerDigest"
    """<p>The digest of the image layer to download.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDownloadUrlForLayerRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    out["layerDigest"] = value["layer_digest"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDownloadUrlForLayerRequest:
    out: GetDownloadUrlForLayerRequest = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("layerDigest") is not None:
        out["layer_digest"] = data["layerDigest"]
    else:
        out["layer_digest"] = ""
    return out
