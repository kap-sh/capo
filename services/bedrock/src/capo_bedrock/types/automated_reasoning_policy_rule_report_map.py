"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyRuleReportMap``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_rule_id
    import capo_bedrock.types.automated_reasoning_policy_rule_report

AutomatedReasoningPolicyRuleReportMap: TypeAlias = dict[
    "capo_bedrock.types.automated_reasoning_policy_definition_rule_id.AutomatedReasoningPolicyDefinitionRuleId",
    "capo_bedrock.types.automated_reasoning_policy_rule_report.AutomatedReasoningPolicyRuleReport",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AutomatedReasoningPolicyRuleReportMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_bedrock.types.automated_reasoning_policy_rule_report

        out[key] = (
            capo_bedrock.types.automated_reasoning_policy_rule_report.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyRuleReportMap:
    out: AutomatedReasoningPolicyRuleReportMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_bedrock.types.automated_reasoning_policy_rule_report

        out[key] = (
            capo_bedrock.types.automated_reasoning_policy_rule_report.deserialize_json(
                value
            )
        )
    return out


def redact_sensitive(value: AutomatedReasoningPolicyRuleReportMap) -> dict[str, Any]:
    import capo_bedrock.types.automated_reasoning_policy_rule_report

    return {
        key: capo_bedrock.types.automated_reasoning_policy_rule_report.redact_sensitive(
            item
        )
        for key, item in value.items()
    }
