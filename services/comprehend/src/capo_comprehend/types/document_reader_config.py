"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentReaderConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.document_read_action
    import capo_comprehend.types.document_read_mode
    import capo_comprehend.types.list_of_document_read_feature_types


class DocumentReaderConfig(TypedDict, closed=True):
    document_read_action: (
        "capo_comprehend.types.document_read_action.DocumentReadAction"
    )
    """<p>This field defines the Amazon Textract API operation that Amazon Comprehend uses to extract text from PDF files and image files. Enter one of the following values:</p> <ul> <li> <p> <code>TEXTRACT_DETECT_DOCUMENT_TEXT</code> - The Amazon Comprehend service uses the <code>DetectDocumentText</code> API operation. </p> </li> <li> <p> <code>TEXTRACT_ANALYZE_DOCUMENT</code> - The Amazon Comprehend service uses the <code>AnalyzeDocument</code> API operation. </p> </li> </ul>"""
    document_read_mode: NotRequired[
        "capo_comprehend.types.document_read_mode.DocumentReadMode"
    ]
    """<p>Determines the text extraction actions for PDF files. Enter one of the following values:</p> <ul> <li> <p> <code>SERVICE_DEFAULT</code> - use the Amazon Comprehend service defaults for PDF files.</p> </li> <li> <p> <code>FORCE_DOCUMENT_READ_ACTION</code> - Amazon Comprehend uses the Textract API specified by DocumentReadAction for all PDF files, including digital PDF files. </p> </li> </ul>"""
    feature_types: NotRequired[
        "capo_comprehend.types.list_of_document_read_feature_types.ListOfDocumentReadFeatureTypes"
    ]
    """<p>Specifies the type of Amazon Textract features to apply. If you chose <code>TEXTRACT_ANALYZE_DOCUMENT</code> as the read action, you must specify one or both of the following values:</p> <ul> <li> <p> <code>TABLES</code> - Returns additional information about any tables that are detected in the input document. </p> </li> <li> <p> <code>FORMS</code> - Returns additional information about any forms that are detected in the input document. </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentReaderConfig) -> dict:
    out: dict = {}
    import capo_comprehend.types.document_read_action

    out["DocumentReadAction"] = (
        capo_comprehend.types.document_read_action.serialize_aws_json_1_1(
            value["document_read_action"]
        )
    )
    if "document_read_mode" in value:
        import capo_comprehend.types.document_read_mode

        out["DocumentReadMode"] = (
            capo_comprehend.types.document_read_mode.serialize_aws_json_1_1(
                value["document_read_mode"]
            )
        )
    if "feature_types" in value:
        import capo_comprehend.types.list_of_document_read_feature_types

        out["FeatureTypes"] = (
            capo_comprehend.types.list_of_document_read_feature_types.serialize_aws_json_1_1(
                value["feature_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentReaderConfig:
    out: DocumentReaderConfig = {}  # type: ignore[typeddict-item]
    if data.get("DocumentReadAction") is not None:
        import capo_comprehend.types.document_read_action

        out["document_read_action"] = (
            capo_comprehend.types.document_read_action.deserialize_aws_json_1_1(
                data["DocumentReadAction"]
            )
        )
    else:
        import typing

        out["document_read_action"] = typing.cast(
            "capo_comprehend.types.document_read_action.DocumentReadAction", ""
        )
    if data.get("DocumentReadMode") is not None:
        import capo_comprehend.types.document_read_mode

        out["document_read_mode"] = (
            capo_comprehend.types.document_read_mode.deserialize_aws_json_1_1(
                data["DocumentReadMode"]
            )
        )
    if data.get("FeatureTypes") is not None:
        import capo_comprehend.types.list_of_document_read_feature_types

        out["feature_types"] = (
            capo_comprehend.types.list_of_document_read_feature_types.deserialize_aws_json_1_1(
                data["FeatureTypes"]
            )
        )
    return out
