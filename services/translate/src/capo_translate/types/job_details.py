"""Generated from Smithy shape ``com.amazonaws.translate#JobDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.integer


class JobDetails(TypedDict, closed=True):
    translated_documents_count: NotRequired["capo_translate.types.integer.Integer"]
    """<p>The number of documents successfully processed during a translation job.</p>"""
    documents_with_errors_count: NotRequired["capo_translate.types.integer.Integer"]
    """<p>The number of documents that could not be processed during a translation job.</p>"""
    input_documents_count: NotRequired["capo_translate.types.integer.Integer"]
    """<p>The number of documents used as input in a translation job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobDetails) -> dict:
    out: dict = {}
    if "translated_documents_count" in value:
        out["TranslatedDocumentsCount"] = value["translated_documents_count"]
    if "documents_with_errors_count" in value:
        out["DocumentsWithErrorsCount"] = value["documents_with_errors_count"]
    if "input_documents_count" in value:
        out["InputDocumentsCount"] = value["input_documents_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JobDetails:
    out: JobDetails = {}  # type: ignore[typeddict-item]
    if data.get("TranslatedDocumentsCount") is not None:
        out["translated_documents_count"] = data["TranslatedDocumentsCount"]
    if data.get("DocumentsWithErrorsCount") is not None:
        out["documents_with_errors_count"] = data["DocumentsWithErrorsCount"]
    if data.get("InputDocumentsCount") is not None:
        out["input_documents_count"] = data["InputDocumentsCount"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: JobDetails) -> dict:
    out: dict = {}
    if "translated_documents_count" in value:
        out["TranslatedDocumentsCount"] = value["translated_documents_count"]
    if "documents_with_errors_count" in value:
        out["DocumentsWithErrorsCount"] = value["documents_with_errors_count"]
    if "input_documents_count" in value:
        out["InputDocumentsCount"] = value["input_documents_count"]
    return out


def deserialize_cbor(data: dict) -> JobDetails:
    out: JobDetails = {}  # type: ignore[typeddict-item]
    if data.get("TranslatedDocumentsCount") is not None:
        out["translated_documents_count"] = data["TranslatedDocumentsCount"]
    if data.get("DocumentsWithErrorsCount") is not None:
        out["documents_with_errors_count"] = data["DocumentsWithErrorsCount"]
    if data.get("InputDocumentsCount") is not None:
        out["input_documents_count"] = data["InputDocumentsCount"]
    return out
