"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DescribeModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.bounded_length_string
    import capo_lookoutequipment.types.data_pre_processing_configuration
    import capo_lookoutequipment.types.dataset_arn
    import capo_lookoutequipment.types.dataset_name
    import capo_lookoutequipment.types.iam_role_arn
    import capo_lookoutequipment.types.integer
    import capo_lookoutequipment.types.kms_key_arn
    import capo_lookoutequipment.types.labels_input_configuration
    import capo_lookoutequipment.types.model_arn
    import capo_lookoutequipment.types.model_diagnostics_output_configuration
    import capo_lookoutequipment.types.model_name
    import capo_lookoutequipment.types.model_quality
    import capo_lookoutequipment.types.model_status
    import capo_lookoutequipment.types.model_version
    import capo_lookoutequipment.types.model_version_arn
    import capo_lookoutequipment.types.model_version_status
    import capo_lookoutequipment.types.off_condition
    import capo_lookoutequipment.types.retraining_scheduler_status
    import capo_lookoutequipment.types.synthesized_json_inline_data_schema
    import capo_lookoutequipment.types.synthesized_json_model_metrics
    import capo_lookoutequipment.types.timestamp


class DescribeModelResponse(TypedDict, closed=True):
    model_name: NotRequired["capo_lookoutequipment.types.model_name.ModelName"]
    """<p>The name of the machine learning model being described. </p>"""
    model_arn: NotRequired["capo_lookoutequipment.types.model_arn.ModelArn"]
    """<p>The Amazon Resource Name (ARN) of the machine learning model being described. </p>"""
    dataset_name: NotRequired["capo_lookoutequipment.types.dataset_name.DatasetName"]
    """<p>The name of the dataset being used by the machine learning being described. </p>"""
    dataset_arn: NotRequired["capo_lookoutequipment.types.dataset_arn.DatasetArn"]
    """<p>The Amazon Resouce Name (ARN) of the dataset used to create the machine learning model being described. </p>"""
    schema: NotRequired[
        "capo_lookoutequipment.types.synthesized_json_inline_data_schema.SynthesizedJsonInlineDataSchema"
    ]
    """<p>A JSON description of the data that is in each time series dataset, including names, column names, and data types. </p>"""
    labels_input_configuration: NotRequired[
        "capo_lookoutequipment.types.labels_input_configuration.LabelsInputConfiguration"
    ]
    """<p>Specifies configuration information about the labels input, including its S3 location. </p>"""
    training_data_start_time: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p> Indicates the time reference in the dataset that was used to begin the subset of training data for the machine learning model. </p>"""
    training_data_end_time: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p> Indicates the time reference in the dataset that was used to end the subset of training data for the machine learning model. </p>"""
    evaluation_data_start_time: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p> Indicates the time reference in the dataset that was used to begin the subset of evaluation data for the machine learning model. </p>"""
    evaluation_data_end_time: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p> Indicates the time reference in the dataset that was used to end the subset of evaluation data for the machine learning model. </p>"""
    role_arn: NotRequired["capo_lookoutequipment.types.iam_role_arn.IamRoleArn"]
    """<p> The Amazon Resource Name (ARN) of a role with permission to access the data source for the machine learning model being described. </p>"""
    data_pre_processing_configuration: NotRequired[
        "capo_lookoutequipment.types.data_pre_processing_configuration.DataPreProcessingConfiguration"
    ]
    """<p>The configuration is the <code>TargetSamplingRate</code>, which is the sampling rate of the data after post processing by Amazon Lookout for Equipment. For example, if you provide data that has been collected at a 1 second level and you want the system to resample the data at a 1 minute rate before training, the <code>TargetSamplingRate</code> is 1 minute.</p> <p>When providing a value for the <code>TargetSamplingRate</code>, you must attach the prefix "PT" to the rate you want. The value for a 1 second rate is therefore <i>PT1S</i>, the value for a 15 minute rate is <i>PT15M</i>, and the value for a 1 hour rate is <i>PT1H</i> </p>"""
    status: NotRequired["capo_lookoutequipment.types.model_status.ModelStatus"]
    """<p>Specifies the current status of the model being described. Status describes the status of the most recent action of the model. </p>"""
    training_execution_start_time: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>Indicates the time at which the training of the machine learning model began. </p>"""
    training_execution_end_time: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>Indicates the time at which the training of the machine learning model was completed. </p>"""
    failed_reason: NotRequired[
        "capo_lookoutequipment.types.bounded_length_string.BoundedLengthString"
    ]
    """<p>If the training of the machine learning model failed, this indicates the reason for that failure. </p>"""
    model_metrics: NotRequired[
        "capo_lookoutequipment.types.synthesized_json_model_metrics.SynthesizedJsonModelMetrics"
    ]
    """<p>The Model Metrics show an aggregated summary of the model's performance within the evaluation time range. This is the JSON content of the metrics created when evaluating the model. </p>"""
    last_updated_time: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p>Indicates the last time the machine learning model was updated. The type of update is not specified. </p>"""
    created_at: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p>Indicates the time and date at which the machine learning model was created. </p>"""
    server_side_kms_key_id: NotRequired[
        "capo_lookoutequipment.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>Provides the identifier of the KMS key used to encrypt model data by Amazon Lookout for Equipment. </p>"""
    off_condition: NotRequired["capo_lookoutequipment.types.off_condition.OffCondition"]
    """<p>Indicates that the asset associated with this sensor has been shut off. As long as this condition is met, Lookout for Equipment will not use data from this asset for training, evaluation, or inference.</p>"""
    source_model_version_arn: NotRequired[
        "capo_lookoutequipment.types.model_version_arn.ModelVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the source model version. This field appears if the active model version was imported.</p>"""
    import_job_start_time: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>The date and time when the import job was started. This field appears if the active model version was imported.</p>"""
    import_job_end_time: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p>The date and time when the import job was completed. This field appears if the active model version was imported.</p>"""
    active_model_version: NotRequired[
        "capo_lookoutequipment.types.model_version.ModelVersion"
    ]
    """<p>The name of the model version used by the inference schedular when running a scheduled inference execution.</p>"""
    active_model_version_arn: NotRequired[
        "capo_lookoutequipment.types.model_version_arn.ModelVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model version used by the inference scheduler when running a scheduled inference execution.</p>"""
    model_version_activated_at: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>The date the active model version was activated.</p>"""
    previous_active_model_version: NotRequired[
        "capo_lookoutequipment.types.model_version.ModelVersion"
    ]
    """<p>The model version that was set as the active model version prior to the current active model version.</p>"""
    previous_active_model_version_arn: NotRequired[
        "capo_lookoutequipment.types.model_version_arn.ModelVersionArn"
    ]
    """<p>The ARN of the model version that was set as the active model version prior to the current active model version.</p>"""
    previous_model_version_activated_at: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>The date and time when the previous active model version was activated.</p>"""
    prior_model_metrics: NotRequired[
        "capo_lookoutequipment.types.synthesized_json_model_metrics.SynthesizedJsonModelMetrics"
    ]
    """<p>If the model version was retrained, this field shows a summary of the performance of the prior model on the new training range. You can use the information in this JSON-formatted object to compare the new model version and the prior model version.</p>"""
    latest_scheduled_retraining_failed_reason: NotRequired[
        "capo_lookoutequipment.types.bounded_length_string.BoundedLengthString"
    ]
    """<p>If the model version was generated by retraining and the training failed, this indicates the reason for that failure. </p>"""
    latest_scheduled_retraining_status: NotRequired[
        "capo_lookoutequipment.types.model_version_status.ModelVersionStatus"
    ]
    """<p>Indicates the status of the most recent scheduled retraining run. </p>"""
    latest_scheduled_retraining_model_version: NotRequired[
        "capo_lookoutequipment.types.model_version.ModelVersion"
    ]
    """<p>Indicates the most recent model version that was generated by retraining. </p>"""
    latest_scheduled_retraining_start_time: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>Indicates the start time of the most recent scheduled retraining run. </p>"""
    latest_scheduled_retraining_available_data_in_days: NotRequired[
        "capo_lookoutequipment.types.integer.Integer"
    ]
    """<p>Indicates the number of days of data used in the most recent scheduled retraining run. </p>"""
    next_scheduled_retraining_start_date: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>Indicates the date and time that the next scheduled retraining run will start on. Lookout for Equipment truncates the time you provide to the nearest UTC day.</p>"""
    accumulated_inference_data_start_time: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>Indicates the start time of the inference data that has been accumulated. </p>"""
    accumulated_inference_data_end_time: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>Indicates the end time of the inference data that has been accumulated. </p>"""
    retraining_scheduler_status: NotRequired[
        "capo_lookoutequipment.types.retraining_scheduler_status.RetrainingSchedulerStatus"
    ]
    """<p>Indicates the status of the retraining scheduler. </p>"""
    model_diagnostics_output_configuration: NotRequired[
        "capo_lookoutequipment.types.model_diagnostics_output_configuration.ModelDiagnosticsOutputConfiguration"
    ]
    """<p>Configuration information for the model's pointwise model diagnostics.</p>"""
    model_quality: NotRequired["capo_lookoutequipment.types.model_quality.ModelQuality"]
    """<p>Provides a quality assessment for a model that uses labels. If Lookout for Equipment determines that the model quality is poor based on training metrics, the value is <code>POOR_QUALITY_DETECTED</code>. Otherwise, the value is <code>QUALITY_THRESHOLD_MET</code>.</p> <p>If the model is unlabeled, the model quality can't be assessed and the value of <code>ModelQuality</code> is <code>CANNOT_DETERMINE_QUALITY</code>. In this situation, you can get a model quality assessment by adding labels to the input dataset and retraining the model.</p> <p>For information about using labels with your models, see <a href="https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/understanding-labeling.html">Understanding labeling</a>.</p> <p>For information about improving the quality of a model, see <a href="https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/best-practices.html">Best practices with Amazon Lookout for Equipment</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeModelResponse) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
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
    if "status" in value:
        import capo_lookoutequipment.types.model_status

        out["Status"] = capo_lookoutequipment.types.model_status.serialize_aws_json_1_0(
            value["status"]
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
    if "active_model_version" in value:
        out["ActiveModelVersion"] = value["active_model_version"]
    if "active_model_version_arn" in value:
        out["ActiveModelVersionArn"] = value["active_model_version_arn"]
    if "model_version_activated_at" in value:
        import capo_lookoutequipment.types.timestamp

        out["ModelVersionActivatedAt"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["model_version_activated_at"]
            )
        )
    if "previous_active_model_version" in value:
        out["PreviousActiveModelVersion"] = value["previous_active_model_version"]
    if "previous_active_model_version_arn" in value:
        out["PreviousActiveModelVersionArn"] = value[
            "previous_active_model_version_arn"
        ]
    if "previous_model_version_activated_at" in value:
        import capo_lookoutequipment.types.timestamp

        out["PreviousModelVersionActivatedAt"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["previous_model_version_activated_at"]
            )
        )
    if "prior_model_metrics" in value:
        out["PriorModelMetrics"] = value["prior_model_metrics"]
    if "latest_scheduled_retraining_failed_reason" in value:
        out["LatestScheduledRetrainingFailedReason"] = value[
            "latest_scheduled_retraining_failed_reason"
        ]
    if "latest_scheduled_retraining_status" in value:
        import capo_lookoutequipment.types.model_version_status

        out["LatestScheduledRetrainingStatus"] = (
            capo_lookoutequipment.types.model_version_status.serialize_aws_json_1_0(
                value["latest_scheduled_retraining_status"]
            )
        )
    if "latest_scheduled_retraining_model_version" in value:
        out["LatestScheduledRetrainingModelVersion"] = value[
            "latest_scheduled_retraining_model_version"
        ]
    if "latest_scheduled_retraining_start_time" in value:
        import capo_lookoutequipment.types.timestamp

        out["LatestScheduledRetrainingStartTime"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["latest_scheduled_retraining_start_time"]
            )
        )
    if "latest_scheduled_retraining_available_data_in_days" in value:
        out["LatestScheduledRetrainingAvailableDataInDays"] = value[
            "latest_scheduled_retraining_available_data_in_days"
        ]
    if "next_scheduled_retraining_start_date" in value:
        import capo_lookoutequipment.types.timestamp

        out["NextScheduledRetrainingStartDate"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["next_scheduled_retraining_start_date"]
            )
        )
    if "accumulated_inference_data_start_time" in value:
        import capo_lookoutequipment.types.timestamp

        out["AccumulatedInferenceDataStartTime"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["accumulated_inference_data_start_time"]
            )
        )
    if "accumulated_inference_data_end_time" in value:
        import capo_lookoutequipment.types.timestamp

        out["AccumulatedInferenceDataEndTime"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["accumulated_inference_data_end_time"]
            )
        )
    if "retraining_scheduler_status" in value:
        import capo_lookoutequipment.types.retraining_scheduler_status

        out["RetrainingSchedulerStatus"] = (
            capo_lookoutequipment.types.retraining_scheduler_status.serialize_aws_json_1_0(
                value["retraining_scheduler_status"]
            )
        )
    if "model_diagnostics_output_configuration" in value:
        import capo_lookoutequipment.types.model_diagnostics_output_configuration

        out["ModelDiagnosticsOutputConfiguration"] = (
            capo_lookoutequipment.types.model_diagnostics_output_configuration.serialize_aws_json_1_0(
                value["model_diagnostics_output_configuration"]
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


def deserialize_aws_json_1_0(data: dict) -> DescribeModelResponse:
    out: DescribeModelResponse = {}  # type: ignore[typeddict-item]
    if data.get("ModelName") is not None:
        out["model_name"] = data["ModelName"]
    if data.get("ModelArn") is not None:
        out["model_arn"] = data["ModelArn"]
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
    if data.get("Status") is not None:
        import capo_lookoutequipment.types.model_status

        out["status"] = (
            capo_lookoutequipment.types.model_status.deserialize_aws_json_1_0(
                data["Status"]
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
    if data.get("ActiveModelVersion") is not None:
        out["active_model_version"] = data["ActiveModelVersion"]
    if data.get("ActiveModelVersionArn") is not None:
        out["active_model_version_arn"] = data["ActiveModelVersionArn"]
    if data.get("ModelVersionActivatedAt") is not None:
        import capo_lookoutequipment.types.timestamp

        out["model_version_activated_at"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["ModelVersionActivatedAt"]
            )
        )
    if data.get("PreviousActiveModelVersion") is not None:
        out["previous_active_model_version"] = data["PreviousActiveModelVersion"]
    if data.get("PreviousActiveModelVersionArn") is not None:
        out["previous_active_model_version_arn"] = data["PreviousActiveModelVersionArn"]
    if data.get("PreviousModelVersionActivatedAt") is not None:
        import capo_lookoutequipment.types.timestamp

        out["previous_model_version_activated_at"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["PreviousModelVersionActivatedAt"]
            )
        )
    if data.get("PriorModelMetrics") is not None:
        out["prior_model_metrics"] = data["PriorModelMetrics"]
    if data.get("LatestScheduledRetrainingFailedReason") is not None:
        out["latest_scheduled_retraining_failed_reason"] = data[
            "LatestScheduledRetrainingFailedReason"
        ]
    if data.get("LatestScheduledRetrainingStatus") is not None:
        import capo_lookoutequipment.types.model_version_status

        out["latest_scheduled_retraining_status"] = (
            capo_lookoutequipment.types.model_version_status.deserialize_aws_json_1_0(
                data["LatestScheduledRetrainingStatus"]
            )
        )
    if data.get("LatestScheduledRetrainingModelVersion") is not None:
        out["latest_scheduled_retraining_model_version"] = data[
            "LatestScheduledRetrainingModelVersion"
        ]
    if data.get("LatestScheduledRetrainingStartTime") is not None:
        import capo_lookoutequipment.types.timestamp

        out["latest_scheduled_retraining_start_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["LatestScheduledRetrainingStartTime"]
            )
        )
    if data.get("LatestScheduledRetrainingAvailableDataInDays") is not None:
        out["latest_scheduled_retraining_available_data_in_days"] = data[
            "LatestScheduledRetrainingAvailableDataInDays"
        ]
    if data.get("NextScheduledRetrainingStartDate") is not None:
        import capo_lookoutequipment.types.timestamp

        out["next_scheduled_retraining_start_date"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["NextScheduledRetrainingStartDate"]
            )
        )
    if data.get("AccumulatedInferenceDataStartTime") is not None:
        import capo_lookoutequipment.types.timestamp

        out["accumulated_inference_data_start_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["AccumulatedInferenceDataStartTime"]
            )
        )
    if data.get("AccumulatedInferenceDataEndTime") is not None:
        import capo_lookoutequipment.types.timestamp

        out["accumulated_inference_data_end_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["AccumulatedInferenceDataEndTime"]
            )
        )
    if data.get("RetrainingSchedulerStatus") is not None:
        import capo_lookoutequipment.types.retraining_scheduler_status

        out["retraining_scheduler_status"] = (
            capo_lookoutequipment.types.retraining_scheduler_status.deserialize_aws_json_1_0(
                data["RetrainingSchedulerStatus"]
            )
        )
    if data.get("ModelDiagnosticsOutputConfiguration") is not None:
        import capo_lookoutequipment.types.model_diagnostics_output_configuration

        out["model_diagnostics_output_configuration"] = (
            capo_lookoutequipment.types.model_diagnostics_output_configuration.deserialize_aws_json_1_0(
                data["ModelDiagnosticsOutputConfiguration"]
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
