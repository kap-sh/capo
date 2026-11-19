"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognizerMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.entity_recognizer_evaluation_metrics
    import capo_comprehend.types.entity_recognizer_metadata_entity_types_list
    import capo_comprehend.types.integer


class EntityRecognizerMetadata(TypedDict, closed=True):
    number_of_trained_documents: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p> The number of documents in the input data that were used to train the entity recognizer. Typically this is 80 to 90 percent of the input documents.</p>"""
    number_of_test_documents: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p> The number of documents in the input data that were used to test the entity recognizer. Typically this is 10 to 20 percent of the input documents.</p>"""
    evaluation_metrics: NotRequired[
        "capo_comprehend.types.entity_recognizer_evaluation_metrics.EntityRecognizerEvaluationMetrics"
    ]
    """<p>Detailed information about the accuracy of an entity recognizer.</p>"""
    entity_types: NotRequired[
        "capo_comprehend.types.entity_recognizer_metadata_entity_types_list.EntityRecognizerMetadataEntityTypesList"
    ]
    """<p>Entity types from the metadata of an entity recognizer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRecognizerMetadata) -> dict:
    out: dict = {}
    if "number_of_trained_documents" in value:
        out["NumberOfTrainedDocuments"] = value["number_of_trained_documents"]
    if "number_of_test_documents" in value:
        out["NumberOfTestDocuments"] = value["number_of_test_documents"]
    if "evaluation_metrics" in value:
        import capo_comprehend.types.entity_recognizer_evaluation_metrics

        out["EvaluationMetrics"] = (
            capo_comprehend.types.entity_recognizer_evaluation_metrics.serialize_aws_json_1_1(
                value["evaluation_metrics"]
            )
        )
    if "entity_types" in value:
        import capo_comprehend.types.entity_recognizer_metadata_entity_types_list

        out["EntityTypes"] = (
            capo_comprehend.types.entity_recognizer_metadata_entity_types_list.serialize_aws_json_1_1(
                value["entity_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityRecognizerMetadata:
    out: EntityRecognizerMetadata = {}  # type: ignore[typeddict-item]
    if data.get("NumberOfTrainedDocuments") is not None:
        out["number_of_trained_documents"] = data["NumberOfTrainedDocuments"]
    if data.get("NumberOfTestDocuments") is not None:
        out["number_of_test_documents"] = data["NumberOfTestDocuments"]
    if data.get("EvaluationMetrics") is not None:
        import capo_comprehend.types.entity_recognizer_evaluation_metrics

        out["evaluation_metrics"] = (
            capo_comprehend.types.entity_recognizer_evaluation_metrics.deserialize_aws_json_1_1(
                data["EvaluationMetrics"]
            )
        )
    if data.get("EntityTypes") is not None:
        import capo_comprehend.types.entity_recognizer_metadata_entity_types_list

        out["entity_types"] = (
            capo_comprehend.types.entity_recognizer_metadata_entity_types_list.deserialize_aws_json_1_1(
                data["EntityTypes"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EntityRecognizerMetadata) -> dict:
    out: dict = {}
    if "number_of_trained_documents" in value:
        out["NumberOfTrainedDocuments"] = value["number_of_trained_documents"]
    if "number_of_test_documents" in value:
        out["NumberOfTestDocuments"] = value["number_of_test_documents"]
    if "evaluation_metrics" in value:
        import capo_comprehend.types.entity_recognizer_evaluation_metrics

        out["EvaluationMetrics"] = (
            capo_comprehend.types.entity_recognizer_evaluation_metrics.serialize_cbor(
                value["evaluation_metrics"]
            )
        )
    if "entity_types" in value:
        import capo_comprehend.types.entity_recognizer_metadata_entity_types_list

        out["EntityTypes"] = (
            capo_comprehend.types.entity_recognizer_metadata_entity_types_list.serialize_cbor(
                value["entity_types"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> EntityRecognizerMetadata:
    out: EntityRecognizerMetadata = {}  # type: ignore[typeddict-item]
    if data.get("NumberOfTrainedDocuments") is not None:
        out["number_of_trained_documents"] = data["NumberOfTrainedDocuments"]
    if data.get("NumberOfTestDocuments") is not None:
        out["number_of_test_documents"] = data["NumberOfTestDocuments"]
    if data.get("EvaluationMetrics") is not None:
        import capo_comprehend.types.entity_recognizer_evaluation_metrics

        out["evaluation_metrics"] = (
            capo_comprehend.types.entity_recognizer_evaluation_metrics.deserialize_cbor(
                data["EvaluationMetrics"]
            )
        )
    if data.get("EntityTypes") is not None:
        import capo_comprehend.types.entity_recognizer_metadata_entity_types_list

        out["entity_types"] = (
            capo_comprehend.types.entity_recognizer_metadata_entity_types_list.deserialize_cbor(
                data["EntityTypes"]
            )
        )
    return out
