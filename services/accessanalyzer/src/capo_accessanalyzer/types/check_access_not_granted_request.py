"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#CheckAccessNotGrantedRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.access_check_policy_document
    import capo_accessanalyzer.types.access_check_policy_type
    import capo_accessanalyzer.types.access_list


class CheckAccessNotGrantedRequest(TypedDict, closed=True):
    policy_document: "capo_accessanalyzer.types.access_check_policy_document.AccessCheckPolicyDocument"
    """<p>The JSON policy document to use as the content for the policy.</p>"""
    access: "capo_accessanalyzer.types.access_list.AccessList"
    """<p>An access object containing the permissions that shouldn't be granted by the specified policy. If only actions are specified, IAM Access Analyzer checks for access to peform at least one of the actions on any resource in the policy. If only resources are specified, then IAM Access Analyzer checks for access to perform any action on at least one of the resources. If both actions and resources are specified, IAM Access Analyzer checks for access to perform at least one of the specified actions on at least one of the specified resources.</p>"""
    policy_type: (
        "capo_accessanalyzer.types.access_check_policy_type.AccessCheckPolicyType"
    )
    """<p>The type of policy. Identity policies grant permissions to IAM principals. Identity policies include managed and inline policies for IAM roles, users, and groups.</p> <p>Resource policies grant permissions on Amazon Web Services resources. Resource policies include trust policies for IAM roles and bucket policies for Amazon S3 buckets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CheckAccessNotGrantedRequest) -> dict:
    out: dict = {}
    out["policyDocument"] = value["policy_document"]
    import capo_accessanalyzer.types.access_list

    out["access"] = capo_accessanalyzer.types.access_list.serialize_json(
        value["access"]
    )
    out["policyType"] = value["policy_type"]
    return out


def deserialize_json(data: dict) -> CheckAccessNotGrantedRequest:
    out: CheckAccessNotGrantedRequest = {}  # type: ignore[typeddict-item]
    if data.get("policyDocument") is not None:
        out["policy_document"] = data["policyDocument"]
    else:
        raise DeserializationError(
            "CheckAccessNotGrantedRequest.policy_document required"
        )
    if data.get("access") is not None:
        import capo_accessanalyzer.types.access_list

        out["access"] = capo_accessanalyzer.types.access_list.deserialize_json(
            data["access"]
        )
    else:
        raise DeserializationError("CheckAccessNotGrantedRequest.access required")
    if data.get("policyType") is not None:
        out["policy_type"] = data["policyType"]
    else:
        raise DeserializationError("CheckAccessNotGrantedRequest.policy_type required")
    return out


def redact_sensitive(value: CheckAccessNotGrantedRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "policy_document" in value:
        out["policy_document"] = "*** Sensitive Data Redacted ***"
    return out
