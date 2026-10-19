"""Generated from Smithy shape ``com.amazonaws.ecr#StartLifecyclePolicyPreviewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.lifecycle_policy_text
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name


class StartLifecyclePolicyPreviewRequest(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.</p>"""
    repository_name: "capo_ecr.types.repository_name.RepositoryName"
    """<p>The name of the repository to be evaluated.</p>"""
    lifecycle_policy_text: NotRequired[
        "capo_ecr.types.lifecycle_policy_text.LifecyclePolicyText"
    ]
    """<p>The policy to be evaluated against. If you do not specify a policy, the current policy for the repository is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartLifecyclePolicyPreviewRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    if "lifecycle_policy_text" in value:
        out["lifecyclePolicyText"] = value["lifecycle_policy_text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartLifecyclePolicyPreviewRequest:
    out: StartLifecyclePolicyPreviewRequest = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("lifecyclePolicyText") is not None:
        out["lifecycle_policy_text"] = data["lifecyclePolicyText"]
    return out
