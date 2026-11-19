"""Generated from Smithy shape ``com.amazonaws.textract#EvaluationMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_textract.types.float


class EvaluationMetric(TypedDict, closed=True):
    f1_score: "capo_textract.types.float.Float"
    """<p>The F1 score for an adapter version.</p>"""
    precision: "capo_textract.types.float.Float"
    """<p>The Precision score for an adapter version.</p>"""
    recall: "capo_textract.types.float.Float"
    """<p>The Recall score for an adapter version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluationMetric) -> dict:
    out: dict = {}
    out["F1Score"] = (
        "NaN"
        if value.get("f1_score", 0) != value.get("f1_score", 0)
        else "Infinity"
        if value.get("f1_score", 0) == float("inf")
        else "-Infinity"
        if value.get("f1_score", 0) == float("-inf")
        else value.get("f1_score", 0)
    )
    out["Precision"] = (
        "NaN"
        if value.get("precision", 0) != value.get("precision", 0)
        else "Infinity"
        if value.get("precision", 0) == float("inf")
        else "-Infinity"
        if value.get("precision", 0) == float("-inf")
        else value.get("precision", 0)
    )
    out["Recall"] = (
        "NaN"
        if value.get("recall", 0) != value.get("recall", 0)
        else "Infinity"
        if value.get("recall", 0) == float("inf")
        else "-Infinity"
        if value.get("recall", 0) == float("-inf")
        else value.get("recall", 0)
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluationMetric:
    out: EvaluationMetric = {}  # type: ignore[typeddict-item]
    if data.get("F1Score") is not None:
        out["f1_score"] = float(data["F1Score"])
    else:
        out["f1_score"] = 0
    if data.get("Precision") is not None:
        out["precision"] = float(data["Precision"])
    else:
        out["precision"] = 0
    if data.get("Recall") is not None:
        out["recall"] = float(data["Recall"])
    else:
        out["recall"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EvaluationMetric) -> dict:
    out: dict = {}
    out["F1Score"] = value.get("f1_score", 0)
    out["Precision"] = value.get("precision", 0)
    out["Recall"] = value.get("recall", 0)
    return out


def deserialize_cbor(data: dict) -> EvaluationMetric:
    out: EvaluationMetric = {}  # type: ignore[typeddict-item]
    if data.get("F1Score") is not None:
        out["f1_score"] = float(data["F1Score"])
    else:
        out["f1_score"] = 0
    if data.get("Precision") is not None:
        out["precision"] = float(data["Precision"])
    else:
        out["precision"] = 0
    if data.get("Recall") is not None:
        out["recall"] = float(data["Recall"])
    else:
        out["recall"] = 0
    return out
