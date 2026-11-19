"""Generated from Smithy shape ``com.amazonaws.comprehend#SentimentScore``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.float


class SentimentScore(TypedDict, closed=True):
    positive: NotRequired["capo_comprehend.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of its detection of the <code>POSITIVE</code> sentiment.</p>"""
    negative: NotRequired["capo_comprehend.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of its detection of the <code>NEGATIVE</code> sentiment.</p>"""
    neutral: NotRequired["capo_comprehend.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of its detection of the <code>NEUTRAL</code> sentiment.</p>"""
    mixed: NotRequired["capo_comprehend.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of its detection of the <code>MIXED</code> sentiment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SentimentScore) -> dict:
    out: dict = {}
    if "positive" in value:
        out["Positive"] = (
            "NaN"
            if value["positive"] != value["positive"]
            else "Infinity"
            if value["positive"] == float("inf")
            else "-Infinity"
            if value["positive"] == float("-inf")
            else value["positive"]
        )
    if "negative" in value:
        out["Negative"] = (
            "NaN"
            if value["negative"] != value["negative"]
            else "Infinity"
            if value["negative"] == float("inf")
            else "-Infinity"
            if value["negative"] == float("-inf")
            else value["negative"]
        )
    if "neutral" in value:
        out["Neutral"] = (
            "NaN"
            if value["neutral"] != value["neutral"]
            else "Infinity"
            if value["neutral"] == float("inf")
            else "-Infinity"
            if value["neutral"] == float("-inf")
            else value["neutral"]
        )
    if "mixed" in value:
        out["Mixed"] = (
            "NaN"
            if value["mixed"] != value["mixed"]
            else "Infinity"
            if value["mixed"] == float("inf")
            else "-Infinity"
            if value["mixed"] == float("-inf")
            else value["mixed"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SentimentScore:
    out: SentimentScore = {}  # type: ignore[typeddict-item]
    if data.get("Positive") is not None:
        out["positive"] = float(data["Positive"])
    if data.get("Negative") is not None:
        out["negative"] = float(data["Negative"])
    if data.get("Neutral") is not None:
        out["neutral"] = float(data["Neutral"])
    if data.get("Mixed") is not None:
        out["mixed"] = float(data["Mixed"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SentimentScore) -> dict:
    out: dict = {}
    if "positive" in value:
        out["Positive"] = value["positive"]
    if "negative" in value:
        out["Negative"] = value["negative"]
    if "neutral" in value:
        out["Neutral"] = value["neutral"]
    if "mixed" in value:
        out["Mixed"] = value["mixed"]
    return out


def deserialize_cbor(data: dict) -> SentimentScore:
    out: SentimentScore = {}  # type: ignore[typeddict-item]
    if data.get("Positive") is not None:
        out["positive"] = float(data["Positive"])
    if data.get("Negative") is not None:
        out["negative"] = float(data["Negative"])
    if data.get("Neutral") is not None:
        out["neutral"] = float(data["Neutral"])
    if data.get("Mixed") is not None:
        out["mixed"] = float(data["Mixed"])
    return out
