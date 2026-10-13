"""Generated from Smithy shape ``com.amazonaws.qconnect#QueryTextInputData``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.query_text


class QueryTextInputData(TypedDict, closed=True):
    text: "capo_qconnect.types.query_text.QueryText"
    """<p>The text to search for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryTextInputData) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> QueryTextInputData:
    out: QueryTextInputData = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        raise DeserializationError("QueryTextInputData.text required")
    return out


def redact_sensitive(value: QueryTextInputData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
