"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#Characters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.integer


class Characters(TypedDict, closed=True):
    original_text_characters: NotRequired[
        "capo_comprehendmedical.types.integer.Integer"
    ]
    """<p> The number of characters present in the input text document as processed by Amazon Comprehend Medical. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Characters) -> dict:
    out: dict = {}
    if "original_text_characters" in value:
        out["OriginalTextCharacters"] = value["original_text_characters"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Characters:
    out: Characters = {}  # type: ignore[typeddict-item]
    if data.get("OriginalTextCharacters") is not None:
        out["original_text_characters"] = data["OriginalTextCharacters"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Characters) -> dict:
    out: dict = {}
    if "original_text_characters" in value:
        out["OriginalTextCharacters"] = value["original_text_characters"]
    return out


def deserialize_cbor(data: dict) -> Characters:
    out: Characters = {}  # type: ignore[typeddict-item]
    if data.get("OriginalTextCharacters") is not None:
        out["original_text_characters"] = data["OriginalTextCharacters"]
    return out
