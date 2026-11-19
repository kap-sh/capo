"""Generated from Smithy shape ``com.amazonaws.elementalinference#DeleteQuestionSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.question_set_arn
    import capo_elementalinference.types.question_set_id


class DeleteQuestionSetResponse(TypedDict, closed=True):
    arn: "capo_elementalinference.types.question_set_arn.QuestionSetArn"
    """<p>The ARN of the deleted question set.</p>"""
    id: "capo_elementalinference.types.question_set_id.QuestionSetId"
    """<p>The ID of the deleted question set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteQuestionSetResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> DeleteQuestionSetResponse:
    out: DeleteQuestionSetResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out
