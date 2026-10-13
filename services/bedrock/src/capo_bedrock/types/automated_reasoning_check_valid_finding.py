"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckValidFinding``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_check_logic_warning
    import capo_bedrock.types.automated_reasoning_check_rule_list
    import capo_bedrock.types.automated_reasoning_check_scenario
    import capo_bedrock.types.automated_reasoning_check_translation


class AutomatedReasoningCheckValidFinding(TypedDict, closed=True):
    translation: NotRequired[
        "capo_bedrock.types.automated_reasoning_check_translation.AutomatedReasoningCheckTranslation"
    ]
    """<p>The logical translation of the input that this finding validates.</p>"""
    claims_true_scenario: NotRequired[
        "capo_bedrock.types.automated_reasoning_check_scenario.AutomatedReasoningCheckScenario"
    ]
    """<p>An example scenario demonstrating how the claims are logically true.</p>"""
    supporting_rules: NotRequired[
        "capo_bedrock.types.automated_reasoning_check_rule_list.AutomatedReasoningCheckRuleList"
    ]
    """<p>The automated reasoning policy rules that support why this result is considered valid.</p>"""
    logic_warning: NotRequired[
        "capo_bedrock.types.automated_reasoning_check_logic_warning.AutomatedReasoningCheckLogicWarning"
    ]
    """<p>Indication of a logic issue with the translation without needing to consider the automated reasoning policy rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckValidFinding) -> dict:
    out: dict = {}
    if "translation" in value:
        import capo_bedrock.types.automated_reasoning_check_translation

        out["translation"] = (
            capo_bedrock.types.automated_reasoning_check_translation.serialize_json(
                value["translation"]
            )
        )
    if "claims_true_scenario" in value:
        import capo_bedrock.types.automated_reasoning_check_scenario

        out["claimsTrueScenario"] = (
            capo_bedrock.types.automated_reasoning_check_scenario.serialize_json(
                value["claims_true_scenario"]
            )
        )
    if "supporting_rules" in value:
        import capo_bedrock.types.automated_reasoning_check_rule_list

        out["supportingRules"] = (
            capo_bedrock.types.automated_reasoning_check_rule_list.serialize_json(
                value["supporting_rules"]
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


def deserialize_json(data: dict) -> AutomatedReasoningCheckValidFinding:
    out: AutomatedReasoningCheckValidFinding = {}  # type: ignore[typeddict-item]
    if data.get("translation") is not None:
        import capo_bedrock.types.automated_reasoning_check_translation

        out["translation"] = (
            capo_bedrock.types.automated_reasoning_check_translation.deserialize_json(
                data["translation"]
            )
        )
    if data.get("claimsTrueScenario") is not None:
        import capo_bedrock.types.automated_reasoning_check_scenario

        out["claims_true_scenario"] = (
            capo_bedrock.types.automated_reasoning_check_scenario.deserialize_json(
                data["claimsTrueScenario"]
            )
        )
    if data.get("supportingRules") is not None:
        import capo_bedrock.types.automated_reasoning_check_rule_list

        out["supporting_rules"] = (
            capo_bedrock.types.automated_reasoning_check_rule_list.deserialize_json(
                data["supportingRules"]
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


def redact_sensitive(value: AutomatedReasoningCheckValidFinding) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "translation" in value:
        import capo_bedrock.types.automated_reasoning_check_translation

        out["translation"] = (
            capo_bedrock.types.automated_reasoning_check_translation.redact_sensitive(
                value["translation"]
            )
        )
    if "claims_true_scenario" in value:
        import capo_bedrock.types.automated_reasoning_check_scenario

        out["claims_true_scenario"] = (
            capo_bedrock.types.automated_reasoning_check_scenario.redact_sensitive(
                value["claims_true_scenario"]
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
