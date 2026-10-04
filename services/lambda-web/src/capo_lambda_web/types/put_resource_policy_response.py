"""Generated from Smithy shape ``com.amazonaws.lambdaweb#PutResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lambda_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_web.types.policy_revision_id
    import capo_lambda_web.types.resource_policy


class PutResourcePolicyResponse(TypedDict, closed=True):
    policy: "capo_lambda_web.types.resource_policy.ResourcePolicy"
    """<p>The JSON-formatted resource-based policy attached to the web function.</p>"""
    revision_id: "capo_lambda_web.types.policy_revision_id.PolicyRevisionId"
    """<p>The revision ID of the policy. Use this value in subsequent <code>PutResourcePolicy</code> or <code>DeleteResourcePolicy</code> requests to prevent conflicts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyResponse) -> dict:
    out: dict = {}
    out["Policy"] = value["policy"]
    out["RevisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyResponse:
    out: PutResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("PutResourcePolicyResponse.policy required")
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    else:
        raise DeserializationError("PutResourcePolicyResponse.revision_id required")
    return out
