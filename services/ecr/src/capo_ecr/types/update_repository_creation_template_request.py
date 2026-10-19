"""Generated from Smithy shape ``com.amazonaws.ecr#UpdateRepositoryCreationTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.custom_role_arn
    import capo_ecr.types.encryption_configuration_for_repository_creation_template
    import capo_ecr.types.image_tag_mutability
    import capo_ecr.types.image_tag_mutability_exclusion_filters
    import capo_ecr.types.lifecycle_policy_text_for_repository_creation_template
    import capo_ecr.types.prefix
    import capo_ecr.types.rct_applied_for_list
    import capo_ecr.types.repository_policy_text
    import capo_ecr.types.repository_template_description
    import capo_ecr.types.tag_list


class UpdateRepositoryCreationTemplateRequest(TypedDict, closed=True):
    prefix: "capo_ecr.types.prefix.Prefix"
    """<p>The repository namespace prefix that matches an existing repository creation template in the registry. All repositories created using this namespace prefix will have the settings defined in this template applied. For example, a prefix of <code>prod</code> would apply to all repositories beginning with <code>prod/</code>. This includes a repository named <code>prod/team1</code> as well as a repository named <code>prod/repository1</code>.</p> <p>To apply a template to all repositories in your registry that don't have an associated creation template, you can use <code>ROOT</code> as the prefix.</p>"""
    description: NotRequired[
        "capo_ecr.types.repository_template_description.RepositoryTemplateDescription"
    ]
    """<p>A description for the repository creation template.</p>"""
    encryption_configuration: NotRequired[
        "capo_ecr.types.encryption_configuration_for_repository_creation_template.EncryptionConfigurationForRepositoryCreationTemplate"
    ]
    resource_tags: NotRequired["capo_ecr.types.tag_list.TagList"]
    """<p>The metadata to apply to the repository to help you categorize and organize. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>"""
    image_tag_mutability: NotRequired[
        "capo_ecr.types.image_tag_mutability.ImageTagMutability"
    ]
    """<p>Updates the tag mutability setting for the repository. If this parameter is omitted, the default setting of <code>MUTABLE</code> will be used which will allow image tags to be overwritten. If <code>IMMUTABLE</code> is specified, all image tags within the repository will be immutable which will prevent them from being overwritten.</p>"""
    image_tag_mutability_exclusion_filters: NotRequired[
        "capo_ecr.types.image_tag_mutability_exclusion_filters.ImageTagMutabilityExclusionFilters"
    ]
    """<p>A list of filters that specify which image tags should be excluded from the repository creation template's image tag mutability setting.</p>"""
    repository_policy: NotRequired[
        "capo_ecr.types.repository_policy_text.RepositoryPolicyText"
    ]
    """<p>Updates the repository policy created using the template. A repository policy is a permissions policy associated with a repository to control access permissions. </p>"""
    lifecycle_policy: NotRequired[
        "capo_ecr.types.lifecycle_policy_text_for_repository_creation_template.LifecyclePolicyTextForRepositoryCreationTemplate"
    ]
    """<p>Updates the lifecycle policy associated with the specified repository creation template.</p>"""
    applied_for: NotRequired["capo_ecr.types.rct_applied_for_list.RCTAppliedForList"]
    """<p>Updates the list of enumerable strings representing the Amazon ECR repository creation scenarios that this template will apply towards. The supported scenarios are <code>PULL_THROUGH_CACHE</code>, <code>REPLICATION</code>, and <code>CREATE_ON_PUSH</code> </p>"""
    custom_role_arn: NotRequired["capo_ecr.types.custom_role_arn.CustomRoleArn"]
    """<p>The ARN of the role to be assumed by Amazon ECR. This role must be in the same account as the registry that you are configuring. Amazon ECR will assume your supplied role when the customRoleArn is specified. When this field isn't specified, Amazon ECR will use the service-linked role for the repository creation template.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRepositoryCreationTemplateRequest) -> dict:
    out: dict = {}
    out["prefix"] = value["prefix"]
    if "description" in value:
        out["description"] = value["description"]
    if "encryption_configuration" in value:
        import capo_ecr.types.encryption_configuration_for_repository_creation_template

        out["encryptionConfiguration"] = (
            capo_ecr.types.encryption_configuration_for_repository_creation_template.serialize_aws_json_1_1(
                value["encryption_configuration"]
            )
        )
    if "resource_tags" in value:
        import capo_ecr.types.tag_list

        out["resourceTags"] = capo_ecr.types.tag_list.serialize_aws_json_1_1(
            value["resource_tags"]
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
    if "repository_policy" in value:
        out["repositoryPolicy"] = value["repository_policy"]
    if "lifecycle_policy" in value:
        out["lifecyclePolicy"] = value["lifecycle_policy"]
    if "applied_for" in value:
        import capo_ecr.types.rct_applied_for_list

        out["appliedFor"] = capo_ecr.types.rct_applied_for_list.serialize_aws_json_1_1(
            value["applied_for"]
        )
    if "custom_role_arn" in value:
        out["customRoleArn"] = value["custom_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRepositoryCreationTemplateRequest:
    out: UpdateRepositoryCreationTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    else:
        out["prefix"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("encryptionConfiguration") is not None:
        import capo_ecr.types.encryption_configuration_for_repository_creation_template

        out["encryption_configuration"] = (
            capo_ecr.types.encryption_configuration_for_repository_creation_template.deserialize_aws_json_1_1(
                data["encryptionConfiguration"]
            )
        )
    if data.get("resourceTags") is not None:
        import capo_ecr.types.tag_list

        out["resource_tags"] = capo_ecr.types.tag_list.deserialize_aws_json_1_1(
            data["resourceTags"]
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
    if data.get("repositoryPolicy") is not None:
        out["repository_policy"] = data["repositoryPolicy"]
    if data.get("lifecyclePolicy") is not None:
        out["lifecycle_policy"] = data["lifecyclePolicy"]
    if data.get("appliedFor") is not None:
        import capo_ecr.types.rct_applied_for_list

        out["applied_for"] = (
            capo_ecr.types.rct_applied_for_list.deserialize_aws_json_1_1(
                data["appliedFor"]
            )
        )
    if data.get("customRoleArn") is not None:
        out["custom_role_arn"] = data["customRoleArn"]
    return out
