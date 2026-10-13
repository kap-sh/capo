"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#CheckNoPublicAccessRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.access_check_policy_document
    import capo_accessanalyzer.types.access_check_resource_type


class CheckNoPublicAccessRequest(TypedDict, closed=True):
    policy_document: "capo_accessanalyzer.types.access_check_policy_document.AccessCheckPolicyDocument"
    """<p>The JSON policy document to evaluate for public access.</p>"""
    resource_type: (
        "capo_accessanalyzer.types.access_check_resource_type.AccessCheckResourceType"
    )
    """<p>The type of resource to evaluate for public access. For example, to check for public access to Amazon S3 buckets, you can choose <code>AWS::S3::Bucket</code> for the resource type.</p> <p>For resource types not supported as valid values, IAM Access Analyzer will return an error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CheckNoPublicAccessRequest) -> dict:
    out: dict = {}
    out["policyDocument"] = value["policy_document"]
    out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> CheckNoPublicAccessRequest:
    out: CheckNoPublicAccessRequest = {}  # type: ignore[typeddict-item]
    if data.get("policyDocument") is not None:
        out["policy_document"] = data["policyDocument"]
    else:
        raise DeserializationError(
            "CheckNoPublicAccessRequest.policy_document required"
        )
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("CheckNoPublicAccessRequest.resource_type required")
    return out


def redact_sensitive(value: CheckNoPublicAccessRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "policy_document" in value:
        out["policy_document"] = "*** Sensitive Data Redacted ***"
    return out
