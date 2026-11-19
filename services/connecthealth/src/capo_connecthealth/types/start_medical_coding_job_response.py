"""Generated from Smithy shape ``com.amazonaws.connecthealth#StartMedicalCodingJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_connecthealth.types.job_id
    import capo_connecthealth.types.medical_coding_job_arn


class StartMedicalCodingJobResponse(TypedDict, closed=True):
    job_arn: "capo_connecthealth.types.medical_coding_job_arn.MedicalCodingJobArn"
    """<p>The Amazon Resource Name (ARN) of the medical coding job.</p>"""
    job_id: "capo_connecthealth.types.job_id.JobId"
    """<p>The unique identifier of the medical coding job.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>The date and time that the medical coding job was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMedicalCodingJobResponse) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    out["jobId"] = value["job_id"]
    if "creation_time" in value:
        import capo_connecthealth._protocol.serialize

        out["creationTime"] = capo_connecthealth._protocol.serialize.fmt_date_time(
            value["creation_time"]
        )
    return out


def deserialize_json(data: dict) -> StartMedicalCodingJobResponse:
    out: StartMedicalCodingJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobArn") is not None:
        out["job_arn"] = data["jobArn"]
    else:
        out["job_arn"] = ""
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("creationTime") is not None:
        import datetime

        out["creation_time"] = datetime.datetime.fromisoformat(
            data["creationTime"].replace("Z", "+00:00")
        )
    return out
