"""Generated from Smithy shape ``com.amazonaws.elementalinference#QuestionSetSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elementalinference.types.question_set_summary

QuestionSetSummaryList: TypeAlias = list[
    "capo_elementalinference.types.question_set_summary.QuestionSetSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuestionSetSummaryList) -> list:
    import capo_elementalinference.types.question_set_summary

    out: list = []
    for item in value:
        out.append(
            capo_elementalinference.types.question_set_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> QuestionSetSummaryList:
    import capo_elementalinference.types.question_set_summary

    out: QuestionSetSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_elementalinference.types.question_set_summary.deserialize_json(item)
        )
    return out
