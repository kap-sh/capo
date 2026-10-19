"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#CheckNoNewAccessRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.access_check_policy_document
    import capo_accessanalyzer.types.access_check_policy_type


class CheckNoNewAccessRequest(TypedDict, closed=True):
    new_policy_document: "capo_accessanalyzer.types.access_check_policy_document.AccessCheckPolicyDocument"
    """<p>The JSON policy document to use as the content for the updated policy.</p>"""
    existing_policy_document: "capo_accessanalyzer.types.access_check_policy_document.AccessCheckPolicyDocument"
    """<p>The JSON policy document to use as the content for the existing policy.</p>"""
    policy_type: (
        "capo_accessanalyzer.types.access_check_policy_type.AccessCheckPolicyType"
    )
    """<p>The type of policy to compare. Identity policies grant permissions to IAM principals. Identity policies include managed and inline policies for IAM roles, users, and groups.</p> <p>Resource policies grant permissions on Amazon Web Services resources. Resource policies include trust policies for IAM roles and bucket policies for Amazon S3 buckets. You can provide a generic input such as identity policy or resource policy or a specific input such as managed policy or Amazon S3 bucket policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CheckNoNewAccessRequest) -> dict:
    out: dict = {}
    out["newPolicyDocument"] = value["new_policy_document"]
    out["existingPolicyDocument"] = value["existing_policy_document"]
    out["policyType"] = value["policy_type"]
    return out


def deserialize_json(data: dict) -> CheckNoNewAccessRequest:
    out: CheckNoNewAccessRequest = {}  # type: ignore[typeddict-item]
    if data.get("newPolicyDocument") is not None:
        out["new_policy_document"] = data["newPolicyDocument"]
    else:
        out["new_policy_document"] = ""
    if data.get("existingPolicyDocument") is not None:
        out["existing_policy_document"] = data["existingPolicyDocument"]
    else:
        out["existing_policy_document"] = ""
    if data.get("policyType") is not None:
        out["policy_type"] = data["policyType"]
    else:
        out["policy_type"] = ""
    return out


def redact_sensitive(value: CheckNoNewAccessRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "new_policy_document" in value:
        out["new_policy_document"] = "*** Sensitive Data Redacted ***"
    if "existing_policy_document" in value:
        out["existing_policy_document"] = "*** Sensitive Data Redacted ***"
    return out
