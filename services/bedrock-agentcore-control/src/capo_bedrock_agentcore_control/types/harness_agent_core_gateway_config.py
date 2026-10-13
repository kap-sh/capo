"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessAgentCoreGatewayConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_arn
    import capo_bedrock_agentcore_control.types.harness_gateway_outbound_auth


class HarnessAgentCoreGatewayConfig(TypedDict, closed=True):
    gateway_arn: "capo_bedrock_agentcore_control.types.gateway_arn.GatewayArn"
    """<p>The ARN of the desired AgentCore Gateway.</p>"""
    outbound_auth: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_gateway_outbound_auth.HarnessGatewayOutboundAuth"
    ]
    """<p>How harness authenticates to this Gateway. Defaults to AWS_IAM (SigV4) if omitted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessAgentCoreGatewayConfig) -> dict:
    out: dict = {}
    out["gatewayArn"] = value["gateway_arn"]
    if "outbound_auth" in value:
        import capo_bedrock_agentcore_control.types.harness_gateway_outbound_auth

        out["outboundAuth"] = (
            capo_bedrock_agentcore_control.types.harness_gateway_outbound_auth.serialize_json(
                value["outbound_auth"]
            )
        )
    return out


def deserialize_json(data: dict) -> HarnessAgentCoreGatewayConfig:
    out: HarnessAgentCoreGatewayConfig = {}  # type: ignore[typeddict-item]
    if data.get("gatewayArn") is not None:
        out["gateway_arn"] = data["gatewayArn"]
    else:
        raise DeserializationError("HarnessAgentCoreGatewayConfig.gateway_arn required")
    if data.get("outboundAuth") is not None:
        import capo_bedrock_agentcore_control.types.harness_gateway_outbound_auth

        out["outbound_auth"] = (
            capo_bedrock_agentcore_control.types.harness_gateway_outbound_auth.deserialize_json(
                data["outboundAuth"]
            )
        )
    return out


def redact_sensitive(value: HarnessAgentCoreGatewayConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "outbound_auth" in value:
        import capo_bedrock_agentcore_control.types.harness_gateway_outbound_auth

        out["outbound_auth"] = (
            capo_bedrock_agentcore_control.types.harness_gateway_outbound_auth.redact_sensitive(
                value["outbound_auth"]
            )
        )
    return out
