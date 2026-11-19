"""Generated from Smithy shape ``com.amazonaws.comprehend#BatchDetectDominantLanguageItemResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.integer
    import capo_comprehend.types.list_of_dominant_languages


class BatchDetectDominantLanguageItemResult(TypedDict, closed=True):
    index: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>The zero-based index of the document in the input list.</p>"""
    languages: NotRequired[
        "capo_comprehend.types.list_of_dominant_languages.ListOfDominantLanguages"
    ]
    """<p>One or more <a>DominantLanguage</a> objects describing the dominant languages in the document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDetectDominantLanguageItemResult) -> dict:
    out: dict = {}
    if "index" in value:
        out["Index"] = value["index"]
    if "languages" in value:
        import capo_comprehend.types.list_of_dominant_languages

        out["Languages"] = (
            capo_comprehend.types.list_of_dominant_languages.serialize_aws_json_1_1(
                value["languages"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDetectDominantLanguageItemResult:
    out: BatchDetectDominantLanguageItemResult = {}  # type: ignore[typeddict-item]
    if data.get("Index") is not None:
        out["index"] = data["Index"]
    if data.get("Languages") is not None:
        import capo_comprehend.types.list_of_dominant_languages

        out["languages"] = (
            capo_comprehend.types.list_of_dominant_languages.deserialize_aws_json_1_1(
                data["Languages"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchDetectDominantLanguageItemResult) -> dict:
    out: dict = {}
    if "index" in value:
        out["Index"] = value["index"]
    if "languages" in value:
        import capo_comprehend.types.list_of_dominant_languages

        out["Languages"] = (
            capo_comprehend.types.list_of_dominant_languages.serialize_cbor(
                value["languages"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> BatchDetectDominantLanguageItemResult:
    out: BatchDetectDominantLanguageItemResult = {}  # type: ignore[typeddict-item]
    if data.get("Index") is not None:
        out["index"] = data["Index"]
    if data.get("Languages") is not None:
        import capo_comprehend.types.list_of_dominant_languages

        out["languages"] = (
            capo_comprehend.types.list_of_dominant_languages.deserialize_cbor(
                data["Languages"]
            )
        )
    return out
