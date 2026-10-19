"""Generated from Smithy shape ``com.amazonaws.kendra#DataSourceSyncJobMetricTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.data_source_id
    import capo_kendra.types.data_source_sync_job_id


class DataSourceSyncJobMetricTarget(TypedDict, closed=True):
    data_source_id: "capo_kendra.types.data_source_id.DataSourceId"
    """<p>The ID of the data source that is running the sync job.</p>"""
    data_source_sync_job_id: NotRequired[
        "capo_kendra.types.data_source_sync_job_id.DataSourceSyncJobId"
    ]
    """<p>The ID of the sync job that is running on the data source.</p> <p>If the ID of a sync job is not provided and there is a sync job running, then the ID of this sync job is used and metrics are generated for this sync job.</p> <p>If the ID of a sync job is not provided and there is no sync job running, then no metrics are generated and documents are indexed/deleted at the index level without sync job metrics included.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSourceSyncJobMetricTarget) -> dict:
    out: dict = {}
    out["DataSourceId"] = value["data_source_id"]
    if "data_source_sync_job_id" in value:
        out["DataSourceSyncJobId"] = value["data_source_sync_job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataSourceSyncJobMetricTarget:
    out: DataSourceSyncJobMetricTarget = {}  # type: ignore[typeddict-item]
    if data.get("DataSourceId") is not None:
        out["data_source_id"] = data["DataSourceId"]
    else:
        out["data_source_id"] = ""
    if data.get("DataSourceSyncJobId") is not None:
        out["data_source_sync_job_id"] = data["DataSourceSyncJobId"]
    return out
