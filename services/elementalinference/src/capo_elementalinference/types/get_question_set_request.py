"""Generated from Smithy shape ``com.amazonaws.elementalinference#GetQuestionSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.question_set_id
    import capo_elementalinference.types.question_set_version


class GetQuestionSetRequest(TypedDict, closed=True):
    id: "capo_elementalinference.types.question_set_id.QuestionSetId"
    """<p>The ID of the question set to retrieve.</p>"""
    question_set_version: NotRequired[
        "capo_elementalinference.types.question_set_version.QuestionSetVersion"
    ]
    """<p>The version of the question set to retrieve: DRAFT or the number of a published version. If you don't specify a version, Elemental Inference returns DRAFT. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQuestionSetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQuestionSetRequest:
    out: GetQuestionSetRequest = {}  # type: ignore[typeddict-item]
    return out
