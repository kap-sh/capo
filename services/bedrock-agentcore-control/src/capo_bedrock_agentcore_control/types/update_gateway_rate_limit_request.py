"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateGatewayRateLimitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_identifier
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_description
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_id
    import capo_bedrock_agentcore_control.types.limit_entries


class UpdateGatewayRateLimitRequest(TypedDict, closed=True):
    gateway_identifier: (
        "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier"
    )
    """<p>The unique identifier of the gateway.</p>"""
    rate_limit_id: (
        "capo_bedrock_agentcore_control.types.gateway_rate_limit_id.GatewayRateLimitId"
    )
    """<p>The unique identifier of the rate limit to update.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_rate_limit_description.GatewayRateLimitDescription"
    ]
    """<p>The updated human-readable description for this rate limit.</p>"""
    entries: "capo_bedrock_agentcore_control.types.limit_entries.LimitEntries"
    """<p>The updated rule entries. The dimension keys are immutable after creation and cannot be changed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGatewayRateLimitRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agentcore_control.types.limit_entries

    out["entries"] = capo_bedrock_agentcore_control.types.limit_entries.serialize_json(
        value["entries"]
    )
    return out


def deserialize_json(data: dict) -> UpdateGatewayRateLimitRequest:
    out: UpdateGatewayRateLimitRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("entries") is not None:
        import capo_bedrock_agentcore_control.types.limit_entries

        out["entries"] = (
            capo_bedrock_agentcore_control.types.limit_entries.deserialize_json(
                data["entries"]
            )
        )
    else:
        out["entries"] = []
    return out
