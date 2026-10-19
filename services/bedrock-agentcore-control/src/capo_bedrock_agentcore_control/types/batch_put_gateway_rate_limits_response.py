"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BatchPutGatewayRateLimitsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_rate_limits


class BatchPutGatewayRateLimitsResponse(TypedDict, closed=True):
    rate_limits: (
        "capo_bedrock_agentcore_control.types.gateway_rate_limits.GatewayRateLimits"
    )
    """<p>The resulting set of rate limits after the batch operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutGatewayRateLimitsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.gateway_rate_limits

    out["rateLimits"] = (
        capo_bedrock_agentcore_control.types.gateway_rate_limits.serialize_json(
            value["rate_limits"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchPutGatewayRateLimitsResponse:
    out: BatchPutGatewayRateLimitsResponse = {}  # type: ignore[typeddict-item]
    if data.get("rateLimits") is not None:
        import capo_bedrock_agentcore_control.types.gateway_rate_limits

        out["rate_limits"] = (
            capo_bedrock_agentcore_control.types.gateway_rate_limits.deserialize_json(
                data["rateLimits"]
            )
        )
    else:
        out["rate_limits"] = []
    return out
