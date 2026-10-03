"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DescribeModelVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.auto_promotion_result
    import capo_lookoutequipment.types.auto_promotion_result_reason
    import capo_lookoutequipment.types.bounded_length_string
    import capo_lookoutequipment.types.data_pre_processing_configuration
    import capo_lookoutequipment.types.data_size_in_bytes
    import capo_lookoutequipment.types.dataset_arn
    import capo_lookoutequipment.types.dataset_name
    import capo_lookoutequipment.types.iam_role_arn
    import capo_lookoutequipment.types.inline_data_schema
    import capo_lookoutequipment.types.integer
    import capo_lookoutequipment.types.kms_key_arn
    import capo_lookoutequipment.types.labels_input_configuration
    import capo_lookoutequipment.types.model_arn
    import capo_lookoutequipment.types.model_diagnostics_output_configuration
    import capo_lookoutequipment.types.model_metrics
    import capo_lookoutequipment.types.model_name
    import capo_lookoutequipment.types.model_quality
    import capo_lookoutequipment.types.model_version
    import capo_lookoutequipment.types.model_version_arn
    import capo_lookoutequipment.types.model_version_source_type
    import capo_lookoutequipment.types.model_version_status
    import capo_lookoutequipment.types.off_condition
    import capo_lookoutequipment.types.s3_object
    import capo_lookoutequipment.types.timestamp


