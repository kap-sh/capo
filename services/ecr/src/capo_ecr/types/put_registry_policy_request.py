"""Generated from Smithy shape ``com.amazonaws.ecr#PutRegistryPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecr.types.registry_policy_text


class PutRegistryPolicyRequest(TypedDict, closed=True):
    policy_text: "capo_ecr.types.registry_policy_text.RegistryPolicyText"
    """<p>The JSON policy text to apply to your registry. The policy text follows the same format as IAM policy text. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-permissions.html">Registry permissions</a> in the <i>Amazon Elastic Container Registry User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRegistryPolicyRequest) -> dict:
    out: dict = {}
    out["policyText"] = value["policy_text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRegistryPolicyRequest:
    out: PutRegistryPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("policyText") is not None:
        out["policy_text"] = data["policyText"]
    else:
        raise DeserializationError("PutRegistryPolicyRequest.policy_text required")
    return out
