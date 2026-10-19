"""Generated from Smithy shape ``com.amazonaws.connect#MultiSelectQuestionRuleCategoryAutomation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.multi_select_question_rule_category_automation_condition
    import capo_connect.types.multi_select_question_rule_category_automation_label
    import capo_connect.types.reference_id_list


class MultiSelectQuestionRuleCategoryAutomation(TypedDict, closed=True):
    category: "capo_connect.types.multi_select_question_rule_category_automation_label.MultiSelectQuestionRuleCategoryAutomationLabel"
    """<p>The category name for this automation rule.</p>"""
    condition: "capo_connect.types.multi_select_question_rule_category_automation_condition.MultiSelectQuestionRuleCategoryAutomationCondition"
    """<p>The condition for this automation rule.</p>"""
    option_ref_ids: "capo_connect.types.reference_id_list.ReferenceIdList"
    """<p>Reference IDs of options for this automation rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultiSelectQuestionRuleCategoryAutomation) -> dict:
    out: dict = {}
    out["Category"] = value["category"]
    import capo_connect.types.multi_select_question_rule_category_automation_condition

    out["Condition"] = (
        capo_connect.types.multi_select_question_rule_category_automation_condition.serialize_json(
            value["condition"]
        )
    )
    import capo_connect.types.reference_id_list

    out["OptionRefIds"] = capo_connect.types.reference_id_list.serialize_json(
        value["option_ref_ids"]
    )
    return out


def deserialize_json(data: dict) -> MultiSelectQuestionRuleCategoryAutomation:
    out: MultiSelectQuestionRuleCategoryAutomation = {}  # type: ignore[typeddict-item]
    if data.get("Category") is not None:
        out["category"] = data["Category"]
    else:
        out["category"] = ""
    if data.get("Condition") is not None:
        import capo_connect.types.multi_select_question_rule_category_automation_condition

        out["condition"] = (
            capo_connect.types.multi_select_question_rule_category_automation_condition.deserialize_json(
                data["Condition"]
            )
        )
    else:
        import typing

        out["condition"] = typing.cast(
            "capo_connect.types.multi_select_question_rule_category_automation_condition.MultiSelectQuestionRuleCategoryAutomationCondition",
            "",
        )
    if data.get("OptionRefIds") is not None:
        import capo_connect.types.reference_id_list

        out["option_ref_ids"] = capo_connect.types.reference_id_list.deserialize_json(
            data["OptionRefIds"]
        )
    else:
        out["option_ref_ids"] = []
    return out
