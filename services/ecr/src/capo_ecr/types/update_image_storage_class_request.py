"""Generated from Smithy shape ``com.amazonaws.ecr#UpdateImageStorageClassRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecr.types.image_identifier
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name
    import capo_ecr.types.target_storage_class


class UpdateImageStorageClassRequest(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry that contains the image to transition. If you do not specify a registry, the default registry is assumed.</p>"""
    repository_name: "capo_ecr.types.repository_name.RepositoryName"
    """<p>The name of the repository that contains the image to transition.</p>"""
    image_id: "capo_ecr.types.image_identifier.ImageIdentifier"
    target_storage_class: "capo_ecr.types.target_storage_class.TargetStorageClass"
    """<p>The target storage class for the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateImageStorageClassRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    import capo_ecr.types.image_identifier

    out["imageId"] = capo_ecr.types.image_identifier.serialize_aws_json_1_1(
        value["image_id"]
    )
    import capo_ecr.types.target_storage_class

    out["targetStorageClass"] = (
        capo_ecr.types.target_storage_class.serialize_aws_json_1_1(
            value["target_storage_class"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateImageStorageClassRequest:
    out: UpdateImageStorageClassRequest = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
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
        raise DeserializationError("UpdateImageStorageClassRequest.image_id required")
    if data.get("targetStorageClass") is not None:
        import capo_ecr.types.target_storage_class

        out["target_storage_class"] = (
            capo_ecr.types.target_storage_class.deserialize_aws_json_1_1(
                data["targetStorageClass"]
            )
        )
    else:
        import typing

        out["target_storage_class"] = typing.cast(
            "capo_ecr.types.target_storage_class.TargetStorageClass", ""
        )
    return out
