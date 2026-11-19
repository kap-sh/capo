"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormMultiSelectQuestionAutomation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_multi_select_question_automation_option_list
    import capo_connect.types.evaluation_form_question_automation_answer_source
    import capo_connect.types.reference_id_list


class EvaluationFormMultiSelectQuestionAutomation(TypedDict, closed=True):
    options: NotRequired[
        "capo_connect.types.evaluation_form_multi_select_question_automation_option_list.EvaluationFormMultiSelectQuestionAutomationOptionList"
    ]
    """<p>Automation options for the multi-select question.</p>"""
    default_option_ref_ids: NotRequired[
        "capo_connect.types.reference_id_list.ReferenceIdList"
    ]
    """<p>Reference IDs of default options.</p>"""
    answer_source: NotRequired[
        "capo_connect.types.evaluation_form_question_automation_answer_source.EvaluationFormQuestionAutomationAnswerSource"
    ]
    """<p>Automation answer source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormMultiSelectQuestionAutomation) -> dict:
    out: dict = {}
    if "options" in value:
        import capo_connect.types.evaluation_form_multi_select_question_automation_option_list

        out["Options"] = (
            capo_connect.types.evaluation_form_multi_select_question_automation_option_list.serialize_json(
                value["options"]
            )
        )
    if "default_option_ref_ids" in value:
        import capo_connect.types.reference_id_list

        out["DefaultOptionRefIds"] = (
            capo_connect.types.reference_id_list.serialize_json(
                value["default_option_ref_ids"]
            )
        )
    if "answer_source" in value:
        import capo_connect.types.evaluation_form_question_automation_answer_source

        out["AnswerSource"] = (
            capo_connect.types.evaluation_form_question_automation_answer_source.serialize_json(
                value["answer_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationFormMultiSelectQuestionAutomation:
    out: EvaluationFormMultiSelectQuestionAutomation = {}  # type: ignore[typeddict-item]
    if data.get("Options") is not None:
        import capo_connect.types.evaluation_form_multi_select_question_automation_option_list

        out["options"] = (
            capo_connect.types.evaluation_form_multi_select_question_automation_option_list.deserialize_json(
                data["Options"]
            )
        )
    if data.get("DefaultOptionRefIds") is not None:
        import capo_connect.types.reference_id_list

        out["default_option_ref_ids"] = (
            capo_connect.types.reference_id_list.deserialize_json(
                data["DefaultOptionRefIds"]
            )
        )
    if data.get("AnswerSource") is not None:
        import capo_connect.types.evaluation_form_question_automation_answer_source

        out["answer_source"] = (
            capo_connect.types.evaluation_form_question_automation_answer_source.deserialize_json(
                data["AnswerSource"]
            )
        )
    return out
