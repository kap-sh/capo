"""Generated from Smithy shape ``com.amazonaws.iam#SetDefaultPolicyVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.policy_version_id_type


class SetDefaultPolicyVersionRequest(TypedDict, closed=True):
    policy_arn: "capo_iam.types.arn_type.arnType"
    """<p>The Amazon Resource Name (ARN) of the IAM policy whose default version you want to set.</p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    version_id: "capo_iam.types.policy_version_id_type.policyVersionIdType"
    """<p>The version of the policy to set as the default (operative) version.</p> <p>For more information about managed policy versions, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html">Versioning for managed policies</a> in the <i>IAM User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetDefaultPolicyVersionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}PolicyArn", str(value["policy_arn"])))
    pairs.append((f"{key_prefix}VersionId", str(value["version_id"])))


def deserialize_query(el: Element) -> SetDefaultPolicyVersionRequest:
    out: SetDefaultPolicyVersionRequest = {}  # type: ignore[typeddict-item]
    child_policy_arn = el.find("PolicyArn")
    if child_policy_arn is not None:
        out["policy_arn"] = str(child_policy_arn.text or "")
    else:
        raise DeserializationError("SetDefaultPolicyVersionRequest.policy_arn required")
    child_version_id = el.find("VersionId")
    if child_version_id is not None:
        out["version_id"] = str(child_version_id.text or "")
    else:
        raise DeserializationError("SetDefaultPolicyVersionRequest.version_id required")
    return out
