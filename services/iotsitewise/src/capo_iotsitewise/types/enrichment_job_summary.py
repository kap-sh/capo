"""Generated from Smithy shape ``com.amazonaws.iotsitewise#EnrichmentJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_iotsitewise.types.asset_property_alias
    import capo_iotsitewise.types.enrichment_job_status
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.job_type
    import capo_iotsitewise.types.time_series_id
    import capo_iotsitewise.types.workspace_name


class EnrichmentJobSummary(TypedDict, closed=True):
    job_id: "capo_iotsitewise.types.id.ID"
    """<p>Unique identifier for the enrichment job.</p>"""
    status: "capo_iotsitewise.types.enrichment_job_status.EnrichmentJobStatus"
    """<p>Current status of the job: PENDING, RUNNING, COMPLETED, FAILED, TIMED_OUT, or CANCELLED. Use this to quickly identify active jobs or jobs requiring attention.</p>"""
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the IoT SiteWise workspace containing this job.</p>"""
    job_type: "capo_iotsitewise.types.job_type.JobType"
    """<p>The type of enrichment job. Currently EVENT_DETECTION is the only supported type.</p>"""
    dataset_id: "capo_iotsitewise.types.id.ID"
    """<p>The dataset being enriched. Useful for filtering and identifying jobs without fetching the full configuration. This allows you to quickly find all jobs related to a specific dataset.</p>"""
    property_alias: NotRequired[
        "capo_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
    ]
    """<p>The property alias (human-readable sensor name) of the time series being enriched. Present when the job was created using a propertyAlias. Use this to identify which sensor the job analyzes.</p>"""
    time_series_id: NotRequired["capo_iotsitewise.types.time_series_id.TimeSeriesId"]
    """<p>The system identifier of the time series being enriched. Present when the job was created using a timeSeriesId. Use this to identify which time series the job analyzes.</p>"""
    created_at: "datetime.datetime"
    """<p>Timestamp when the job was created in ISO 8601 format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>Timestamp of the last job status change in ISO 8601 format. Use this to track recent activity and identify stale jobs. For active jobs, this shows the last time the job transitioned to a new status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnrichmentJobSummary) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    import capo_iotsitewise.types.enrichment_job_status

    out["status"] = capo_iotsitewise.types.enrichment_job_status.serialize_json(
        value["status"]
    )
    out["workspaceName"] = value["workspace_name"]
    import capo_iotsitewise.types.job_type

    out["jobType"] = capo_iotsitewise.types.job_type.serialize_json(value["job_type"])
    out["datasetId"] = value["dataset_id"]
    if "property_alias" in value:
        out["propertyAlias"] = value["property_alias"]
    if "time_series_id" in value:
        out["timeSeriesId"] = value["time_series_id"]
    import capo_iotsitewise.types._prelude.timestamp

    out["createdAt"] = capo_iotsitewise.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    if "updated_at" in value:
        import capo_iotsitewise.types._prelude.timestamp

        out["updatedAt"] = capo_iotsitewise.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> EnrichmentJobSummary:
    out: EnrichmentJobSummary = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("status") is not None:
        import capo_iotsitewise.types.enrichment_job_status

        out["status"] = capo_iotsitewise.types.enrichment_job_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_iotsitewise.types.enrichment_job_status.EnrichmentJobStatus", ""
        )
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    else:
        out["workspace_name"] = ""
    if data.get("jobType") is not None:
        import capo_iotsitewise.types.job_type

        out["job_type"] = capo_iotsitewise.types.job_type.deserialize_json(
            data["jobType"]
        )
    else:
        import typing

        out["job_type"] = typing.cast("capo_iotsitewise.types.job_type.JobType", "")
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    else:
        out["dataset_id"] = ""
    if data.get("propertyAlias") is not None:
        out["property_alias"] = data["propertyAlias"]
    if data.get("timeSeriesId") is not None:
        out["time_series_id"] = data["timeSeriesId"]
    if data.get("createdAt") is not None:
        import capo_iotsitewise.types._prelude.timestamp

        out["created_at"] = capo_iotsitewise.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_iotsitewise.types._prelude.timestamp

        out["updated_at"] = capo_iotsitewise.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    return out
