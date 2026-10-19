"""Generated from Smithy shape ``com.amazonaws.ecr#DescribeImageSigningStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecr.types.image_identifier
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name


class DescribeImageSigningStatusRequest(TypedDict, closed=True):
    repository_name: "capo_ecr.types.repository_name.RepositoryName"
    """<p>The name of the repository that contains the image.</p>"""
    image_id: "capo_ecr.types.image_identifier.ImageIdentifier"
    """<p>An object containing identifying information for an image.</p>"""
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImageSigningStatusRequest) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    import capo_ecr.types.image_identifier

    out["imageId"] = capo_ecr.types.image_identifier.serialize_aws_json_1_1(
        value["image_id"]
    )
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImageSigningStatusRequest:
    out: DescribeImageSigningStatusRequest = {}  # type: ignore[typeddict-item]
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
            "DescribeImageSigningStatusRequest.image_id required"
        )
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    return out
