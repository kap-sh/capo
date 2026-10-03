"""Generated from Smithy shape ``com.amazonaws.securityhub#Note``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class Note(TypedDict, closed=True):
    text: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The text of a note.</p> <p>Length Constraints: Minimum of 1. Maximum of 512.</p>"""
    updated_by: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The principal that created a note.</p>"""
    updated_at: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A timestamp that indicates when the note was updated.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Note) -> dict:
    out: dict = {}
    if "text" in value:
        out["Text"] = value["text"]
    if "updated_by" in value:
        out["UpdatedBy"] = value["updated_by"]
    if "updated_at" in value:
        out["UpdatedAt"] = value["updated_at"]
    return out


def deserialize_json(data: dict) -> Note:
    out: Note = {}  # type: ignore[typeddict-item]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("UpdatedBy") is not None:
        out["updated_by"] = data["UpdatedBy"]
    if data.get("UpdatedAt") is not None:
        out["updated_at"] = data["UpdatedAt"]
    return out
