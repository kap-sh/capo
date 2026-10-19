"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteGatewayRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_rule_id
    import capo_bedrock_agentcore_control.types.gateway_rule_status


class DeleteGatewayRuleResponse(TypedDict, closed=True):
    rule_id: "capo_bedrock_agentcore_control.types.gateway_rule_id.GatewayRuleId"
    """<p>The unique identifier of the deleted rule.</p>"""
    status: "capo_bedrock_agentcore_control.types.gateway_rule_status.GatewayRuleStatus"
    """<p>The status of the rule deletion operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGatewayRuleResponse) -> dict:
    out: dict = {}
    out["ruleId"] = value["rule_id"]
    import capo_bedrock_agentcore_control.types.gateway_rule_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.gateway_rule_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteGatewayRuleResponse:
    out: DeleteGatewayRuleResponse = {}  # type: ignore[typeddict-item]
    if data.get("ruleId") is not None:
        out["rule_id"] = data["ruleId"]
    else:
        out["rule_id"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.gateway_rule_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.gateway_rule_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.gateway_rule_status.GatewayRuleStatus",
            "",
        )
    return out
