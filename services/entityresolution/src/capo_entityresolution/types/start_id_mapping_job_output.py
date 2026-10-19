"""Generated from Smithy shape ``com.amazonaws.entityresolution#StartIdMappingJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.id_mapping_job_output_source_config
    import capo_entityresolution.types.job_id
    import capo_entityresolution.types.job_type


class StartIdMappingJobOutput(TypedDict, closed=True):
    job_id: "capo_entityresolution.types.job_id.JobId"
    """<p>The ID of the job.</p>"""
    output_source_config: NotRequired[
        "capo_entityresolution.types.id_mapping_job_output_source_config.IdMappingJobOutputSourceConfig"
    ]
    """<p>A list of <code>OutputSource</code> objects.</p>"""
    job_type: NotRequired["capo_entityresolution.types.job_type.JobType"]
    """<p> The job type for the started ID mapping job.</p> <p>A value of <code>INCREMENTAL</code> indicates that only new or changed data was processed since the last job run. This is the default job type if the workflow was created with an <code>incrementalRunConfig</code>.</p> <p>A value of <code>BATCH</code> indicates that all data was processed from the input source, regardless of previous job runs. This is the default job type if the workflow wasn't created with an <code>incrementalRunConfig</code>.</p> <p>A value of <code>DELETE_ONLY</code> indicates that only deletion requests from <code>BatchDeleteUniqueIds</code> were processed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartIdMappingJobOutput) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
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


def deserialize_json(data: dict) -> StartIdMappingJobOutput:
    out: StartIdMappingJobOutput = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
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
