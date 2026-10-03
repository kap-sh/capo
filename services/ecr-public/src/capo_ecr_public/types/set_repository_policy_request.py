"""Generated from Smithy shape ``com.amazonaws.ecrpublic#SetRepositoryPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecr_public.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecr_public.types.force_flag
    import capo_ecr_public.types.registry_id
    import capo_ecr_public.types.repository_name
    import capo_ecr_public.types.repository_policy_text


class SetRepositoryPolicyRequest(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr_public.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID that's associated with the registry that contains the repository. If you do not specify a registry, the default public registry is assumed.</p>"""
    repository_name: "capo_ecr_public.types.repository_name.RepositoryName"
    """<p>The name of the repository to receive the policy.</p>"""
    policy_text: "capo_ecr_public.types.repository_policy_text.RepositoryPolicyText"
    """<p>The JSON repository policy text to apply to the repository. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policy-examples.html">Amazon ECR Repository Policies</a> in the <i>Amazon Elastic Container Registry User Guide</i>.</p>"""
    force: "capo_ecr_public.types.force_flag.ForceFlag"
    """<p>If the policy that you want to set on a repository policy would prevent you from setting another policy in the future, you must force the <a>SetRepositoryPolicy</a> operation. This prevents accidental repository lockouts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetRepositoryPolicyRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    out["policyText"] = value["policy_text"]
    out["force"] = value.get("force", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> SetRepositoryPolicyRequest:
    out: SetRepositoryPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "SetRepositoryPolicyRequest.repository_name required"
        )
    if data.get("policyText") is not None:
        out["policy_text"] = data["policyText"]
    else:
        raise DeserializationError("SetRepositoryPolicyRequest.policy_text required")
    if data.get("force") is not None:
        out["force"] = data["force"]
    else:
        out["force"] = False
    return out
