"""Generated from Smithy shape ``com.amazonaws.textract#AnalyzeIDDetections``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.normalized_value
    import capo_textract.types.percent
    import capo_textract.types.string


class AnalyzeIDDetections(TypedDict, closed=True):
    text: "capo_textract.types.string.String"
    """<p>Text of either the normalized field or value associated with it.</p>"""
    normalized_value: NotRequired[
        "capo_textract.types.normalized_value.NormalizedValue"
    ]
    """<p>Only returned for dates, returns the type of value detected and the date written in a more machine readable way.</p>"""
    confidence: NotRequired["capo_textract.types.percent.Percent"]
    """<p>The confidence score of the detected text.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalyzeIDDetections) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    if "normalized_value" in value:
        import capo_textract.types.normalized_value

        out["NormalizedValue"] = (
            capo_textract.types.normalized_value.serialize_aws_json_1_1(
                value["normalized_value"]
            )
        )
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


def deserialize_aws_json_1_1(data: dict) -> AnalyzeIDDetections:
    out: AnalyzeIDDetections = {}  # type: ignore[typeddict-item]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    else:
        out["text"] = ""
    if data.get("NormalizedValue") is not None:
        import capo_textract.types.normalized_value

        out["normalized_value"] = (
            capo_textract.types.normalized_value.deserialize_aws_json_1_1(
                data["NormalizedValue"]
            )
        )
    if data.get("Confidence") is not None:
        out["confidence"] = float(data["Confidence"])
    return out
