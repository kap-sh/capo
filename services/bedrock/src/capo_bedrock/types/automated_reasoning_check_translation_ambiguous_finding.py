"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckTranslationAmbiguousFinding``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_check_difference_scenario_list
    import capo_bedrock.types.automated_reasoning_check_translation_option_list


class AutomatedReasoningCheckTranslationAmbiguousFinding(TypedDict, closed=True):
    options: NotRequired[
        "capo_bedrock.types.automated_reasoning_check_translation_option_list.AutomatedReasoningCheckTranslationOptionList"
    ]
    """<p>Different logical interpretations that were detected during translation of the input.</p>"""
    difference_scenarios: NotRequired[
        "capo_bedrock.types.automated_reasoning_check_difference_scenario_list.AutomatedReasoningCheckDifferenceScenarioList"
    ]
    """<p>Scenarios showing how the different translation options differ in meaning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckTranslationAmbiguousFinding) -> dict:
    out: dict = {}
    if "options" in value:
        import capo_bedrock.types.automated_reasoning_check_translation_option_list

        out["options"] = (
            capo_bedrock.types.automated_reasoning_check_translation_option_list.serialize_json(
                value["options"]
            )
        )
    if "difference_scenarios" in value:
        import capo_bedrock.types.automated_reasoning_check_difference_scenario_list

        out["differenceScenarios"] = (
            capo_bedrock.types.automated_reasoning_check_difference_scenario_list.serialize_json(
                value["difference_scenarios"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningCheckTranslationAmbiguousFinding:
    out: AutomatedReasoningCheckTranslationAmbiguousFinding = {}  # type: ignore[typeddict-item]
    if data.get("options") is not None:
        import capo_bedrock.types.automated_reasoning_check_translation_option_list

        out["options"] = (
            capo_bedrock.types.automated_reasoning_check_translation_option_list.deserialize_json(
                data["options"]
            )
        )
    if data.get("differenceScenarios") is not None:
        import capo_bedrock.types.automated_reasoning_check_difference_scenario_list

        out["difference_scenarios"] = (
            capo_bedrock.types.automated_reasoning_check_difference_scenario_list.deserialize_json(
                data["differenceScenarios"]
            )
        )
    return out


def redact_sensitive(
    value: AutomatedReasoningCheckTranslationAmbiguousFinding,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "options" in value:
        import capo_bedrock.types.automated_reasoning_check_translation_option_list

        out["options"] = (
            capo_bedrock.types.automated_reasoning_check_translation_option_list.redact_sensitive(
                value["options"]
            )
        )
    if "difference_scenarios" in value:
        import capo_bedrock.types.automated_reasoning_check_difference_scenario_list

        out["difference_scenarios"] = (
            capo_bedrock.types.automated_reasoning_check_difference_scenario_list.redact_sensitive(
                value["difference_scenarios"]
            )
        )
    return out
