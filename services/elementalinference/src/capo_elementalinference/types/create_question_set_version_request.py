"""Generated from Smithy shape ``com.amazonaws.elementalinference#CreateQuestionSetVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.question_set_id
    import capo_elementalinference.types.question_set_sha256
    import capo_elementalinference.types.question_set_version_description


class CreateQuestionSetVersionRequest(TypedDict, closed=True):
    id: "capo_elementalinference.types.question_set_id.QuestionSetId"
    """<p>The ID of the question set whose DRAFT version you want to publish.</p>"""
    sha256: NotRequired[
        "capo_elementalinference.types.question_set_sha256.QuestionSetSha256"
    ]
    """<p>The SHA-256 hash of the DRAFT version that you want to publish, as returned by GetQuestionSet or UpdateQuestionSet. If you specify this value, Elemental Inference publishes DRAFT only if its current hash matches. If it doesn't match, because DRAFT changed after you retrieved it, the request fails with ConflictException. </p> <p>If you don't specify this value, Elemental Inference publishes DRAFT as it is when it receives the request. </p>"""
    description: NotRequired[
        "capo_elementalinference.types.question_set_version_description.QuestionSetVersionDescription"
    ]
    """<p>A description of the new version. You can't change the description after Elemental Inference publishes the version. If DRAFT hasn't changed since the latest version, Elemental Inference ignores this value and returns the latest version with its existing description. </p> <p>The description can be up to 256 characters. It can contain the letters A-Z and a-z, the digits 0-9, underscores, spaces, and the following characters: <code>- . ' , @ : ;</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQuestionSetVersionRequest) -> dict:
    out: dict = {}
    if "sha256" in value:
        out["sha256"] = value["sha256"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateQuestionSetVersionRequest:
    out: CreateQuestionSetVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("sha256") is not None:
        out["sha256"] = data["sha256"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
