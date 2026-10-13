"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckImpossibleFinding``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_check_logic_warning
    import capo_bedrock.types.automated_reasoning_check_rule_list
    import capo_bedrock.types.automated_reasoning_check_translation


class AutomatedReasoningCheckImpossibleFinding(TypedDict, closed=True):
    translation: NotRequired[
        "capo_bedrock.types.automated_reasoning_check_translation.AutomatedReasoningCheckTranslation"
    ]
    """<p>The logical translation of the input that this finding evaluates.</p>"""
    contradicting_rules: NotRequired[
        "capo_bedrock.types.automated_reasoning_check_rule_list.AutomatedReasoningCheckRuleList"
    ]
    """<p>The automated reasoning policy rules that contradict the claims and/or premises in the input.</p>"""
    logic_warning: NotRequired[
        "capo_bedrock.types.automated_reasoning_check_logic_warning.AutomatedReasoningCheckLogicWarning"
    ]
    """<p>Indication of a logic issue with the translation without needing to consider the automated reasoning policy rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckImpossibleFinding) -> dict:
    out: dict = {}
    if "translation" in value:
        import capo_bedrock.types.automated_reasoning_check_translation

        out["translation"] = (
            capo_bedrock.types.automated_reasoning_check_translation.serialize_json(
                value["translation"]
            )
        )
    if "contradicting_rules" in value:
        import capo_bedrock.types.automated_reasoning_check_rule_list

        out["contradictingRules"] = (
            capo_bedrock.types.automated_reasoning_check_rule_list.serialize_json(
                value["contradicting_rules"]
            )
        )
    if "logic_warning" in value:
        import capo_bedrock.types.automated_reasoning_check_logic_warning

        out["logicWarning"] = (
            capo_bedrock.types.automated_reasoning_check_logic_warning.serialize_json(
                value["logic_warning"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningCheckImpossibleFinding:
    out: AutomatedReasoningCheckImpossibleFinding = {}  # type: ignore[typeddict-item]
    if data.get("translation") is not None:
        import capo_bedrock.types.automated_reasoning_check_translation

        out["translation"] = (
            capo_bedrock.types.automated_reasoning_check_translation.deserialize_json(
                data["translation"]
            )
        )
    if data.get("contradictingRules") is not None:
        import capo_bedrock.types.automated_reasoning_check_rule_list

        out["contradicting_rules"] = (
            capo_bedrock.types.automated_reasoning_check_rule_list.deserialize_json(
                data["contradictingRules"]
            )
        )
    if data.get("logicWarning") is not None:
        import capo_bedrock.types.automated_reasoning_check_logic_warning

        out["logic_warning"] = (
            capo_bedrock.types.automated_reasoning_check_logic_warning.deserialize_json(
                data["logicWarning"]
            )
        )
    return out


def redact_sensitive(value: AutomatedReasoningCheckImpossibleFinding) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "translation" in value:
        import capo_bedrock.types.automated_reasoning_check_translation

        out["translation"] = (
            capo_bedrock.types.automated_reasoning_check_translation.redact_sensitive(
                value["translation"]
            )
        )
    if "logic_warning" in value:
        import capo_bedrock.types.automated_reasoning_check_logic_warning

        out["logic_warning"] = (
            capo_bedrock.types.automated_reasoning_check_logic_warning.redact_sensitive(
                value["logic_warning"]
            )
        )
    return out
