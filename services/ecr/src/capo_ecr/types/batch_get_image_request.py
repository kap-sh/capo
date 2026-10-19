"""Generated from Smithy shape ``com.amazonaws.ecr#BatchGetImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.image_identifier_list
    import capo_ecr.types.media_type_list
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name


class BatchGetImageRequest(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry that contains the images to describe. If you do not specify a registry, the default registry is assumed.</p>"""
    repository_name: "capo_ecr.types.repository_name.RepositoryName"
    """<p>The repository that contains the images to describe.</p>"""
    image_ids: "capo_ecr.types.image_identifier_list.ImageIdentifierList"
    """<p>A list of image ID references that correspond to images to describe. The format of the <code>imageIds</code> reference is <code>imageTag=tag</code> or <code>imageDigest=digest</code>.</p>"""
    accepted_media_types: NotRequired["capo_ecr.types.media_type_list.MediaTypeList"]
    """<p>The accepted media types for the request.</p> <p>Valid values: <code>application/vnd.docker.distribution.manifest.v1+json</code> | <code>application/vnd.docker.distribution.manifest.v2+json</code> | <code>application/vnd.oci.image.manifest.v1+json</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetImageRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    import capo_ecr.types.image_identifier_list

    out["imageIds"] = capo_ecr.types.image_identifier_list.serialize_aws_json_1_1(
        value["image_ids"]
    )
    if "accepted_media_types" in value:
        import capo_ecr.types.media_type_list

        out["acceptedMediaTypes"] = (
            capo_ecr.types.media_type_list.serialize_aws_json_1_1(
                value["accepted_media_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetImageRequest:
    out: BatchGetImageRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("acceptedMediaTypes") is not None:
        import capo_ecr.types.media_type_list

        out["accepted_media_types"] = (
            capo_ecr.types.media_type_list.deserialize_aws_json_1_1(
                data["acceptedMediaTypes"]
            )
        )
    return out
