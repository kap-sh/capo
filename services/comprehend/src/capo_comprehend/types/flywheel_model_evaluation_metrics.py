"""Generated from Smithy shape ``com.amazonaws.comprehend#FlywheelModelEvaluationMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.double


class FlywheelModelEvaluationMetrics(TypedDict, closed=True):
    average_f1_score: NotRequired["capo_comprehend.types.double.Double"]
    """<p>The average F1 score from the evaluation metrics.</p>"""
    average_precision: NotRequired["capo_comprehend.types.double.Double"]
    """<p>Average precision metric for the model.</p>"""
    average_recall: NotRequired["capo_comprehend.types.double.Double"]
    """<p>Average recall metric for the model.</p>"""
    average_accuracy: NotRequired["capo_comprehend.types.double.Double"]
    """<p>Average accuracy metric for the model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlywheelModelEvaluationMetrics) -> dict:
    out: dict = {}
    if "average_f1_score" in value:
        out["AverageF1Score"] = (
            "NaN"
            if value["average_f1_score"] != value["average_f1_score"]
            else "Infinity"
            if value["average_f1_score"] == float("inf")
            else "-Infinity"
            if value["average_f1_score"] == float("-inf")
            else value["average_f1_score"]
        )
    if "average_precision" in value:
        out["AveragePrecision"] = (
            "NaN"
            if value["average_precision"] != value["average_precision"]
            else "Infinity"
            if value["average_precision"] == float("inf")
            else "-Infinity"
            if value["average_precision"] == float("-inf")
            else value["average_precision"]
        )
    if "average_recall" in value:
        out["AverageRecall"] = (
            "NaN"
            if value["average_recall"] != value["average_recall"]
            else "Infinity"
            if value["average_recall"] == float("inf")
            else "-Infinity"
            if value["average_recall"] == float("-inf")
            else value["average_recall"]
        )
    if "average_accuracy" in value:
        out["AverageAccuracy"] = (
            "NaN"
            if value["average_accuracy"] != value["average_accuracy"]
            else "Infinity"
            if value["average_accuracy"] == float("inf")
            else "-Infinity"
            if value["average_accuracy"] == float("-inf")
            else value["average_accuracy"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FlywheelModelEvaluationMetrics:
    out: FlywheelModelEvaluationMetrics = {}  # type: ignore[typeddict-item]
    if data.get("AverageF1Score") is not None:
        out["average_f1_score"] = float(data["AverageF1Score"])
    if data.get("AveragePrecision") is not None:
        out["average_precision"] = float(data["AveragePrecision"])
    if data.get("AverageRecall") is not None:
        out["average_recall"] = float(data["AverageRecall"])
    if data.get("AverageAccuracy") is not None:
        out["average_accuracy"] = float(data["AverageAccuracy"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FlywheelModelEvaluationMetrics) -> dict:
    out: dict = {}
    if "average_f1_score" in value:
        out["AverageF1Score"] = value["average_f1_score"]
    if "average_precision" in value:
        out["AveragePrecision"] = value["average_precision"]
    if "average_recall" in value:
        out["AverageRecall"] = value["average_recall"]
    if "average_accuracy" in value:
        out["AverageAccuracy"] = value["average_accuracy"]
    return out


def deserialize_cbor(data: dict) -> FlywheelModelEvaluationMetrics:
    out: FlywheelModelEvaluationMetrics = {}  # type: ignore[typeddict-item]
    if data.get("AverageF1Score") is not None:
        out["average_f1_score"] = float(data["AverageF1Score"])
    if data.get("AveragePrecision") is not None:
        out["average_precision"] = float(data["AveragePrecision"])
    if data.get("AverageRecall") is not None:
        out["average_recall"] = float(data["AverageRecall"])
    if data.get("AverageAccuracy") is not None:
        out["average_accuracy"] = float(data["AverageAccuracy"])
    return out
