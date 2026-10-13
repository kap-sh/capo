"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningInvalidFinding``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_logic_warning
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_rule_list
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_translation


class GuardrailAutomatedReasoningInvalidFinding(TypedDict, closed=True):
    translation: NotRequired[
        "capo_bedrock_runtime.types.guardrail_automated_reasoning_translation.GuardrailAutomatedReasoningTranslation"
    ]
    """<p>The logical translation of the input that this finding invalidates.</p>"""
    contradicting_rules: NotRequired[
        "capo_bedrock_runtime.types.guardrail_automated_reasoning_rule_list.GuardrailAutomatedReasoningRuleList"
    ]
    """<p>The automated reasoning policy rules that contradict the claims in the input.</p>"""
    logic_warning: NotRequired[
        "capo_bedrock_runtime.types.guardrail_automated_reasoning_logic_warning.GuardrailAutomatedReasoningLogicWarning"
    ]
    """<p>Indication of a logic issue with the translation without needing to consider the automated reasoning policy rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningInvalidFinding) -> dict:
    out: dict = {}
    if "translation" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_translation

        out["translation"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_translation.serialize_json(
                value["translation"]
            )
        )
    if "contradicting_rules" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_rule_list

        out["contradictingRules"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_rule_list.serialize_json(
                value["contradicting_rules"]
            )
        )
    if "logic_warning" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_logic_warning

        out["logicWarning"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_logic_warning.serialize_json(
                value["logic_warning"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailAutomatedReasoningInvalidFinding:
    out: GuardrailAutomatedReasoningInvalidFinding = {}  # type: ignore[typeddict-item]
    if data.get("translation") is not None:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_translation

        out["translation"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_translation.deserialize_json(
                data["translation"]
            )
        )
    if data.get("contradictingRules") is not None:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_rule_list

        out["contradicting_rules"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_rule_list.deserialize_json(
                data["contradictingRules"]
            )
        )
    if data.get("logicWarning") is not None:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_logic_warning

        out["logic_warning"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_logic_warning.deserialize_json(
                data["logicWarning"]
            )
        )
    return out


def redact_sensitive(
    value: GuardrailAutomatedReasoningInvalidFinding,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "translation" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_translation

        out["translation"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_translation.redact_sensitive(
                value["translation"]
            )
        )
    if "logic_warning" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_logic_warning

        out["logic_warning"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_logic_warning.redact_sensitive(
                value["logic_warning"]
            )
        )
    return out
