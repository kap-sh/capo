"""Generated from Smithy shape ``com.amazonaws.entityresolution#GetIdMappingJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_entityresolution.types.error_details
    import capo_entityresolution.types.id_mapping_job_metrics
    import capo_entityresolution.types.id_mapping_job_output_source_config
    import capo_entityresolution.types.job_id
    import capo_entityresolution.types.job_status
    import capo_entityresolution.types.job_type


class GetIdMappingJobOutput(TypedDict, closed=True):
    job_id: "capo_entityresolution.types.job_id.JobId"
    """<p>The ID of the job.</p>"""
    status: "capo_entityresolution.types.job_status.JobStatus"
    """<p>The current status of the job.</p>"""
    start_time: "datetime.datetime"
    """<p>The time at which the job was started.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The time at which the job has finished.</p>"""
    metrics: NotRequired[
        "capo_entityresolution.types.id_mapping_job_metrics.IdMappingJobMetrics"
    ]
    """<p>Metrics associated with the execution, specifically total records processed, unique IDs generated, and records the execution skipped.</p>"""
    error_details: NotRequired["capo_entityresolution.types.error_details.ErrorDetails"]
    output_source_config: NotRequired[
        "capo_entityresolution.types.id_mapping_job_output_source_config.IdMappingJobOutputSourceConfig"
    ]
    """<p>A list of <code>OutputSource</code> objects.</p>"""
    job_type: NotRequired["capo_entityresolution.types.job_type.JobType"]
    """<p> The job type of the ID mapping job.</p> <p>A value of <code>INCREMENTAL</code> indicates that only new or changed data was processed since the last job run. This is the default job type if the workflow was created with an <code>incrementalRunConfig</code>.</p> <p>A value of <code>BATCH</code> indicates that all data was processed from the input source, regardless of previous job runs. This is the default job type if the workflow wasn't created with an <code>incrementalRunConfig</code>.</p> <p>A value of <code>DELETE_ONLY</code> indicates that only deletion requests from <code>BatchDeleteUniqueIds</code> were processed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIdMappingJobOutput) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    import capo_entityresolution.types.job_status

    out["status"] = capo_entityresolution.types.job_status.serialize_json(
        value["status"]
    )
    import capo_entityresolution.types._prelude.timestamp

    out["startTime"] = capo_entityresolution.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    if "end_time" in value:
        import capo_entityresolution.types._prelude.timestamp

        out["endTime"] = capo_entityresolution.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    if "metrics" in value:
        import capo_entityresolution.types.id_mapping_job_metrics

        out["metrics"] = (
            capo_entityresolution.types.id_mapping_job_metrics.serialize_json(
                value["metrics"]
            )
        )
    if "error_details" in value:
        import capo_entityresolution.types.error_details

        out["errorDetails"] = capo_entityresolution.types.error_details.serialize_json(
            value["error_details"]
        )
    if "output_source_config" in value:
        import capo_entityresolution.types.id_mapping_job_output_source_config

        out["outputSourceConfig"] = (
            capo_entityresolution.types.id_mapping_job_output_source_config.serialize_json(
                value["output_source_config"]
            )
        )
    if "job_type" in value:
        import capo_entityresolution.types.job_type

        out["jobType"] = capo_entityresolution.types.job_type.serialize_json(
            value["job_type"]
        )
    return out


def deserialize_json(data: dict) -> GetIdMappingJobOutput:
    out: GetIdMappingJobOutput = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("status") is not None:
        import capo_entityresolution.types.job_status

        out["status"] = capo_entityresolution.types.job_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_entityresolution.types.job_status.JobStatus", ""
        )
    if data.get("startTime") is not None:
        import capo_entityresolution.types._prelude.timestamp

        out["start_time"] = (
            capo_entityresolution.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endTime") is not None:
        import capo_entityresolution.types._prelude.timestamp

        out["end_time"] = (
            capo_entityresolution.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    if data.get("metrics") is not None:
        import capo_entityresolution.types.id_mapping_job_metrics

        out["metrics"] = (
            capo_entityresolution.types.id_mapping_job_metrics.deserialize_json(
                data["metrics"]
            )
        )
    if data.get("errorDetails") is not None:
        import capo_entityresolution.types.error_details

        out["error_details"] = (
            capo_entityresolution.types.error_details.deserialize_json(
                data["errorDetails"]
            )
        )
    if data.get("outputSourceConfig") is not None:
        import capo_entityresolution.types.id_mapping_job_output_source_config

        out["output_source_config"] = (
            capo_entityresolution.types.id_mapping_job_output_source_config.deserialize_json(
                data["outputSourceConfig"]
            )
        )
    if data.get("jobType") is not None:
        import capo_entityresolution.types.job_type

        out["job_type"] = capo_entityresolution.types.job_type.deserialize_json(
            data["jobType"]
        )
    return out
