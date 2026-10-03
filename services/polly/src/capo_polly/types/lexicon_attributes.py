"""Generated from Smithy shape ``com.amazonaws.polly#LexiconAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_polly.types.alphabet
    import capo_polly.types.language_code
    import capo_polly.types.last_modified
    import capo_polly.types.lexemes_count
    import capo_polly.types.lexicon_arn
    import capo_polly.types.size


class LexiconAttributes(TypedDict, closed=True):
    alphabet: NotRequired["capo_polly.types.alphabet.Alphabet"]
    """<p>Phonetic alphabet used in the lexicon. Valid values are <code>ipa</code> and <code>x-sampa</code>.</p>"""
    language_code: NotRequired["capo_polly.types.language_code.LanguageCode"]
    """<p>Language code that the lexicon applies to. A lexicon with a language code such as "en" would be applied to all English languages (en-GB, en-US, en-AUS, en-WLS, and so on.</p>"""
    last_modified: NotRequired["capo_polly.types.last_modified.LastModified"]
    """<p>Date lexicon was last modified (a timestamp value).</p>"""
    lexicon_arn: NotRequired["capo_polly.types.lexicon_arn.LexiconArn"]
    """<p>Amazon Resource Name (ARN) of the lexicon.</p>"""
    lexemes_count: "capo_polly.types.lexemes_count.LexemesCount"
    """<p>Number of lexemes in the lexicon.</p>"""
    size: "capo_polly.types.size.Size"
    """<p>Total size of the lexicon, in characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LexiconAttributes) -> dict:
    out: dict = {}
    if "alphabet" in value:
        out["Alphabet"] = value["alphabet"]
    if "language_code" in value:
        import capo_polly.types.language_code

        out["LanguageCode"] = capo_polly.types.language_code.serialize_json(
            value["language_code"]
        )
    if "last_modified" in value:
        import capo_polly.types.last_modified

        out["LastModified"] = capo_polly.types.last_modified.serialize_json(
            value["last_modified"]
        )
    if "lexicon_arn" in value:
        out["LexiconArn"] = value["lexicon_arn"]
    out["LexemesCount"] = value.get("lexemes_count", 0)
    out["Size"] = value.get("size", 0)
    return out


def deserialize_json(data: dict) -> LexiconAttributes:
    out: LexiconAttributes = {}  # type: ignore[typeddict-item]
    if data.get("Alphabet") is not None:
        out["alphabet"] = data["Alphabet"]
    if data.get("LanguageCode") is not None:
        import capo_polly.types.language_code

        out["language_code"] = capo_polly.types.language_code.deserialize_json(
            data["LanguageCode"]
        )
    if data.get("LastModified") is not None:
        import capo_polly.types.last_modified

        out["last_modified"] = capo_polly.types.last_modified.deserialize_json(
            data["LastModified"]
        )
    if data.get("LexiconArn") is not None:
        out["lexicon_arn"] = data["LexiconArn"]
    if data.get("LexemesCount") is not None:
        out["lexemes_count"] = data["LexemesCount"]
    else:
        out["lexemes_count"] = 0
    if data.get("Size") is not None:
        out["size"] = data["Size"]
    else:
        out["size"] = 0
    return out
