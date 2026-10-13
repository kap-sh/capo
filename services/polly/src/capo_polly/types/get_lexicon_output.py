"""Generated from Smithy shape ``com.amazonaws.polly#GetLexiconOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_polly.types.lexicon
    import capo_polly.types.lexicon_attributes


class GetLexiconOutput(TypedDict, closed=True):
    lexicon: NotRequired["capo_polly.types.lexicon.Lexicon"]
    """<p>Lexicon object that provides name and the string content of the lexicon. </p>"""
    lexicon_attributes: NotRequired[
        "capo_polly.types.lexicon_attributes.LexiconAttributes"
    ]
    """<p>Metadata of the lexicon, including phonetic alphabetic used, language code, lexicon ARN, number of lexemes defined in the lexicon, and size of lexicon in bytes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLexiconOutput) -> dict:
    out: dict = {}
    if "lexicon" in value:
        import capo_polly.types.lexicon

        out["Lexicon"] = capo_polly.types.lexicon.serialize_json(value["lexicon"])
    if "lexicon_attributes" in value:
        import capo_polly.types.lexicon_attributes

        out["LexiconAttributes"] = capo_polly.types.lexicon_attributes.serialize_json(
            value["lexicon_attributes"]
        )
    return out


def deserialize_json(data: dict) -> GetLexiconOutput:
    out: GetLexiconOutput = {}  # type: ignore[typeddict-item]
    if data.get("Lexicon") is not None:
        import capo_polly.types.lexicon

        out["lexicon"] = capo_polly.types.lexicon.deserialize_json(data["Lexicon"])
    if data.get("LexiconAttributes") is not None:
        import capo_polly.types.lexicon_attributes

        out["lexicon_attributes"] = (
            capo_polly.types.lexicon_attributes.deserialize_json(
                data["LexiconAttributes"]
            )
        )
    return out


def redact_sensitive(value: GetLexiconOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "lexicon" in value:
        import capo_polly.types.lexicon

        out["lexicon"] = capo_polly.types.lexicon.redact_sensitive(value["lexicon"])
    return out
