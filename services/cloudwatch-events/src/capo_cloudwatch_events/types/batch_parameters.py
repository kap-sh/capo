"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#BatchParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.batch_array_properties
    import capo_cloudwatch_events.types.batch_retry_strategy
    import capo_cloudwatch_events.types.string


class BatchParameters(TypedDict, closed=True):
    job_definition: "capo_cloudwatch_events.types.string.String"
    """<p>The ARN or name of the job definition to use if the event target is an Batch job. This job definition must already exist.</p>"""
    job_name: "capo_cloudwatch_events.types.string.String"
    """<p>The name to use for this execution of the job, if the target is an Batch job.</p>"""
    array_properties: NotRequired[
        "capo_cloudwatch_events.types.batch_array_properties.BatchArrayProperties"
    ]
    """<p>The array properties for the submitted job, such as the size of the array. The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. This parameter is used only if the target is an Batch job.</p>"""
    retry_strategy: NotRequired[
        "capo_cloudwatch_events.types.batch_retry_strategy.BatchRetryStrategy"
    ]
    """<p>The retry strategy to use for failed jobs, if the target is an Batch job. The retry strategy is the number of times to retry the failed job execution. Valid values are 1–10. When you specify a retry strategy here, it overrides the retry strategy defined in the job definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchParameters) -> dict:
    out: dict = {}
    out["JobDefinition"] = value["job_definition"]
    out["JobName"] = value["job_name"]
    if "array_properties" in value:
        import capo_cloudwatch_events.types.batch_array_properties

        out["ArrayProperties"] = (
            capo_cloudwatch_events.types.batch_array_properties.serialize_aws_json_1_1(
                value["array_properties"]
            )
        )
    if "retry_strategy" in value:
        import capo_cloudwatch_events.types.batch_retry_strategy

        out["RetryStrategy"] = (
            capo_cloudwatch_events.types.batch_retry_strategy.serialize_aws_json_1_1(
                value["retry_strategy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchParameters:
    out: BatchParameters = {}  # type: ignore[typeddict-item]
    if data.get("JobDefinition") is not None:
        out["job_definition"] = data["JobDefinition"]
    else:
        out["job_definition"] = ""
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    else:
        out["job_name"] = ""
    if data.get("ArrayProperties") is not None:
        import capo_cloudwatch_events.types.batch_array_properties

        out["array_properties"] = (
            capo_cloudwatch_events.types.batch_array_properties.deserialize_aws_json_1_1(
                data["ArrayProperties"]
            )
        )
    if data.get("RetryStrategy") is not None:
        import capo_cloudwatch_events.types.batch_retry_strategy

        out["retry_strategy"] = (
            capo_cloudwatch_events.types.batch_retry_strategy.deserialize_aws_json_1_1(
                data["RetryStrategy"]
            )
        )
    return out
