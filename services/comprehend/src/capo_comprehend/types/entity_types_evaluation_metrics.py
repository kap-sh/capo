"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityTypesEvaluationMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.double


class EntityTypesEvaluationMetrics(TypedDict, closed=True):
    precision: NotRequired["capo_comprehend.types.double.Double"]
    """<p>A measure of the usefulness of the recognizer results for a specific entity type in the test data. High precision means that the recognizer returned substantially more relevant results than irrelevant ones. </p>"""
    recall: NotRequired["capo_comprehend.types.double.Double"]
    """<p>A measure of how complete the recognizer results are for a specific entity type in the test data. High recall means that the recognizer returned most of the relevant results.</p>"""
    f1_score: NotRequired["capo_comprehend.types.double.Double"]
    """<p>A measure of how accurate the recognizer results are for a specific entity type in the test data. It is derived from the <code>Precision</code> and <code>Recall</code> values. The <code>F1Score</code> is the harmonic average of the two scores. The highest score is 1, and the worst score is 0. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityTypesEvaluationMetrics) -> dict:
    out: dict = {}
    if "precision" in value:
        out["Precision"] = (
            "NaN"
            if value["precision"] != value["precision"]
            else "Infinity"
            if value["precision"] == float("inf")
            else "-Infinity"
            if value["precision"] == float("-inf")
            else value["precision"]
        )
    if "recall" in value:
        out["Recall"] = (
            "NaN"
            if value["recall"] != value["recall"]
            else "Infinity"
            if value["recall"] == float("inf")
            else "-Infinity"
            if value["recall"] == float("-inf")
            else value["recall"]
        )
    if "f1_score" in value:
        out["F1Score"] = (
            "NaN"
            if value["f1_score"] != value["f1_score"]
            else "Infinity"
            if value["f1_score"] == float("inf")
            else "-Infinity"
            if value["f1_score"] == float("-inf")
            else value["f1_score"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityTypesEvaluationMetrics:
    out: EntityTypesEvaluationMetrics = {}  # type: ignore[typeddict-item]
    if data.get("Precision") is not None:
        out["precision"] = float(data["Precision"])
    if data.get("Recall") is not None:
        out["recall"] = float(data["Recall"])
    if data.get("F1Score") is not None:
        out["f1_score"] = float(data["F1Score"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EntityTypesEvaluationMetrics) -> dict:
    out: dict = {}
    if "precision" in value:
        out["Precision"] = value["precision"]
    if "recall" in value:
        out["Recall"] = value["recall"]
    if "f1_score" in value:
        out["F1Score"] = value["f1_score"]
    return out


def deserialize_cbor(data: dict) -> EntityTypesEvaluationMetrics:
    out: EntityTypesEvaluationMetrics = {}  # type: ignore[typeddict-item]
    if data.get("Precision") is not None:
        out["precision"] = float(data["Precision"])
    if data.get("Recall") is not None:
        out["recall"] = float(data["Recall"])
    if data.get("F1Score") is not None:
        out["f1_score"] = float(data["F1Score"])
    return out
