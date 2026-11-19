"""Generated from Smithy shape ``com.amazonaws.textract#GetDocumentAnalysisResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.block_list
    import capo_textract.types.document_metadata
    import capo_textract.types.job_status
    import capo_textract.types.pagination_token
    import capo_textract.types.status_message
    import capo_textract.types.string
    import capo_textract.types.warnings


class GetDocumentAnalysisResponse(TypedDict, closed=True):
    document_metadata: NotRequired[
        "capo_textract.types.document_metadata.DocumentMetadata"
    ]
    """<p>Information about a document that Amazon Textract processed. <code>DocumentMetadata</code> is returned in every page of paginated responses from an Amazon Textract video operation.</p>"""
    job_status: NotRequired["capo_textract.types.job_status.JobStatus"]
    """<p>The current status of the text detection job.</p>"""
    next_token: NotRequired["capo_textract.types.pagination_token.PaginationToken"]
    """<p>If the response is truncated, Amazon Textract returns this token. You can use this token in the subsequent request to retrieve the next set of text detection results.</p>"""
    blocks: NotRequired["capo_textract.types.block_list.BlockList"]
    """<p>The results of the text-analysis operation.</p>"""
    warnings: NotRequired["capo_textract.types.warnings.Warnings"]
    """<p>A list of warnings that occurred during the document-analysis operation.</p>"""
    status_message: NotRequired["capo_textract.types.status_message.StatusMessage"]
    """<p>Returns if the detection job could not be completed. Contains explanation for what error occured.</p>"""
    analyze_document_model_version: NotRequired["capo_textract.types.string.String"]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDocumentAnalysisResponse) -> dict:
    out: dict = {}
    if "document_metadata" in value:
        import capo_textract.types.document_metadata

        out["DocumentMetadata"] = (
            capo_textract.types.document_metadata.serialize_aws_json_1_1(
                value["document_metadata"]
            )
        )
    if "job_status" in value:
        import capo_textract.types.job_status

        out["JobStatus"] = capo_textract.types.job_status.serialize_aws_json_1_1(
            value["job_status"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "blocks" in value:
        import capo_textract.types.block_list

        out["Blocks"] = capo_textract.types.block_list.serialize_aws_json_1_1(
            value["blocks"]
        )
    if "warnings" in value:
        import capo_textract.types.warnings

        out["Warnings"] = capo_textract.types.warnings.serialize_aws_json_1_1(
            value["warnings"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "analyze_document_model_version" in value:
        out["AnalyzeDocumentModelVersion"] = value["analyze_document_model_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDocumentAnalysisResponse:
    out: GetDocumentAnalysisResponse = {}  # type: ignore[typeddict-item]
    if data.get("DocumentMetadata") is not None:
        import capo_textract.types.document_metadata

        out["document_metadata"] = (
            capo_textract.types.document_metadata.deserialize_aws_json_1_1(
                data["DocumentMetadata"]
            )
        )
    if data.get("JobStatus") is not None:
        import capo_textract.types.job_status

        out["job_status"] = capo_textract.types.job_status.deserialize_aws_json_1_1(
            data["JobStatus"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Blocks") is not None:
        import capo_textract.types.block_list

        out["blocks"] = capo_textract.types.block_list.deserialize_aws_json_1_1(
            data["Blocks"]
        )
    if data.get("Warnings") is not None:
        import capo_textract.types.warnings

        out["warnings"] = capo_textract.types.warnings.deserialize_aws_json_1_1(
            data["Warnings"]
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("AnalyzeDocumentModelVersion") is not None:
        out["analyze_document_model_version"] = data["AnalyzeDocumentModelVersion"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetDocumentAnalysisResponse) -> dict:
    out: dict = {}
    if "document_metadata" in value:
        import capo_textract.types.document_metadata

        out["DocumentMetadata"] = capo_textract.types.document_metadata.serialize_cbor(
            value["document_metadata"]
        )
    if "job_status" in value:
        import capo_textract.types.job_status

        out["JobStatus"] = capo_textract.types.job_status.serialize_cbor(
            value["job_status"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "blocks" in value:
        import capo_textract.types.block_list

        out["Blocks"] = capo_textract.types.block_list.serialize_cbor(value["blocks"])
    if "warnings" in value:
        import capo_textract.types.warnings

        out["Warnings"] = capo_textract.types.warnings.serialize_cbor(value["warnings"])
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "analyze_document_model_version" in value:
        out["AnalyzeDocumentModelVersion"] = value["analyze_document_model_version"]
    return out


def deserialize_cbor(data: dict) -> GetDocumentAnalysisResponse:
    out: GetDocumentAnalysisResponse = {}  # type: ignore[typeddict-item]
    if data.get("DocumentMetadata") is not None:
        import capo_textract.types.document_metadata

        out["document_metadata"] = (
            capo_textract.types.document_metadata.deserialize_cbor(
                data["DocumentMetadata"]
            )
        )
    if data.get("JobStatus") is not None:
        import capo_textract.types.job_status

        out["job_status"] = capo_textract.types.job_status.deserialize_cbor(
            data["JobStatus"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Blocks") is not None:
        import capo_textract.types.block_list

        out["blocks"] = capo_textract.types.block_list.deserialize_cbor(data["Blocks"])
    if data.get("Warnings") is not None:
        import capo_textract.types.warnings

        out["warnings"] = capo_textract.types.warnings.deserialize_cbor(
            data["Warnings"]
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("AnalyzeDocumentModelVersion") is not None:
        out["analyze_document_model_version"] = data["AnalyzeDocumentModelVersion"]
    return out
