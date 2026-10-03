"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateGatewayRateLimitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.dimension_keys
    import capo_bedrock_agentcore_control.types.gateway_identifier
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_description
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_id
    import capo_bedrock_agentcore_control.types.limit_entries


class CreateGatewayRateLimitRequest(TypedDict, closed=True):
    gateway_identifier: (
        "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier"
    )
    """<p>The unique identifier of the gateway to create the rate limit for.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    rate_limit_id: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_rate_limit_id.GatewayRateLimitId"
    ]
    """<p>An optional customer-defined identifier for the rate limit. If not provided, the system generates one.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_rate_limit_description.GatewayRateLimitDescription"
    ]
    """<p>An optional human-readable description for this rate limit. If not provided, the rate limit is created without a description.</p>"""
    dimension_keys: "capo_bedrock_agentcore_control.types.dimension_keys.DimensionKeys"
    """<p>The ordered list of dimension key names that define the scope of this rate limit. Must be unique per gateway—no two rate limits can share the same dimension keys.</p>"""
    entries: "capo_bedrock_agentcore_control.types.limit_entries.LimitEntries"
    """<p>The rule entries that map dimension values to rate configurations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGatewayRateLimitRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "rate_limit_id" in value:
        out["rateLimitId"] = value["rate_limit_id"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agentcore_control.types.dimension_keys

    out["dimensionKeys"] = (
        capo_bedrock_agentcore_control.types.dimension_keys.serialize_json(
            value["dimension_keys"]
        )
    )
    import capo_bedrock_agentcore_control.types.limit_entries

    out["entries"] = capo_bedrock_agentcore_control.types.limit_entries.serialize_json(
        value["entries"]
    )
    return out


def deserialize_json(data: dict) -> CreateGatewayRateLimitRequest:
    out: CreateGatewayRateLimitRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("rateLimitId") is not None:
        out["rate_limit_id"] = data["rateLimitId"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("dimensionKeys") is not None:
        import capo_bedrock_agentcore_control.types.dimension_keys

        out["dimension_keys"] = (
            capo_bedrock_agentcore_control.types.dimension_keys.deserialize_json(
                data["dimensionKeys"]
            )
        )
    else:
        raise DeserializationError(
            "CreateGatewayRateLimitRequest.dimension_keys required"
        )
    if data.get("entries") is not None:
        import capo_bedrock_agentcore_control.types.limit_entries

        out["entries"] = (
            capo_bedrock_agentcore_control.types.limit_entries.deserialize_json(
                data["entries"]
            )
        )
    else:
        raise DeserializationError("CreateGatewayRateLimitRequest.entries required")
    return out
