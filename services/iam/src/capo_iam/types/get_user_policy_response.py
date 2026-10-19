"""Generated from Smithy shape ``com.amazonaws.iam#GetUserPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.existing_user_name_type
    import capo_iam.types.policy_document_type
    import capo_iam.types.policy_name_type


class GetUserPolicyResponse(TypedDict, closed=True):
    user_name: "capo_iam.types.existing_user_name_type.existingUserNameType"
    """<p>The user the policy is associated with.</p>"""
    policy_name: "capo_iam.types.policy_name_type.policyNameType"
    """<p>The name of the policy.</p>"""
    policy_document: "capo_iam.types.policy_document_type.policyDocumentType"
    """<p>The policy document.</p> <p>IAM stores policies in JSON format. However, resources that were created using CloudFormation templates can be formatted in YAML. CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetUserPolicyResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}UserName", str(value["user_name"])))
    pairs.append((f"{key_prefix}PolicyName", str(value["policy_name"])))
    pairs.append((f"{key_prefix}PolicyDocument", str(value["policy_document"])))


def deserialize_query(el: Element) -> GetUserPolicyResponse:
    out: GetUserPolicyResponse = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        out["user_name"] = ""
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    else:
        out["policy_name"] = ""
    child_policy_document = el.find("PolicyDocument")
    if child_policy_document is not None:
        out["policy_document"] = str(child_policy_document.text or "")
    else:
        out["policy_document"] = ""
    return out
