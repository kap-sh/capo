"""Generated from Smithy shape ``com.amazonaws.elementalinference#QuestionSetVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_elementalinference.types.question_set_sha256
    import capo_elementalinference.types.question_set_version
    import capo_elementalinference.types.question_set_version_description


class QuestionSetVersionSummary(TypedDict, closed=True):
    version: "capo_elementalinference.types.question_set_version.QuestionSetVersion"
    """<p>The version: DRAFT or the number of a published version.</p>"""
    description: NotRequired[
        "capo_elementalinference.types.question_set_version_description.QuestionSetVersionDescription"
    ]
    """<p>The description that you specified when you published this version. Elemental Inference doesn't return this property for DRAFT, or for a version that you published without a description. </p>"""
    sha256: "capo_elementalinference.types.question_set_sha256.QuestionSetSha256"
    """<p>The SHA-256 hash of this version, as 64 lowercase hexadecimal characters. The hash covers the name of the question set and its questions at this version. </p>"""
    last_modified_at: "datetime.datetime"
    """<p>For DRAFT, the time when you created the question set or last updated DRAFT. For a published version, the time when you published it. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuestionSetVersionSummary) -> dict:
    out: dict = {}
    out["version"] = value["version"]
    if "description" in value:
        out["description"] = value["description"]
    out["sha256"] = value["sha256"]
    import capo_elementalinference.types._prelude.timestamp

    out["lastModifiedAt"] = (
        capo_elementalinference.types._prelude.timestamp.serialize_json(
            value["last_modified_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> QuestionSetVersionSummary:
    out: QuestionSetVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("sha256") is not None:
        out["sha256"] = data["sha256"]
    else:
        out["sha256"] = ""
    if data.get("lastModifiedAt") is not None:
        import capo_elementalinference.types._prelude.timestamp

        out["last_modified_at"] = (
            capo_elementalinference.types._prelude.timestamp.deserialize_json(
                data["lastModifiedAt"]
            )
        )
    else:
        import datetime

        out["last_modified_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
