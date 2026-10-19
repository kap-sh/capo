"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteGatewayRateLimitResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_id
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_status


class DeleteGatewayRateLimitResponse(TypedDict, closed=True):
    rate_limit_id: (
        "capo_bedrock_agentcore_control.types.gateway_rate_limit_id.GatewayRateLimitId"
    )
    """<p>The unique identifier of the deleted rate limit.</p>"""
    status: "capo_bedrock_agentcore_control.types.gateway_rate_limit_status.GatewayRateLimitStatus"
    """<p>The current status of the rate limit deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGatewayRateLimitResponse) -> dict:
    out: dict = {}
    out["rateLimitId"] = value["rate_limit_id"]
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.gateway_rate_limit_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteGatewayRateLimitResponse:
    out: DeleteGatewayRateLimitResponse = {}  # type: ignore[typeddict-item]
    if data.get("rateLimitId") is not None:
        out["rate_limit_id"] = data["rateLimitId"]
    else:
        out["rate_limit_id"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.gateway_rate_limit_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.gateway_rate_limit_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.gateway_rate_limit_status.GatewayRateLimitStatus",
            "",
        )
    return out
