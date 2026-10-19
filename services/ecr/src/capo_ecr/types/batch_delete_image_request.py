"""Generated from Smithy shape ``com.amazonaws.ecr#BatchDeleteImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.image_identifier_list
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name


class BatchDeleteImageRequest(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry that contains the image to delete. If you do not specify a registry, the default registry is assumed.</p>"""
    repository_name: "capo_ecr.types.repository_name.RepositoryName"
    """<p>The repository that contains the image to delete.</p>"""
    image_ids: "capo_ecr.types.image_identifier_list.ImageIdentifierList"
    """<p>A list of image ID references that correspond to images to delete. The format of the <code>imageIds</code> reference is <code>imageTag=tag</code> or <code>imageDigest=digest</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteImageRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    import capo_ecr.types.image_identifier_list

    out["imageIds"] = capo_ecr.types.image_identifier_list.serialize_aws_json_1_1(
        value["image_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteImageRequest:
    out: BatchDeleteImageRequest = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("imageIds") is not None:
        import capo_ecr.types.image_identifier_list

        out["image_ids"] = (
            capo_ecr.types.image_identifier_list.deserialize_aws_json_1_1(
                data["imageIds"]
            )
        )
    else:
        out["image_ids"] = []
    return out
