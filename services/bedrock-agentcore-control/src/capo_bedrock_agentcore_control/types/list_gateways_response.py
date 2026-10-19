"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListGatewaysResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_next_token
    import capo_bedrock_agentcore_control.types.gateway_summaries


class ListGatewaysResponse(TypedDict, closed=True):
    items: "capo_bedrock_agentcore_control.types.gateway_summaries.GatewaySummaries"
    """<p>The list of gateway summaries.</p>"""
    next_token: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_next_token.GatewayNextToken"
    ]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGatewaysResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.gateway_summaries

    out["items"] = (
        capo_bedrock_agentcore_control.types.gateway_summaries.serialize_json(
            value["items"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGatewaysResponse:
    out: ListGatewaysResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_bedrock_agentcore_control.types.gateway_summaries

        out["items"] = (
            capo_bedrock_agentcore_control.types.gateway_summaries.deserialize_json(
                data["items"]
            )
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListGatewaysResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_bedrock_agentcore_control.types.gateway_summaries

        out["items"] = (
            capo_bedrock_agentcore_control.types.gateway_summaries.redact_sensitive(
                value["items"]
            )
        )
    return out
