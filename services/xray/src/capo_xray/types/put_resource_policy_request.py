"""Generated from Smithy shape ``com.amazonaws.xray#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.boolean
    import capo_xray.types.policy_document
    import capo_xray.types.policy_name
    import capo_xray.types.policy_revision_id


class PutResourcePolicyRequest(TypedDict, closed=True):
    policy_name: "capo_xray.types.policy_name.PolicyName"
    """<p>The name of the resource policy. Must be unique within a specific Amazon Web Services account.</p>"""
    policy_document: "capo_xray.types.policy_document.PolicyDocument"
    """<p>The resource policy document, which can be up to 5kb in size.</p>"""
    policy_revision_id: NotRequired[
        "capo_xray.types.policy_revision_id.PolicyRevisionId"
    ]
    """<p>Specifies a specific policy revision, to ensure an atomic create operation. By default the resource policy is created if it does not exist, or updated with an incremented revision id. The revision id is unique to each policy in the account.</p> <p>If the policy revision id does not match the latest revision id, the operation will fail with an <code>InvalidPolicyRevisionIdException</code> exception. You can also provide a <code>PolicyRevisionId</code> of 0. In this case, the operation will fail with an <code>InvalidPolicyRevisionIdException</code> exception if a resource policy with the same name already exists. </p>"""
    bypass_policy_lockout_check: NotRequired["capo_xray.types.boolean.Boolean"]
    """<p>A flag to indicate whether to bypass the resource policy lockout safety check.</p> <important> <p>Setting this value to true increases the risk that the policy becomes unmanageable. Do not set this value to true indiscriminately.</p> </important> <p>Use this parameter only when you include a policy in the request and you intend to prevent the principal that is making the request from making a subsequent <code>PutResourcePolicy</code> request.</p> <p>The default value is false.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["PolicyName"] = value["policy_name"]
    out["PolicyDocument"] = value["policy_document"]
    if "policy_revision_id" in value:
        out["PolicyRevisionId"] = value["policy_revision_id"]
    if "bypass_policy_lockout_check" in value:
        out["BypassPolicyLockoutCheck"] = value["bypass_policy_lockout_check"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    else:
        out["policy_name"] = ""
    if data.get("PolicyDocument") is not None:
        out["policy_document"] = data["PolicyDocument"]
    else:
        out["policy_document"] = ""
    if data.get("PolicyRevisionId") is not None:
        out["policy_revision_id"] = data["PolicyRevisionId"]
    if data.get("BypassPolicyLockoutCheck") is not None:
        out["bypass_policy_lockout_check"] = data["BypassPolicyLockoutCheck"]
    return out
