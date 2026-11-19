"""Generated from Smithy shape ``com.amazonaws.textract#AnalyzeIDResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.document_metadata
    import capo_textract.types.identity_document_list
    import capo_textract.types.string


class AnalyzeIDResponse(TypedDict, closed=True):
    identity_documents: NotRequired[
        "capo_textract.types.identity_document_list.IdentityDocumentList"
    ]
    """<p>The list of documents processed by AnalyzeID. Includes a number denoting their place in the list and the response structure for the document.</p>"""
    document_metadata: NotRequired[
        "capo_textract.types.document_metadata.DocumentMetadata"
    ]
    analyze_id_model_version: NotRequired["capo_textract.types.string.String"]
    """<p>The version of the AnalyzeIdentity API being used to process documents.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalyzeIDResponse) -> dict:
    out: dict = {}
    if "identity_documents" in value:
        import capo_textract.types.identity_document_list

        out["IdentityDocuments"] = (
            capo_textract.types.identity_document_list.serialize_aws_json_1_1(
                value["identity_documents"]
            )
        )
    if "document_metadata" in value:
        import capo_textract.types.document_metadata

        out["DocumentMetadata"] = (
            capo_textract.types.document_metadata.serialize_aws_json_1_1(
                value["document_metadata"]
            )
        )
    if "analyze_id_model_version" in value:
        out["AnalyzeIDModelVersion"] = value["analyze_id_model_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AnalyzeIDResponse:
    out: AnalyzeIDResponse = {}  # type: ignore[typeddict-item]
    if data.get("IdentityDocuments") is not None:
        import capo_textract.types.identity_document_list

        out["identity_documents"] = (
            capo_textract.types.identity_document_list.deserialize_aws_json_1_1(
                data["IdentityDocuments"]
            )
        )
    if data.get("DocumentMetadata") is not None:
        import capo_textract.types.document_metadata

        out["document_metadata"] = (
            capo_textract.types.document_metadata.deserialize_aws_json_1_1(
                data["DocumentMetadata"]
            )
        )
    if data.get("AnalyzeIDModelVersion") is not None:
        out["analyze_id_model_version"] = data["AnalyzeIDModelVersion"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AnalyzeIDResponse) -> dict:
    out: dict = {}
    if "identity_documents" in value:
        import capo_textract.types.identity_document_list

        out["IdentityDocuments"] = (
            capo_textract.types.identity_document_list.serialize_cbor(
                value["identity_documents"]
            )
        )
    if "document_metadata" in value:
        import capo_textract.types.document_metadata

        out["DocumentMetadata"] = capo_textract.types.document_metadata.serialize_cbor(
            value["document_metadata"]
        )
    if "analyze_id_model_version" in value:
        out["AnalyzeIDModelVersion"] = value["analyze_id_model_version"]
    return out


def deserialize_cbor(data: dict) -> AnalyzeIDResponse:
    out: AnalyzeIDResponse = {}  # type: ignore[typeddict-item]
    if data.get("IdentityDocuments") is not None:
        import capo_textract.types.identity_document_list

        out["identity_documents"] = (
            capo_textract.types.identity_document_list.deserialize_cbor(
                data["IdentityDocuments"]
            )
        )
    if data.get("DocumentMetadata") is not None:
        import capo_textract.types.document_metadata

        out["document_metadata"] = (
            capo_textract.types.document_metadata.deserialize_cbor(
                data["DocumentMetadata"]
            )
        )
    if data.get("AnalyzeIDModelVersion") is not None:
        out["analyze_id_model_version"] = data["AnalyzeIDModelVersion"]
    return out
