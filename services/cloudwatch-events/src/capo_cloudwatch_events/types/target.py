"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#Target``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_events.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.batch_parameters
    import capo_cloudwatch_events.types.dead_letter_config
    import capo_cloudwatch_events.types.ecs_parameters
    import capo_cloudwatch_events.types.http_parameters
    import capo_cloudwatch_events.types.input_transformer
    import capo_cloudwatch_events.types.kinesis_parameters
    import capo_cloudwatch_events.types.redshift_data_parameters
    import capo_cloudwatch_events.types.retry_policy
    import capo_cloudwatch_events.types.role_arn
    import capo_cloudwatch_events.types.run_command_parameters
    import capo_cloudwatch_events.types.sage_maker_pipeline_parameters
    import capo_cloudwatch_events.types.sqs_parameters
    import capo_cloudwatch_events.types.target_arn
    import capo_cloudwatch_events.types.target_id
    import capo_cloudwatch_events.types.target_input
    import capo_cloudwatch_events.types.target_input_path


class Target(TypedDict, closed=True):
    id: "capo_cloudwatch_events.types.target_id.TargetId"
    """<p>The ID of the target. We recommend using a memorable and unique string.</p>"""
    arn: "capo_cloudwatch_events.types.target_arn.TargetArn"
    """<p>The Amazon Resource Name (ARN) of the target.</p>"""
    role_arn: NotRequired["capo_cloudwatch_events.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. If one rule triggers multiple targets, you can use a different IAM role for each target.</p>"""
    input: NotRequired["capo_cloudwatch_events.types.target_input.TargetInput"]
    """<p>Valid JSON text passed to the target. In this case, nothing from the event itself is passed to the target. For more information, see <a href="http://www.rfc-editor.org/rfc/rfc7159.txt">The JavaScript Object Notation (JSON) Data Interchange Format</a>.</p>"""
    input_path: NotRequired[
        "capo_cloudwatch_events.types.target_input_path.TargetInputPath"
    ]
    """<p>The value of the JSONPath that is used for extracting part of the matched event when passing it to the target. You must use JSON dot notation, not bracket notation. For more information about JSON paths, see <a href="http://goessner.net/articles/JsonPath/">JSONPath</a>.</p>"""
    input_transformer: NotRequired[
        "capo_cloudwatch_events.types.input_transformer.InputTransformer"
    ]
    """<p>Settings to enable you to provide custom input to a target based on certain event data. You can extract one or more key-value pairs from the event and then use that data to send customized input to the target.</p>"""
    kinesis_parameters: NotRequired[
        "capo_cloudwatch_events.types.kinesis_parameters.KinesisParameters"
    ]
    """<p>The custom parameter you can use to control the shard assignment, when the target is a Kinesis data stream. If you do not include this parameter, the default is to use the <code>eventId</code> as the partition key.</p>"""
    run_command_parameters: NotRequired[
        "capo_cloudwatch_events.types.run_command_parameters.RunCommandParameters"
    ]
    """<p>Parameters used when you are using the rule to invoke Amazon EC2 Run Command.</p>"""
    ecs_parameters: NotRequired[
        "capo_cloudwatch_events.types.ecs_parameters.EcsParameters"
    ]
    """<p>Contains the Amazon ECS task definition and task count to be used, if the event target is an Amazon ECS task. For more information about Amazon ECS tasks, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html">Task Definitions </a> in the <i>Amazon EC2 Container Service Developer Guide</i>.</p>"""
    batch_parameters: NotRequired[
        "capo_cloudwatch_events.types.batch_parameters.BatchParameters"
    ]
    """<p>If the event target is an Batch job, this contains the job definition, job name, and other parameters. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/jobs.html">Jobs</a> in the <i>Batch User Guide</i>.</p>"""
    sqs_parameters: NotRequired[
        "capo_cloudwatch_events.types.sqs_parameters.SqsParameters"
    ]
    """<p>Contains the message group ID to use when the target is a FIFO queue.</p> <p>If you specify an SQS FIFO queue as a target, the queue must have content-based deduplication enabled.</p>"""
    http_parameters: NotRequired[
        "capo_cloudwatch_events.types.http_parameters.HttpParameters"
    ]
    """<p>Contains the HTTP parameters to use when the target is a API Gateway REST endpoint or EventBridge ApiDestination.</p> <p>If you specify an API Gateway REST API or EventBridge ApiDestination as a target, you can use this parameter to specify headers, path parameters, and query string keys/values as part of your target invoking request. If you're using ApiDestinations, the corresponding Connection can also have these values configured. In case of any conflicting keys, values from the Connection take precedence.</p>"""
    redshift_data_parameters: NotRequired[
        "capo_cloudwatch_events.types.redshift_data_parameters.RedshiftDataParameters"
    ]
    """<p>Contains the Amazon Redshift Data API parameters to use when the target is a Amazon Redshift cluster.</p> <p>If you specify a Amazon Redshift Cluster as a Target, you can use this to specify parameters to invoke the Amazon Redshift Data API ExecuteStatement based on EventBridge events.</p>"""
    sage_maker_pipeline_parameters: NotRequired[
        "capo_cloudwatch_events.types.sage_maker_pipeline_parameters.SageMakerPipelineParameters"
    ]
    """<p>Contains the SageMaker AI Model Building Pipeline parameters to start execution of a SageMaker AI Model Building Pipeline.</p> <p>If you specify a SageMaker AI Model Building Pipeline as a target, you can use this to specify parameters to start a pipeline execution based on EventBridge events.</p>"""
    dead_letter_config: NotRequired[
        "capo_cloudwatch_events.types.dead_letter_config.DeadLetterConfig"
    ]
    """<p>The <code>DeadLetterConfig</code> that defines the target queue to send dead-letter queue events to.</p>"""
    retry_policy: NotRequired["capo_cloudwatch_events.types.retry_policy.RetryPolicy"]
    """<p>The <code>RetryPolicy</code> object that contains the retry policy configuration to use for the dead-letter queue.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Target) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "input" in value:
        out["Input"] = value["input"]
    if "input_path" in value:
        out["InputPath"] = value["input_path"]
    if "input_transformer" in value:
        import capo_cloudwatch_events.types.input_transformer

        out["InputTransformer"] = (
            capo_cloudwatch_events.types.input_transformer.serialize_aws_json_1_1(
                value["input_transformer"]
            )
        )
    if "kinesis_parameters" in value:
        import capo_cloudwatch_events.types.kinesis_parameters

        out["KinesisParameters"] = (
            capo_cloudwatch_events.types.kinesis_parameters.serialize_aws_json_1_1(
                value["kinesis_parameters"]
            )
        )
    if "run_command_parameters" in value:
        import capo_cloudwatch_events.types.run_command_parameters

        out["RunCommandParameters"] = (
            capo_cloudwatch_events.types.run_command_parameters.serialize_aws_json_1_1(
                value["run_command_parameters"]
            )
        )
    if "ecs_parameters" in value:
        import capo_cloudwatch_events.types.ecs_parameters

        out["EcsParameters"] = (
            capo_cloudwatch_events.types.ecs_parameters.serialize_aws_json_1_1(
                value["ecs_parameters"]
            )
        )
    if "batch_parameters" in value:
        import capo_cloudwatch_events.types.batch_parameters

        out["BatchParameters"] = (
            capo_cloudwatch_events.types.batch_parameters.serialize_aws_json_1_1(
                value["batch_parameters"]
            )
        )
    if "sqs_parameters" in value:
        import capo_cloudwatch_events.types.sqs_parameters

        out["SqsParameters"] = (
            capo_cloudwatch_events.types.sqs_parameters.serialize_aws_json_1_1(
                value["sqs_parameters"]
            )
        )
    if "http_parameters" in value:
        import capo_cloudwatch_events.types.http_parameters

        out["HttpParameters"] = (
            capo_cloudwatch_events.types.http_parameters.serialize_aws_json_1_1(
                value["http_parameters"]
            )
        )
    if "redshift_data_parameters" in value:
        import capo_cloudwatch_events.types.redshift_data_parameters

        out["RedshiftDataParameters"] = (
            capo_cloudwatch_events.types.redshift_data_parameters.serialize_aws_json_1_1(
                value["redshift_data_parameters"]
            )
        )
    if "sage_maker_pipeline_parameters" in value:
        import capo_cloudwatch_events.types.sage_maker_pipeline_parameters

        out["SageMakerPipelineParameters"] = (
            capo_cloudwatch_events.types.sage_maker_pipeline_parameters.serialize_aws_json_1_1(
                value["sage_maker_pipeline_parameters"]
            )
        )
    if "dead_letter_config" in value:
        import capo_cloudwatch_events.types.dead_letter_config

        out["DeadLetterConfig"] = (
            capo_cloudwatch_events.types.dead_letter_config.serialize_aws_json_1_1(
                value["dead_letter_config"]
            )
        )
    if "retry_policy" in value:
        import capo_cloudwatch_events.types.retry_policy

        out["RetryPolicy"] = (
            capo_cloudwatch_events.types.retry_policy.serialize_aws_json_1_1(
                value["retry_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Target:
    out: Target = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("Target.id required")
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("Target.arn required")
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("Input") is not None:
        out["input"] = data["Input"]
    if data.get("InputPath") is not None:
        out["input_path"] = data["InputPath"]
    if data.get("InputTransformer") is not None:
        import capo_cloudwatch_events.types.input_transformer

        out["input_transformer"] = (
            capo_cloudwatch_events.types.input_transformer.deserialize_aws_json_1_1(
                data["InputTransformer"]
            )
        )
    if data.get("KinesisParameters") is not None:
        import capo_cloudwatch_events.types.kinesis_parameters

        out["kinesis_parameters"] = (
            capo_cloudwatch_events.types.kinesis_parameters.deserialize_aws_json_1_1(
                data["KinesisParameters"]
            )
        )
    if data.get("RunCommandParameters") is not None:
        import capo_cloudwatch_events.types.run_command_parameters

        out["run_command_parameters"] = (
            capo_cloudwatch_events.types.run_command_parameters.deserialize_aws_json_1_1(
                data["RunCommandParameters"]
            )
        )
    if data.get("EcsParameters") is not None:
        import capo_cloudwatch_events.types.ecs_parameters

        out["ecs_parameters"] = (
            capo_cloudwatch_events.types.ecs_parameters.deserialize_aws_json_1_1(
                data["EcsParameters"]
            )
        )
    if data.get("BatchParameters") is not None:
        import capo_cloudwatch_events.types.batch_parameters

        out["batch_parameters"] = (
            capo_cloudwatch_events.types.batch_parameters.deserialize_aws_json_1_1(
                data["BatchParameters"]
            )
        )
    if data.get("SqsParameters") is not None:
        import capo_cloudwatch_events.types.sqs_parameters

        out["sqs_parameters"] = (
            capo_cloudwatch_events.types.sqs_parameters.deserialize_aws_json_1_1(
                data["SqsParameters"]
            )
        )
    if data.get("HttpParameters") is not None:
        import capo_cloudwatch_events.types.http_parameters

        out["http_parameters"] = (
            capo_cloudwatch_events.types.http_parameters.deserialize_aws_json_1_1(
                data["HttpParameters"]
            )
        )
    if data.get("RedshiftDataParameters") is not None:
        import capo_cloudwatch_events.types.redshift_data_parameters

        out["redshift_data_parameters"] = (
            capo_cloudwatch_events.types.redshift_data_parameters.deserialize_aws_json_1_1(
                data["RedshiftDataParameters"]
            )
        )
    if data.get("SageMakerPipelineParameters") is not None:
        import capo_cloudwatch_events.types.sage_maker_pipeline_parameters

        out["sage_maker_pipeline_parameters"] = (
            capo_cloudwatch_events.types.sage_maker_pipeline_parameters.deserialize_aws_json_1_1(
                data["SageMakerPipelineParameters"]
            )
        )
    if data.get("DeadLetterConfig") is not None:
        import capo_cloudwatch_events.types.dead_letter_config

        out["dead_letter_config"] = (
            capo_cloudwatch_events.types.dead_letter_config.deserialize_aws_json_1_1(
                data["DeadLetterConfig"]
            )
        )
    if data.get("RetryPolicy") is not None:
        import capo_cloudwatch_events.types.retry_policy

        out["retry_policy"] = (
            capo_cloudwatch_events.types.retry_policy.deserialize_aws_json_1_1(
                data["RetryPolicy"]
            )
        )
    return out
