"""Generated from Smithy shape ``com.amazonaws.textract#ExpenseType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.percent
    import capo_textract.types.string


class ExpenseType(TypedDict, closed=True):
    text: NotRequired["capo_textract.types.string.String"]
    """<p>The word or line of text detected by Amazon Textract.</p>"""
    confidence: NotRequired["capo_textract.types.percent.Percent"]
    """<p>The confidence of accuracy, as a percentage.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpenseType) -> dict:
    out: dict = {}
    if "text" in value:
        out["Text"] = value["text"]
    if "confidence" in value:
        out["Confidence"] = (
            "NaN"
            if value["confidence"] != value["confidence"]
            else "Infinity"
            if value["confidence"] == float("inf")
            else "-Infinity"
            if value["confidence"] == float("-inf")
            else value["confidence"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpenseType:
    out: ExpenseType = {}  # type: ignore[typeddict-item]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("Confidence") is not None:
        out["confidence"] = float(data["Confidence"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExpenseType) -> dict:
    out: dict = {}
    if "text" in value:
        out["Text"] = value["text"]
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    return out


def deserialize_cbor(data: dict) -> ExpenseType:
    out: ExpenseType = {}  # type: ignore[typeddict-item]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("Confidence") is not None:
        out["confidence"] = float(data["Confidence"])
    return out
