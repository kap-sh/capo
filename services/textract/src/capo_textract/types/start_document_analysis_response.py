"""Generated from Smithy shape ``com.amazonaws.textract#StartDocumentAnalysisResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.job_id


class StartDocumentAnalysisResponse(TypedDict, closed=True):
    job_id: NotRequired["capo_textract.types.job_id.JobId"]
    """<p>The identifier for the document text detection job. Use <code>JobId</code> to identify the job in a subsequent call to <code>GetDocumentAnalysis</code>. A <code>JobId</code> value is only valid for 7 days.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartDocumentAnalysisResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartDocumentAnalysisResponse:
    out: StartDocumentAnalysisResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartDocumentAnalysisResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    return out


def deserialize_cbor(data: dict) -> StartDocumentAnalysisResponse:
    out: StartDocumentAnalysisResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    return out
