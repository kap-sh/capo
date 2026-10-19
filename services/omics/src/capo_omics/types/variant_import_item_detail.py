"""Generated from Smithy shape ``com.amazonaws.omics#VariantImportItemDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.job_status
    import capo_omics.types.job_status_msg
    import capo_omics.types.s3_uri


class VariantImportItemDetail(TypedDict, closed=True):
    source: "capo_omics.types.s3_uri.S3Uri"
    """<p>The source file's location in Amazon S3.</p>"""
    job_status: "capo_omics.types.job_status.JobStatus"
    """<p>The item's job status.</p>"""
    status_message: NotRequired["capo_omics.types.job_status_msg.JobStatusMsg"]
    """<p> A message that provides additional context about a job </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VariantImportItemDetail) -> dict:
    out: dict = {}
    out["source"] = value["source"]
    out["jobStatus"] = value["job_status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> VariantImportItemDetail:
    out: VariantImportItemDetail = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        out["source"] = ""
    if data.get("jobStatus") is not None:
        out["job_status"] = data["jobStatus"]
    else:
        out["job_status"] = ""
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    return out
