"""Generated from Smithy shape ``com.amazonaws.iot#CreatePolicyVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.policy_document
    import capo_iot.types.policy_name
    import capo_iot.types.set_as_default


class CreatePolicyVersionRequest(TypedDict, closed=True):
    policy_name: "capo_iot.types.policy_name.PolicyName"
    """<p>The policy name.</p>"""
    policy_document: "capo_iot.types.policy_document.PolicyDocument"
    """<p>The JSON document that describes the policy. Minimum length of 1. Maximum length of 2048, excluding whitespace.</p>"""
    set_as_default: NotRequired["capo_iot.types.set_as_default.SetAsDefault"]
    """<p>Specifies whether the policy version is set as the default. When this parameter is true, the new policy version becomes the operative version (that is, the version that is in effect for the certificates to which the policy is attached).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePolicyVersionRequest) -> dict:
    out: dict = {}
    out["policyDocument"] = value["policy_document"]
    return out


def deserialize_json(data: dict) -> CreatePolicyVersionRequest:
    out: CreatePolicyVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("policyDocument") is not None:
        out["policy_document"] = data["policyDocument"]
    else:
        out["policy_document"] = ""
    return out
