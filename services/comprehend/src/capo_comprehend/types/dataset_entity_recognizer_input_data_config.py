"""Generated from Smithy shape ``com.amazonaws.comprehend#DatasetEntityRecognizerInputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import capo_comprehend.types.dataset_entity_recognizer_annotations
    import capo_comprehend.types.dataset_entity_recognizer_documents
    import capo_comprehend.types.dataset_entity_recognizer_entity_list


class DatasetEntityRecognizerInputDataConfig(TypedDict, closed=True):
    annotations: NotRequired[
        "capo_comprehend.types.dataset_entity_recognizer_annotations.DatasetEntityRecognizerAnnotations"
    ]
    """<p>The S3 location of the annotation documents for your custom entity recognizer.</p>"""
    documents: "capo_comprehend.types.dataset_entity_recognizer_documents.DatasetEntityRecognizerDocuments"
    """<p>The format and location of the training documents for your custom entity recognizer.</p>"""
    entity_list: NotRequired[
        "capo_comprehend.types.dataset_entity_recognizer_entity_list.DatasetEntityRecognizerEntityList"
    ]
    """<p>The S3 location of the entity list for your custom entity recognizer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetEntityRecognizerInputDataConfig) -> dict:
    out: dict = {}
    if "annotations" in value:
        import capo_comprehend.types.dataset_entity_recognizer_annotations

        out["Annotations"] = (
            capo_comprehend.types.dataset_entity_recognizer_annotations.serialize_aws_json_1_1(
                value["annotations"]
            )
        )
    import capo_comprehend.types.dataset_entity_recognizer_documents

    out["Documents"] = (
        capo_comprehend.types.dataset_entity_recognizer_documents.serialize_aws_json_1_1(
            value["documents"]
        )
    )
    if "entity_list" in value:
        import capo_comprehend.types.dataset_entity_recognizer_entity_list

        out["EntityList"] = (
            capo_comprehend.types.dataset_entity_recognizer_entity_list.serialize_aws_json_1_1(
                value["entity_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetEntityRecognizerInputDataConfig:
    out: DatasetEntityRecognizerInputDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("Annotations") is not None:
        import capo_comprehend.types.dataset_entity_recognizer_annotations

        out["annotations"] = (
            capo_comprehend.types.dataset_entity_recognizer_annotations.deserialize_aws_json_1_1(
                data["Annotations"]
            )
        )
    if data.get("Documents") is not None:
        import capo_comprehend.types.dataset_entity_recognizer_documents

        out["documents"] = (
            capo_comprehend.types.dataset_entity_recognizer_documents.deserialize_aws_json_1_1(
                data["Documents"]
            )
        )
    else:
        raise DeserializationError(
            "DatasetEntityRecognizerInputDataConfig.documents required"
        )
    if data.get("EntityList") is not None:
        import capo_comprehend.types.dataset_entity_recognizer_entity_list

        out["entity_list"] = (
            capo_comprehend.types.dataset_entity_recognizer_entity_list.deserialize_aws_json_1_1(
                data["EntityList"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DatasetEntityRecognizerInputDataConfig) -> dict:
    out: dict = {}
    if "annotations" in value:
        import capo_comprehend.types.dataset_entity_recognizer_annotations

        out["Annotations"] = (
            capo_comprehend.types.dataset_entity_recognizer_annotations.serialize_cbor(
                value["annotations"]
            )
        )
    import capo_comprehend.types.dataset_entity_recognizer_documents

    out["Documents"] = (
        capo_comprehend.types.dataset_entity_recognizer_documents.serialize_cbor(
            value["documents"]
        )
    )
    if "entity_list" in value:
        import capo_comprehend.types.dataset_entity_recognizer_entity_list

        out["EntityList"] = (
            capo_comprehend.types.dataset_entity_recognizer_entity_list.serialize_cbor(
                value["entity_list"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DatasetEntityRecognizerInputDataConfig:
    out: DatasetEntityRecognizerInputDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("Annotations") is not None:
        import capo_comprehend.types.dataset_entity_recognizer_annotations

        out["annotations"] = (
            capo_comprehend.types.dataset_entity_recognizer_annotations.deserialize_cbor(
                data["Annotations"]
            )
        )
    if data.get("Documents") is not None:
        import capo_comprehend.types.dataset_entity_recognizer_documents

        out["documents"] = (
            capo_comprehend.types.dataset_entity_recognizer_documents.deserialize_cbor(
                data["Documents"]
            )
        )
    else:
        raise DeserializationError(
            "DatasetEntityRecognizerInputDataConfig.documents required"
        )
    if data.get("EntityList") is not None:
        import capo_comprehend.types.dataset_entity_recognizer_entity_list

        out["entity_list"] = (
            capo_comprehend.types.dataset_entity_recognizer_entity_list.deserialize_cbor(
                data["EntityList"]
            )
        )
    return out
