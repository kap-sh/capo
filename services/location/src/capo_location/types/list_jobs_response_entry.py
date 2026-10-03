"""Generated from Smithy shape ``com.amazonaws.location#ListJobsResponseEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.geo_arn
    import capo_location.types.iam_role_arn
    import capo_location.types.job_action
    import capo_location.types.job_action_options
    import capo_location.types.job_error
    import capo_location.types.job_id
    import capo_location.types.job_input_options
    import capo_location.types.job_output_options
    import capo_location.types.job_status
    import capo_location.types.resource_name
    import capo_location.types.timestamp


class ListJobsResponseEntry(TypedDict, closed=True):
    action: "capo_location.types.job_action.JobAction"
    """<p>Action performed by the job.</p>"""
    action_options: NotRequired[
        "capo_location.types.job_action_options.JobActionOptions"
    ]
    """<p>Additional options for configuring job action parameters.</p>"""
    created_at: "capo_location.types.timestamp.Timestamp"
    """<p>Job creation time in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sss</code>.</p>"""
    execution_role_arn: "capo_location.types.iam_role_arn.IamRoleArn"
    """<p>IAM role used for job execution.</p>"""
    ended_at: NotRequired["capo_location.types.timestamp.Timestamp"]
    """<p>Job completion time in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sss</code>. Only returned for jobs in a terminal status: <code>Completed</code> | <code>Failed</code> | <code>Cancelled</code>.</p>"""
    error: NotRequired["capo_location.types.job_error.JobError"]
    """<p>Error information if the job failed.</p>"""
    input_options: "capo_location.types.job_input_options.JobInputOptions"
    """<p>Input configuration.</p>"""
    job_id: "capo_location.types.job_id.JobId"
    """<p>Unique job identifier.</p>"""
    job_arn: "capo_location.types.geo_arn.GeoArn"
    """<p>Amazon Resource Name (ARN) of the job.</p>"""
    name: NotRequired["capo_location.types.resource_name.ResourceName"]
    """<p>Job name (if provided during creation).</p>"""
    output_options: "capo_location.types.job_output_options.JobOutputOptions"
    """<p>Output configuration.</p>"""
    status: "capo_location.types.job_status.JobStatus"
    """<p>Current job status.</p>"""
    updated_at: "capo_location.types.timestamp.Timestamp"
    """<p>Last update time in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sss</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsResponseEntry) -> dict:
    out: dict = {}
    out["Action"] = value["action"]
    if "action_options" in value:
        import capo_location.types.job_action_options

        out["ActionOptions"] = capo_location.types.job_action_options.serialize_json(
            value["action_options"]
        )
    import capo_location.types.timestamp

    out["CreatedAt"] = capo_location.types.timestamp.serialize_json(value["created_at"])
    out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "ended_at" in value:
        import capo_location.types.timestamp

        out["EndedAt"] = capo_location.types.timestamp.serialize_json(value["ended_at"])
    if "error" in value:
        import capo_location.types.job_error

        out["Error"] = capo_location.types.job_error.serialize_json(value["error"])
    import capo_location.types.job_input_options

    out["InputOptions"] = capo_location.types.job_input_options.serialize_json(
        value["input_options"]
    )
    out["JobId"] = value["job_id"]
    out["JobArn"] = value["job_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    import capo_location.types.job_output_options

    out["OutputOptions"] = capo_location.types.job_output_options.serialize_json(
        value["output_options"]
    )
    out["Status"] = value["status"]
    import capo_location.types.timestamp

    out["UpdatedAt"] = capo_location.types.timestamp.serialize_json(value["updated_at"])
    return out


def deserialize_json(data: dict) -> ListJobsResponseEntry:
    out: ListJobsResponseEntry = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        out["action"] = data["Action"]
    else:
        raise DeserializationError("ListJobsResponseEntry.action required")
    if data.get("ActionOptions") is not None:
        import capo_location.types.job_action_options

        out["action_options"] = capo_location.types.job_action_options.deserialize_json(
            data["ActionOptions"]
        )
    if data.get("CreatedAt") is not None:
        import capo_location.types.timestamp

        out["created_at"] = capo_location.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError("ListJobsResponseEntry.created_at required")
    if data.get("ExecutionRoleArn") is not None:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    else:
        raise DeserializationError("ListJobsResponseEntry.execution_role_arn required")
    if data.get("EndedAt") is not None:
        import capo_location.types.timestamp

        out["ended_at"] = capo_location.types.timestamp.deserialize_json(
            data["EndedAt"]
        )
    if data.get("Error") is not None:
        import capo_location.types.job_error

        out["error"] = capo_location.types.job_error.deserialize_json(data["Error"])
    if data.get("InputOptions") is not None:
        import capo_location.types.job_input_options

        out["input_options"] = capo_location.types.job_input_options.deserialize_json(
            data["InputOptions"]
        )
    else:
        raise DeserializationError("ListJobsResponseEntry.input_options required")
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("ListJobsResponseEntry.job_id required")
    if data.get("JobArn") is not None:
        out["job_arn"] = data["JobArn"]
    else:
        raise DeserializationError("ListJobsResponseEntry.job_arn required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("OutputOptions") is not None:
        import capo_location.types.job_output_options

        out["output_options"] = capo_location.types.job_output_options.deserialize_json(
            data["OutputOptions"]
        )
    else:
        raise DeserializationError("ListJobsResponseEntry.output_options required")
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("ListJobsResponseEntry.status required")
    if data.get("UpdatedAt") is not None:
        import capo_location.types.timestamp

        out["updated_at"] = capo_location.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    else:
        raise DeserializationError("ListJobsResponseEntry.updated_at required")
    return out
