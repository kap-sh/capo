"""Generated from Smithy shape ``com.amazonaws.comprehend#ClassifyDocumentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.document_metadata
    import capo_comprehend.types.list_of_classes
    import capo_comprehend.types.list_of_document_type
    import capo_comprehend.types.list_of_errors
    import capo_comprehend.types.list_of_labels
    import capo_comprehend.types.list_of_warnings


class ClassifyDocumentResponse(TypedDict, closed=True):
    classes: NotRequired["capo_comprehend.types.list_of_classes.ListOfClasses"]
    """<p>The classes used by the document being analyzed. These are used for models trained in multi-class mode. Individual classes are mutually exclusive and each document is expected to have only a single class assigned to it. For example, an animal can be a dog or a cat, but not both at the same time. </p> <p>For prompt safety classification, the response includes only two classes (SAFE_PROMPT and UNSAFE_PROMPT), along with a confidence score for each class. The value range of the score is zero to one, where one is the highest confidence.</p>"""
    labels: NotRequired["capo_comprehend.types.list_of_labels.ListOfLabels"]
    """<p>The labels used in the document being analyzed. These are used for multi-label trained models. Individual labels represent different categories that are related in some manner and are not mutually exclusive. For example, a movie can be just an action movie, or it can be an action movie, a science fiction movie, and a comedy, all at the same time. </p>"""
    document_metadata: NotRequired[
        "capo_comprehend.types.document_metadata.DocumentMetadata"
    ]
    """<p>Extraction information about the document. This field is present in the response only if your request includes the <code>Byte</code> parameter. </p>"""
    document_type: NotRequired[
        "capo_comprehend.types.list_of_document_type.ListOfDocumentType"
    ]
    """<p>The document type for each page in the input document. This field is present in the response only if your request includes the <code>Byte</code> parameter. </p>"""
    errors: NotRequired["capo_comprehend.types.list_of_errors.ListOfErrors"]
    """<p>Page-level errors that the system detected while processing the input document. The field is empty if the system encountered no errors.</p>"""
    warnings: NotRequired["capo_comprehend.types.list_of_warnings.ListOfWarnings"]
    """<p>Warnings detected while processing the input document. The response includes a warning if there is a mismatch between the input document type and the model type associated with the endpoint that you specified. The response can also include warnings for individual pages that have a mismatch. </p> <p>The field is empty if the system generated no warnings.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClassifyDocumentResponse) -> dict:
    out: dict = {}
    if "classes" in value:
        import capo_comprehend.types.list_of_classes

        out["Classes"] = capo_comprehend.types.list_of_classes.serialize_aws_json_1_1(
            value["classes"]
        )
    if "labels" in value:
        import capo_comprehend.types.list_of_labels

        out["Labels"] = capo_comprehend.types.list_of_labels.serialize_aws_json_1_1(
            value["labels"]
        )
    if "document_metadata" in value:
        import capo_comprehend.types.document_metadata

        out["DocumentMetadata"] = (
            capo_comprehend.types.document_metadata.serialize_aws_json_1_1(
                value["document_metadata"]
            )
        )
    if "document_type" in value:
        import capo_comprehend.types.list_of_document_type

        out["DocumentType"] = (
            capo_comprehend.types.list_of_document_type.serialize_aws_json_1_1(
                value["document_type"]
            )
        )
    if "errors" in value:
        import capo_comprehend.types.list_of_errors

        out["Errors"] = capo_comprehend.types.list_of_errors.serialize_aws_json_1_1(
            value["errors"]
        )
    if "warnings" in value:
        import capo_comprehend.types.list_of_warnings

        out["Warnings"] = capo_comprehend.types.list_of_warnings.serialize_aws_json_1_1(
            value["warnings"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClassifyDocumentResponse:
    out: ClassifyDocumentResponse = {}  # type: ignore[typeddict-item]
    if data.get("Classes") is not None:
        import capo_comprehend.types.list_of_classes

        out["classes"] = capo_comprehend.types.list_of_classes.deserialize_aws_json_1_1(
            data["Classes"]
        )
    if data.get("Labels") is not None:
        import capo_comprehend.types.list_of_labels

        out["labels"] = capo_comprehend.types.list_of_labels.deserialize_aws_json_1_1(
            data["Labels"]
        )
    if data.get("DocumentMetadata") is not None:
        import capo_comprehend.types.document_metadata

        out["document_metadata"] = (
            capo_comprehend.types.document_metadata.deserialize_aws_json_1_1(
                data["DocumentMetadata"]
            )
        )
    if data.get("DocumentType") is not None:
        import capo_comprehend.types.list_of_document_type

        out["document_type"] = (
            capo_comprehend.types.list_of_document_type.deserialize_aws_json_1_1(
                data["DocumentType"]
            )
        )
    if data.get("Errors") is not None:
        import capo_comprehend.types.list_of_errors

        out["errors"] = capo_comprehend.types.list_of_errors.deserialize_aws_json_1_1(
            data["Errors"]
        )
    if data.get("Warnings") is not None:
        import capo_comprehend.types.list_of_warnings

        out["warnings"] = (
            capo_comprehend.types.list_of_warnings.deserialize_aws_json_1_1(
                data["Warnings"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ClassifyDocumentResponse) -> dict:
    out: dict = {}
    if "classes" in value:
        import capo_comprehend.types.list_of_classes

        out["Classes"] = capo_comprehend.types.list_of_classes.serialize_cbor(
            value["classes"]
        )
    if "labels" in value:
        import capo_comprehend.types.list_of_labels

        out["Labels"] = capo_comprehend.types.list_of_labels.serialize_cbor(
            value["labels"]
        )
    if "document_metadata" in value:
        import capo_comprehend.types.document_metadata

        out["DocumentMetadata"] = (
            capo_comprehend.types.document_metadata.serialize_cbor(
                value["document_metadata"]
            )
        )
    if "document_type" in value:
        import capo_comprehend.types.list_of_document_type

        out["DocumentType"] = (
            capo_comprehend.types.list_of_document_type.serialize_cbor(
                value["document_type"]
            )
        )
    if "errors" in value:
        import capo_comprehend.types.list_of_errors

        out["Errors"] = capo_comprehend.types.list_of_errors.serialize_cbor(
            value["errors"]
        )
    if "warnings" in value:
        import capo_comprehend.types.list_of_warnings

        out["Warnings"] = capo_comprehend.types.list_of_warnings.serialize_cbor(
            value["warnings"]
        )
    return out


def deserialize_cbor(data: dict) -> ClassifyDocumentResponse:
    out: ClassifyDocumentResponse = {}  # type: ignore[typeddict-item]
    if data.get("Classes") is not None:
        import capo_comprehend.types.list_of_classes

        out["classes"] = capo_comprehend.types.list_of_classes.deserialize_cbor(
            data["Classes"]
        )
    if data.get("Labels") is not None:
        import capo_comprehend.types.list_of_labels

        out["labels"] = capo_comprehend.types.list_of_labels.deserialize_cbor(
            data["Labels"]
        )
    if data.get("DocumentMetadata") is not None:
        import capo_comprehend.types.document_metadata

        out["document_metadata"] = (
            capo_comprehend.types.document_metadata.deserialize_cbor(
                data["DocumentMetadata"]
            )
        )
    if data.get("DocumentType") is not None:
        import capo_comprehend.types.list_of_document_type

        out["document_type"] = (
            capo_comprehend.types.list_of_document_type.deserialize_cbor(
                data["DocumentType"]
            )
        )
    if data.get("Errors") is not None:
        import capo_comprehend.types.list_of_errors

        out["errors"] = capo_comprehend.types.list_of_errors.deserialize_cbor(
            data["Errors"]
        )
    if data.get("Warnings") is not None:
        import capo_comprehend.types.list_of_warnings

        out["warnings"] = capo_comprehend.types.list_of_warnings.deserialize_cbor(
            data["Warnings"]
        )
    return out
