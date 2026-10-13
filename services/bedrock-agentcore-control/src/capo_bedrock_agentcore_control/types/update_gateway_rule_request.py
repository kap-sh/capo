"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateGatewayRuleRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.actions
    import capo_bedrock_agentcore_control.types.conditions
    import capo_bedrock_agentcore_control.types.gateway_identifier
    import capo_bedrock_agentcore_control.types.gateway_rule_description
    import capo_bedrock_agentcore_control.types.gateway_rule_id
    import capo_bedrock_agentcore_control.types.gateway_rule_priority


class UpdateGatewayRuleRequest(TypedDict, closed=True):
    gateway_identifier: (
        "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier"
    )
    """<p>The identifier of the gateway containing the rule.</p>"""
    rule_id: "capo_bedrock_agentcore_control.types.gateway_rule_id.GatewayRuleId"
    """<p>The unique identifier of the rule to update.</p>"""
    priority: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_rule_priority.GatewayRulePriority"
    ]
    """<p>The updated priority of the rule.</p>"""
    conditions: NotRequired[
        "capo_bedrock_agentcore_control.types.conditions.Conditions"
    ]
    """<p>The updated conditions for the rule.</p>"""
    actions: NotRequired["capo_bedrock_agentcore_control.types.actions.Actions"]
    """<p>The updated actions for the rule.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_rule_description.GatewayRuleDescription"
    ]
    """<p>The updated description of the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGatewayRuleRequest) -> dict:
    out: dict = {}
    if "priority" in value:
        out["priority"] = value["priority"]
    if "conditions" in value:
        import capo_bedrock_agentcore_control.types.conditions

        out["conditions"] = (
            capo_bedrock_agentcore_control.types.conditions.serialize_json(
                value["conditions"]
            )
        )
    if "actions" in value:
        import capo_bedrock_agentcore_control.types.actions

        out["actions"] = capo_bedrock_agentcore_control.types.actions.serialize_json(
            value["actions"]
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateGatewayRuleRequest:
    out: UpdateGatewayRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    if data.get("conditions") is not None:
        import capo_bedrock_agentcore_control.types.conditions

        out["conditions"] = (
            capo_bedrock_agentcore_control.types.conditions.deserialize_json(
                data["conditions"]
            )
        )
    if data.get("actions") is not None:
        import capo_bedrock_agentcore_control.types.actions

        out["actions"] = capo_bedrock_agentcore_control.types.actions.deserialize_json(
            data["actions"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(value: UpdateGatewayRuleRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "actions" in value:
        import capo_bedrock_agentcore_control.types.actions

        out["actions"] = capo_bedrock_agentcore_control.types.actions.redact_sensitive(
            value["actions"]
        )
    return out
