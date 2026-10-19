"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognizerInputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.entity_recognizer_annotations
    import capo_comprehend.types.entity_recognizer_augmented_manifests_list
    import capo_comprehend.types.entity_recognizer_data_format
    import capo_comprehend.types.entity_recognizer_documents
    import capo_comprehend.types.entity_recognizer_entity_list
    import capo_comprehend.types.entity_types_list


class EntityRecognizerInputDataConfig(TypedDict, closed=True):
    data_format: NotRequired[
        "capo_comprehend.types.entity_recognizer_data_format.EntityRecognizerDataFormat"
    ]
    """<p>The format of your training data:</p> <ul> <li> <p> <code>COMPREHEND_CSV</code>: A CSV file that supplements your training documents. The CSV file contains information about the custom entities that your trained model will detect. The required format of the file depends on whether you are providing annotations or an entity list.</p> <p>If you use this value, you must provide your CSV file by using either the <code>Annotations</code> or <code>EntityList</code> parameters. You must provide your training documents by using the <code>Documents</code> parameter.</p> </li> <li> <p> <code>AUGMENTED_MANIFEST</code>: A labeled dataset that is produced by Amazon SageMaker Ground Truth. This file is in JSON lines format. Each line is a complete JSON object that contains a training document and its labels. Each label annotates a named entity in the training document. </p> <p>If you use this value, you must provide the <code>AugmentedManifests</code> parameter in your request.</p> </li> </ul> <p>If you don't specify a value, Amazon Comprehend uses <code>COMPREHEND_CSV</code> as the default.</p>"""
    entity_types: "capo_comprehend.types.entity_types_list.EntityTypesList"
    r"""<p>The entity types in the labeled training data that Amazon Comprehend uses to train the custom entity recognizer. Any entity types that you don't specify are ignored.</p> <p>A maximum of 25 entity types can be used at one time to train an entity recognizer. Entity types must not contain the following invalid characters: \n (line break), \\n (escaped line break), \r (carriage return), \\r (escaped carriage return), \t (tab), \\t (escaped tab), space, and , (comma). </p>"""
    documents: NotRequired[
        "capo_comprehend.types.entity_recognizer_documents.EntityRecognizerDocuments"
    ]
    """<p>The S3 location of the folder that contains the training documents for your custom entity recognizer.</p> <p>This parameter is required if you set <code>DataFormat</code> to <code>COMPREHEND_CSV</code>.</p>"""
    annotations: NotRequired[
        "capo_comprehend.types.entity_recognizer_annotations.EntityRecognizerAnnotations"
    ]
    """<p>The S3 location of the CSV file that annotates your training documents.</p>"""
    entity_list: NotRequired[
        "capo_comprehend.types.entity_recognizer_entity_list.EntityRecognizerEntityList"
    ]
    """<p>The S3 location of the CSV file that has the entity list for your custom entity recognizer.</p>"""
    augmented_manifests: NotRequired[
        "capo_comprehend.types.entity_recognizer_augmented_manifests_list.EntityRecognizerAugmentedManifestsList"
    ]
    """<p>A list of augmented manifest files that provide training data for your custom model. An augmented manifest file is a labeled dataset that is produced by Amazon SageMaker Ground Truth.</p> <p>This parameter is required if you set <code>DataFormat</code> to <code>AUGMENTED_MANIFEST</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRecognizerInputDataConfig) -> dict:
    out: dict = {}
    if "data_format" in value:
        import capo_comprehend.types.entity_recognizer_data_format

        out["DataFormat"] = (
            capo_comprehend.types.entity_recognizer_data_format.serialize_aws_json_1_1(
                value["data_format"]
            )
        )
    import capo_comprehend.types.entity_types_list

    out["EntityTypes"] = capo_comprehend.types.entity_types_list.serialize_aws_json_1_1(
        value["entity_types"]
    )
    if "documents" in value:
        import capo_comprehend.types.entity_recognizer_documents

        out["Documents"] = (
            capo_comprehend.types.entity_recognizer_documents.serialize_aws_json_1_1(
                value["documents"]
            )
        )
    if "annotations" in value:
        import capo_comprehend.types.entity_recognizer_annotations

        out["Annotations"] = (
            capo_comprehend.types.entity_recognizer_annotations.serialize_aws_json_1_1(
                value["annotations"]
            )
        )
    if "entity_list" in value:
        import capo_comprehend.types.entity_recognizer_entity_list

        out["EntityList"] = (
            capo_comprehend.types.entity_recognizer_entity_list.serialize_aws_json_1_1(
                value["entity_list"]
            )
        )
    if "augmented_manifests" in value:
        import capo_comprehend.types.entity_recognizer_augmented_manifests_list

        out["AugmentedManifests"] = (
            capo_comprehend.types.entity_recognizer_augmented_manifests_list.serialize_aws_json_1_1(
                value["augmented_manifests"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityRecognizerInputDataConfig:
    out: EntityRecognizerInputDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("DataFormat") is not None:
        import capo_comprehend.types.entity_recognizer_data_format

        out["data_format"] = (
            capo_comprehend.types.entity_recognizer_data_format.deserialize_aws_json_1_1(
                data["DataFormat"]
            )
        )
    if data.get("EntityTypes") is not None:
        import capo_comprehend.types.entity_types_list

        out["entity_types"] = (
            capo_comprehend.types.entity_types_list.deserialize_aws_json_1_1(
                data["EntityTypes"]
            )
        )
    else:
        out["entity_types"] = []
    if data.get("Documents") is not None:
        import capo_comprehend.types.entity_recognizer_documents

        out["documents"] = (
            capo_comprehend.types.entity_recognizer_documents.deserialize_aws_json_1_1(
                data["Documents"]
            )
        )
    if data.get("Annotations") is not None:
        import capo_comprehend.types.entity_recognizer_annotations

        out["annotations"] = (
            capo_comprehend.types.entity_recognizer_annotations.deserialize_aws_json_1_1(
                data["Annotations"]
            )
        )
    if data.get("EntityList") is not None:
        import capo_comprehend.types.entity_recognizer_entity_list

        out["entity_list"] = (
            capo_comprehend.types.entity_recognizer_entity_list.deserialize_aws_json_1_1(
                data["EntityList"]
            )
        )
    if data.get("AugmentedManifests") is not None:
        import capo_comprehend.types.entity_recognizer_augmented_manifests_list

        out["augmented_manifests"] = (
            capo_comprehend.types.entity_recognizer_augmented_manifests_list.deserialize_aws_json_1_1(
                data["AugmentedManifests"]
            )
        )
    return out
