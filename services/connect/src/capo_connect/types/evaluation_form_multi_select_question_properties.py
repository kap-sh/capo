"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormMultiSelectQuestionProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_multi_select_question_automation
    import capo_connect.types.evaluation_form_multi_select_question_display_mode
    import capo_connect.types.evaluation_form_multi_select_question_option_list


class EvaluationFormMultiSelectQuestionProperties(TypedDict, closed=True):
    options: "capo_connect.types.evaluation_form_multi_select_question_option_list.EvaluationFormMultiSelectQuestionOptionList"
    """<p>Options available for this multi-select question.</p>"""
    display_as: NotRequired[
        "capo_connect.types.evaluation_form_multi_select_question_display_mode.EvaluationFormMultiSelectQuestionDisplayMode"
    ]
    """<p>Display format for the multi-select question.</p>"""
    automation: NotRequired[
        "capo_connect.types.evaluation_form_multi_select_question_automation.EvaluationFormMultiSelectQuestionAutomation"
    ]
    """<p>Automation configuration for this multi-select question.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormMultiSelectQuestionProperties) -> dict:
    out: dict = {}
    import capo_connect.types.evaluation_form_multi_select_question_option_list

    out["Options"] = (
        capo_connect.types.evaluation_form_multi_select_question_option_list.serialize_json(
            value["options"]
        )
    )
    if "display_as" in value:
        import capo_connect.types.evaluation_form_multi_select_question_display_mode

        out["DisplayAs"] = (
            capo_connect.types.evaluation_form_multi_select_question_display_mode.serialize_json(
                value["display_as"]
            )
        )
    if "automation" in value:
        import capo_connect.types.evaluation_form_multi_select_question_automation

        out["Automation"] = (
            capo_connect.types.evaluation_form_multi_select_question_automation.serialize_json(
                value["automation"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationFormMultiSelectQuestionProperties:
    out: EvaluationFormMultiSelectQuestionProperties = {}  # type: ignore[typeddict-item]
    if data.get("Options") is not None:
        import capo_connect.types.evaluation_form_multi_select_question_option_list

        out["options"] = (
            capo_connect.types.evaluation_form_multi_select_question_option_list.deserialize_json(
                data["Options"]
            )
        )
    else:
        out["options"] = []
    if data.get("DisplayAs") is not None:
        import capo_connect.types.evaluation_form_multi_select_question_display_mode

        out["display_as"] = (
            capo_connect.types.evaluation_form_multi_select_question_display_mode.deserialize_json(
                data["DisplayAs"]
            )
        )
    if data.get("Automation") is not None:
        import capo_connect.types.evaluation_form_multi_select_question_automation

        out["automation"] = (
            capo_connect.types.evaluation_form_multi_select_question_automation.deserialize_json(
                data["Automation"]
            )
        )
    return out
