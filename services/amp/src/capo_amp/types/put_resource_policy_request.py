"""Generated from Smithy shape ``com.amazonaws.amp#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amp.types.idempotency_token
    import capo_amp.types.workspace_id


class PutResourcePolicyRequest(TypedDict, closed=True):
    workspace_id: "capo_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to attach the resource-based policy to.</p>"""
    policy_document: "str"
    """<p>The JSON policy document to use as the resource-based policy. This policy defines the permissions that other AWS accounts or services have to access your workspace.</p>"""
    client_token: NotRequired["capo_amp.types.idempotency_token.IdempotencyToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the request is safe to retry (idempotent).</p>"""
    revision_id: NotRequired["str"]
    """<p>The revision ID of the policy to update. Use this parameter to ensure that you are updating the correct version of the policy. If you don't specify a revision ID, the policy is updated regardless of its current revision.</p> <p>For the first <b>PUT</b> request on a workspace that doesn't have an existing resource policy, you can specify <code>NO_POLICY</code> as the revision ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["policyDocument"] = value["policy_document"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("policyDocument") is not None:
        out["policy_document"] = data["policyDocument"]
    else:
        out["policy_document"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    return out
