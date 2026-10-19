"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormMultiSelectQuestionAutomationOption``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError
from capo_connect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connect.types.multi_select_question_rule_category_automation


class _EvaluationFormMultiSelectQuestionAutomationOption_RuleCategory(
    TypedDict, closed=True
):
    RuleCategory: "capo_connect.types.multi_select_question_rule_category_automation.MultiSelectQuestionRuleCategoryAutomation"


EvaluationFormMultiSelectQuestionAutomationOption: TypeAlias = (
    _EvaluationFormMultiSelectQuestionAutomationOption_RuleCategory | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormMultiSelectQuestionAutomationOption) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"EvaluationFormMultiSelectQuestionAutomationOption: cannot serialize unknown variant {value.name!r}"
        )
    elif "RuleCategory" in value:
        import capo_connect.types.multi_select_question_rule_category_automation

        return {
            "RuleCategory": capo_connect.types.multi_select_question_rule_category_automation.serialize_json(
                value["RuleCategory"]
            )
        }
    else:
        raise SerializationError(
            "EvaluationFormMultiSelectQuestionAutomationOption: no variant present"
        )


def deserialize_json(data: dict) -> EvaluationFormMultiSelectQuestionAutomationOption:
    if data.get("RuleCategory") is not None:
        import capo_connect.types.multi_select_question_rule_category_automation

        return {
            "RuleCategory": capo_connect.types.multi_select_question_rule_category_automation.deserialize_json(
                data["RuleCategory"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "EvaluationFormMultiSelectQuestionAutomationOption: no recognized variant key"
        )
