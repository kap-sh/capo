"""Generated from Smithy shape ``com.amazonaws.comprehend#DetectKeyPhrasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.list_of_key_phrases


class DetectKeyPhrasesResponse(TypedDict, closed=True):
    key_phrases: NotRequired[
        "capo_comprehend.types.list_of_key_phrases.ListOfKeyPhrases"
    ]
    """<p>A collection of key phrases that Amazon Comprehend identified in the input text. For each key phrase, the response provides the text of the key phrase, where the key phrase begins and ends, and the level of confidence that Amazon Comprehend has in the accuracy of the detection. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectKeyPhrasesResponse) -> dict:
    out: dict = {}
    if "key_phrases" in value:
        import capo_comprehend.types.list_of_key_phrases

        out["KeyPhrases"] = (
            capo_comprehend.types.list_of_key_phrases.serialize_aws_json_1_1(
                value["key_phrases"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectKeyPhrasesResponse:
    out: DetectKeyPhrasesResponse = {}  # type: ignore[typeddict-item]
    if data.get("KeyPhrases") is not None:
        import capo_comprehend.types.list_of_key_phrases

        out["key_phrases"] = (
            capo_comprehend.types.list_of_key_phrases.deserialize_aws_json_1_1(
                data["KeyPhrases"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DetectKeyPhrasesResponse) -> dict:
    out: dict = {}
    if "key_phrases" in value:
        import capo_comprehend.types.list_of_key_phrases

        out["KeyPhrases"] = capo_comprehend.types.list_of_key_phrases.serialize_cbor(
            value["key_phrases"]
        )
    return out


def deserialize_cbor(data: dict) -> DetectKeyPhrasesResponse:
    out: DetectKeyPhrasesResponse = {}  # type: ignore[typeddict-item]
    if data.get("KeyPhrases") is not None:
        import capo_comprehend.types.list_of_key_phrases

        out["key_phrases"] = capo_comprehend.types.list_of_key_phrases.deserialize_cbor(
            data["KeyPhrases"]
        )
    return out
