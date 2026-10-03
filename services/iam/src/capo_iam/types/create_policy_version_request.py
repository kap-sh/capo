"""Generated from Smithy shape ``com.amazonaws.iam#CreatePolicyVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.boolean_type
    import capo_iam.types.policy_document_type


class CreatePolicyVersionRequest(TypedDict, closed=True):
    policy_arn: "capo_iam.types.arn_type.arnType"
    """<p>The Amazon Resource Name (ARN) of the IAM policy to which you want to add a new version.</p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    policy_document: "capo_iam.types.policy_document_type.policyDocumentType"
    r"""<p>The JSON policy document that you want to use as the content for this new version of the policy.</p> <p>You must provide policies in JSON format in IAM. However, for CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.</p> <p>The maximum length of the policy document that you can pass in this operation, including whitespace, is listed below. To view the maximum character counts of a managed policy with no whitespaces, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-entity-length">IAM and STS character quotas</a>.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> used to validate this parameter is a string of characters consisting of the following:</p> <ul> <li> <p>Any printable ASCII character ranging from the space character (<code>\u0020</code>) through the end of the ASCII character range</p> </li> <li> <p>The printable characters in the Basic Latin and Latin-1 Supplement character set (through <code>\u00FF</code>)</p> </li> <li> <p>The special characters tab (<code>\u0009</code>), line feed (<code>\u000A</code>), and carriage return (<code>\u000D</code>)</p> </li> </ul>"""
    set_as_default: "capo_iam.types.boolean_type.booleanType"
    """<p>Specifies whether to set this version as the policy's default version.</p> <p>When this parameter is <code>true</code>, the new policy version becomes the operative version. That is, it becomes the version that is in effect for the IAM users, groups, and roles that the policy is attached to.</p> <p>For more information about managed policy versions, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html">Versioning for managed policies</a> in the <i>IAM User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreatePolicyVersionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}PolicyArn", str(value["policy_arn"])))
    pairs.append((f"{key_prefix}PolicyDocument", str(value["policy_document"])))
    pairs.append(
        (
            f"{key_prefix}SetAsDefault",
            "true" if value.get("set_as_default", False) else "false",
        )
    )


def deserialize_query(el: Element) -> CreatePolicyVersionRequest:
    out: CreatePolicyVersionRequest = {}  # type: ignore[typeddict-item]
    child_policy_arn = el.find("PolicyArn")
    if child_policy_arn is not None:
        out["policy_arn"] = str(child_policy_arn.text or "")
    else:
        raise DeserializationError("CreatePolicyVersionRequest.policy_arn required")
    child_policy_document = el.find("PolicyDocument")
    if child_policy_document is not None:
        out["policy_document"] = str(child_policy_document.text or "")
    else:
        raise DeserializationError(
            "CreatePolicyVersionRequest.policy_document required"
        )
    child_set_as_default = el.find("SetAsDefault")
    if child_set_as_default is not None:
        out["set_as_default"] = (child_set_as_default.text or "").lower() == "true"
    else:
        out["set_as_default"] = False
    return out
