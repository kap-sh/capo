"""Generated from Smithy shape ``com.amazonaws.ecr#PutImageScanningConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecr.types.image_scanning_configuration
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name


class PutImageScanningConfigurationRequest(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry that contains the repository in which to update the image scanning configuration setting. If you do not specify a registry, the default registry is assumed.</p>"""
    repository_name: "capo_ecr.types.repository_name.RepositoryName"
    """<p>The name of the repository in which to update the image scanning configuration setting.</p>"""
    image_scanning_configuration: (
        "capo_ecr.types.image_scanning_configuration.ImageScanningConfiguration"
    )
    """<p>The image scanning configuration for the repository. This setting determines whether images are scanned for known vulnerabilities after being pushed to the repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutImageScanningConfigurationRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    import capo_ecr.types.image_scanning_configuration

    out["imageScanningConfiguration"] = (
        capo_ecr.types.image_scanning_configuration.serialize_aws_json_1_1(
            value["image_scanning_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutImageScanningConfigurationRequest:
    out: PutImageScanningConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("imageScanningConfiguration") is not None:
        import capo_ecr.types.image_scanning_configuration

        out["image_scanning_configuration"] = (
            capo_ecr.types.image_scanning_configuration.deserialize_aws_json_1_1(
                data["imageScanningConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutImageScanningConfigurationRequest.image_scanning_configuration required"
        )
    return out
