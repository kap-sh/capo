"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinition``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_rule_list
    import capo_bedrock.types.automated_reasoning_policy_definition_type_list
    import capo_bedrock.types.automated_reasoning_policy_definition_variable_list
    import capo_bedrock.types.automated_reasoning_policy_format_version


class AutomatedReasoningPolicyDefinition(TypedDict, closed=True):
    version: "capo_bedrock.types.automated_reasoning_policy_format_version.AutomatedReasoningPolicyFormatVersion"
    """<p>The version of the policy definition format.</p>"""
    types: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_definition_type_list.AutomatedReasoningPolicyDefinitionTypeList"
    ]
    """<p>The custom user-defined vairable types used in the policy. Types are enum-based variable types that provide additional context beyond the predefined variable types.</p>"""
    rules: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_definition_rule_list.AutomatedReasoningPolicyDefinitionRuleList"
    ]
    """<p>The formal logic rules extracted from the source document. Rules define the logical constraints that determine whether model responses are valid, invalid, or satisfiable.</p>"""
    variables: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_definition_variable_list.AutomatedReasoningPolicyDefinitionVariableList"
    ]
    """<p>The variables that represent concepts in the policy. Variables can have values assigned when translating natural language into formal logic. Their descriptions are crucial for accurate translation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinition) -> dict:
    out: dict = {}
    out["version"] = value.get("version", "1")
    if "types" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_type_list

        out["types"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_type_list.serialize_json(
                value["types"]
            )
        )
    if "rules" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_rule_list

        out["rules"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_rule_list.serialize_json(
                value["rules"]
            )
        )
    if "variables" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_variable_list

        out["variables"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_variable_list.serialize_json(
                value["variables"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyDefinition:
    out: AutomatedReasoningPolicyDefinition = {}  # type: ignore[typeddict-item]
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = "1"
    if data.get("types") is not None:
        import capo_bedrock.types.automated_reasoning_policy_definition_type_list

        out["types"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_type_list.deserialize_json(
                data["types"]
            )
        )
    if data.get("rules") is not None:
        import capo_bedrock.types.automated_reasoning_policy_definition_rule_list

        out["rules"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_rule_list.deserialize_json(
                data["rules"]
            )
        )
    if data.get("variables") is not None:
        import capo_bedrock.types.automated_reasoning_policy_definition_variable_list

        out["variables"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_variable_list.deserialize_json(
                data["variables"]
            )
        )
    return out


def redact_sensitive(value: AutomatedReasoningPolicyDefinition) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "types" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_type_list

        out["types"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_type_list.redact_sensitive(
                value["types"]
            )
        )
    if "rules" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_rule_list

        out["rules"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_rule_list.redact_sensitive(
                value["rules"]
            )
        )
    if "variables" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_variable_list

        out["variables"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_variable_list.redact_sensitive(
                value["variables"]
            )
        )
    return out
