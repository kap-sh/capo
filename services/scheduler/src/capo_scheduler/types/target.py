"""Generated from Smithy shape ``com.amazonaws.scheduler#Target``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_scheduler.errors import DeserializationError

if TYPE_CHECKING:
    import capo_scheduler.types.dead_letter_config
    import capo_scheduler.types.ecs_parameters
    import capo_scheduler.types.event_bridge_parameters
    import capo_scheduler.types.kinesis_parameters
    import capo_scheduler.types.retry_policy
    import capo_scheduler.types.role_arn
    import capo_scheduler.types.sage_maker_pipeline_parameters
    import capo_scheduler.types.sqs_parameters
    import capo_scheduler.types.target_arn
    import capo_scheduler.types.target_input


class Target(TypedDict, closed=True):
    arn: "capo_scheduler.types.target_arn.TargetArn"
    """<p>The Amazon Resource Name (ARN) of the target.</p>"""
    role_arn: "capo_scheduler.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that EventBridge Scheduler will use for this target when the schedule is invoked.</p>"""
    dead_letter_config: NotRequired[
        "capo_scheduler.types.dead_letter_config.DeadLetterConfig"
    ]
    """<p>An object that contains information about an Amazon SQS queue that EventBridge Scheduler uses as a dead-letter queue for your schedule. If specified, EventBridge Scheduler delivers failed events that could not be successfully delivered to a target to the queue.</p>"""
    retry_policy: NotRequired["capo_scheduler.types.retry_policy.RetryPolicy"]
    """<p>A <code>RetryPolicy</code> object that includes information about the retry policy settings, including the maximum age of an event, and the maximum number of times EventBridge Scheduler will try to deliver the event to a target.</p>"""
    input: NotRequired["capo_scheduler.types.target_input.TargetInput"]
    """<p>The text, or well-formed JSON, passed to the target. If you are configuring a templated Lambda, AWS Step Functions, or Amazon EventBridge target, the input must be a well-formed JSON. For all other target types, a JSON is not required. If you do not specify anything for this field, EventBridge Scheduler delivers a default notification to the target.</p>"""
    ecs_parameters: NotRequired["capo_scheduler.types.ecs_parameters.EcsParameters"]
    """<p>The templated target type for the Amazon ECS <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html"> <code>RunTask</code> </a> API operation.</p>"""
    event_bridge_parameters: NotRequired[
        "capo_scheduler.types.event_bridge_parameters.EventBridgeParameters"
    ]
    """<p>The templated target type for the EventBridge <a href="https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html"> <code>PutEvents</code> </a> API operation.</p>"""
    kinesis_parameters: NotRequired[
        "capo_scheduler.types.kinesis_parameters.KinesisParameters"
    ]
    """<p>The templated target type for the Amazon Kinesis <a href="kinesis/latest/APIReference/API_PutRecord.html"> <code>PutRecord</code> </a> API operation.</p>"""
    sage_maker_pipeline_parameters: NotRequired[
        "capo_scheduler.types.sage_maker_pipeline_parameters.SageMakerPipelineParameters"
    ]
    """<p>The templated target type for the Amazon SageMaker <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartPipelineExecution.html"> <code>StartPipelineExecution</code> </a> API operation.</p>"""
    sqs_parameters: NotRequired["capo_scheduler.types.sqs_parameters.SqsParameters"]
    """<p>The templated target type for the Amazon SQS <a href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html"> <code>SendMessage</code> </a> API operation. Contains the message group ID to use when the target is a FIFO queue. If you specify an Amazon SQS FIFO queue as a target, the queue must have content-based deduplication enabled. For more information, see <a href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagededuplicationid-property.html">Using the Amazon SQS message deduplication ID</a> in the <i>Amazon SQS Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Target) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["RoleArn"] = value["role_arn"]
    if "dead_letter_config" in value:
        import capo_scheduler.types.dead_letter_config

        out["DeadLetterConfig"] = (
            capo_scheduler.types.dead_letter_config.serialize_json(
                value["dead_letter_config"]
            )
        )
    if "retry_policy" in value:
        import capo_scheduler.types.retry_policy

        out["RetryPolicy"] = capo_scheduler.types.retry_policy.serialize_json(
            value["retry_policy"]
        )
    if "input" in value:
        out["Input"] = value["input"]
    if "ecs_parameters" in value:
        import capo_scheduler.types.ecs_parameters

        out["EcsParameters"] = capo_scheduler.types.ecs_parameters.serialize_json(
            value["ecs_parameters"]
        )
    if "event_bridge_parameters" in value:
        import capo_scheduler.types.event_bridge_parameters

        out["EventBridgeParameters"] = (
            capo_scheduler.types.event_bridge_parameters.serialize_json(
                value["event_bridge_parameters"]
            )
        )
    if "kinesis_parameters" in value:
        import capo_scheduler.types.kinesis_parameters

        out["KinesisParameters"] = (
            capo_scheduler.types.kinesis_parameters.serialize_json(
                value["kinesis_parameters"]
            )
        )
    if "sage_maker_pipeline_parameters" in value:
        import capo_scheduler.types.sage_maker_pipeline_parameters

        out["SageMakerPipelineParameters"] = (
            capo_scheduler.types.sage_maker_pipeline_parameters.serialize_json(
                value["sage_maker_pipeline_parameters"]
            )
        )
    if "sqs_parameters" in value:
        import capo_scheduler.types.sqs_parameters

        out["SqsParameters"] = capo_scheduler.types.sqs_parameters.serialize_json(
            value["sqs_parameters"]
        )
    return out


def deserialize_json(data: dict) -> Target:
    out: Target = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("Target.arn required")
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("Target.role_arn required")
    if data.get("DeadLetterConfig") is not None:
        import capo_scheduler.types.dead_letter_config

        out["dead_letter_config"] = (
            capo_scheduler.types.dead_letter_config.deserialize_json(
                data["DeadLetterConfig"]
            )
        )
    if data.get("RetryPolicy") is not None:
        import capo_scheduler.types.retry_policy

        out["retry_policy"] = capo_scheduler.types.retry_policy.deserialize_json(
            data["RetryPolicy"]
        )
    if data.get("Input") is not None:
        out["input"] = data["Input"]
    if data.get("EcsParameters") is not None:
        import capo_scheduler.types.ecs_parameters

        out["ecs_parameters"] = capo_scheduler.types.ecs_parameters.deserialize_json(
            data["EcsParameters"]
        )
    if data.get("EventBridgeParameters") is not None:
        import capo_scheduler.types.event_bridge_parameters

        out["event_bridge_parameters"] = (
            capo_scheduler.types.event_bridge_parameters.deserialize_json(
                data["EventBridgeParameters"]
            )
        )
    if data.get("KinesisParameters") is not None:
        import capo_scheduler.types.kinesis_parameters

        out["kinesis_parameters"] = (
            capo_scheduler.types.kinesis_parameters.deserialize_json(
                data["KinesisParameters"]
            )
        )
    if data.get("SageMakerPipelineParameters") is not None:
        import capo_scheduler.types.sage_maker_pipeline_parameters

        out["sage_maker_pipeline_parameters"] = (
            capo_scheduler.types.sage_maker_pipeline_parameters.deserialize_json(
                data["SageMakerPipelineParameters"]
            )
        )
    if data.get("SqsParameters") is not None:
        import capo_scheduler.types.sqs_parameters

        out["sqs_parameters"] = capo_scheduler.types.sqs_parameters.deserialize_json(
            data["SqsParameters"]
        )
    return out
