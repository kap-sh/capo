"""Generated from Smithy shape ``com.amazonaws.elementalinference#YesNoQuestionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elementalinference.types.yes_no_question

YesNoQuestionList: TypeAlias = list[
    "capo_elementalinference.types.yes_no_question.YesNoQuestion"
]


# --- restJson1 ser/de ---
def serialize_json(value: YesNoQuestionList) -> list:
    import capo_elementalinference.types.yes_no_question

    out: list = []
    for item in value:
        out.append(capo_elementalinference.types.yes_no_question.serialize_json(item))
    return out


def deserialize_json(data: list) -> YesNoQuestionList:
    import capo_elementalinference.types.yes_no_question

    out: YesNoQuestionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_elementalinference.types.yes_no_question.deserialize_json(item))
    return out
