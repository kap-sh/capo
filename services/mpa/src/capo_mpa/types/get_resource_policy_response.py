"""Generated from Smithy shape ``com.amazonaws.mpa#GetResourcePolicyResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_mpa.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mpa.types.policy_document
    import capo_mpa.types.policy_name
    import capo_mpa.types.policy_type
    import capo_mpa.types.string


class GetResourcePolicyResponse(TypedDict, closed=True):
    resource_arn: "capo_mpa.types.string.String"
    """<p>Amazon Resource Name (ARN) for the resource.</p>"""
    policy_type: "capo_mpa.types.policy_type.PolicyType"
    """<p>The type of policy</p>"""
    policy_version_arn: NotRequired["capo_mpa.types.string.String"]
    """<p>Amazon Resource Name (ARN) for the policy version.</p>"""
    policy_name: "capo_mpa.types.policy_name.PolicyName"
    """<p>Name of the policy.</p>"""
    policy_document: "capo_mpa.types.policy_document.PolicyDocument"
    """<p>Document that contains the contents for the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePolicyResponse) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_mpa.types.policy_type

    out["PolicyType"] = capo_mpa.types.policy_type.serialize_json(value["policy_type"])
    if "policy_version_arn" in value:
        out["PolicyVersionArn"] = value["policy_version_arn"]
    out["PolicyName"] = value["policy_name"]
    out["PolicyDocument"] = value["policy_document"]
    return out


def deserialize_json(data: dict) -> GetResourcePolicyResponse:
    out: GetResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("GetResourcePolicyResponse.resource_arn required")
    if data.get("PolicyType") is not None:
        import capo_mpa.types.policy_type

        out["policy_type"] = capo_mpa.types.policy_type.deserialize_json(
            data["PolicyType"]
        )
    else:
        raise DeserializationError("GetResourcePolicyResponse.policy_type required")
    if data.get("PolicyVersionArn") is not None:
        out["policy_version_arn"] = data["PolicyVersionArn"]
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    else:
        raise DeserializationError("GetResourcePolicyResponse.policy_name required")
    if data.get("PolicyDocument") is not None:
        out["policy_document"] = data["PolicyDocument"]
    else:
        raise DeserializationError("GetResourcePolicyResponse.policy_document required")
    return out


def redact_sensitive(value: GetResourcePolicyResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "policy_document" in value:
        out["policy_document"] = "*** Sensitive Data Redacted ***"
    return out
