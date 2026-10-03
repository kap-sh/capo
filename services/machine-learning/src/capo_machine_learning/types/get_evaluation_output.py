"""Generated from Smithy shape ``com.amazonaws.machinelearning#GetEvaluationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.aws_user_arn
    import capo_machine_learning.types.entity_id
    import capo_machine_learning.types.entity_name
    import capo_machine_learning.types.entity_status
    import capo_machine_learning.types.epoch_time
    import capo_machine_learning.types.long_type
    import capo_machine_learning.types.message
    import capo_machine_learning.types.performance_metrics
    import capo_machine_learning.types.presigned_s3_url
    import capo_machine_learning.types.s3_url


class GetEvaluationOutput(TypedDict, closed=True):
    evaluation_id: NotRequired["capo_machine_learning.types.entity_id.EntityId"]
    """<p>The evaluation ID which is same as the <code>EvaluationId</code> in the request.</p>"""
    ml_model_id: NotRequired["capo_machine_learning.types.entity_id.EntityId"]
    """<p>The ID of the <code>MLModel</code> that was the focus of the evaluation.</p>"""
    evaluation_data_source_id: NotRequired[
        "capo_machine_learning.types.entity_id.EntityId"
    ]
    """<p>The <code>DataSource</code> used for this evaluation.</p>"""
    input_data_location_s3: NotRequired["capo_machine_learning.types.s3_url.S3Url"]
    """<p>The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).</p>"""
    created_by_iam_user: NotRequired[
        "capo_machine_learning.types.aws_user_arn.AwsUserArn"
    ]
    """<p>The AWS user account that invoked the evaluation. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.</p>"""
    created_at: NotRequired["capo_machine_learning.types.epoch_time.EpochTime"]
    """<p>The time that the <code>Evaluation</code> was created. The time is expressed in epoch time.</p>"""
    last_updated_at: NotRequired["capo_machine_learning.types.epoch_time.EpochTime"]
    """<p>The time of the most recent edit to the <code>Evaluation</code>. The time is expressed in epoch time.</p>"""
    name: NotRequired["capo_machine_learning.types.entity_name.EntityName"]
    """<p>A user-supplied name or description of the <code>Evaluation</code>. </p>"""
    status: NotRequired["capo_machine_learning.types.entity_status.EntityStatus"]
    """<p>The status of the evaluation. This element can have one of the following values:</p> <ul> <li> <p> <code>PENDING</code> - Amazon Machine Language (Amazon ML) submitted a request to evaluate an <code>MLModel</code>.</p> </li> <li> <p> <code>INPROGRESS</code> - The evaluation is underway.</p> </li> <li> <p> <code>FAILED</code> - The request to evaluate an <code>MLModel</code> did not run to completion. It is not usable.</p> </li> <li> <p> <code>COMPLETED</code> - The evaluation process completed successfully.</p> </li> <li> <p> <code>DELETED</code> - The <code>Evaluation</code> is marked as deleted. It is not usable.</p> </li> </ul>"""
    performance_metrics: NotRequired[
        "capo_machine_learning.types.performance_metrics.PerformanceMetrics"
    ]
    """<p>Measurements of how well the <code>MLModel</code> performed using observations referenced by the <code>DataSource</code>. One of the following metric is returned based on the type of the <code>MLModel</code>: </p> <ul> <li> <p>BinaryAUC: A binary <code>MLModel</code> uses the Area Under the Curve (AUC) technique to measure performance. </p> </li> <li> <p>RegressionRMSE: A regression <code>MLModel</code> uses the Root Mean Square Error (RMSE) technique to measure performance. RMSE measures the difference between predicted and actual values for a single variable.</p> </li> <li> <p>MulticlassAvgFScore: A multiclass <code>MLModel</code> uses the F1 score technique to measure performance. </p> </li> </ul> <p> For more information about performance metrics, please see the <a href="https://docs.aws.amazon.com/machine-learning/latest/dg">Amazon Machine Learning Developer Guide</a>. </p>"""
    log_uri: NotRequired["capo_machine_learning.types.presigned_s3_url.PresignedS3Url"]
    """<p>A link to the file that contains logs of the <code>CreateEvaluation</code> operation.</p>"""
    message: NotRequired["capo_machine_learning.types.message.Message"]
    """<p>A description of the most recent details about evaluating the <code>MLModel</code>.</p>"""
    compute_time: NotRequired["capo_machine_learning.types.long_type.LongType"]
    """<p>The approximate CPU time in milliseconds that Amazon Machine Learning spent processing the <code>Evaluation</code>, normalized and scaled on computation resources. <code>ComputeTime</code> is only available if the <code>Evaluation</code> is in the <code>COMPLETED</code> state.</p>"""
    finished_at: NotRequired["capo_machine_learning.types.epoch_time.EpochTime"]
    """<p>The epoch time when Amazon Machine Learning marked the <code>Evaluation</code> as <code>COMPLETED</code> or <code>FAILED</code>. <code>FinishedAt</code> is only available when the <code>Evaluation</code> is in the <code>COMPLETED</code> or <code>FAILED</code> state.</p>"""
    started_at: NotRequired["capo_machine_learning.types.epoch_time.EpochTime"]
    """<p>The epoch time when Amazon Machine Learning marked the <code>Evaluation</code> as <code>INPROGRESS</code>. <code>StartedAt</code> isn't available if the <code>Evaluation</code> is in the <code>PENDING</code> state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEvaluationOutput) -> dict:
    out: dict = {}
    if "evaluation_id" in value:
        out["EvaluationId"] = value["evaluation_id"]
    if "ml_model_id" in value:
        out["MLModelId"] = value["ml_model_id"]
    if "evaluation_data_source_id" in value:
        out["EvaluationDataSourceId"] = value["evaluation_data_source_id"]
    if "input_data_location_s3" in value:
        out["InputDataLocationS3"] = value["input_data_location_s3"]
    if "created_by_iam_user" in value:
        out["CreatedByIamUser"] = value["created_by_iam_user"]
    if "created_at" in value:
        import capo_machine_learning.types.epoch_time

        out["CreatedAt"] = (
            capo_machine_learning.types.epoch_time.serialize_aws_json_1_1(
                value["created_at"]
            )
        )
    if "last_updated_at" in value:
        import capo_machine_learning.types.epoch_time

        out["LastUpdatedAt"] = (
            capo_machine_learning.types.epoch_time.serialize_aws_json_1_1(
                value["last_updated_at"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_machine_learning.types.entity_status

        out["Status"] = (
            capo_machine_learning.types.entity_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "performance_metrics" in value:
        import capo_machine_learning.types.performance_metrics

        out["PerformanceMetrics"] = (
            capo_machine_learning.types.performance_metrics.serialize_aws_json_1_1(
                value["performance_metrics"]
            )
        )
    if "log_uri" in value:
        out["LogUri"] = value["log_uri"]
    if "message" in value:
        out["Message"] = value["message"]
    if "compute_time" in value:
        out["ComputeTime"] = value["compute_time"]
    if "finished_at" in value:
        import capo_machine_learning.types.epoch_time

        out["FinishedAt"] = (
            capo_machine_learning.types.epoch_time.serialize_aws_json_1_1(
                value["finished_at"]
            )
        )
    if "started_at" in value:
        import capo_machine_learning.types.epoch_time

        out["StartedAt"] = (
            capo_machine_learning.types.epoch_time.serialize_aws_json_1_1(
                value["started_at"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEvaluationOutput:
    out: GetEvaluationOutput = {}  # type: ignore[typeddict-item]
    if data.get("EvaluationId") is not None:
        out["evaluation_id"] = data["EvaluationId"]
    if data.get("MLModelId") is not None:
        out["ml_model_id"] = data["MLModelId"]
    if data.get("EvaluationDataSourceId") is not None:
        out["evaluation_data_source_id"] = data["EvaluationDataSourceId"]
    if data.get("InputDataLocationS3") is not None:
        out["input_data_location_s3"] = data["InputDataLocationS3"]
    if data.get("CreatedByIamUser") is not None:
        out["created_by_iam_user"] = data["CreatedByIamUser"]
    if data.get("CreatedAt") is not None:
        import capo_machine_learning.types.epoch_time

        out["created_at"] = (
            capo_machine_learning.types.epoch_time.deserialize_aws_json_1_1(
                data["CreatedAt"]
            )
        )
    if data.get("LastUpdatedAt") is not None:
        import capo_machine_learning.types.epoch_time

        out["last_updated_at"] = (
            capo_machine_learning.types.epoch_time.deserialize_aws_json_1_1(
                data["LastUpdatedAt"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        import capo_machine_learning.types.entity_status

        out["status"] = (
            capo_machine_learning.types.entity_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("PerformanceMetrics") is not None:
        import capo_machine_learning.types.performance_metrics

        out["performance_metrics"] = (
            capo_machine_learning.types.performance_metrics.deserialize_aws_json_1_1(
                data["PerformanceMetrics"]
            )
        )
    if data.get("LogUri") is not None:
        out["log_uri"] = data["LogUri"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ComputeTime") is not None:
        out["compute_time"] = data["ComputeTime"]
    if data.get("FinishedAt") is not None:
        import capo_machine_learning.types.epoch_time

        out["finished_at"] = (
            capo_machine_learning.types.epoch_time.deserialize_aws_json_1_1(
                data["FinishedAt"]
            )
        )
    if data.get("StartedAt") is not None:
        import capo_machine_learning.types.epoch_time

        out["started_at"] = (
            capo_machine_learning.types.epoch_time.deserialize_aws_json_1_1(
                data["StartedAt"]
            )
        )
    return out
