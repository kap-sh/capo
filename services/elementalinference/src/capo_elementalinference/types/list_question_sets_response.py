"""Generated from Smithy shape ``com.amazonaws.elementalinference#ListQuestionSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.question_set_summary_list


class ListQuestionSetsResponse(TypedDict, closed=True):
    question_sets: (
        "capo_elementalinference.types.question_set_summary_list.QuestionSetSummaryList"
    )
    """<p>A list of QuestionSetSummary objects.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to use to retrieve the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQuestionSetsResponse) -> dict:
    out: dict = {}
    import capo_elementalinference.types.question_set_summary_list

    out["questionSets"] = (
        capo_elementalinference.types.question_set_summary_list.serialize_json(
            value["question_sets"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListQuestionSetsResponse:
    out: ListQuestionSetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("questionSets") is not None:
        import capo_elementalinference.types.question_set_summary_list

        out["question_sets"] = (
            capo_elementalinference.types.question_set_summary_list.deserialize_json(
                data["questionSets"]
            )
        )
    else:
        out["question_sets"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
