"""Generated from Smithy shape ``com.amazonaws.comprehend#DatasetAugmentedManifestsListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.attribute_names_list
    import capo_comprehend.types.augmented_manifests_document_type_format
    import capo_comprehend.types.s3_uri


class DatasetAugmentedManifestsListItem(TypedDict, closed=True):
    attribute_names: "capo_comprehend.types.attribute_names_list.AttributeNamesList"
    """<p>The JSON attribute that contains the annotations for your training documents. The number of attribute names that you specify depends on whether your augmented manifest file is the output of a single labeling job or a chained labeling job.</p> <p>If your file is the output of a single labeling job, specify the LabelAttributeName key that was used when the job was created in Ground Truth.</p> <p>If your file is the output of a chained labeling job, specify the LabelAttributeName key for one or more jobs in the chain. Each LabelAttributeName key provides the annotations from an individual job.</p>"""
    s3_uri: "capo_comprehend.types.s3_uri.S3Uri"
    """<p>The Amazon S3 location of the augmented manifest file.</p>"""
    annotation_data_s3_uri: NotRequired["capo_comprehend.types.s3_uri.S3Uri"]
    """<p>The S3 prefix to the annotation files that are referred in the augmented manifest file.</p>"""
    source_documents_s3_uri: NotRequired["capo_comprehend.types.s3_uri.S3Uri"]
    """<p>The S3 prefix to the source files (PDFs) that are referred to in the augmented manifest file.</p>"""
    document_type: NotRequired[
        "capo_comprehend.types.augmented_manifests_document_type_format.AugmentedManifestsDocumentTypeFormat"
    ]
    """<p>The type of augmented manifest. If you don't specify, the default is PlainTextDocument. </p> <p> <code>PLAIN_TEXT_DOCUMENT</code> A document type that represents any unicode text that is encoded in UTF-8.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetAugmentedManifestsListItem) -> dict:
    out: dict = {}
    import capo_comprehend.types.attribute_names_list

    out["AttributeNames"] = (
        capo_comprehend.types.attribute_names_list.serialize_aws_json_1_1(
            value["attribute_names"]
        )
    )
    out["S3Uri"] = value["s3_uri"]
    if "annotation_data_s3_uri" in value:
        out["AnnotationDataS3Uri"] = value["annotation_data_s3_uri"]
    if "source_documents_s3_uri" in value:
        out["SourceDocumentsS3Uri"] = value["source_documents_s3_uri"]
    if "document_type" in value:
        import capo_comprehend.types.augmented_manifests_document_type_format

        out["DocumentType"] = (
            capo_comprehend.types.augmented_manifests_document_type_format.serialize_aws_json_1_1(
                value["document_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetAugmentedManifestsListItem:
    out: DatasetAugmentedManifestsListItem = {}  # type: ignore[typeddict-item]
    if data.get("AttributeNames") is not None:
        import capo_comprehend.types.attribute_names_list

        out["attribute_names"] = (
            capo_comprehend.types.attribute_names_list.deserialize_aws_json_1_1(
                data["AttributeNames"]
            )
        )
    else:
        out["attribute_names"] = []
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    else:
        out["s3_uri"] = ""
    if data.get("AnnotationDataS3Uri") is not None:
        out["annotation_data_s3_uri"] = data["AnnotationDataS3Uri"]
    if data.get("SourceDocumentsS3Uri") is not None:
        out["source_documents_s3_uri"] = data["SourceDocumentsS3Uri"]
    if data.get("DocumentType") is not None:
        import capo_comprehend.types.augmented_manifests_document_type_format

        out["document_type"] = (
            capo_comprehend.types.augmented_manifests_document_type_format.deserialize_aws_json_1_1(
                data["DocumentType"]
            )
        )
    return out
