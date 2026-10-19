"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.resource_arn
    import capo_bedrock_agent.types.resource_policy
    import capo_bedrock_agent.types.revision_id


class GetResourcePolicyResponse(TypedDict, closed=True):
    resource_arn: "capo_bedrock_agent.types.resource_arn.ResourceArn"
    """<p>The ARN of the knowledge base that the resource policy is associated with.</p>"""
    policy: "capo_bedrock_agent.types.resource_policy.ResourcePolicy"
    """<p>The JSON-formatted resource policy associated with the knowledge base.</p>"""
    revision_id: "capo_bedrock_agent.types.revision_id.RevisionId"
    """<p>The revision identifier of the resource policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePolicyResponse) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["policy"] = value["policy"]
    out["revisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> GetResourcePolicyResponse:
    out: GetResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    else:
        out["revision_id"] = ""
    return out
