"""Generated from Smithy shape ``com.amazonaws.textract#ExpenseCurrency``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.percent
    import capo_textract.types.string


class ExpenseCurrency(TypedDict, closed=True):
    code: NotRequired["capo_textract.types.string.String"]
    """<p>Currency code for detected currency. the current supported codes are:</p> <ul> <li> <p>USD</p> </li> <li> <p>EUR</p> </li> <li> <p>GBP</p> </li> <li> <p>CAD</p> </li> <li> <p>INR</p> </li> <li> <p>JPY</p> </li> <li> <p>CHF</p> </li> <li> <p>AUD</p> </li> <li> <p>CNY</p> </li> <li> <p>BZR</p> </li> <li> <p>SEK</p> </li> <li> <p>HKD</p> </li> </ul>"""
    confidence: NotRequired["capo_textract.types.percent.Percent"]
    """<p>Percentage confideence in the detected currency.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpenseCurrency) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
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


def deserialize_aws_json_1_1(data: dict) -> ExpenseCurrency:
    out: ExpenseCurrency = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Confidence") is not None:
        out["confidence"] = float(data["Confidence"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExpenseCurrency) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    return out


def deserialize_cbor(data: dict) -> ExpenseCurrency:
    out: ExpenseCurrency = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Confidence") is not None:
        out["confidence"] = float(data["Confidence"])
    return out
