"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateGatewayRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.actions
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.conditions
    import capo_bedrock_agentcore_control.types.gateway_identifier
    import capo_bedrock_agentcore_control.types.gateway_rule_description
    import capo_bedrock_agentcore_control.types.gateway_rule_priority


class CreateGatewayRuleRequest(TypedDict, closed=True):
    gateway_identifier: (
        "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier"
    )
    """<p>The identifier of the gateway to create a rule for.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    priority: (
        "capo_bedrock_agentcore_control.types.gateway_rule_priority.GatewayRulePriority"
    )
    """<p>The priority of the rule. Rules are evaluated in order of priority, with lower numbers evaluated first. Must be between 1 and 1,000,000.</p>"""
    conditions: NotRequired[
        "capo_bedrock_agentcore_control.types.conditions.Conditions"
    ]
    """<p>The conditions that must be met for the rule to apply. Conditions can match on principals (IAM ARNs) or request paths.</p>"""
    actions: "capo_bedrock_agentcore_control.types.actions.Actions"
    """<p>The actions to take when the rule conditions are met. Actions can route to a specific target or apply a configuration bundle override.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_rule_description.GatewayRuleDescription"
    ]
    """<p>The description of the gateway rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGatewayRuleRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
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
    return out


def deserialize_json(data: dict) -> CreateGatewayRuleRequest:
    out: CreateGatewayRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    else:
        raise DeserializationError("CreateGatewayRuleRequest.priority required")
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
        raise DeserializationError("CreateGatewayRuleRequest.actions required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
