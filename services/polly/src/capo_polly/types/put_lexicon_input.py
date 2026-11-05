"""Generated from Smithy shape ``com.amazonaws.polly#PutLexiconInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_polly.types.lexicon_content
    import capo_polly.types.lexicon_name
    import capo_polly.types.tag_map


class PutLexiconInput(TypedDict, closed=True):
    name: "capo_polly.types.lexicon_name.LexiconName"
    """<p>Name of the lexicon. The name must follow the regular expression format [0-9A-Za-z]{1,20}. That is, the name is a case-sensitive alphanumeric string up to 20 characters long. </p>"""
    content: "capo_polly.types.lexicon_content.LexiconContent"
    """<p>Content of the PLS lexicon as string data.</p>"""
    tags: NotRequired["capo_polly.types.tag_map.TagMap"]
    """<p>The metadata that you apply to the lexicon to help you categorize and organize it. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters. You can't replace the tags of an existing lexicon by overwriting it with PutLexicon.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutLexiconInput) -> dict:
    out: dict = {}
    out["Content"] = value["content"]
    if "tags" in value:
        import capo_polly.types.tag_map

        out["Tags"] = capo_polly.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> PutLexiconInput:
    out: PutLexiconInput = {}  # type: ignore[typeddict-item]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    else:
        out["content"] = ""
    if data.get("Tags") is not None:
        import capo_polly.types.tag_map

        out["tags"] = capo_polly.types.tag_map.deserialize_json(data["Tags"])
    return out


def redact_sensitive(value: PutLexiconInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        out["content"] = "*** Sensitive Data Redacted ***"
    return out
