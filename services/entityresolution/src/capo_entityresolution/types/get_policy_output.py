"""Generated from Smithy shape ``com.amazonaws.entityresolution#GetPolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.policy_document
    import capo_entityresolution.types.policy_token
    import capo_entityresolution.types.venice_global_arn


class GetPolicyOutput(TypedDict, closed=True):
    arn: "capo_entityresolution.types.venice_global_arn.VeniceGlobalArn"
    """<p>The Entity Resolution resource ARN.</p>"""
    token: "capo_entityresolution.types.policy_token.PolicyToken"
    """<p>A unique identifier for the current revision of the policy.</p>"""
    policy: NotRequired["capo_entityresolution.types.policy_document.PolicyDocument"]
    """<p>The resource-based policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyOutput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["token"] = value["token"]
    if "policy" in value:
        out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> GetPolicyOutput:
    out: GetPolicyOutput = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("token") is not None:
        out["token"] = data["token"]
    else:
        out["token"] = ""
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    return out
