"""Generated from Smithy shape ``com.amazonaws.ecr#CreatePullThroughCacheRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.credential_arn
    import capo_ecr.types.custom_role_arn
    import capo_ecr.types.pull_through_cache_rule_repository_prefix
    import capo_ecr.types.registry_id
    import capo_ecr.types.upstream_registry
    import capo_ecr.types.url


class CreatePullThroughCacheRuleRequest(TypedDict, closed=True):
    ecr_repository_prefix: "capo_ecr.types.pull_through_cache_rule_repository_prefix.PullThroughCacheRuleRepositoryPrefix"
    """<p>The repository name prefix to use when caching images from the source registry.</p> <important> <p>There is always an assumed <code>/</code> applied to the end of the prefix. If you specify <code>ecr-public</code> as the prefix, Amazon ECR treats that as <code>ecr-public/</code>.</p> </important>"""
    upstream_registry_url: "capo_ecr.types.url.Url"
    """<p>The registry URL of the upstream public registry to use as the source for the pull through cache rule. The following is the syntax to use for each supported upstream registry.</p> <ul> <li> <p>Amazon ECR (<code>ecr</code>) – <code><accountId>.dkr.ecr.<region>.amazonaws.com</code> </p> </li> <li> <p>Amazon ECR Public (<code>ecr-public</code>) – <code>public.ecr.aws</code> </p> </li> <li> <p>Docker Hub (<code>docker-hub</code>) – <code>registry-1.docker.io</code> </p> </li> <li> <p>GitHub Container Registry (<code>github-container-registry</code>) – <code>ghcr.io</code> </p> </li> <li> <p>GitLab Container Registry (<code>gitlab-container-registry</code>) – <code>registry.gitlab.com</code> </p> </li> <li> <p>Kubernetes (<code>k8s</code>) – <code>registry.k8s.io</code> </p> </li> <li> <p>Microsoft Azure Container Registry (<code>azure-container-registry</code>) – <code><custom>.azurecr.io</code> </p> </li> <li> <p>Quay (<code>quay</code>) – <code>quay.io</code> </p> </li> </ul>"""
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry to create the pull through cache rule for. If you do not specify a registry, the default registry is assumed.</p>"""
    upstream_registry: NotRequired["capo_ecr.types.upstream_registry.UpstreamRegistry"]
    """<p>The name of the upstream registry.</p>"""
    credential_arn: NotRequired["capo_ecr.types.credential_arn.CredentialArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret that identifies the credentials to authenticate to the upstream registry.</p>"""
    custom_role_arn: NotRequired["capo_ecr.types.custom_role_arn.CustomRoleArn"]
    """<p>Amazon Resource Name (ARN) of the IAM role to be assumed by Amazon ECR to authenticate to the ECR upstream registry. This role must be in the same account as the registry that you are configuring.</p>"""
    upstream_repository_prefix: NotRequired[
        "capo_ecr.types.pull_through_cache_rule_repository_prefix.PullThroughCacheRuleRepositoryPrefix"
    ]
    """<p>The repository name prefix of the upstream registry to match with the upstream repository name. When this field isn't specified, Amazon ECR will use the <code>ROOT</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePullThroughCacheRuleRequest) -> dict:
    out: dict = {}
    out["ecrRepositoryPrefix"] = value["ecr_repository_prefix"]
    out["upstreamRegistryUrl"] = value["upstream_registry_url"]
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "upstream_registry" in value:
        import capo_ecr.types.upstream_registry

        out["upstreamRegistry"] = (
            capo_ecr.types.upstream_registry.serialize_aws_json_1_1(
                value["upstream_registry"]
            )
        )
    if "credential_arn" in value:
        out["credentialArn"] = value["credential_arn"]
    if "custom_role_arn" in value:
        out["customRoleArn"] = value["custom_role_arn"]
    if "upstream_repository_prefix" in value:
        out["upstreamRepositoryPrefix"] = value["upstream_repository_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePullThroughCacheRuleRequest:
    out: CreatePullThroughCacheRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("ecrRepositoryPrefix") is not None:
        out["ecr_repository_prefix"] = data["ecrRepositoryPrefix"]
    else:
        out["ecr_repository_prefix"] = ""
    if data.get("upstreamRegistryUrl") is not None:
        out["upstream_registry_url"] = data["upstreamRegistryUrl"]
    else:
        out["upstream_registry_url"] = ""
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("upstreamRegistry") is not None:
        import capo_ecr.types.upstream_registry

        out["upstream_registry"] = (
            capo_ecr.types.upstream_registry.deserialize_aws_json_1_1(
                data["upstreamRegistry"]
            )
        )
    if data.get("credentialArn") is not None:
        out["credential_arn"] = data["credentialArn"]
    if data.get("customRoleArn") is not None:
        out["custom_role_arn"] = data["customRoleArn"]
    if data.get("upstreamRepositoryPrefix") is not None:
        out["upstream_repository_prefix"] = data["upstreamRepositoryPrefix"]
    return out
