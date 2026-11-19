"""Generated from Smithy shape ``com.amazonaws.elementalinference#ListQuestionSetVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.question_set_id


class ListQuestionSetVersionsRequest(TypedDict, closed=True):
    id: "capo_elementalinference.types.question_set_id.QuestionSetId"
    """<p>The ID of the question set whose versions you want to list.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return per API request. Valid range: 1 to 100.</p>"""
    next_token: NotRequired["str"]
    """<p>The token that identifies the next batch of results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQuestionSetVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListQuestionSetVersionsRequest:
    out: ListQuestionSetVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
