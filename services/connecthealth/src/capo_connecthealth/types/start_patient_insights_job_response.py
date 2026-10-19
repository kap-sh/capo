"""Generated from Smithy shape ``com.amazonaws.connecthealth#StartPatientInsightsJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_connecthealth.types.job_arn
    import capo_connecthealth.types.job_id


class StartPatientInsightsJobResponse(TypedDict, closed=True):
    job_arn: "capo_connecthealth.types.job_arn.JobArn"
    """<p/>"""
    job_id: "capo_connecthealth.types.job_id.JobId"
    """<p/>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>Date and time the patient insights job was submitted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartPatientInsightsJobResponse) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    out["jobId"] = value["job_id"]
    if "creation_time" in value:
        import capo_connecthealth._protocol.serialize

        out["creationTime"] = capo_connecthealth._protocol.serialize.fmt_date_time(
            value["creation_time"]
        )
    return out


def deserialize_json(data: dict) -> StartPatientInsightsJobResponse:
    out: StartPatientInsightsJobResponse = {}  # type: ignore[typeddict-item]
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
