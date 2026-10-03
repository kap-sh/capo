"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BatchPutGatewayRateLimitsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.batch_put_limit_entries
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.gateway_identifier


class BatchPutGatewayRateLimitsRequest(TypedDict, closed=True):
    gateway_identifier: (
        "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier"
    )
    """<p>The unique identifier of the gateway.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    rate_limits: "capo_bedrock_agentcore_control.types.batch_put_limit_entries.BatchPutLimitEntries"
    """<p>The complete set of rate limits for this gateway. This operation replaces all existing rate limits in a single request. If the operation fails, no rate limits are changed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutGatewayRateLimitsRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_bedrock_agentcore_control.types.batch_put_limit_entries

    out["rateLimits"] = (
        capo_bedrock_agentcore_control.types.batch_put_limit_entries.serialize_json(
            value["rate_limits"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchPutGatewayRateLimitsRequest:
    out: BatchPutGatewayRateLimitsRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("rateLimits") is not None:
        import capo_bedrock_agentcore_control.types.batch_put_limit_entries

        out["rate_limits"] = (
            capo_bedrock_agentcore_control.types.batch_put_limit_entries.deserialize_json(
                data["rateLimits"]
            )
        )
    else:
        raise DeserializationError(
            "BatchPutGatewayRateLimitsRequest.rate_limits required"
        )
    return out