class DescribeModelVersionResponse(TypedDict, closed=True):
    model_name: NotRequired["capo_lookoutequipment.types.model_name.ModelName"]
    """<p>The name of the machine learning model that this version belongs to.</p>"""
    model_arn: NotRequired["capo_lookoutequipment.types.model_arn.ModelArn"]
    """<p>The Amazon Resource Name (ARN) of the parent machine learning model that this version belong to.</p>"""
    model_version: NotRequired["capo_lookoutequipment.types.model_version.ModelVersion"]
    """<p>The version of the machine learning model.</p>"""
    model_version_arn: NotRequired[
        "capo_lookoutequipment.types.model_version_arn.ModelVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model version.</p>"""
    status: NotRequired[
        "capo_lookoutequipment.types.model_version_status.ModelVersionStatus"
    ]
    """<p>The current status of the model version.</p>"""
    source_type: NotRequired[
        "capo_lookoutequipment.types.model_version_source_type.ModelVersionSourceType"
    ]
    """<p>Indicates whether this model version was created by training or by importing.</p>"""
    dataset_name: NotRequired["capo_lookoutequipment.types.dataset_name.DatasetName"]
    """<p>The name of the dataset used to train the model version.</p>"""
    dataset_arn: NotRequired["capo_lookoutequipment.types.dataset_arn.DatasetArn"]
    """<p>The Amazon Resource Name (ARN) of the dataset used to train the model version.</p>"""
    schema: NotRequired[
        "capo_lookoutequipment.types.inline_data_schema.InlineDataSchema"
    ]
    """<p>The schema of the data used to train the model version.</p>"""
    labels_input_configuration: NotRequired[
        "capo_lookoutequipment.types.labels_input_configuration.LabelsInputConfiguration"
    ]
    training_data_start_time: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>The date on which the training data began being gathered. If you imported the version, this is the date that the training data in the source version began being gathered.</p>"""
    training_data_end_time: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>The date on which the training data finished being gathered. If you imported the version, this is the date that the training data in the source version finished being gathered.</p>"""
    evaluation_data_start_time: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>The date on which the data in the evaluation set began being gathered. If you imported the version, this is the date that the evaluation set data in the source version began being gathered.</p>"""
    evaluation_data_end_time: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>The date on which the data in the evaluation set began being gathered. If you imported the version, this is the date that the evaluation set data in the source version finished being gathered.</p>"""
    role_arn: NotRequired["capo_lookoutequipment.types.iam_role_arn.IamRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the role that was used to train the model version.</p>"""
    data_pre_processing_configuration: NotRequired[
        "capo_lookoutequipment.types.data_pre_processing_configuration.DataPreProcessingConfiguration"
    ]
    training_execution_start_time: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>The time when the training of the version began.</p>"""
    training_execution_end_time: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>The time when the training of the version completed.</p>"""
    failed_reason: NotRequired[
        "capo_lookoutequipment.types.bounded_length_string.BoundedLengthString"
    ]
    """<p>The failure message if the training of the model version failed.</p>"""
    model_metrics: NotRequired["capo_lookoutequipment.types.model_metrics.ModelMetrics"]
    """<p>Shows an aggregated summary, in JSON format, of the model's performance within the evaluation time range. These metrics are created when evaluating the model.</p>"""
    last_updated_time: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p>Indicates the last time the machine learning model version was updated.</p>"""
    created_at: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p>Indicates the time and date at which the machine learning model version was created.</p>"""
    server_side_kms_key_id: NotRequired[
        "capo_lookoutequipment.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The identifier of the KMS key key used to encrypt model version data by Amazon Lookout for Equipment.</p>"""
    off_condition: NotRequired["capo_lookoutequipment.types.off_condition.OffCondition"]
    """<p>Indicates that the asset associated with this sensor has been shut off. As long as this condition is met, Lookout for Equipment will not use data from this asset for training, evaluation, or inference.</p>"""
    source_model_version_arn: NotRequired[
        "capo_lookoutequipment.types.model_version_arn.ModelVersionArn"
    ]
    """<p>If model version was imported, then this field is the arn of the source model version.</p>"""
    import_job_start_time: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>The date and time when the import job began. This field appears if the model version was imported.</p>"""
    import_job_end_time: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p>The date and time when the import job completed. This field appears if the model version was imported.</p>"""
    imported_data_size_in_bytes: NotRequired[
        "capo_lookoutequipment.types.data_size_in_bytes.DataSizeInBytes"
    ]
    """<p>The size in bytes of the imported data. This field appears if the model version was imported.</p>"""
    prior_model_metrics: NotRequired[
        "capo_lookoutequipment.types.model_metrics.ModelMetrics"
    ]
    """<p>If the model version was retrained, this field shows a summary of the performance of the prior model on the new training range. You can use the information in this JSON-formatted object to compare the new model version and the prior model version.</p>"""
    retraining_available_data_in_days: NotRequired[
        "capo_lookoutequipment.types.integer.Integer"
    ]
    """<p>Indicates the number of days of data used in the most recent scheduled retraining run. </p>"""
    auto_promotion_result: NotRequired[
        "capo_lookoutequipment.types.auto_promotion_result.AutoPromotionResult"
    ]
    """<p>Indicates whether the model version was promoted to be the active version after retraining or if there was an error with or cancellation of the retraining. </p>"""
    auto_promotion_result_reason: NotRequired[
        "capo_lookoutequipment.types.auto_promotion_result_reason.AutoPromotionResultReason"
    ]
    """<p>Indicates the reason for the <code>AutoPromotionResult</code>. For example, a model might not be promoted if its performance was worse than the active version, if there was an error during training, or if the retraining scheduler was using <code>MANUAL</code> promote mode. The model will be promoted in <code>MANAGED</code> promote mode if the performance is better than the previous model. </p>"""
    model_diagnostics_output_configuration: NotRequired[
        "capo_lookoutequipment.types.model_diagnostics_output_configuration.ModelDiagnosticsOutputConfiguration"
    ]
    """<p>The Amazon S3 location where Amazon Lookout for Equipment saves the pointwise model diagnostics for the model version.</p>"""
    model_diagnostics_results_object: NotRequired[
        "capo_lookoutequipment.types.s3_object.S3Object"
    ]
    """<p>The Amazon S3 output prefix for where Lookout for Equipment saves the pointwise model diagnostics for the model version.</p>"""
    model_quality: NotRequired["capo_lookoutequipment.types.model_quality.ModelQuality"]
    """<p>Provides a quality assessment for a model that uses labels. If Lookout for Equipment determines that the model quality is poor based on training metrics, the value is <code>POOR_QUALITY_DETECTED</code>. Otherwise, the value is <code>QUALITY_THRESHOLD_MET</code>.</p> <p>If the model is unlabeled, the model quality can't be assessed and the value of <code>ModelQuality</code> is <code>CANNOT_DETERMINE_QUALITY</code>. In this situation, you can get a model quality assessment by adding labels to the input dataset and retraining the model.</p> <p>For information about using labels with your models, see <a href="https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/understanding-labeling.html">Understanding labeling</a>.</p> <p>For information about improving the quality of a model, see <a href="https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/best-practices.html">Best practices with Amazon Lookout for Equipment</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeModelVersionResponse) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    if "model_version" in value:
        out["ModelVersion"] = value["model_version"]
    if "model_version_arn" in value:
        out["ModelVersionArn"] = value["model_version_arn"]
    if "status" in value:
        import capo_lookoutequipment.types.model_version_status

        out["Status"] = (
            capo_lookoutequipment.types.model_version_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "source_type" in value:
        import capo_lookoutequipment.types.model_version_source_type

        out["SourceType"] = (
            capo_lookoutequipment.types.model_version_source_type.serialize_aws_json_1_0(
                value["source_type"]
            )
        )
    if "dataset_name" in value:
        out["DatasetName"] = value["dataset_name"]
    if "dataset_arn" in value:
        out["DatasetArn"] = value["dataset_arn"]
    if "schema" in value:
        out["Schema"] = value["schema"]
    if "labels_input_configuration" in value:
        import capo_lookoutequipment.types.labels_input_configuration

        out["LabelsInputConfiguration"] = (
            capo_lookoutequipment.types.labels_input_configuration.serialize_aws_json_1_0(
                value["labels_input_configuration"]
            )
        )
    if "training_data_start_time" in value:
        import capo_lookoutequipment.types.timestamp

        out["TrainingDataStartTime"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["training_data_start_time"]
            )
        )
    if "training_data_end_time" in value:
        import capo_lookoutequipment.types.timestamp

        out["TrainingDataEndTime"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["training_data_end_time"]
            )
        )
    if "evaluation_data_start_time" in value:
        import capo_lookoutequipment.types.timestamp

        out["EvaluationDataStartTime"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["evaluation_data_start_time"]
            )
        )
    if "evaluation_data_end_time" in value:
        import capo_lookoutequipment.types.timestamp

        out["EvaluationDataEndTime"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["evaluation_data_end_time"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "data_pre_processing_configuration" in value:
        import capo_lookoutequipment.types.data_pre_processing_configuration

        out["DataPreProcessingConfiguration"] = (
            capo_lookoutequipment.types.data_pre_processing_configuration.serialize_aws_json_1_0(
                value["data_pre_processing_configuration"]
            )
        )
    if "training_execution_start_time" in value:
        import capo_lookoutequipment.types.timestamp

        out["TrainingExecutionStartTime"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["training_execution_start_time"]
            )
        )
    if "training_execution_end_time" in value:
        import capo_lookoutequipment.types.timestamp

        out["TrainingExecutionEndTime"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["training_execution_end_time"]
            )
        )
    if "failed_reason" in value:
        out["FailedReason"] = value["failed_reason"]
    if "model_metrics" in value:
        out["ModelMetrics"] = value["model_metrics"]
    if "last_updated_time" in value:
        import capo_lookoutequipment.types.timestamp

        out["LastUpdatedTime"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["last_updated_time"]
            )
        )
    if "created_at" in value:
        import capo_lookoutequipment.types.timestamp

        out["CreatedAt"] = capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "server_side_kms_key_id" in value:
        out["ServerSideKmsKeyId"] = value["server_side_kms_key_id"]
    if "off_condition" in value:
        out["OffCondition"] = value["off_condition"]
    if "source_model_version_arn" in value:
        out["SourceModelVersionArn"] = value["source_model_version_arn"]
    if "import_job_start_time" in value:
        import capo_lookoutequipment.types.timestamp

        out["ImportJobStartTime"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["import_job_start_time"]
            )
        )
    if "import_job_end_time" in value:
        import capo_lookoutequipment.types.timestamp

        out["ImportJobEndTime"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["import_job_end_time"]
            )
        )
    if "imported_data_size_in_bytes" in value:
        out["ImportedDataSizeInBytes"] = value["imported_data_size_in_bytes"]
    if "prior_model_metrics" in value:
        out["PriorModelMetrics"] = value["prior_model_metrics"]
    if "retraining_available_data_in_days" in value:
        out["RetrainingAvailableDataInDays"] = value[
            "retraining_available_data_in_days"
        ]
    if "auto_promotion_result" in value:
        import capo_lookoutequipment.types.auto_promotion_result

        out["AutoPromotionResult"] = (
            capo_lookoutequipment.types.auto_promotion_result.serialize_aws_json_1_0(
                value["auto_promotion_result"]
            )
        )
    if "auto_promotion_result_reason" in value:
        out["AutoPromotionResultReason"] = value["auto_promotion_result_reason"]
    if "model_diagnostics_output_configuration" in value:
        import capo_lookoutequipment.types.model_diagnostics_output_configuration

        out["ModelDiagnosticsOutputConfiguration"] = (
            capo_lookoutequipment.types.model_diagnostics_output_configuration.serialize_aws_json_1_0(
                value["model_diagnostics_output_configuration"]
            )
        )
    if "model_diagnostics_results_object" in value:
        import capo_lookoutequipment.types.s3_object

        out["ModelDiagnosticsResultsObject"] = (
            capo_lookoutequipment.types.s3_object.serialize_aws_json_1_0(
                value["model_diagnostics_results_object"]
            )
        )
    if "model_quality" in value:
        import capo_lookoutequipment.types.model_quality

        out["ModelQuality"] = (
            capo_lookoutequipment.types.model_quality.serialize_aws_json_1_0(
                value["model_quality"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeModelVersionResponse:
    out: DescribeModelVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("ModelName") is not None:
        out["model_name"] = data["ModelName"]
    if data.get("ModelArn") is not None:
        out["model_arn"] = data["ModelArn"]
    if data.get("ModelVersion") is not None:
        out["model_version"] = data["ModelVersion"]
    if data.get("ModelVersionArn") is not None:
        out["model_version_arn"] = data["ModelVersionArn"]
    if data.get("Status") is not None:
        import capo_lookoutequipment.types.model_version_status

        out["status"] = (
            capo_lookoutequipment.types.model_version_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if data.get("SourceType") is not None:
        import capo_lookoutequipment.types.model_version_source_type

        out["source_type"] = (
            capo_lookoutequipment.types.model_version_source_type.deserialize_aws_json_1_0(
                data["SourceType"]
            )
        )
    if data.get("DatasetName") is not None:
        out["dataset_name"] = data["DatasetName"]
    if data.get("DatasetArn") is not None:
        out["dataset_arn"] = data["DatasetArn"]
    if data.get("Schema") is not None:
        out["schema"] = data["Schema"]
    if data.get("LabelsInputConfiguration") is not None:
        import capo_lookoutequipment.types.labels_input_configuration

        out["labels_input_configuration"] = (
            capo_lookoutequipment.types.labels_input_configuration.deserialize_aws_json_1_0(
                data["LabelsInputConfiguration"]
            )
        )
    if data.get("TrainingDataStartTime") is not None:
        import capo_lookoutequipment.types.timestamp

        out["training_data_start_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["TrainingDataStartTime"]
            )
        )
    if data.get("TrainingDataEndTime") is not None:
        import capo_lookoutequipment.types.timestamp

        out["training_data_end_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["TrainingDataEndTime"]
            )
        )
    if data.get("EvaluationDataStartTime") is not None:
        import capo_lookoutequipment.types.timestamp

        out["evaluation_data_start_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["EvaluationDataStartTime"]
            )
        )
    if data.get("EvaluationDataEndTime") is not None:
        import capo_lookoutequipment.types.timestamp

        out["evaluation_data_end_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["EvaluationDataEndTime"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("DataPreProcessingConfiguration") is not None:
        import capo_lookoutequipment.types.data_pre_processing_configuration

        out["data_pre_processing_configuration"] = (
            capo_lookoutequipment.types.data_pre_processing_configuration.deserialize_aws_json_1_0(
                data["DataPreProcessingConfiguration"]
            )
        )
    if data.get("TrainingExecutionStartTime") is not None:
        import capo_lookoutequipment.types.timestamp

        out["training_execution_start_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["TrainingExecutionStartTime"]
            )
        )
    if data.get("TrainingExecutionEndTime") is not None:
        import capo_lookoutequipment.types.timestamp

        out["training_execution_end_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["TrainingExecutionEndTime"]
            )
        )
    if data.get("FailedReason") is not None:
        out["failed_reason"] = data["FailedReason"]
    if data.get("ModelMetrics") is not None:
        out["model_metrics"] = data["ModelMetrics"]
    if data.get("LastUpdatedTime") is not None:
        import capo_lookoutequipment.types.timestamp

        out["last_updated_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["LastUpdatedTime"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_lookoutequipment.types.timestamp

        out["created_at"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if data.get("ServerSideKmsKeyId") is not None:
        out["server_side_kms_key_id"] = data["ServerSideKmsKeyId"]
    if data.get("OffCondition") is not None:
        out["off_condition"] = data["OffCondition"]
    if data.get("SourceModelVersionArn") is not None:
        out["source_model_version_arn"] = data["SourceModelVersionArn"]
    if data.get("ImportJobStartTime") is not None:
        import capo_lookoutequipment.types.timestamp

        out["import_job_start_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["ImportJobStartTime"]
            )
        )
    if data.get("ImportJobEndTime") is not None:
        import capo_lookoutequipment.types.timestamp

        out["import_job_end_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["ImportJobEndTime"]
            )
        )
    if data.get("ImportedDataSizeInBytes") is not None:
        out["imported_data_size_in_bytes"] = data["ImportedDataSizeInBytes"]
    if data.get("PriorModelMetrics") is not None:
        out["prior_model_metrics"] = data["PriorModelMetrics"]
    if data.get("RetrainingAvailableDataInDays") is not None:
        out["retraining_available_data_in_days"] = data["RetrainingAvailableDataInDays"]
    if data.get("AutoPromotionResult") is not None:
        import capo_lookoutequipment.types.auto_promotion_result

        out["auto_promotion_result"] = (
            capo_lookoutequipment.types.auto_promotion_result.deserialize_aws_json_1_0(
                data["AutoPromotionResult"]
            )
        )
    if data.get("AutoPromotionResultReason") is not None:
        out["auto_promotion_result_reason"] = data["AutoPromotionResultReason"]
    if data.get("ModelDiagnosticsOutputConfiguration") is not None:
        import capo_lookoutequipment.types.model_diagnostics_output_configuration

        out["model_diagnostics_output_configuration"] = (
            capo_lookoutequipment.types.model_diagnostics_output_configuration.deserialize_aws_json_1_0(
                data["ModelDiagnosticsOutputConfiguration"]
            )
        )
    if data.get("ModelDiagnosticsResultsObject") is not None:
        import capo_lookoutequipment.types.s3_object

        out["model_diagnostics_results_object"] = (
            capo_lookoutequipment.types.s3_object.deserialize_aws_json_1_0(
                data["ModelDiagnosticsResultsObject"]
            )
        )
    if data.get("ModelQuality") is not None:
        import capo_lookoutequipment.types.model_quality

        out["model_quality"] = (
            capo_lookoutequipment.types.model_quality.deserialize_aws_json_1_0(
                data["ModelQuality"]
            )
        )
    return out
