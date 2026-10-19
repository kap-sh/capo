"""Generated from Smithy shape ``com.amazonaws.healthlake#DescribeFHIRExportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.datastore_id
    import capo_healthlake.types.job_id


class DescribeFHIRExportJobRequest(TypedDict, closed=True):
    datastore_id: "capo_healthlake.types.datastore_id.DatastoreId"
    """<p>The data store identifier from which FHIR data is being exported from.</p>"""
    job_id: "capo_healthlake.types.job_id.JobId"
    """<p>The export job identifier.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeFHIRExportJobRequest) -> dict:
    out: dict = {}
    out["DatastoreId"] = value["datastore_id"]
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeFHIRExportJobRequest:
    out: DescribeFHIRExportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatastoreId") is not None:
        out["datastore_id"] = data["DatastoreId"]
    else:
        out["datastore_id"] = ""
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    return out
