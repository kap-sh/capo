"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListGatewayRulesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_rule_next_token
    import capo_bedrock_agentcore_control.types.gateway_rules


class ListGatewayRulesResponse(TypedDict, closed=True):
    gateway_rules: "capo_bedrock_agentcore_control.types.gateway_rules.GatewayRules"
    """<p>The list of gateway rules.</p>"""
    next_token: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_rule_next_token.GatewayRuleNextToken"
    ]
    """<p>The pagination token to use in a subsequent request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGatewayRulesResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.gateway_rules

    out["gatewayRules"] = (
        capo_bedrock_agentcore_control.types.gateway_rules.serialize_json(
            value["gateway_rules"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGatewayRulesResponse:
    out: ListGatewayRulesResponse = {}  # type: ignore[typeddict-item]
    if data.get("gatewayRules") is not None:
        import capo_bedrock_agentcore_control.types.gateway_rules

        out["gateway_rules"] = (
            capo_bedrock_agentcore_control.types.gateway_rules.deserialize_json(
                data["gatewayRules"]
            )
        )
    else:
        raise DeserializationError("ListGatewayRulesResponse.gateway_rules required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListGatewayRulesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "gateway_rules" in value:
        import capo_bedrock_agentcore_control.types.gateway_rules

        out["gateway_rules"] = (
            capo_bedrock_agentcore_control.types.gateway_rules.redact_sensitive(
                value["gateway_rules"]
            )
        )
    return out
