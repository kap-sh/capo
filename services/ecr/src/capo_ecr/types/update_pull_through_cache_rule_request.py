"""Generated from Smithy shape ``com.amazonaws.ecr#UpdatePullThroughCacheRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.credential_arn
    import capo_ecr.types.custom_role_arn
    import capo_ecr.types.pull_through_cache_rule_repository_prefix
    import capo_ecr.types.registry_id


class UpdatePullThroughCacheRuleRequest(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry associated with the pull through cache rule. If you do not specify a registry, the default registry is assumed.</p>"""
    ecr_repository_prefix: "capo_ecr.types.pull_through_cache_rule_repository_prefix.PullThroughCacheRuleRepositoryPrefix"
    """<p>The repository name prefix to use when caching images from the source registry.</p>"""
    credential_arn: NotRequired["capo_ecr.types.credential_arn.CredentialArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret that identifies the credentials to authenticate to the upstream registry.</p>"""
    custom_role_arn: NotRequired["capo_ecr.types.custom_role_arn.CustomRoleArn"]
    """<p>Amazon Resource Name (ARN) of the IAM role to be assumed by Amazon ECR to authenticate to the ECR upstream registry. This role must be in the same account as the registry that you are configuring.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePullThroughCacheRuleRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["ecrRepositoryPrefix"] = value["ecr_repository_prefix"]
    if "credential_arn" in value:
        out["credentialArn"] = value["credential_arn"]
    if "custom_role_arn" in value:
        out["customRoleArn"] = value["custom_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePullThroughCacheRuleRequest:
    out: UpdatePullThroughCacheRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("ecrRepositoryPrefix") is not None:
        out["ecr_repository_prefix"] = data["ecrRepositoryPrefix"]
    else:
        out["ecr_repository_prefix"] = ""
    if data.get("credentialArn") is not None:
        out["credential_arn"] = data["credentialArn"]
    if data.get("customRoleArn") is not None:
        out["custom_role_arn"] = data["customRoleArn"]
    return out
