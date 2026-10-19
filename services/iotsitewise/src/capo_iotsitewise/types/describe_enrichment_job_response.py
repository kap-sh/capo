"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeEnrichmentJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_iotsitewise.types.enrichment_job_configuration
    import capo_iotsitewise.types.enrichment_job_status
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.job_type
    import capo_iotsitewise.types.workspace_name


class DescribeEnrichmentJobResponse(TypedDict, closed=True):
    job_id: "capo_iotsitewise.types.id.ID"
    """<p>The unique identifier of the enrichment job.</p>"""
    status: "capo_iotsitewise.types.enrichment_job_status.EnrichmentJobStatus"
    """<p>Current status of the enrichment job. Possible values:</p> <ul> <li>PENDING: Job is waiting to start processing</li> <li>RUNNING: Job is actively processing video data</li> <li>COMPLETED: Job finished successfully; embeddings available in IoT SiteWise</li> <li>FAILED: Job encountered an error; see failureMessage for details</li> <li>TIMED_OUT: Job exceeded maximum processing time limit</li> <li>CANCELLED: Job was cancelled by user request</li> </ul>"""
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the IoT SiteWise workspace containing the job.</p>"""
    job_type: "capo_iotsitewise.types.job_type.JobType"
    """<p>The type of enrichment job, derived from the job configuration. Currently EVENT_DETECTION is the only supported type.</p>"""
    job_configuration: (
        "capo_iotsitewise.types.enrichment_job_configuration.EnrichmentJobConfiguration"
    )
    """<p>The complete job configuration as originally submitted, including the analysis type and parameters. For event detection jobs, this includes the dataset ID, time series identifier, and trim settings defining the analysis time range.</p>"""
    created_at: "datetime.datetime"
    """<p>Timestamp when the enrichment job was created in ISO 8601 format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>Timestamp when the job status was last updated in ISO 8601 format. Useful for tracking recent activity.</p>"""
    completed_at: NotRequired["datetime.datetime"]
    """<p>Timestamp when the job completed successfully in ISO 8601 format. Only present if status is COMPLETED.</p>"""
    cancelled_at: NotRequired["datetime.datetime"]
    """<p>Timestamp when the job was cancelled in ISO 8601 format. Only present if status is CANCELLED.</p>"""
    failure_message: NotRequired["str"]
    """<p>Human-readable error message explaining why the job failed. Only present if status is FAILED. Use this information to diagnose configuration issues, permission problems, or data processing errors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeEnrichmentJobResponse) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    import capo_iotsitewise.types.enrichment_job_status

    out["status"] = capo_iotsitewise.types.enrichment_job_status.serialize_json(
        value["status"]
    )
    out["workspaceName"] = value["workspace_name"]
    import capo_iotsitewise.types.job_type

    out["jobType"] = capo_iotsitewise.types.job_type.serialize_json(value["job_type"])
    import capo_iotsitewise.types.enrichment_job_configuration

    out["jobConfiguration"] = (
        capo_iotsitewise.types.enrichment_job_configuration.serialize_json(
            value["job_configuration"]
        )
    )
    import capo_iotsitewise.types._prelude.timestamp

    out["createdAt"] = capo_iotsitewise.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    if "updated_at" in value:
        import capo_iotsitewise.types._prelude.timestamp

        out["updatedAt"] = capo_iotsitewise.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "completed_at" in value:
        import capo_iotsitewise.types._prelude.timestamp

        out["completedAt"] = capo_iotsitewise.types._prelude.timestamp.serialize_json(
            value["completed_at"]
        )
    if "cancelled_at" in value:
        import capo_iotsitewise.types._prelude.timestamp

        out["cancelledAt"] = capo_iotsitewise.types._prelude.timestamp.serialize_json(
            value["cancelled_at"]
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    return out


def deserialize_json(data: dict) -> DescribeEnrichmentJobResponse:
    out: DescribeEnrichmentJobResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("jobConfiguration") is not None:
        import capo_iotsitewise.types.enrichment_job_configuration

        out["job_configuration"] = (
            capo_iotsitewise.types.enrichment_job_configuration.deserialize_json(
                data["jobConfiguration"]
            )
        )
    else:
        import capo_iotsitewise.types._unknown

        out["job_configuration"] = capo_iotsitewise.types._unknown.UnknownUnionMember(
            ""
        )
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
    if data.get("completedAt") is not None:
        import capo_iotsitewise.types._prelude.timestamp

        out["completed_at"] = (
            capo_iotsitewise.types._prelude.timestamp.deserialize_json(
                data["completedAt"]
            )
        )
    if data.get("cancelledAt") is not None:
        import capo_iotsitewise.types._prelude.timestamp

        out["cancelled_at"] = (
            capo_iotsitewise.types._prelude.timestamp.deserialize_json(
                data["cancelledAt"]
            )
        )
    if data.get("failureMessage") is not None:
        out["failure_message"] = data["failureMessage"]
    return out
