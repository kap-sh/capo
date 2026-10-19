"""Generated from Smithy shape ``com.amazonaws.healthlake#StartFHIRImportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.datastore_id
    import capo_healthlake.types.job_id
    import capo_healthlake.types.job_status


class StartFHIRImportJobResponse(TypedDict, closed=True):
    job_id: "capo_healthlake.types.job_id.JobId"
    """<p>The import job identifier.</p>"""
    job_status: "capo_healthlake.types.job_status.JobStatus"
    """<p>The import job status.</p>"""
    datastore_id: NotRequired["capo_healthlake.types.datastore_id.DatastoreId"]
    """<p>The data store identifier.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartFHIRImportJobResponse) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    import capo_healthlake.types.job_status

    out["JobStatus"] = capo_healthlake.types.job_status.serialize_aws_json_1_0(
        value["job_status"]
    )
    if "datastore_id" in value:
        out["DatastoreId"] = value["datastore_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartFHIRImportJobResponse:
    out: StartFHIRImportJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    if data.get("JobStatus") is not None:
        import capo_healthlake.types.job_status

        out["job_status"] = capo_healthlake.types.job_status.deserialize_aws_json_1_0(
            data["JobStatus"]
        )
    else:
        import typing

        out["job_status"] = typing.cast(
            "capo_healthlake.types.job_status.JobStatus", ""
        )
    if data.get("DatastoreId") is not None:
        out["datastore_id"] = data["DatastoreId"]
    return out
