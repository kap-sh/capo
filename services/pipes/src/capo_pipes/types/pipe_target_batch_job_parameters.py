"""Generated from Smithy shape ``com.amazonaws.pipes#PipeTargetBatchJobParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.batch_array_properties
    import capo_pipes.types.batch_container_overrides
    import capo_pipes.types.batch_depends_on
    import capo_pipes.types.batch_parameters_map
    import capo_pipes.types.batch_retry_strategy


class PipeTargetBatchJobParameters(TypedDict, closed=True):
    job_definition: "str"
    """<p>The job definition used by this job. This value can be one of <code>name</code>, <code>name:revision</code>, or the Amazon Resource Name (ARN) for the job definition. If name is specified without a revision then the latest active revision is used.</p>"""
    job_name: "str"
    """<p>The name of the job. It can be up to 128 letters long. The first character must be alphanumeric, can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).</p>"""
    array_properties: NotRequired[
        "capo_pipes.types.batch_array_properties.BatchArrayProperties"
    ]
    """<p>The array properties for the submitted job, such as the size of the array. The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. This parameter is used only if the target is an Batch job.</p>"""
    retry_strategy: NotRequired[
        "capo_pipes.types.batch_retry_strategy.BatchRetryStrategy"
    ]
    """<p>The retry strategy to use for failed jobs. When a retry strategy is specified here, it overrides the retry strategy defined in the job definition.</p>"""
    container_overrides: NotRequired[
        "capo_pipes.types.batch_container_overrides.BatchContainerOverrides"
    ]
    """<p>The overrides that are sent to a container.</p>"""
    depends_on: NotRequired["capo_pipes.types.batch_depends_on.BatchDependsOn"]
    """<p>A list of dependencies for the job. A job can depend upon a maximum of 20 jobs. You can specify a <code>SEQUENTIAL</code> type dependency without specifying a job ID for array jobs so that each child array job completes sequentially, starting at index 0. You can also specify an <code>N_TO_N</code> type dependency with a job ID for array jobs. In that case, each index child of this job must wait for the corresponding index child of each dependency to complete before it can begin.</p>"""
    parameters: NotRequired["capo_pipes.types.batch_parameters_map.BatchParametersMap"]
    """<p>Additional parameters passed to the job that replace parameter substitution placeholders that are set in the job definition. Parameters are specified as a key and value pair mapping. Parameters included here override any corresponding parameter defaults from the job definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeTargetBatchJobParameters) -> dict:
    out: dict = {}
    out["JobDefinition"] = value["job_definition"]
    out["JobName"] = value["job_name"]
    if "array_properties" in value:
        import capo_pipes.types.batch_array_properties

        out["ArrayProperties"] = capo_pipes.types.batch_array_properties.serialize_json(
            value["array_properties"]
        )
    if "retry_strategy" in value:
        import capo_pipes.types.batch_retry_strategy

        out["RetryStrategy"] = capo_pipes.types.batch_retry_strategy.serialize_json(
            value["retry_strategy"]
        )
    if "container_overrides" in value:
        import capo_pipes.types.batch_container_overrides

        out["ContainerOverrides"] = (
            capo_pipes.types.batch_container_overrides.serialize_json(
                value["container_overrides"]
            )
        )
    if "depends_on" in value:
        import capo_pipes.types.batch_depends_on

        out["DependsOn"] = capo_pipes.types.batch_depends_on.serialize_json(
            value["depends_on"]
        )
    if "parameters" in value:
        import capo_pipes.types.batch_parameters_map

        out["Parameters"] = capo_pipes.types.batch_parameters_map.serialize_json(
            value["parameters"]
        )
    return out


def deserialize_json(data: dict) -> PipeTargetBatchJobParameters:
    out: PipeTargetBatchJobParameters = {}  # type: ignore[typeddict-item]
    if data.get("JobDefinition") is not None:
        out["job_definition"] = data["JobDefinition"]
    else:
        out["job_definition"] = ""
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    else:
        out["job_name"] = ""
    if data.get("ArrayProperties") is not None:
        import capo_pipes.types.batch_array_properties

        out["array_properties"] = (
            capo_pipes.types.batch_array_properties.deserialize_json(
                data["ArrayProperties"]
            )
        )
    if data.get("RetryStrategy") is not None:
        import capo_pipes.types.batch_retry_strategy

        out["retry_strategy"] = capo_pipes.types.batch_retry_strategy.deserialize_json(
            data["RetryStrategy"]
        )
    if data.get("ContainerOverrides") is not None:
        import capo_pipes.types.batch_container_overrides

        out["container_overrides"] = (
            capo_pipes.types.batch_container_overrides.deserialize_json(
                data["ContainerOverrides"]
            )
        )
    if data.get("DependsOn") is not None:
        import capo_pipes.types.batch_depends_on

        out["depends_on"] = capo_pipes.types.batch_depends_on.deserialize_json(
            data["DependsOn"]
        )
    if data.get("Parameters") is not None:
        import capo_pipes.types.batch_parameters_map

        out["parameters"] = capo_pipes.types.batch_parameters_map.deserialize_json(
            data["Parameters"]
        )
    return out
