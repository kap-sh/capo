"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognizerMetadataEntityTypesListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.any_length_string
    import capo_comprehend.types.entity_types_evaluation_metrics
    import capo_comprehend.types.integer


class EntityRecognizerMetadataEntityTypesListItem(TypedDict, closed=True):
    type: NotRequired["capo_comprehend.types.any_length_string.AnyLengthString"]
    """<p>Type of entity from the list of entity types in the metadata of an entity recognizer. </p>"""
    evaluation_metrics: NotRequired[
        "capo_comprehend.types.entity_types_evaluation_metrics.EntityTypesEvaluationMetrics"
    ]
    """<p>Detailed information about the accuracy of the entity recognizer for a specific item on the list of entity types. </p>"""
    number_of_train_mentions: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>Indicates the number of times the given entity type was seen in the training data. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRecognizerMetadataEntityTypesListItem) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "evaluation_metrics" in value:
        import capo_comprehend.types.entity_types_evaluation_metrics

        out["EvaluationMetrics"] = (
            capo_comprehend.types.entity_types_evaluation_metrics.serialize_aws_json_1_1(
                value["evaluation_metrics"]
            )
        )
    if "number_of_train_mentions" in value:
        out["NumberOfTrainMentions"] = value["number_of_train_mentions"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityRecognizerMetadataEntityTypesListItem:
    out: EntityRecognizerMetadataEntityTypesListItem = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("EvaluationMetrics") is not None:
        import capo_comprehend.types.entity_types_evaluation_metrics

        out["evaluation_metrics"] = (
            capo_comprehend.types.entity_types_evaluation_metrics.deserialize_aws_json_1_1(
                data["EvaluationMetrics"]
            )
        )
    if data.get("NumberOfTrainMentions") is not None:
        out["number_of_train_mentions"] = data["NumberOfTrainMentions"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EntityRecognizerMetadataEntityTypesListItem) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "evaluation_metrics" in value:
        import capo_comprehend.types.entity_types_evaluation_metrics

        out["EvaluationMetrics"] = (
            capo_comprehend.types.entity_types_evaluation_metrics.serialize_cbor(
                value["evaluation_metrics"]
            )
        )
    if "number_of_train_mentions" in value:
        out["NumberOfTrainMentions"] = value["number_of_train_mentions"]
    return out


def deserialize_cbor(data: dict) -> EntityRecognizerMetadataEntityTypesListItem:
    out: EntityRecognizerMetadataEntityTypesListItem = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("EvaluationMetrics") is not None:
        import capo_comprehend.types.entity_types_evaluation_metrics

        out["evaluation_metrics"] = (
            capo_comprehend.types.entity_types_evaluation_metrics.deserialize_cbor(
                data["EvaluationMetrics"]
            )
        )
    if data.get("NumberOfTrainMentions") is not None:
        out["number_of_train_mentions"] = data["NumberOfTrainMentions"]
    return out
