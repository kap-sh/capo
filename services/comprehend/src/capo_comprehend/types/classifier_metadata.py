"""Generated from Smithy shape ``com.amazonaws.comprehend#ClassifierMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.classifier_evaluation_metrics
    import capo_comprehend.types.integer


class ClassifierMetadata(TypedDict, closed=True):
    number_of_labels: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>The number of labels in the input data. </p>"""
    number_of_trained_documents: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>The number of documents in the input data that were used to train the classifier. Typically this is 80 to 90 percent of the input documents.</p>"""
    number_of_test_documents: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>The number of documents in the input data that were used to test the classifier. Typically this is 10 to 20 percent of the input documents, up to 10,000 documents.</p>"""
    evaluation_metrics: NotRequired[
        "capo_comprehend.types.classifier_evaluation_metrics.ClassifierEvaluationMetrics"
    ]
    """<p> Describes the result metrics for the test data associated with an documentation classifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClassifierMetadata) -> dict:
    out: dict = {}
    if "number_of_labels" in value:
        out["NumberOfLabels"] = value["number_of_labels"]
    if "number_of_trained_documents" in value:
        out["NumberOfTrainedDocuments"] = value["number_of_trained_documents"]
    if "number_of_test_documents" in value:
        out["NumberOfTestDocuments"] = value["number_of_test_documents"]
    if "evaluation_metrics" in value:
        import capo_comprehend.types.classifier_evaluation_metrics

        out["EvaluationMetrics"] = (
            capo_comprehend.types.classifier_evaluation_metrics.serialize_aws_json_1_1(
                value["evaluation_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClassifierMetadata:
    out: ClassifierMetadata = {}  # type: ignore[typeddict-item]
    if data.get("NumberOfLabels") is not None:
        out["number_of_labels"] = data["NumberOfLabels"]
    if data.get("NumberOfTrainedDocuments") is not None:
        out["number_of_trained_documents"] = data["NumberOfTrainedDocuments"]
    if data.get("NumberOfTestDocuments") is not None:
        out["number_of_test_documents"] = data["NumberOfTestDocuments"]
    if data.get("EvaluationMetrics") is not None:
        import capo_comprehend.types.classifier_evaluation_metrics

        out["evaluation_metrics"] = (
            capo_comprehend.types.classifier_evaluation_metrics.deserialize_aws_json_1_1(
                data["EvaluationMetrics"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ClassifierMetadata) -> dict:
    out: dict = {}
    if "number_of_labels" in value:
        out["NumberOfLabels"] = value["number_of_labels"]
    if "number_of_trained_documents" in value:
        out["NumberOfTrainedDocuments"] = value["number_of_trained_documents"]
    if "number_of_test_documents" in value:
        out["NumberOfTestDocuments"] = value["number_of_test_documents"]
    if "evaluation_metrics" in value:
        import capo_comprehend.types.classifier_evaluation_metrics

        out["EvaluationMetrics"] = (
            capo_comprehend.types.classifier_evaluation_metrics.serialize_cbor(
                value["evaluation_metrics"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ClassifierMetadata:
    out: ClassifierMetadata = {}  # type: ignore[typeddict-item]
    if data.get("NumberOfLabels") is not None:
        out["number_of_labels"] = data["NumberOfLabels"]
    if data.get("NumberOfTrainedDocuments") is not None:
        out["number_of_trained_documents"] = data["NumberOfTrainedDocuments"]
    if data.get("NumberOfTestDocuments") is not None:
        out["number_of_test_documents"] = data["NumberOfTestDocuments"]
    if data.get("EvaluationMetrics") is not None:
        import capo_comprehend.types.classifier_evaluation_metrics

        out["evaluation_metrics"] = (
            capo_comprehend.types.classifier_evaluation_metrics.deserialize_cbor(
                data["EvaluationMetrics"]
            )
        )
    return out
