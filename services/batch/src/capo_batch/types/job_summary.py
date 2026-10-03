"""Generated from Smithy shape ``com.amazonaws.batch#JobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.array_properties_summary
    import capo_batch.types.boolean
    import capo_batch.types.container_summary
    import capo_batch.types.job_capacity_usage_summary_list
    import capo_batch.types.job_status
    import capo_batch.types.long
    import capo_batch.types.node_properties_summary
    import capo_batch.types.string


class JobSummary(TypedDict, closed=True):
    job_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the job.</p>"""
    job_id: NotRequired["capo_batch.types.string.String"]
    """<p>The job ID.</p>"""
    job_name: NotRequired["capo_batch.types.string.String"]
    """<p>The job name.</p>"""
    capacity_usage: NotRequired[
        "capo_batch.types.job_capacity_usage_summary_list.JobCapacityUsageSummaryList"
    ]
    """<p>The configured capacity usage information for this job, including the unit of measure and quantity of resources.</p>"""
    created_at: NotRequired["capo_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the job was created. For non-array jobs and parent array jobs, this is when the job entered the <code>SUBMITTED</code> state (at the time <a href="https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html">SubmitJob</a> was called). For array child jobs, this is when the child job was spawned by its parent and entered the <code>PENDING</code> state.</p>"""
    scheduled_at: NotRequired["capo_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the job was scheduled for execution. For more information on job statues, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/service-job-status.html">Service job status</a> in the <i>Batch User Guide</i>.</p>"""
    share_identifier: NotRequired["capo_batch.types.string.String"]
    """<p>The share identifier for the fairshare scheduling queue that this job is associated with.</p>"""
    status: NotRequired["capo_batch.types.job_status.JobStatus"]
    """<p>The current status for the job.</p>"""
    status_reason: NotRequired["capo_batch.types.string.String"]
    """<p>A short, human-readable string to provide more details for the current status of the job.</p>"""
    started_at: NotRequired["capo_batch.types.long.Long"]
    """<p>The Unix timestamp for when the job was started. More specifically, it's when the job transitioned from the <code>STARTING</code> state to the <code>RUNNING</code> state.</p>"""
    stopped_at: NotRequired["capo_batch.types.long.Long"]
    """<p>The Unix timestamp for when the job was stopped. More specifically, it's when the job transitioned from the <code>RUNNING</code> state to a terminal state, such as <code>SUCCEEDED</code> or <code>FAILED</code>.</p>"""
    container: NotRequired["capo_batch.types.container_summary.ContainerSummary"]
    """<p>An object that represents the details of the container that's associated with the job.</p>"""
    array_properties: NotRequired[
        "capo_batch.types.array_properties_summary.ArrayPropertiesSummary"
    ]
    """<p>The array properties of the job, if it's an array job.</p>"""
    node_properties: NotRequired[
        "capo_batch.types.node_properties_summary.NodePropertiesSummary"
    ]
    """<p>The node properties for a single node in a job summary list.</p> <note> <p>This isn't applicable to jobs that are running on Fargate resources.</p> </note>"""
    job_definition: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the job definition.</p>"""
    is_cancelled: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>Indicates whether a cancellation request has been accepted for the job. This field is only present when the value is <code>true</code>.</p>"""
    is_terminated: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>Indicates whether a termination request has been accepted for the job. This field is only present when the value is <code>true</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobSummary) -> dict:
    out: dict = {}
    if "job_arn" in value:
        out["jobArn"] = value["job_arn"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "capacity_usage" in value:
        import capo_batch.types.job_capacity_usage_summary_list

        out["capacityUsage"] = (
            capo_batch.types.job_capacity_usage_summary_list.serialize_json(
                value["capacity_usage"]
            )
        )
    if "created_at" in value:
        out["createdAt"] = value["created_at"]
    if "scheduled_at" in value:
        out["scheduledAt"] = value["scheduled_at"]
    if "share_identifier" in value:
        out["shareIdentifier"] = value["share_identifier"]
    if "status" in value:
        import capo_batch.types.job_status

        out["status"] = capo_batch.types.job_status.serialize_json(value["status"])
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "started_at" in value:
        out["startedAt"] = value["started_at"]
    if "stopped_at" in value:
        out["stoppedAt"] = value["stopped_at"]
    if "container" in value:
        import capo_batch.types.container_summary

        out["container"] = capo_batch.types.container_summary.serialize_json(
            value["container"]
        )
    if "array_properties" in value:
        import capo_batch.types.array_properties_summary

        out["arrayProperties"] = (
            capo_batch.types.array_properties_summary.serialize_json(
                value["array_properties"]
            )
        )
    if "node_properties" in value:
        import capo_batch.types.node_properties_summary

        out["nodeProperties"] = capo_batch.types.node_properties_summary.serialize_json(
            value["node_properties"]
        )
    if "job_definition" in value:
        out["jobDefinition"] = value["job_definition"]
    if "is_cancelled" in value:
        out["isCancelled"] = value["is_cancelled"]
    if "is_terminated" in value:
        out["isTerminated"] = value["is_terminated"]
    return out


def deserialize_json(data: dict) -> JobSummary:
    out: JobSummary = {}  # type: ignore[typeddict-item]
    if data.get("jobArn") is not None:
        out["job_arn"] = data["jobArn"]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    if data.get("capacityUsage") is not None:
        import capo_batch.types.job_capacity_usage_summary_list

        out["capacity_usage"] = (
            capo_batch.types.job_capacity_usage_summary_list.deserialize_json(
                data["capacityUsage"]
            )
        )
    if data.get("createdAt") is not None:
        out["created_at"] = data["createdAt"]
    if data.get("scheduledAt") is not None:
        out["scheduled_at"] = data["scheduledAt"]
    if data.get("shareIdentifier") is not None:
        out["share_identifier"] = data["shareIdentifier"]
    if data.get("status") is not None:
        import capo_batch.types.job_status

        out["status"] = capo_batch.types.job_status.deserialize_json(data["status"])
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("startedAt") is not None:
        out["started_at"] = data["startedAt"]
    if data.get("stoppedAt") is not None:
        out["stopped_at"] = data["stoppedAt"]
    if data.get("container") is not None:
        import capo_batch.types.container_summary

        out["container"] = capo_batch.types.container_summary.deserialize_json(
            data["container"]
        )
    if data.get("arrayProperties") is not None:
        import capo_batch.types.array_properties_summary

        out["array_properties"] = (
            capo_batch.types.array_properties_summary.deserialize_json(
                data["arrayProperties"]
            )
        )
    if data.get("nodeProperties") is not None:
        import capo_batch.types.node_properties_summary

        out["node_properties"] = (
            capo_batch.types.node_properties_summary.deserialize_json(
                data["nodeProperties"]
            )
        )
    if data.get("jobDefinition") is not None:
        out["job_definition"] = data["jobDefinition"]
    if data.get("isCancelled") is not None:
        out["is_cancelled"] = data["isCancelled"]
    if data.get("isTerminated") is not None:
        out["is_terminated"] = data["isTerminated"]
    return out
