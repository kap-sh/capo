"""Generated from Smithy shape ``com.amazonaws.comprehend#StopEventsDetectionJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.job_id
    import capo_comprehend.types.job_status


class StopEventsDetectionJobResponse(TypedDict, closed=True):
    job_id: NotRequired["capo_comprehend.types.job_id.JobId"]
    """<p>The identifier of the events detection job to stop.</p>"""
    job_status: NotRequired["capo_comprehend.types.job_status.JobStatus"]
    """<p>The status of the events detection job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopEventsDetectionJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_status" in value:
        import capo_comprehend.types.job_status

        out["JobStatus"] = capo_comprehend.types.job_status.serialize_aws_json_1_1(
            value["job_status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopEventsDetectionJobResponse:
    out: StopEventsDetectionJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    if data.get("JobStatus") is not None:
        import capo_comprehend.types.job_status

        out["job_status"] = capo_comprehend.types.job_status.deserialize_aws_json_1_1(
            data["JobStatus"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StopEventsDetectionJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_status" in value:
        import capo_comprehend.types.job_status

        out["JobStatus"] = capo_comprehend.types.job_status.serialize_cbor(
            value["job_status"]
        )
    return out


def deserialize_cbor(data: dict) -> StopEventsDetectionJobResponse:
    out: StopEventsDetectionJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    if data.get("JobStatus") is not None:
        import capo_comprehend.types.job_status

        out["job_status"] = capo_comprehend.types.job_status.deserialize_cbor(
            data["JobStatus"]
        )
    return out
