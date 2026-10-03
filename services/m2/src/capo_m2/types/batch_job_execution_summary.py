"""Generated from Smithy shape ``com.amazonaws.m2#BatchJobExecutionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_m2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_m2.types.batch_job_execution_status
    import capo_m2.types.batch_job_identifier
    import capo_m2.types.batch_job_type
    import capo_m2.types.identifier
    import capo_m2.types.string100
    import capo_m2.types.timestamp


class BatchJobExecutionSummary(TypedDict, closed=True):
    execution_id: "capo_m2.types.identifier.Identifier"
    """<p>The unique identifier of this execution of the batch job.</p>"""
    application_id: "capo_m2.types.identifier.Identifier"
    """<p>The unique identifier of the application that hosts this batch job.</p>"""
    job_id: NotRequired["capo_m2.types.string100.String100"]
    """<p>The unique identifier of a particular batch job.</p>"""
    job_name: NotRequired["capo_m2.types.string100.String100"]
    """<p>The name of a particular batch job.</p>"""
    job_type: NotRequired["capo_m2.types.batch_job_type.BatchJobType"]
    """<p>The type of a particular batch job execution.</p>"""
    status: "capo_m2.types.batch_job_execution_status.BatchJobExecutionStatus"
    """<p>The status of a particular batch job execution.</p>"""
    start_time: "capo_m2.types.timestamp.Timestamp"
    """<p>The timestamp when a particular batch job execution started.</p>"""
    end_time: NotRequired["capo_m2.types.timestamp.Timestamp"]
    """<p>The timestamp when this batch job execution ended.</p>"""
    return_code: NotRequired["str"]
    """<p>The batch job return code from either the Blu Age or Micro Focus runtime engines. For more information, see <a href="https://www.ibm.com/docs/en/was/8.5.5?topic=model-batch-return-codes">Batch return codes</a> in the <i>IBM WebSphere Application Server</i> documentation.</p>"""
    batch_job_identifier: NotRequired[
        "capo_m2.types.batch_job_identifier.BatchJobIdentifier"
    ]
    """<p>The unique identifier of this batch job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchJobExecutionSummary) -> dict:
    out: dict = {}
    out["executionId"] = value["execution_id"]
    out["applicationId"] = value["application_id"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "job_type" in value:
        out["jobType"] = value["job_type"]
    out["status"] = value["status"]
    import capo_m2.types.timestamp

    out["startTime"] = capo_m2.types.timestamp.serialize_json(value["start_time"])
    if "end_time" in value:
        import capo_m2.types.timestamp

        out["endTime"] = capo_m2.types.timestamp.serialize_json(value["end_time"])
    if "return_code" in value:
        out["returnCode"] = value["return_code"]
    if "batch_job_identifier" in value:
        import capo_m2.types.batch_job_identifier

        out["batchJobIdentifier"] = capo_m2.types.batch_job_identifier.serialize_json(
            value["batch_job_identifier"]
        )
    return out


def deserialize_json(data: dict) -> BatchJobExecutionSummary:
    out: BatchJobExecutionSummary = {}  # type: ignore[typeddict-item]
    if data.get("executionId") is not None:
        out["execution_id"] = data["executionId"]
    else:
        raise DeserializationError("BatchJobExecutionSummary.execution_id required")
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError("BatchJobExecutionSummary.application_id required")
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    if data.get("jobType") is not None:
        out["job_type"] = data["jobType"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("BatchJobExecutionSummary.status required")
    if data.get("startTime") is not None:
        import capo_m2.types.timestamp

        out["start_time"] = capo_m2.types.timestamp.deserialize_json(data["startTime"])
    else:
        raise DeserializationError("BatchJobExecutionSummary.start_time required")
    if data.get("endTime") is not None:
        import capo_m2.types.timestamp

        out["end_time"] = capo_m2.types.timestamp.deserialize_json(data["endTime"])
    if data.get("returnCode") is not None:
        out["return_code"] = data["returnCode"]
    if data.get("batchJobIdentifier") is not None:
        import capo_m2.types.batch_job_identifier

        out["batch_job_identifier"] = (
            capo_m2.types.batch_job_identifier.deserialize_json(
                data["batchJobIdentifier"]
            )
        )
    return out
