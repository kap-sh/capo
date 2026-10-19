"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListGatewayRateLimitsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_next_token
    import capo_bedrock_agentcore_control.types.gateway_rate_limits


class ListGatewayRateLimitsResponse(TypedDict, closed=True):
    rate_limits: (
        "capo_bedrock_agentcore_control.types.gateway_rate_limits.GatewayRateLimits"
    )
    """<p>The list of rate limits for the gateway.</p>"""
    next_token: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_rate_limit_next_token.GatewayRateLimitNextToken"
    ]
    """<p>The token for the next page of results. If this value is absent, there are no more results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGatewayRateLimitsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.gateway_rate_limits

    out["rateLimits"] = (
        capo_bedrock_agentcore_control.types.gateway_rate_limits.serialize_json(
            value["rate_limits"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGatewayRateLimitsResponse:
    out: ListGatewayRateLimitsResponse = {}  # type: ignore[typeddict-item]
    if data.get("rateLimits") is not None:
        import capo_bedrock_agentcore_control.types.gateway_rate_limits

        out["rate_limits"] = (
            capo_bedrock_agentcore_control.types.gateway_rate_limits.deserialize_json(
                data["rateLimits"]
            )
        )
    else:
        out["rate_limits"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
