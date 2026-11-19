"""Generated from Smithy shape ``com.amazonaws.elementalinference#ListQuestionSetVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.question_set_version_summary_list


class ListQuestionSetVersionsResponse(TypedDict, closed=True):
    versions: "capo_elementalinference.types.question_set_version_summary_list.QuestionSetVersionSummaryList"
    """<p>A list of QuestionSetVersionSummary objects.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to use to retrieve the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQuestionSetVersionsResponse) -> dict:
    out: dict = {}
    import capo_elementalinference.types.question_set_version_summary_list

    out["versions"] = (
        capo_elementalinference.types.question_set_version_summary_list.serialize_json(
            value["versions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListQuestionSetVersionsResponse:
    out: ListQuestionSetVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("versions") is not None:
        import capo_elementalinference.types.question_set_version_summary_list

        out["versions"] = (
            capo_elementalinference.types.question_set_version_summary_list.deserialize_json(
                data["versions"]
            )
        )
    else:
        out["versions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
