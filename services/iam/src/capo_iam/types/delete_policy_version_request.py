"""Generated from Smithy shape ``com.amazonaws.iam#DeletePolicyVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.policy_version_id_type


class DeletePolicyVersionRequest(TypedDict, closed=True):
    policy_arn: "capo_iam.types.arn_type.arnType"
    """<p>The Amazon Resource Name (ARN) of the IAM policy from which you want to delete a version.</p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    version_id: "capo_iam.types.policy_version_id_type.policyVersionIdType"
    """<p>The policy version to delete.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters that consists of the lowercase letter 'v' followed by one or two digits, and optionally followed by a period '.' and a string of letters and digits.</p> <p>For more information about managed policy versions, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html">Versioning for managed policies</a> in the <i>IAM User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeletePolicyVersionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}PolicyArn", str(value["policy_arn"])))
    pairs.append((f"{key_prefix}VersionId", str(value["version_id"])))


def deserialize_query(el: Element) -> DeletePolicyVersionRequest:
    out: DeletePolicyVersionRequest = {}  # type: ignore[typeddict-item]
    child_policy_arn = el.find("PolicyArn")
    if child_policy_arn is not None:
        out["policy_arn"] = str(child_policy_arn.text or "")
    else:
        raise DeserializationError("DeletePolicyVersionRequest.policy_arn required")
    child_version_id = el.find("VersionId")
    if child_version_id is not None:
        out["version_id"] = str(child_version_id.text or "")
    else:
        raise DeserializationError("DeletePolicyVersionRequest.version_id required")
    return out
