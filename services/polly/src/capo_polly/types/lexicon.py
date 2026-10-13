"""Generated from Smithy shape ``com.amazonaws.polly#Lexicon``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_polly.types.lexicon_content
    import capo_polly.types.lexicon_name


class Lexicon(TypedDict, closed=True):
    content: NotRequired["capo_polly.types.lexicon_content.LexiconContent"]
    """<p>Lexicon content in string format. The content of a lexicon must be in PLS format.</p>"""
    name: NotRequired["capo_polly.types.lexicon_name.LexiconName"]
    """<p>Name of the lexicon.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Lexicon) -> dict:
    out: dict = {}
    if "content" in value:
        out["Content"] = value["content"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> Lexicon:
    out: Lexicon = {}  # type: ignore[typeddict-item]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out


def redact_sensitive(value: Lexicon) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        out["content"] = "*** Sensitive Data Redacted ***"
    return out
