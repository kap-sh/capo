"""Generated from Smithy shape ``com.amazonaws.elementalinference#YesNoPerOptionOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elementalinference.types.question_option

YesNoPerOptionOptionList: TypeAlias = list[
    "capo_elementalinference.types.question_option.QuestionOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: YesNoPerOptionOptionList) -> list:
    import capo_elementalinference.types.question_option

    out: list = []
    for item in value:
        out.append(capo_elementalinference.types.question_option.serialize_json(item))
    return out


def deserialize_json(data: list) -> YesNoPerOptionOptionList:
    import capo_elementalinference.types.question_option

    out: YesNoPerOptionOptionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_elementalinference.types.question_option.deserialize_json(item))
    return out
