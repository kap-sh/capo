"""Generated from Smithy shape ``com.amazonaws.qconnect#NotesChunkDataDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.next_token
    import capo_qconnect.types.non_empty_sensitive_string


class NotesChunkDataDetails(TypedDict, closed=True):
    completion: NotRequired[
        "capo_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
    ]
    """<p>A chunk of the notes completion.</p>"""
    next_chunk_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>The token for the next chunk of notes data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotesChunkDataDetails) -> dict:
    out: dict = {}
    if "completion" in value:
        out["completion"] = value["completion"]
    if "next_chunk_token" in value:
        out["nextChunkToken"] = value["next_chunk_token"]
    return out


def deserialize_json(data: dict) -> NotesChunkDataDetails:
    out: NotesChunkDataDetails = {}  # type: ignore[typeddict-item]
    if data.get("completion") is not None:
        out["completion"] = data["completion"]
    if data.get("nextChunkToken") is not None:
        out["next_chunk_token"] = data["nextChunkToken"]
    return out


def redact_sensitive(value: NotesChunkDataDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "completion" in value:
        out["completion"] = "*** Sensitive Data Redacted ***"
    return out
