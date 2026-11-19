"""Generated from Smithy shape ``com.amazonaws.textract#StartExpenseAnalysisResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.job_id


class StartExpenseAnalysisResponse(TypedDict, closed=True):
    job_id: NotRequired["capo_textract.types.job_id.JobId"]
    """<p>A unique identifier for the text detection job. The <code>JobId</code> is returned from <code>StartExpenseAnalysis</code>. A <code>JobId</code> value is only valid for 7 days.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartExpenseAnalysisResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartExpenseAnalysisResponse:
    out: StartExpenseAnalysisResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartExpenseAnalysisResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    return out


def deserialize_cbor(data: dict) -> StartExpenseAnalysisResponse:
    out: StartExpenseAnalysisResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    return out
