"""Generated from Smithy shape ``com.amazonaws.comprehend#BatchDetectKeyPhrasesItemResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.integer
    import capo_comprehend.types.list_of_key_phrases


class BatchDetectKeyPhrasesItemResult(TypedDict, closed=True):
    index: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>The zero-based index of the document in the input list.</p>"""
    key_phrases: NotRequired[
        "capo_comprehend.types.list_of_key_phrases.ListOfKeyPhrases"
    ]
    """<p>One or more <a>KeyPhrase</a> objects, one for each key phrase detected in the document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDetectKeyPhrasesItemResult) -> dict:
    out: dict = {}
    if "index" in value:
        out["Index"] = value["index"]
    if "key_phrases" in value:
        import capo_comprehend.types.list_of_key_phrases

        out["KeyPhrases"] = (
            capo_comprehend.types.list_of_key_phrases.serialize_aws_json_1_1(
                value["key_phrases"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDetectKeyPhrasesItemResult:
    out: BatchDetectKeyPhrasesItemResult = {}  # type: ignore[typeddict-item]
    if data.get("Index") is not None:
        out["index"] = data["Index"]
    if data.get("KeyPhrases") is not None:
        import capo_comprehend.types.list_of_key_phrases

        out["key_phrases"] = (
            capo_comprehend.types.list_of_key_phrases.deserialize_aws_json_1_1(
                data["KeyPhrases"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchDetectKeyPhrasesItemResult) -> dict:
    out: dict = {}
    if "index" in value:
        out["Index"] = value["index"]
    if "key_phrases" in value:
        import capo_comprehend.types.list_of_key_phrases

        out["KeyPhrases"] = capo_comprehend.types.list_of_key_phrases.serialize_cbor(
            value["key_phrases"]
        )
    return out


def deserialize_cbor(data: dict) -> BatchDetectKeyPhrasesItemResult:
    out: BatchDetectKeyPhrasesItemResult = {}  # type: ignore[typeddict-item]
    if data.get("Index") is not None:
        out["index"] = data["Index"]
    if data.get("KeyPhrases") is not None:
        import capo_comprehend.types.list_of_key_phrases

        out["key_phrases"] = capo_comprehend.types.list_of_key_phrases.deserialize_cbor(
            data["KeyPhrases"]
        )
    return out
