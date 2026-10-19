"""Generated from Smithy shape ``com.amazonaws.ecr#CreateRepositoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.encryption_configuration
    import capo_ecr.types.image_scanning_configuration
    import capo_ecr.types.image_tag_mutability
    import capo_ecr.types.image_tag_mutability_exclusion_filters
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name
    import capo_ecr.types.tag_list


class CreateRepositoryRequest(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry to create the repository. If you do not specify a registry, the default registry is assumed.</p>"""
    repository_name: "capo_ecr.types.repository_name.RepositoryName"
    """<p>The name to use for the repository. The repository name may be specified on its own (such as <code>nginx-web-app</code>) or it can be prepended with a namespace to group the repository into a category (such as <code>project-a/nginx-web-app</code>).</p> <p>The repository name must start with a letter and can only contain lowercase letters, numbers, hyphens, underscores, and forward slashes.</p>"""
    tags: NotRequired["capo_ecr.types.tag_list.TagList"]
    """<p>The metadata that you apply to the repository to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>"""
    image_tag_mutability: NotRequired[
        "capo_ecr.types.image_tag_mutability.ImageTagMutability"
    ]
    """<p>The tag mutability setting for the repository. If this parameter is omitted, the default setting of <code>MUTABLE</code> will be used which will allow image tags to be overwritten. If <code>IMMUTABLE</code> is specified, all image tags within the repository will be immutable which will prevent them from being overwritten.</p>"""
    image_tag_mutability_exclusion_filters: NotRequired[
        "capo_ecr.types.image_tag_mutability_exclusion_filters.ImageTagMutabilityExclusionFilters"
    ]
    """<p>A list of filters that specify which image tags should be excluded from the repository's image tag mutability setting.</p>"""
    image_scanning_configuration: NotRequired[
        "capo_ecr.types.image_scanning_configuration.ImageScanningConfiguration"
    ]
    """<important> <p>The <code>imageScanningConfiguration</code> parameter is being deprecated, in favor of specifying the image scanning configuration at the registry level. For more information, see <code>PutRegistryScanningConfiguration</code>.</p> </important> <p>The image scanning configuration for the repository. This determines whether images are scanned for known vulnerabilities after being pushed to the repository.</p>"""
    encryption_configuration: NotRequired[
        "capo_ecr.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRepositoryRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    if "tags" in value:
        import capo_ecr.types.tag_list

        out["tags"] = capo_ecr.types.tag_list.serialize_aws_json_1_1(value["tags"])
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


def deserialize_aws_json_1_1(data: dict) -> CreateRepositoryRequest:
    out: CreateRepositoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("tags") is not None:
        import capo_ecr.types.tag_list

        out["tags"] = capo_ecr.types.tag_list.deserialize_aws_json_1_1(data["tags"])
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
