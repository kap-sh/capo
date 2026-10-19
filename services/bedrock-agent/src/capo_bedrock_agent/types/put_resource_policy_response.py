"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PutResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.resource_arn
    import capo_bedrock_agent.types.revision_id


class PutResourcePolicyResponse(TypedDict, closed=True):
    resource_arn: "capo_bedrock_agent.types.resource_arn.ResourceArn"
    """<p>The ARN of the knowledge base that the resource policy was attached to.</p>"""
    revision_id: "capo_bedrock_agent.types.revision_id.RevisionId"
    """<p>The revision identifier of the resource policy. Use this value in the <code>expectedRevisionId</code> field of a subsequent <code>PutResourcePolicy</code> or <code>DeleteResourcePolicy</code> request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyResponse) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["revisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyResponse:
    out: PutResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    else:
        out["revision_id"] = ""
    return out
