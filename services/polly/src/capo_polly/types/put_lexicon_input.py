"""Generated from Smithy shape ``com.amazonaws.polly#PutLexiconInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_polly.types.lexicon_content
    import capo_polly.types.lexicon_name


class PutLexiconInput(TypedDict, closed=True):
    name: "capo_polly.types.lexicon_name.LexiconName"
    """<p>Name of the lexicon. The name must follow the regular express format [0-9A-Za-z]{1,20}. That is, the name is a case-sensitive alphanumeric string up to 20 characters long. </p>"""
    content: "capo_polly.types.lexicon_content.LexiconContent"
    """<p>Content of the PLS lexicon as string data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutLexiconInput) -> dict:
    out: dict = {}
    out["Content"] = value["content"]
    return out


def deserialize_json(data: dict) -> PutLexiconInput:
    out: PutLexiconInput = {}  # type: ignore[typeddict-item]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    else:
        out["content"] = ""
    return out


def redact_sensitive(value: PutLexiconInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        out["content"] = "*** Sensitive Data Redacted ***"
    return out
