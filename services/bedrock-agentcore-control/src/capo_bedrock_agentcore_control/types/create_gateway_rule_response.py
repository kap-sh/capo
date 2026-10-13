"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateGatewayRuleResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.actions
    import capo_bedrock_agentcore_control.types.conditions
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.gateway_arn
    import capo_bedrock_agentcore_control.types.gateway_rule_description
    import capo_bedrock_agentcore_control.types.gateway_rule_id
    import capo_bedrock_agentcore_control.types.gateway_rule_priority
    import capo_bedrock_agentcore_control.types.gateway_rule_status
    import capo_bedrock_agentcore_control.types.system_managed_block


class CreateGatewayRuleResponse(TypedDict, closed=True):
    rule_id: "capo_bedrock_agentcore_control.types.gateway_rule_id.GatewayRuleId"
    """<p>The unique identifier of the gateway rule.</p>"""
    gateway_arn: "capo_bedrock_agentcore_control.types.gateway_arn.GatewayArn"
    """<p>The Amazon Resource Name (ARN) of the gateway that the rule belongs to.</p>"""
    priority: (
        "capo_bedrock_agentcore_control.types.gateway_rule_priority.GatewayRulePriority"
    )
    """<p>The priority of the rule. Rules are evaluated in order of priority, with lower numbers evaluated first.</p>"""
    conditions: NotRequired[
        "capo_bedrock_agentcore_control.types.conditions.Conditions"
    ]
    """<p>The conditions that must be met for the rule to apply.</p>"""
    actions: "capo_bedrock_agentcore_control.types.actions.Actions"
    """<p>The actions to take when the rule conditions are met.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_rule_description.GatewayRuleDescription"
    ]
    """<p>The description of the gateway rule.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the rule was created.</p>"""
    status: "capo_bedrock_agentcore_control.types.gateway_rule_status.GatewayRuleStatus"
    """<p>The current status of the rule.</p>"""
    system: NotRequired[
        "capo_bedrock_agentcore_control.types.system_managed_block.SystemManagedBlock"
    ]
    """<p>System-managed metadata for rules created by automated processes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGatewayRuleResponse) -> dict:
    out: dict = {}
    out["ruleId"] = value["rule_id"]
    out["gatewayArn"] = value["gateway_arn"]
    out["priority"] = value["priority"]
    if "conditions" in value:
        import capo_bedrock_agentcore_control.types.conditions

        out["conditions"] = (
            capo_bedrock_agentcore_control.types.conditions.serialize_json(
                value["conditions"]
            )
        )
    import capo_bedrock_agentcore_control.types.actions

    out["actions"] = capo_bedrock_agentcore_control.types.actions.serialize_json(
        value["actions"]
    )
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.gateway_rule_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.gateway_rule_status.serialize_json(
            value["status"]
        )
    )
    if "system" in value:
        import capo_bedrock_agentcore_control.types.system_managed_block

        out["system"] = (
            capo_bedrock_agentcore_control.types.system_managed_block.serialize_json(
                value["system"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateGatewayRuleResponse:
    out: CreateGatewayRuleResponse = {}  # type: ignore[typeddict-item]
    if data.get("ruleId") is not None:
        out["rule_id"] = data["ruleId"]
    else:
        raise DeserializationError("CreateGatewayRuleResponse.rule_id required")
    if data.get("gatewayArn") is not None:
        out["gateway_arn"] = data["gatewayArn"]
    else:
        raise DeserializationError("CreateGatewayRuleResponse.gateway_arn required")
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    else:
        raise DeserializationError("CreateGatewayRuleResponse.priority required")
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
    else:
        raise DeserializationError("CreateGatewayRuleResponse.actions required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("CreateGatewayRuleResponse.created_at required")
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.gateway_rule_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.gateway_rule_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreateGatewayRuleResponse.status required")
    if data.get("system") is not None:
        import capo_bedrock_agentcore_control.types.system_managed_block

        out["system"] = (
            capo_bedrock_agentcore_control.types.system_managed_block.deserialize_json(
                data["system"]
            )
        )
    return out


def redact_sensitive(value: CreateGatewayRuleResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "actions" in value:
        import capo_bedrock_agentcore_control.types.actions

        out["actions"] = capo_bedrock_agentcore_control.types.actions.redact_sensitive(
            value["actions"]
        )
    return out
