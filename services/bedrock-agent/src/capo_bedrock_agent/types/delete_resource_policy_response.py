"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeleteResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.resource_arn
    import capo_bedrock_agent.types.revision_id


class DeleteResourcePolicyResponse(TypedDict, closed=True):
    resource_arn: "capo_bedrock_agent.types.resource_arn.ResourceArn"
    """<p>The ARN of the knowledge base that the resource policy was removed from.</p>"""
    revision_id: NotRequired["capo_bedrock_agent.types.revision_id.RevisionId"]
    """<p>The revision identifier after the resource policy was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourcePolicyResponse) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> DeleteResourcePolicyResponse:
    out: DeleteResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    return out
