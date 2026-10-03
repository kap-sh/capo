"""Generated from Smithy shape ``com.amazonaws.comprehend#DominantLanguage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.float
    import capo_comprehend.types.string


class DominantLanguage(TypedDict, closed=True):
    language_code: NotRequired["capo_comprehend.types.string.String"]
    """<p>The RFC 5646 language code for the dominant language. For more information about RFC 5646, see <a href="https://tools.ietf.org/html/rfc5646">Tags for Identifying Languages</a> on the <i>IETF Tools</i> web site.</p>"""
    score: NotRequired["capo_comprehend.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of the detection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DominantLanguage) -> dict:
    out: dict = {}
    if "language_code" in value:
        out["LanguageCode"] = value["language_code"]
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


def deserialize_aws_json_1_1(data: dict) -> DominantLanguage:
    out: DominantLanguage = {}  # type: ignore[typeddict-item]
    if data.get("LanguageCode") is not None:
        out["language_code"] = data["LanguageCode"]
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    return out
