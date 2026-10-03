"""Generated from Smithy shape ``com.amazonaws.sagemaker#PipelineExecutionStep``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cache_hit_result
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.integer
    import capo_sagemaker.types.pipeline_execution_step_metadata
    import capo_sagemaker.types.selective_execution_result
    import capo_sagemaker.types.step_description
    import capo_sagemaker.types.step_display_name
    import capo_sagemaker.types.step_name
    import capo_sagemaker.types.step_status
    import capo_sagemaker.types.timestamp


class PipelineExecutionStep(TypedDict, closed=True):
    step_name: NotRequired["capo_sagemaker.types.step_name.StepName"]
    """<p>The name of the step that is executed.</p>"""
    step_display_name: NotRequired[
        "capo_sagemaker.types.step_display_name.StepDisplayName"
    ]
    """<p>The display name of the step.</p>"""
    step_description: NotRequired[
        "capo_sagemaker.types.step_description.StepDescription"
    ]
    """<p>The description of the step.</p>"""
    start_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time that the step started executing.</p>"""
    end_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time that the step stopped executing.</p>"""
    step_status: NotRequired["capo_sagemaker.types.step_status.StepStatus"]
    """<p>The status of the step execution.</p>"""
    cache_hit_result: NotRequired[
        "capo_sagemaker.types.cache_hit_result.CacheHitResult"
    ]
    """<p>If this pipeline execution step was cached, details on the cache hit.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>The reason why the step failed execution. This is only returned if the step failed its execution.</p>"""
    metadata: NotRequired[
        "capo_sagemaker.types.pipeline_execution_step_metadata.PipelineExecutionStepMetadata"
    ]
    """<p>Metadata to run the pipeline step.</p>"""
    attempt_count: NotRequired["capo_sagemaker.types.integer.Integer"]
    """<p>The current attempt of the execution step. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-retry-policy.html">Retry Policy for SageMaker Pipelines steps</a>.</p>"""
    selective_execution_result: NotRequired[
        "capo_sagemaker.types.selective_execution_result.SelectiveExecutionResult"
    ]
    """<p>The ARN from an execution of the current pipeline from which results are reused for this step.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineExecutionStep) -> dict:
    out: dict = {}
    if "step_name" in value:
        out["StepName"] = value["step_name"]
    if "step_display_name" in value:
        out["StepDisplayName"] = value["step_display_name"]
    if "step_description" in value:
        out["StepDescription"] = value["step_description"]
    if "start_time" in value:
        import capo_sagemaker.types.timestamp

        out["StartTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_sagemaker.types.timestamp

        out["EndTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "step_status" in value:
        import capo_sagemaker.types.step_status

        out["StepStatus"] = capo_sagemaker.types.step_status.serialize_aws_json_1_1(
            value["step_status"]
        )
    if "cache_hit_result" in value:
        import capo_sagemaker.types.cache_hit_result

        out["CacheHitResult"] = (
            capo_sagemaker.types.cache_hit_result.serialize_aws_json_1_1(
                value["cache_hit_result"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "metadata" in value:
        import capo_sagemaker.types.pipeline_execution_step_metadata

        out["Metadata"] = (
            capo_sagemaker.types.pipeline_execution_step_metadata.serialize_aws_json_1_1(
                value["metadata"]
            )
        )
    if "attempt_count" in value:
        out["AttemptCount"] = value["attempt_count"]
    if "selective_execution_result" in value:
        import capo_sagemaker.types.selective_execution_result

        out["SelectiveExecutionResult"] = (
            capo_sagemaker.types.selective_execution_result.serialize_aws_json_1_1(
                value["selective_execution_result"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineExecutionStep:
    out: PipelineExecutionStep = {}  # type: ignore[typeddict-item]
    if data.get("StepName") is not None:
        out["step_name"] = data["StepName"]
    if data.get("StepDisplayName") is not None:
        out["step_display_name"] = data["StepDisplayName"]
    if data.get("StepDescription") is not None:
        out["step_description"] = data["StepDescription"]
    if data.get("StartTime") is not None:
        import capo_sagemaker.types.timestamp

        out["start_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_sagemaker.types.timestamp

        out["end_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if data.get("StepStatus") is not None:
        import capo_sagemaker.types.step_status

        out["step_status"] = capo_sagemaker.types.step_status.deserialize_aws_json_1_1(
            data["StepStatus"]
        )
    if data.get("CacheHitResult") is not None:
        import capo_sagemaker.types.cache_hit_result

        out["cache_hit_result"] = (
            capo_sagemaker.types.cache_hit_result.deserialize_aws_json_1_1(
                data["CacheHitResult"]
            )
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("Metadata") is not None:
        import capo_sagemaker.types.pipeline_execution_step_metadata

        out["metadata"] = (
            capo_sagemaker.types.pipeline_execution_step_metadata.deserialize_aws_json_1_1(
                data["Metadata"]
            )
        )
    if data.get("AttemptCount") is not None:
        out["attempt_count"] = data["AttemptCount"]
    if data.get("SelectiveExecutionResult") is not None:
        import capo_sagemaker.types.selective_execution_result

        out["selective_execution_result"] = (
            capo_sagemaker.types.selective_execution_result.deserialize_aws_json_1_1(
                data["SelectiveExecutionResult"]
            )
        )
    return out
