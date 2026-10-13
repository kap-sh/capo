"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListGatewayTargetsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.target_next_token
    import capo_bedrock_agentcore_control.types.target_summaries


class ListGatewayTargetsResponse(TypedDict, closed=True):
    items: "capo_bedrock_agentcore_control.types.target_summaries.TargetSummaries"
    """<p>The list of gateway target summaries.</p>"""
    next_token: NotRequired[
        "capo_bedrock_agentcore_control.types.target_next_token.TargetNextToken"
    ]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGatewayTargetsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.target_summaries

    out["items"] = capo_bedrock_agentcore_control.types.target_summaries.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGatewayTargetsResponse:
    out: ListGatewayTargetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_bedrock_agentcore_control.types.target_summaries

        out["items"] = (
            capo_bedrock_agentcore_control.types.target_summaries.deserialize_json(
                data["items"]
            )
        )
    else:
        raise DeserializationError("ListGatewayTargetsResponse.items required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListGatewayTargetsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_bedrock_agentcore_control.types.target_summaries

        out["items"] = (
            capo_bedrock_agentcore_control.types.target_summaries.redact_sensitive(
                value["items"]
            )
        )
    return out
