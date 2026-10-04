"""Generated from Smithy shape ``com.amazonaws.lambdaweb#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_web.types.policy_revision_id
    import capo_lambda_web.types.resource_arn
    import capo_lambda_web.types.resource_policy


class PutResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_lambda_web.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the web function.</p>"""
    policy: "capo_lambda_web.types.resource_policy.ResourcePolicy"
    """<p>The JSON-formatted resource-based policy to attach to the web function.</p>"""
    revision_id: NotRequired[
        "capo_lambda_web.types.policy_revision_id.PolicyRevisionId"
    ]
    """<p>The revision ID of the existing policy. Use this to prevent conflicts when updating a policy concurrently. If you don't specify a value, the update proceeds without checking the current revision.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["Policy"] = value["policy"]
    if "revision_id" in value:
        out["RevisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.policy required")
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    return out
