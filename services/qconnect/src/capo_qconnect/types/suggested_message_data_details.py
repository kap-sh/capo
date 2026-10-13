"""Generated from Smithy shape ``com.amazonaws.qconnect#SuggestedMessageDataDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_sensitive_string


class SuggestedMessageDataDetails(TypedDict, closed=True):
    message_text: (
        "capo_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
    )
    """<p>The text content of the suggested message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuggestedMessageDataDetails) -> dict:
    out: dict = {}
    out["messageText"] = value["message_text"]
    return out


def deserialize_json(data: dict) -> SuggestedMessageDataDetails:
    out: SuggestedMessageDataDetails = {}  # type: ignore[typeddict-item]
    if data.get("messageText") is not None:
        out["message_text"] = data["messageText"]
    else:
        raise DeserializationError("SuggestedMessageDataDetails.message_text required")
    return out


def redact_sensitive(value: SuggestedMessageDataDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "message_text" in value:
        out["message_text"] = "*** Sensitive Data Redacted ***"
    return out
