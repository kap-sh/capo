"""Generated from Smithy shape ``com.amazonaws.comprehend#ClassifierEvaluationMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.double


class ClassifierEvaluationMetrics(TypedDict, closed=True):
    accuracy: NotRequired["capo_comprehend.types.double.Double"]
    """<p>The fraction of the labels that were correct recognized. It is computed by dividing the number of labels in the test documents that were correctly recognized by the total number of labels in the test documents.</p>"""
    precision: NotRequired["capo_comprehend.types.double.Double"]
    """<p>A measure of the usefulness of the classifier results in the test data. High precision means that the classifier returned substantially more relevant results than irrelevant ones.</p>"""
    recall: NotRequired["capo_comprehend.types.double.Double"]
    """<p>A measure of how complete the classifier results are for the test data. High recall means that the classifier returned most of the relevant results. </p>"""
    f1_score: NotRequired["capo_comprehend.types.double.Double"]
    """<p>A measure of how accurate the classifier results are for the test data. It is derived from the <code>Precision</code> and <code>Recall</code> values. The <code>F1Score</code> is the harmonic average of the two scores. The highest score is 1, and the worst score is 0. </p>"""
    micro_precision: NotRequired["capo_comprehend.types.double.Double"]
    """<p>A measure of the usefulness of the recognizer results in the test data. High precision means that the recognizer returned substantially more relevant results than irrelevant ones. Unlike the Precision metric which comes from averaging the precision of all available labels, this is based on the overall score of all precision scores added together.</p>"""
    micro_recall: NotRequired["capo_comprehend.types.double.Double"]
    """<p>A measure of how complete the classifier results are for the test data. High recall means that the classifier returned most of the relevant results. Specifically, this indicates how many of the correct categories in the text that the model can predict. It is a percentage of correct categories in the text that can found. Instead of averaging the recall scores of all labels (as with Recall), micro Recall is based on the overall score of all recall scores added together.</p>"""
    micro_f1_score: NotRequired["capo_comprehend.types.double.Double"]
    """<p>A measure of how accurate the classifier results are for the test data. It is a combination of the <code>Micro Precision</code> and <code>Micro Recall</code> values. The <code>Micro F1Score</code> is the harmonic mean of the two scores. The highest score is 1, and the worst score is 0.</p>"""
    hamming_loss: NotRequired["capo_comprehend.types.double.Double"]
    """<p>Indicates the fraction of labels that are incorrectly predicted. Also seen as the fraction of wrong labels compared to the total number of labels. Scores closer to zero are better.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClassifierEvaluationMetrics) -> dict:
    out: dict = {}
    if "accuracy" in value:
        out["Accuracy"] = (
            "NaN"
            if value["accuracy"] != value["accuracy"]
            else "Infinity"
            if value["accuracy"] == float("inf")
            else "-Infinity"
            if value["accuracy"] == float("-inf")
            else value["accuracy"]
        )
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
    if "micro_precision" in value:
        out["MicroPrecision"] = (
            "NaN"
            if value["micro_precision"] != value["micro_precision"]
            else "Infinity"
            if value["micro_precision"] == float("inf")
            else "-Infinity"
            if value["micro_precision"] == float("-inf")
            else value["micro_precision"]
        )
    if "micro_recall" in value:
        out["MicroRecall"] = (
            "NaN"
            if value["micro_recall"] != value["micro_recall"]
            else "Infinity"
            if value["micro_recall"] == float("inf")
            else "-Infinity"
            if value["micro_recall"] == float("-inf")
            else value["micro_recall"]
        )
    if "micro_f1_score" in value:
        out["MicroF1Score"] = (
            "NaN"
            if value["micro_f1_score"] != value["micro_f1_score"]
            else "Infinity"
            if value["micro_f1_score"] == float("inf")
            else "-Infinity"
            if value["micro_f1_score"] == float("-inf")
            else value["micro_f1_score"]
        )
    if "hamming_loss" in value:
        out["HammingLoss"] = (
            "NaN"
            if value["hamming_loss"] != value["hamming_loss"]
            else "Infinity"
            if value["hamming_loss"] == float("inf")
            else "-Infinity"
            if value["hamming_loss"] == float("-inf")
            else value["hamming_loss"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClassifierEvaluationMetrics:
    out: ClassifierEvaluationMetrics = {}  # type: ignore[typeddict-item]
    if data.get("Accuracy") is not None:
        out["accuracy"] = float(data["Accuracy"])
    if data.get("Precision") is not None:
        out["precision"] = float(data["Precision"])
    if data.get("Recall") is not None:
        out["recall"] = float(data["Recall"])
    if data.get("F1Score") is not None:
        out["f1_score"] = float(data["F1Score"])
    if data.get("MicroPrecision") is not None:
        out["micro_precision"] = float(data["MicroPrecision"])
    if data.get("MicroRecall") is not None:
        out["micro_recall"] = float(data["MicroRecall"])
    if data.get("MicroF1Score") is not None:
        out["micro_f1_score"] = float(data["MicroF1Score"])
    if data.get("HammingLoss") is not None:
        out["hamming_loss"] = float(data["HammingLoss"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ClassifierEvaluationMetrics) -> dict:
    out: dict = {}
    if "accuracy" in value:
        out["Accuracy"] = value["accuracy"]
    if "precision" in value:
        out["Precision"] = value["precision"]
    if "recall" in value:
        out["Recall"] = value["recall"]
    if "f1_score" in value:
        out["F1Score"] = value["f1_score"]
    if "micro_precision" in value:
        out["MicroPrecision"] = value["micro_precision"]
    if "micro_recall" in value:
        out["MicroRecall"] = value["micro_recall"]
    if "micro_f1_score" in value:
        out["MicroF1Score"] = value["micro_f1_score"]
    if "hamming_loss" in value:
        out["HammingLoss"] = value["hamming_loss"]
    return out


def deserialize_cbor(data: dict) -> ClassifierEvaluationMetrics:
    out: ClassifierEvaluationMetrics = {}  # type: ignore[typeddict-item]
    if data.get("Accuracy") is not None:
        out["accuracy"] = float(data["Accuracy"])
    if data.get("Precision") is not None:
        out["precision"] = float(data["Precision"])
    if data.get("Recall") is not None:
        out["recall"] = float(data["Recall"])
    if data.get("F1Score") is not None:
        out["f1_score"] = float(data["F1Score"])
    if data.get("MicroPrecision") is not None:
        out["micro_precision"] = float(data["MicroPrecision"])
    if data.get("MicroRecall") is not None:
        out["micro_recall"] = float(data["MicroRecall"])
    if data.get("MicroF1Score") is not None:
        out["micro_f1_score"] = float(data["MicroF1Score"])
    if data.get("HammingLoss") is not None:
        out["hamming_loss"] = float(data["HammingLoss"])
    return out
