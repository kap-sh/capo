"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormSingleSelectQuestionAutomationOption``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError
from capo_connect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connect.types.single_select_question_rule_category_automation


class _EvaluationFormSingleSelectQuestionAutomationOption_RuleCategory(
    TypedDict, closed=True
):
    RuleCategory: "capo_connect.types.single_select_question_rule_category_automation.SingleSelectQuestionRuleCategoryAutomation"


EvaluationFormSingleSelectQuestionAutomationOption: TypeAlias = (
    _EvaluationFormSingleSelectQuestionAutomationOption_RuleCategory
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormSingleSelectQuestionAutomationOption) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EvaluationFormSingleSelectQuestionAutomationOption: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "RuleCategory" in value:
        import capo_connect.types.single_select_question_rule_category_automation

        return {
            "RuleCategory": capo_connect.types.single_select_question_rule_category_automation.serialize_json(
                value["RuleCategory"]
            )
        }
    else:
        raise SerializationError(
            "EvaluationFormSingleSelectQuestionAutomationOption: no variant present"
        )


def deserialize_json(data: dict) -> EvaluationFormSingleSelectQuestionAutomationOption:
    if data.get("RuleCategory") is not None:
        import capo_connect.types.single_select_question_rule_category_automation

        return {
            "RuleCategory": capo_connect.types.single_select_question_rule_category_automation.deserialize_json(
                data["RuleCategory"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "EvaluationFormSingleSelectQuestionAutomationOption: no recognized variant key"
        )
