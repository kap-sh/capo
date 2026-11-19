"""Generated from Smithy shape ``com.amazonaws.elementalinference#ChooseOneQuestionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elementalinference.types.choose_one_question

ChooseOneQuestionList: TypeAlias = list[
    "capo_elementalinference.types.choose_one_question.ChooseOneQuestion"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChooseOneQuestionList) -> list:
    import capo_elementalinference.types.choose_one_question

    out: list = []
    for item in value:
        out.append(
            capo_elementalinference.types.choose_one_question.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ChooseOneQuestionList:
    import capo_elementalinference.types.choose_one_question

    out: ChooseOneQuestionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_elementalinference.types.choose_one_question.deserialize_json(item)
        )
    return out
