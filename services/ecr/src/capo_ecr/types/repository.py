"""Generated from Smithy shape ``com.amazonaws.ecr#Repository``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.arn
    import capo_ecr.types.creation_timestamp
    import capo_ecr.types.encryption_configuration
    import capo_ecr.types.image_scanning_configuration
    import capo_ecr.types.image_tag_mutability
    import capo_ecr.types.image_tag_mutability_exclusion_filters
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name
    import capo_ecr.types.url


class Repository(TypedDict, closed=True):
    repository_arn: NotRequired["capo_ecr.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the <code>arn:aws:ecr</code> namespace, followed by the region of the repository, Amazon Web Services account ID of the repository owner, and repository name. For example, <code>arn:aws:ecr:region:012345678910:repository/repository-name</code>.</p>"""
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry that contains the repository.</p>"""
    repository_name: NotRequired["capo_ecr.types.repository_name.RepositoryName"]
    """<p>The name of the repository.</p>"""
    repository_uri: NotRequired["capo_ecr.types.url.Url"]
    """<p>The URI for the repository. You can use this URI for container image <code>push</code> and <code>pull</code> operations.</p>"""
    created_at: NotRequired["capo_ecr.types.creation_timestamp.CreationTimestamp"]
    """<p>The date and time, in JavaScript date format, when the repository was created.</p>"""
    image_tag_mutability: NotRequired[
        "capo_ecr.types.image_tag_mutability.ImageTagMutability"
    ]
    """<p>The tag mutability setting for the repository.</p>"""
    image_tag_mutability_exclusion_filters: NotRequired[
        "capo_ecr.types.image_tag_mutability_exclusion_filters.ImageTagMutabilityExclusionFilters"
    ]
    """<p>A list of filters that specify which image tags are excluded from the repository's image tag mutability setting.</p>"""
    image_scanning_configuration: NotRequired[
        "capo_ecr.types.image_scanning_configuration.ImageScanningConfiguration"
    ]
    encryption_configuration: NotRequired[
        "capo_ecr.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Repository) -> dict:
    out: dict = {}
    if "repository_arn" in value:
        out["repositoryArn"] = value["repository_arn"]
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "repository_uri" in value:
        out["repositoryUri"] = value["repository_uri"]
    if "created_at" in value:
        import capo_ecr.types.creation_timestamp

        out["createdAt"] = capo_ecr.types.creation_timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "image_tag_mutability" in value:
        import capo_ecr.types.image_tag_mutability

        out["imageTagMutability"] = (
            capo_ecr.types.image_tag_mutability.serialize_aws_json_1_1(
                value["image_tag_mutability"]
            )
        )
    if "image_tag_mutability_exclusion_filters" in value:
        import capo_ecr.types.image_tag_mutability_exclusion_filters

        out["imageTagMutabilityExclusionFilters"] = (
            capo_ecr.types.image_tag_mutability_exclusion_filters.serialize_aws_json_1_1(
                value["image_tag_mutability_exclusion_filters"]
            )
        )
    if "image_scanning_configuration" in value:
        import capo_ecr.types.image_scanning_configuration

        out["imageScanningConfiguration"] = (
            capo_ecr.types.image_scanning_configuration.serialize_aws_json_1_1(
                value["image_scanning_configuration"]
            )
        )
    if "encryption_configuration" in value:
        import capo_ecr.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_ecr.types.encryption_configuration.serialize_aws_json_1_1(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Repository:
    out: Repository = {}  # type: ignore[typeddict-item]
    if data.get("repositoryArn") is not None:
        out["repository_arn"] = data["repositoryArn"]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    if data.get("repositoryUri") is not None:
        out["repository_uri"] = data["repositoryUri"]
    if data.get("createdAt") is not None:
        import capo_ecr.types.creation_timestamp

        out["created_at"] = capo_ecr.types.creation_timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if data.get("imageTagMutability") is not None:
        import capo_ecr.types.image_tag_mutability

        out["image_tag_mutability"] = (
            capo_ecr.types.image_tag_mutability.deserialize_aws_json_1_1(
                data["imageTagMutability"]
            )
        )
    if data.get("imageTagMutabilityExclusionFilters") is not None:
        import capo_ecr.types.image_tag_mutability_exclusion_filters

        out["image_tag_mutability_exclusion_filters"] = (
            capo_ecr.types.image_tag_mutability_exclusion_filters.deserialize_aws_json_1_1(
                data["imageTagMutabilityExclusionFilters"]
            )
        )
    if data.get("imageScanningConfiguration") is not None:
        import capo_ecr.types.image_scanning_configuration

        out["image_scanning_configuration"] = (
            capo_ecr.types.image_scanning_configuration.deserialize_aws_json_1_1(
                data["imageScanningConfiguration"]
            )
        )
    if data.get("encryptionConfiguration") is not None:
        import capo_ecr.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_ecr.types.encryption_configuration.deserialize_aws_json_1_1(
                data["encryptionConfiguration"]
            )
        )
    return out
