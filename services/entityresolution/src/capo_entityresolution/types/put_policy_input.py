"""Generated from Smithy shape ``com.amazonaws.entityresolution#PutPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.policy_document
    import capo_entityresolution.types.policy_token
    import capo_entityresolution.types.venice_global_arn


class PutPolicyInput(TypedDict, closed=True):
    arn: "capo_entityresolution.types.venice_global_arn.VeniceGlobalArn"
    """<p>The Amazon Resource Name (ARN) of the resource for which the policy needs to be updated.</p>"""
    token: NotRequired["capo_entityresolution.types.policy_token.PolicyToken"]
    """<p>A unique identifier for the current revision of the policy.</p>"""
    policy: "capo_entityresolution.types.policy_document.PolicyDocument"
    """<p>The resource-based policy.</p> <important> <p>If you set the value of the <code>effect</code> parameter in the <code>policy</code> to <code>Deny</code> for the <code>PutPolicy</code> operation, you must also set the value of the <code>effect</code> parameter to <code>Deny</code> for the <code>AddPolicyStatement</code> operation.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutPolicyInput) -> dict:
    out: dict = {}
    if "token" in value:
        out["token"] = value["token"]
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutPolicyInput:
    out: PutPolicyInput = {}  # type: ignore[typeddict-item]
    if data.get("token") is not None:
        out["token"] = data["token"]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    return out
