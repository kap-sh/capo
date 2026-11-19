"""Generated from Smithy shape ``com.amazonaws.elementalinference#DeleteQuestionSetVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.published_question_set_version
    import capo_elementalinference.types.question_set_id


class DeleteQuestionSetVersionRequest(TypedDict, closed=True):
    id: "capo_elementalinference.types.question_set_id.QuestionSetId"
    """<p>The ID of the question set that contains the version.</p>"""
    question_set_version: "capo_elementalinference.types.published_question_set_version.PublishedQuestionSetVersion"
    """<p>The number of the published version to delete. You can't specify DRAFT.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteQuestionSetVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteQuestionSetVersionRequest:
    out: DeleteQuestionSetVersionRequest = {}  # type: ignore[typeddict-item]
    return out
