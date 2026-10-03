"""Generated from Smithy shape ``com.amazonaws.comprehend#SyntaxToken``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.integer
    import capo_comprehend.types.part_of_speech_tag
    import capo_comprehend.types.string


class SyntaxToken(TypedDict, closed=True):
    token_id: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>A unique identifier for a token.</p>"""
    text: NotRequired["capo_comprehend.types.string.String"]
    """<p>The word that was recognized in the source text.</p>"""
    begin_offset: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>The zero-based offset from the beginning of the source text to the first character in the word.</p>"""
    end_offset: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>The zero-based offset from the beginning of the source text to the last character in the word.</p>"""
    part_of_speech: NotRequired[
        "capo_comprehend.types.part_of_speech_tag.PartOfSpeechTag"
    ]
    """<p>Provides the part of speech label and the confidence level that Amazon Comprehend has that the part of speech was correctly identified. For more information, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/how-syntax.html">Syntax</a> in the Comprehend Developer Guide. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SyntaxToken) -> dict:
    out: dict = {}
    if "token_id" in value:
        out["TokenId"] = value["token_id"]
    if "text" in value:
        out["Text"] = value["text"]
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    if "part_of_speech" in value:
        import capo_comprehend.types.part_of_speech_tag

        out["PartOfSpeech"] = (
            capo_comprehend.types.part_of_speech_tag.serialize_aws_json_1_1(
                value["part_of_speech"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SyntaxToken:
    out: SyntaxToken = {}  # type: ignore[typeddict-item]
    if data.get("TokenId") is not None:
        out["token_id"] = data["TokenId"]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("BeginOffset") is not None:
        out["begin_offset"] = data["BeginOffset"]
    if data.get("EndOffset") is not None:
        out["end_offset"] = data["EndOffset"]
    if data.get("PartOfSpeech") is not None:
        import capo_comprehend.types.part_of_speech_tag

        out["part_of_speech"] = (
            capo_comprehend.types.part_of_speech_tag.deserialize_aws_json_1_1(
                data["PartOfSpeech"]
            )
        )
    return out
