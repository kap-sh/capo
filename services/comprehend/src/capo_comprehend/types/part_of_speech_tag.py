"""Generated from Smithy shape ``com.amazonaws.comprehend#PartOfSpeechTag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.float
    import capo_comprehend.types.part_of_speech_tag_type


class PartOfSpeechTag(TypedDict, closed=True):
    tag: NotRequired[
        "capo_comprehend.types.part_of_speech_tag_type.PartOfSpeechTagType"
    ]
    """<p>Identifies the part of speech that the token represents.</p>"""
    score: NotRequired["capo_comprehend.types.float.Float"]
    """<p>The confidence that Amazon Comprehend has that the part of speech was correctly identified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartOfSpeechTag) -> dict:
    out: dict = {}
    if "tag" in value:
        import capo_comprehend.types.part_of_speech_tag_type

        out["Tag"] = (
            capo_comprehend.types.part_of_speech_tag_type.serialize_aws_json_1_1(
                value["tag"]
            )
        )
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
    return out


def deserialize_aws_json_1_1(data: dict) -> PartOfSpeechTag:
    out: PartOfSpeechTag = {}  # type: ignore[typeddict-item]
    if data.get("Tag") is not None:
        import capo_comprehend.types.part_of_speech_tag_type

        out["tag"] = (
            capo_comprehend.types.part_of_speech_tag_type.deserialize_aws_json_1_1(
                data["Tag"]
            )
        )
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PartOfSpeechTag) -> dict:
    out: dict = {}
    if "tag" in value:
        import capo_comprehend.types.part_of_speech_tag_type

        out["Tag"] = capo_comprehend.types.part_of_speech_tag_type.serialize_cbor(
            value["tag"]
        )
    if "score" in value:
        out["Score"] = value["score"]
    return out


def deserialize_cbor(data: dict) -> PartOfSpeechTag:
    out: PartOfSpeechTag = {}  # type: ignore[typeddict-item]
    if data.get("Tag") is not None:
        import capo_comprehend.types.part_of_speech_tag_type

        out["tag"] = capo_comprehend.types.part_of_speech_tag_type.deserialize_cbor(
            data["Tag"]
        )
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    return out
