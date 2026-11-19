"""Generated from Smithy shape ``com.amazonaws.elementalinference#DeleteQuestionSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.question_set_id


class DeleteQuestionSetRequest(TypedDict, closed=True):
    id: "capo_elementalinference.types.question_set_id.QuestionSetId"
    """<p>The ID of the question set to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteQuestionSetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteQuestionSetRequest:
    out: DeleteQuestionSetRequest = {}  # type: ignore[typeddict-item]
    return out
