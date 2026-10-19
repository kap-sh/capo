"""Generated from Smithy shape ``com.amazonaws.ecr#DescribeImageReplicationStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecr.types.image_identifier
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name


class DescribeImageReplicationStatusRequest(TypedDict, closed=True):
    repository_name: "capo_ecr.types.repository_name.RepositoryName"
    """<p>The name of the repository that the image is in.</p>"""
    image_id: "capo_ecr.types.image_identifier.ImageIdentifier"
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry. If you do not specify a registry, the default registry is assumed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImageReplicationStatusRequest) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    import capo_ecr.types.image_identifier

    out["imageId"] = capo_ecr.types.image_identifier.serialize_aws_json_1_1(
        value["image_id"]
    )
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImageReplicationStatusRequest:
    out: DescribeImageReplicationStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("imageId") is not None:
        import capo_ecr.types.image_identifier

        out["image_id"] = capo_ecr.types.image_identifier.deserialize_aws_json_1_1(
            data["imageId"]
        )
    else:
        raise DeserializationError(
            "DescribeImageReplicationStatusRequest.image_id required"
        )
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    return out
