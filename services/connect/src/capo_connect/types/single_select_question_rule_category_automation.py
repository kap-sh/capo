"""Generated from Smithy shape ``com.amazonaws.connect#SingleSelectQuestionRuleCategoryAutomation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.reference_id
    import capo_connect.types.single_select_question_rule_category_automation_condition
    import capo_connect.types.single_select_question_rule_category_automation_label


class SingleSelectQuestionRuleCategoryAutomation(TypedDict, closed=True):
    category: "capo_connect.types.single_select_question_rule_category_automation_label.SingleSelectQuestionRuleCategoryAutomationLabel"
    """<p> The category name, as defined in Rules.</p>"""
    condition: "capo_connect.types.single_select_question_rule_category_automation_condition.SingleSelectQuestionRuleCategoryAutomationCondition"
    """<p>The condition to apply for the automation option. If the condition is <code>PRESENT</code>, then the option is applied when the contact data includes the category. Similarly, if the condition is <code>NOT_PRESENT</code>, then the option is applied when the contact data does not include the category.</p>"""
    option_ref_id: "capo_connect.types.reference_id.ReferenceId"
    """<p>The identifier of the answer option.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SingleSelectQuestionRuleCategoryAutomation) -> dict:
    out: dict = {}
    out["Category"] = value["category"]
    import capo_connect.types.single_select_question_rule_category_automation_condition

    out["Condition"] = (
        capo_connect.types.single_select_question_rule_category_automation_condition.serialize_json(
            value["condition"]
        )
    )
    out["OptionRefId"] = value["option_ref_id"]
    return out


def deserialize_json(data: dict) -> SingleSelectQuestionRuleCategoryAutomation:
    out: SingleSelectQuestionRuleCategoryAutomation = {}  # type: ignore[typeddict-item]
    if data.get("Category") is not None:
        out["category"] = data["Category"]
    else:
        out["category"] = ""
    if data.get("Condition") is not None:
        import capo_connect.types.single_select_question_rule_category_automation_condition

        out["condition"] = (
            capo_connect.types.single_select_question_rule_category_automation_condition.deserialize_json(
                data["Condition"]
            )
        )
    else:
        import typing

        out["condition"] = typing.cast(
            "capo_connect.types.single_select_question_rule_category_automation_condition.SingleSelectQuestionRuleCategoryAutomationCondition",
            "",
        )
    if data.get("OptionRefId") is not None:
        out["option_ref_id"] = data["OptionRefId"]
    else:
        out["option_ref_id"] = ""
    return out
