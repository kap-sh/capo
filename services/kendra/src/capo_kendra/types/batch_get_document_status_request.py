"""Generated from Smithy shape ``com.amazonaws.kendra#BatchGetDocumentStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.document_info_list
    import capo_kendra.types.index_id


class BatchGetDocumentStatusRequest(TypedDict, closed=True):
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index to add documents to. The index ID is returned by the <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_CreateIndex.html">CreateIndex </a> API.</p>"""
    document_info_list: "capo_kendra.types.document_info_list.DocumentInfoList"
    """<p>A list of <code>DocumentInfo</code> objects that identify the documents for which to get the status. You identify the documents by their document ID and optional attributes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDocumentStatusRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    import capo_kendra.types.document_info_list

    out["DocumentInfoList"] = (
        capo_kendra.types.document_info_list.serialize_aws_json_1_1(
            value["document_info_list"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetDocumentStatusRequest:
    out: BatchGetDocumentStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("BatchGetDocumentStatusRequest.index_id required")
    if data.get("DocumentInfoList") is not None:
        import capo_kendra.types.document_info_list

        out["document_info_list"] = (
            capo_kendra.types.document_info_list.deserialize_aws_json_1_1(
                data["DocumentInfoList"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetDocumentStatusRequest.document_info_list required"
        )
    return out
