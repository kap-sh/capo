"""Generated from Smithy shape ``com.amazonaws.elementalinference#QuestionSetVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elementalinference.types.question_set_version_summary

QuestionSetVersionSummaryList: TypeAlias = list[
    "capo_elementalinference.types.question_set_version_summary.QuestionSetVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuestionSetVersionSummaryList) -> list:
    import capo_elementalinference.types.question_set_version_summary

    out: list = []
    for item in value:
        out.append(
            capo_elementalinference.types.question_set_version_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> QuestionSetVersionSummaryList:
    import capo_elementalinference.types.question_set_version_summary

    out: QuestionSetVersionSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_elementalinference.types.question_set_version_summary.deserialize_json(
                item
            )
        )
    return out
