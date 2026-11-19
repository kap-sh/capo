"""Generated from Smithy shape ``com.amazonaws.elementalinference#YesNoPerOptionQuestionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elementalinference.types.yes_no_per_option_question

YesNoPerOptionQuestionList: TypeAlias = list[
    "capo_elementalinference.types.yes_no_per_option_question.YesNoPerOptionQuestion"
]


# --- restJson1 ser/de ---
def serialize_json(value: YesNoPerOptionQuestionList) -> list:
    import capo_elementalinference.types.yes_no_per_option_question

    out: list = []
    for item in value:
        out.append(
            capo_elementalinference.types.yes_no_per_option_question.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> YesNoPerOptionQuestionList:
    import capo_elementalinference.types.yes_no_per_option_question

    out: YesNoPerOptionQuestionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_elementalinference.types.yes_no_per_option_question.deserialize_json(
                item
            )
        )
    return out
