"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.resource_arn
    import capo_bedrock_agent.types.resource_policy
    import capo_bedrock_agent.types.revision_id


class PutResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_bedrock_agent.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base to attach the resource policy to.</p>"""
    policy: "capo_bedrock_agent.types.resource_policy.ResourcePolicy"
    """<p>The JSON-formatted resource policy to associate with the knowledge base.</p>"""
    expected_revision_id: NotRequired["capo_bedrock_agent.types.revision_id.RevisionId"]
    """<p>The expected revision identifier of the resource policy. Use this to prevent conflicts when multiple users update the same policy concurrently. Specify the <code>revisionId</code> from the most recent <code>GetResourcePolicy</code> or <code>PutResourcePolicy</code> response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["policy"] = value["policy"]
    if "expected_revision_id" in value:
        out["expectedRevisionId"] = value["expected_revision_id"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    if data.get("expectedRevisionId") is not None:
        out["expected_revision_id"] = data["expectedRevisionId"]
    return out
