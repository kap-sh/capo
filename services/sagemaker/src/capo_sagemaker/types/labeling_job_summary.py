"""Generated from Smithy shape ``com.amazonaws.sagemaker#LabelingJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.label_counters
    import capo_sagemaker.types.labeling_job_arn
    import capo_sagemaker.types.labeling_job_input_config
    import capo_sagemaker.types.labeling_job_name
    import capo_sagemaker.types.labeling_job_output
    import capo_sagemaker.types.labeling_job_status
    import capo_sagemaker.types.lambda_function_arn
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.workteam_arn


class LabelingJobSummary(TypedDict, closed=True):
    labeling_job_name: NotRequired[
        "capo_sagemaker.types.labeling_job_name.LabelingJobName"
    ]
    """<p>The name of the labeling job.</p>"""
    labeling_job_arn: NotRequired[
        "capo_sagemaker.types.labeling_job_arn.LabelingJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) assigned to the labeling job when it was created.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the job was created (timestamp).</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the job was last modified (timestamp).</p>"""
    labeling_job_status: NotRequired[
        "capo_sagemaker.types.labeling_job_status.LabelingJobStatus"
    ]
    """<p>The current status of the labeling job. </p>"""
    label_counters: NotRequired["capo_sagemaker.types.label_counters.LabelCounters"]
    """<p>Counts showing the progress of the labeling job.</p>"""
    workteam_arn: NotRequired["capo_sagemaker.types.workteam_arn.WorkteamArn"]
    """<p>The Amazon Resource Name (ARN) of the work team assigned to the job.</p>"""
    pre_human_task_lambda_arn: NotRequired[
        "capo_sagemaker.types.lambda_function_arn.LambdaFunctionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a Lambda function. The function is run before each data object is sent to a worker.</p>"""
    annotation_consolidation_lambda_arn: NotRequired[
        "capo_sagemaker.types.lambda_function_arn.LambdaFunctionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Lambda function used to consolidate the annotations from individual workers into a label for a data object. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sms-annotation-consolidation.html">Annotation Consolidation</a>.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>If the <code>LabelingJobStatus</code> field is <code>Failed</code>, this field contains a description of the error.</p>"""
    labeling_job_output: NotRequired[
        "capo_sagemaker.types.labeling_job_output.LabelingJobOutput"
    ]
    """<p>The location of the output produced by the labeling job.</p>"""
    input_config: NotRequired[
        "capo_sagemaker.types.labeling_job_input_config.LabelingJobInputConfig"
    ]
    """<p>Input configuration for the labeling job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelingJobSummary) -> dict:
    out: dict = {}
    if "labeling_job_name" in value:
        out["LabelingJobName"] = value["labeling_job_name"]
    if "labeling_job_arn" in value:
        out["LabelingJobArn"] = value["labeling_job_arn"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "labeling_job_status" in value:
        import capo_sagemaker.types.labeling_job_status

        out["LabelingJobStatus"] = (
            capo_sagemaker.types.labeling_job_status.serialize_aws_json_1_1(
                value["labeling_job_status"]
            )
        )
    if "label_counters" in value:
        import capo_sagemaker.types.label_counters

        out["LabelCounters"] = (
            capo_sagemaker.types.label_counters.serialize_aws_json_1_1(
                value["label_counters"]
            )
        )
    if "workteam_arn" in value:
        out["WorkteamArn"] = value["workteam_arn"]
    if "pre_human_task_lambda_arn" in value:
        out["PreHumanTaskLambdaArn"] = value["pre_human_task_lambda_arn"]
    if "annotation_consolidation_lambda_arn" in value:
        out["AnnotationConsolidationLambdaArn"] = value[
            "annotation_consolidation_lambda_arn"
        ]
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "labeling_job_output" in value:
        import capo_sagemaker.types.labeling_job_output

        out["LabelingJobOutput"] = (
            capo_sagemaker.types.labeling_job_output.serialize_aws_json_1_1(
                value["labeling_job_output"]
            )
        )
    if "input_config" in value:
        import capo_sagemaker.types.labeling_job_input_config

        out["InputConfig"] = (
            capo_sagemaker.types.labeling_job_input_config.serialize_aws_json_1_1(
                value["input_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelingJobSummary:
    out: LabelingJobSummary = {}  # type: ignore[typeddict-item]
    if data.get("LabelingJobName") is not None:
        out["labeling_job_name"] = data["LabelingJobName"]
    if data.get("LabelingJobArn") is not None:
        out["labeling_job_arn"] = data["LabelingJobArn"]
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("LabelingJobStatus") is not None:
        import capo_sagemaker.types.labeling_job_status

        out["labeling_job_status"] = (
            capo_sagemaker.types.labeling_job_status.deserialize_aws_json_1_1(
                data["LabelingJobStatus"]
            )
        )
    if data.get("LabelCounters") is not None:
        import capo_sagemaker.types.label_counters

        out["label_counters"] = (
            capo_sagemaker.types.label_counters.deserialize_aws_json_1_1(
                data["LabelCounters"]
            )
        )
    if data.get("WorkteamArn") is not None:
        out["workteam_arn"] = data["WorkteamArn"]
    if data.get("PreHumanTaskLambdaArn") is not None:
        out["pre_human_task_lambda_arn"] = data["PreHumanTaskLambdaArn"]
    if data.get("AnnotationConsolidationLambdaArn") is not None:
        out["annotation_consolidation_lambda_arn"] = data[
            "AnnotationConsolidationLambdaArn"
        ]
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("LabelingJobOutput") is not None:
        import capo_sagemaker.types.labeling_job_output

        out["labeling_job_output"] = (
            capo_sagemaker.types.labeling_job_output.deserialize_aws_json_1_1(
                data["LabelingJobOutput"]
            )
        )
    if data.get("InputConfig") is not None:
        import capo_sagemaker.types.labeling_job_input_config

        out["input_config"] = (
            capo_sagemaker.types.labeling_job_input_config.deserialize_aws_json_1_1(
                data["InputConfig"]
            )
        )
    return out
