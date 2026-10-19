"""Generated from Smithy shape ``com.amazonaws.ecr#ValidatePullThroughCacheRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.pull_through_cache_rule_repository_prefix
    import capo_ecr.types.registry_id


class ValidatePullThroughCacheRuleRequest(TypedDict, closed=True):
    ecr_repository_prefix: "capo_ecr.types.pull_through_cache_rule_repository_prefix.PullThroughCacheRuleRepositoryPrefix"
    """<p>The repository name prefix associated with the pull through cache rule.</p>"""
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the pull through cache rule. If you do not specify a registry, the default registry is assumed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidatePullThroughCacheRuleRequest) -> dict:
    out: dict = {}
    out["ecrRepositoryPrefix"] = value["ecr_repository_prefix"]
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidatePullThroughCacheRuleRequest:
    out: ValidatePullThroughCacheRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("ecrRepositoryPrefix") is not None:
        out["ecr_repository_prefix"] = data["ecrRepositoryPrefix"]
    else:
        out["ecr_repository_prefix"] = ""
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    return out
