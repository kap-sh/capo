"""Generated from Smithy shape ``com.amazonaws.elementalinference#ChooseOneOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elementalinference.types.question_option

ChooseOneOptionList: TypeAlias = list[
    "capo_elementalinference.types.question_option.QuestionOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChooseOneOptionList) -> list:
    import capo_elementalinference.types.question_option

    out: list = []
    for item in value:
        out.append(capo_elementalinference.types.question_option.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChooseOneOptionList:
    import capo_elementalinference.types.question_option

    out: ChooseOneOptionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_elementalinference.types.question_option.deserialize_json(item))
    return out
