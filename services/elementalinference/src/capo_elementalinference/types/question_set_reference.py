"""Generated from Smithy shape ``com.amazonaws.elementalinference#QuestionSetReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.question_set_id
    import capo_elementalinference.types.question_set_version


class QuestionSetReference(TypedDict, closed=True):
    question_set_id: "capo_elementalinference.types.question_set_id.QuestionSetId"
    """<p>The ID of the question set. The question set must be in your account.</p>"""
    version: "capo_elementalinference.types.question_set_version.QuestionSetVersion"
    """<p>The version of the question set: DRAFT or the number of a published version. The version must exist. </p> <p>If you specify DRAFT, the output uses the current DRAFT questions and picks up changes that you make later by using UpdateQuestionSet. To keep the questions for the output fixed, specify a published version. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuestionSetReference) -> dict:
    out: dict = {}
    out["questionSetId"] = value["question_set_id"]
    out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> QuestionSetReference:
    out: QuestionSetReference = {}  # type: ignore[typeddict-item]
    if data.get("questionSetId") is not None:
        out["question_set_id"] = data["questionSetId"]
    else:
        out["question_set_id"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    return out
