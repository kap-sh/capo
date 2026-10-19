"""Generated from Smithy shape ``com.amazonaws.ecr#PutLifecyclePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.lifecycle_policy_text
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name


class PutLifecyclePolicyRequest(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.</p>"""
    repository_name: "capo_ecr.types.repository_name.RepositoryName"
    """<p>The name of the repository to receive the policy.</p>"""
    lifecycle_policy_text: "capo_ecr.types.lifecycle_policy_text.LifecyclePolicyText"
    """<p>The JSON repository policy text to apply to the repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutLifecyclePolicyRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    out["lifecyclePolicyText"] = value["lifecycle_policy_text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutLifecyclePolicyRequest:
    out: PutLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("lifecyclePolicyText") is not None:
        out["lifecycle_policy_text"] = data["lifecyclePolicyText"]
    else:
        out["lifecycle_policy_text"] = ""
    return out
