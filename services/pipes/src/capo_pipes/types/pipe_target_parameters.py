"""Generated from Smithy shape ``com.amazonaws.pipes#PipeTargetParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.input_template
    import capo_pipes.types.pipe_target_batch_job_parameters
    import capo_pipes.types.pipe_target_cloud_watch_logs_parameters
    import capo_pipes.types.pipe_target_ecs_task_parameters
    import capo_pipes.types.pipe_target_event_bridge_event_bus_parameters
    import capo_pipes.types.pipe_target_http_parameters
    import capo_pipes.types.pipe_target_kinesis_stream_parameters
    import capo_pipes.types.pipe_target_lambda_function_parameters
    import capo_pipes.types.pipe_target_redshift_data_parameters
    import capo_pipes.types.pipe_target_sage_maker_pipeline_parameters
    import capo_pipes.types.pipe_target_sqs_queue_parameters
    import capo_pipes.types.pipe_target_state_machine_parameters
    import capo_pipes.types.pipe_target_timestream_parameters


class PipeTargetParameters(TypedDict, closed=True):
    input_template: NotRequired["capo_pipes.types.input_template.InputTemplate"]
    """<p>Valid JSON text passed to the target. In this case, nothing from the event itself is passed to the target. For more information, see <a href="http://www.rfc-editor.org/rfc/rfc7159.txt">The JavaScript Object Notation (JSON) Data Interchange Format</a>.</p> <p>To remove an input template, specify an empty string.</p>"""
    lambda_function_parameters: NotRequired[
        "capo_pipes.types.pipe_target_lambda_function_parameters.PipeTargetLambdaFunctionParameters"
    ]
    """<p>The parameters for using a Lambda function as a target.</p>"""
    step_function_state_machine_parameters: NotRequired[
        "capo_pipes.types.pipe_target_state_machine_parameters.PipeTargetStateMachineParameters"
    ]
    """<p>The parameters for using a Step Functions state machine as a target.</p>"""
    kinesis_stream_parameters: NotRequired[
        "capo_pipes.types.pipe_target_kinesis_stream_parameters.PipeTargetKinesisStreamParameters"
    ]
    """<p>The parameters for using a Kinesis stream as a target.</p>"""
    ecs_task_parameters: NotRequired[
        "capo_pipes.types.pipe_target_ecs_task_parameters.PipeTargetEcsTaskParameters"
    ]
    """<p>The parameters for using an Amazon ECS task as a target.</p>"""
    batch_job_parameters: NotRequired[
        "capo_pipes.types.pipe_target_batch_job_parameters.PipeTargetBatchJobParameters"
    ]
    """<p>The parameters for using an Batch job as a target.</p>"""
    sqs_queue_parameters: NotRequired[
        "capo_pipes.types.pipe_target_sqs_queue_parameters.PipeTargetSqsQueueParameters"
    ]
    """<p>The parameters for using a Amazon SQS stream as a target.</p>"""
    http_parameters: NotRequired[
        "capo_pipes.types.pipe_target_http_parameters.PipeTargetHttpParameters"
    ]
    """<p>These are custom parameter to be used when the target is an API Gateway REST APIs or EventBridge ApiDestinations.</p>"""
    redshift_data_parameters: NotRequired[
        "capo_pipes.types.pipe_target_redshift_data_parameters.PipeTargetRedshiftDataParameters"
    ]
    """<p>These are custom parameters to be used when the target is a Amazon Redshift cluster to invoke the Amazon Redshift Data API BatchExecuteStatement.</p>"""
    sage_maker_pipeline_parameters: NotRequired[
        "capo_pipes.types.pipe_target_sage_maker_pipeline_parameters.PipeTargetSageMakerPipelineParameters"
    ]
    """<p>The parameters for using a SageMaker pipeline as a target.</p>"""
    event_bridge_event_bus_parameters: NotRequired[
        "capo_pipes.types.pipe_target_event_bridge_event_bus_parameters.PipeTargetEventBridgeEventBusParameters"
    ]
    """<p>The parameters for using an EventBridge event bus as a target.</p>"""
    cloud_watch_logs_parameters: NotRequired[
        "capo_pipes.types.pipe_target_cloud_watch_logs_parameters.PipeTargetCloudWatchLogsParameters"
    ]
    """<p>The parameters for using an CloudWatch Logs log stream as a target.</p>"""
    timestream_parameters: NotRequired[
        "capo_pipes.types.pipe_target_timestream_parameters.PipeTargetTimestreamParameters"
    ]
    """<p>The parameters for using a Timestream for LiveAnalytics table as a target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeTargetParameters) -> dict:
    out: dict = {}
    if "input_template" in value:
        out["InputTemplate"] = value["input_template"]
    if "lambda_function_parameters" in value:
        import capo_pipes.types.pipe_target_lambda_function_parameters

        out["LambdaFunctionParameters"] = (
            capo_pipes.types.pipe_target_lambda_function_parameters.serialize_json(
                value["lambda_function_parameters"]
            )
        )
    if "step_function_state_machine_parameters" in value:
        import capo_pipes.types.pipe_target_state_machine_parameters

        out["StepFunctionStateMachineParameters"] = (
            capo_pipes.types.pipe_target_state_machine_parameters.serialize_json(
                value["step_function_state_machine_parameters"]
            )
        )
    if "kinesis_stream_parameters" in value:
        import capo_pipes.types.pipe_target_kinesis_stream_parameters

        out["KinesisStreamParameters"] = (
            capo_pipes.types.pipe_target_kinesis_stream_parameters.serialize_json(
                value["kinesis_stream_parameters"]
            )
        )
    if "ecs_task_parameters" in value:
        import capo_pipes.types.pipe_target_ecs_task_parameters

        out["EcsTaskParameters"] = (
            capo_pipes.types.pipe_target_ecs_task_parameters.serialize_json(
                value["ecs_task_parameters"]
            )
        )
    if "batch_job_parameters" in value:
        import capo_pipes.types.pipe_target_batch_job_parameters

        out["BatchJobParameters"] = (
            capo_pipes.types.pipe_target_batch_job_parameters.serialize_json(
                value["batch_job_parameters"]
            )
        )
    if "sqs_queue_parameters" in value:
        import capo_pipes.types.pipe_target_sqs_queue_parameters

        out["SqsQueueParameters"] = (
            capo_pipes.types.pipe_target_sqs_queue_parameters.serialize_json(
                value["sqs_queue_parameters"]
            )
        )
    if "http_parameters" in value:
        import capo_pipes.types.pipe_target_http_parameters

        out["HttpParameters"] = (
            capo_pipes.types.pipe_target_http_parameters.serialize_json(
                value["http_parameters"]
            )
        )
    if "redshift_data_parameters" in value:
        import capo_pipes.types.pipe_target_redshift_data_parameters

        out["RedshiftDataParameters"] = (
            capo_pipes.types.pipe_target_redshift_data_parameters.serialize_json(
                value["redshift_data_parameters"]
            )
        )
    if "sage_maker_pipeline_parameters" in value:
        import capo_pipes.types.pipe_target_sage_maker_pipeline_parameters

        out["SageMakerPipelineParameters"] = (
            capo_pipes.types.pipe_target_sage_maker_pipeline_parameters.serialize_json(
                value["sage_maker_pipeline_parameters"]
            )
        )
    if "event_bridge_event_bus_parameters" in value:
        import capo_pipes.types.pipe_target_event_bridge_event_bus_parameters

        out["EventBridgeEventBusParameters"] = (
            capo_pipes.types.pipe_target_event_bridge_event_bus_parameters.serialize_json(
                value["event_bridge_event_bus_parameters"]
            )
        )
    if "cloud_watch_logs_parameters" in value:
        import capo_pipes.types.pipe_target_cloud_watch_logs_parameters

        out["CloudWatchLogsParameters"] = (
            capo_pipes.types.pipe_target_cloud_watch_logs_parameters.serialize_json(
                value["cloud_watch_logs_parameters"]
            )
        )
    if "timestream_parameters" in value:
        import capo_pipes.types.pipe_target_timestream_parameters

        out["TimestreamParameters"] = (
            capo_pipes.types.pipe_target_timestream_parameters.serialize_json(
                value["timestream_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> PipeTargetParameters:
    out: PipeTargetParameters = {}  # type: ignore[typeddict-item]
    if data.get("InputTemplate") is not None:
        out["input_template"] = data["InputTemplate"]
    if data.get("LambdaFunctionParameters") is not None:
        import capo_pipes.types.pipe_target_lambda_function_parameters

        out["lambda_function_parameters"] = (
            capo_pipes.types.pipe_target_lambda_function_parameters.deserialize_json(
                data["LambdaFunctionParameters"]
            )
        )
    if data.get("StepFunctionStateMachineParameters") is not None:
        import capo_pipes.types.pipe_target_state_machine_parameters

        out["step_function_state_machine_parameters"] = (
            capo_pipes.types.pipe_target_state_machine_parameters.deserialize_json(
                data["StepFunctionStateMachineParameters"]
            )
        )
    if data.get("KinesisStreamParameters") is not None:
        import capo_pipes.types.pipe_target_kinesis_stream_parameters

        out["kinesis_stream_parameters"] = (
            capo_pipes.types.pipe_target_kinesis_stream_parameters.deserialize_json(
                data["KinesisStreamParameters"]
            )
        )
    if data.get("EcsTaskParameters") is not None:
        import capo_pipes.types.pipe_target_ecs_task_parameters

        out["ecs_task_parameters"] = (
            capo_pipes.types.pipe_target_ecs_task_parameters.deserialize_json(
                data["EcsTaskParameters"]
            )
        )
    if data.get("BatchJobParameters") is not None:
        import capo_pipes.types.pipe_target_batch_job_parameters

        out["batch_job_parameters"] = (
            capo_pipes.types.pipe_target_batch_job_parameters.deserialize_json(
                data["BatchJobParameters"]
            )
        )
    if data.get("SqsQueueParameters") is not None:
        import capo_pipes.types.pipe_target_sqs_queue_parameters

        out["sqs_queue_parameters"] = (
            capo_pipes.types.pipe_target_sqs_queue_parameters.deserialize_json(
                data["SqsQueueParameters"]
            )
        )
    if data.get("HttpParameters") is not None:
        import capo_pipes.types.pipe_target_http_parameters

        out["http_parameters"] = (
            capo_pipes.types.pipe_target_http_parameters.deserialize_json(
                data["HttpParameters"]
            )
        )
    if data.get("RedshiftDataParameters") is not None:
        import capo_pipes.types.pipe_target_redshift_data_parameters

        out["redshift_data_parameters"] = (
            capo_pipes.types.pipe_target_redshift_data_parameters.deserialize_json(
                data["RedshiftDataParameters"]
            )
        )
    if data.get("SageMakerPipelineParameters") is not None:
        import capo_pipes.types.pipe_target_sage_maker_pipeline_parameters

        out["sage_maker_pipeline_parameters"] = (
            capo_pipes.types.pipe_target_sage_maker_pipeline_parameters.deserialize_json(
                data["SageMakerPipelineParameters"]
            )
        )
    if data.get("EventBridgeEventBusParameters") is not None:
        import capo_pipes.types.pipe_target_event_bridge_event_bus_parameters

        out["event_bridge_event_bus_parameters"] = (
            capo_pipes.types.pipe_target_event_bridge_event_bus_parameters.deserialize_json(
                data["EventBridgeEventBusParameters"]
            )
        )
    if data.get("CloudWatchLogsParameters") is not None:
        import capo_pipes.types.pipe_target_cloud_watch_logs_parameters

        out["cloud_watch_logs_parameters"] = (
            capo_pipes.types.pipe_target_cloud_watch_logs_parameters.deserialize_json(
                data["CloudWatchLogsParameters"]
            )
        )
    if data.get("TimestreamParameters") is not None:
        import capo_pipes.types.pipe_target_timestream_parameters

        out["timestream_parameters"] = (
            capo_pipes.types.pipe_target_timestream_parameters.deserialize_json(
                data["TimestreamParameters"]
            )
        )
    return out
