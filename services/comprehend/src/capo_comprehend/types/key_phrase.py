"""Generated from Smithy shape ``com.amazonaws.comprehend#KeyPhrase``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.float
    import capo_comprehend.types.integer
    import capo_comprehend.types.string


class KeyPhrase(TypedDict, closed=True):
    score: NotRequired["capo_comprehend.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of the detection.</p>"""
    text: NotRequired["capo_comprehend.types.string.String"]
    """<p>The text of a key noun phrase.</p>"""
    begin_offset: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>The zero-based offset from the beginning of the source text to the first character in the key phrase.</p>"""
    end_offset: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>The zero-based offset from the beginning of the source text to the last character in the key phrase.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyPhrase) -> dict:
    out: dict = {}
    if "score" in value:
        out["Score"] = (
            "NaN"
            if value["score"] != value["score"]
            else "Infinity"
            if value["score"] == float("inf")
            else "-Infinity"
            if value["score"] == float("-inf")
            else value["score"]
        )
    if "text" in value:
        out["Text"] = value["text"]
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KeyPhrase:
    out: KeyPhrase = {}  # type: ignore[typeddict-item]
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("BeginOffset") is not None:
        out["begin_offset"] = data["BeginOffset"]
    if data.get("EndOffset") is not None:
        out["end_offset"] = data["EndOffset"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: KeyPhrase) -> dict:
    out: dict = {}
    if "score" in value:
        out["Score"] = value["score"]
    if "text" in value:
        out["Text"] = value["text"]
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    return out


def deserialize_cbor(data: dict) -> KeyPhrase:
    out: KeyPhrase = {}  # type: ignore[typeddict-item]
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("BeginOffset") is not None:
        out["begin_offset"] = data["BeginOffset"]
    if data.get("EndOffset") is not None:
        out["end_offset"] = data["EndOffset"]
    return out
