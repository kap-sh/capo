"""Generated from Smithy shape ``com.amazonaws.ecr#PutImageTagMutabilityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.image_tag_mutability
    import capo_ecr.types.image_tag_mutability_exclusion_filters
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name


class PutImageTagMutabilityRequest(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry that contains the repository in which to update the image tag mutability settings. If you do not specify a registry, the default registry is assumed.</p>"""
    repository_name: "capo_ecr.types.repository_name.RepositoryName"
    """<p>The name of the repository in which to update the image tag mutability settings.</p>"""
    image_tag_mutability: "capo_ecr.types.image_tag_mutability.ImageTagMutability"
    """<p>The tag mutability setting for the repository. If <code>MUTABLE</code> is specified, image tags can be overwritten. If <code>IMMUTABLE</code> is specified, all image tags within the repository will be immutable which will prevent them from being overwritten.</p>"""
    image_tag_mutability_exclusion_filters: NotRequired[
        "capo_ecr.types.image_tag_mutability_exclusion_filters.ImageTagMutabilityExclusionFilters"
    ]
    """<p>A list of filters that specify which image tags should be excluded from the image tag mutability setting being applied.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutImageTagMutabilityRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> PutImageTagMutabilityRequest:
    out: PutImageTagMutabilityRequest = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("imageTagMutability") is not None:
        import capo_ecr.types.image_tag_mutability

        out["image_tag_mutability"] = (
            capo_ecr.types.image_tag_mutability.deserialize_aws_json_1_1(
                data["imageTagMutability"]
            )
        )
    else:
        import typing

        out["image_tag_mutability"] = typing.cast(
            "capo_ecr.types.image_tag_mutability.ImageTagMutability", ""
        )
    if data.get("imageTagMutabilityExclusionFilters") is not None:
        import capo_ecr.types.image_tag_mutability_exclusion_filters

        out["image_tag_mutability_exclusion_filters"] = (
            capo_ecr.types.image_tag_mutability_exclusion_filters.deserialize_aws_json_1_1(
                data["imageTagMutabilityExclusionFilters"]
            )
        )
    return out
