"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#CreateModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lookoutequipment.types.data_pre_processing_configuration
    import capo_lookoutequipment.types.dataset_identifier
    import capo_lookoutequipment.types.dataset_schema
    import capo_lookoutequipment.types.iam_role_arn
    import capo_lookoutequipment.types.idempotence_token
    import capo_lookoutequipment.types.labels_input_configuration
    import capo_lookoutequipment.types.model_diagnostics_output_configuration
    import capo_lookoutequipment.types.model_name
    import capo_lookoutequipment.types.name_or_arn
    import capo_lookoutequipment.types.off_condition
    import capo_lookoutequipment.types.tag_list
    import capo_lookoutequipment.types.timestamp


class CreateModelRequest(TypedDict, closed=True):
    model_name: "capo_lookoutequipment.types.model_name.ModelName"
    """<p>The name for the machine learning model to be created.</p>"""
    dataset_name: "capo_lookoutequipment.types.dataset_identifier.DatasetIdentifier"
    """<p>The name of the dataset for the machine learning model being created. </p>"""
    dataset_schema: NotRequired[
        "capo_lookoutequipment.types.dataset_schema.DatasetSchema"
    ]
    """<p>The data schema for the machine learning model being created. </p>"""
    labels_input_configuration: NotRequired[
        "capo_lookoutequipment.types.labels_input_configuration.LabelsInputConfiguration"
    ]
    """<p>The input configuration for the labels being used for the machine learning model that's being created. </p>"""
    client_token: "capo_lookoutequipment.types.idempotence_token.IdempotenceToken"
    """<p>A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>"""
    training_data_start_time: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>Indicates the time reference in the dataset that should be used to begin the subset of training data for the machine learning model. </p>"""
    training_data_end_time: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>Indicates the time reference in the dataset that should be used to end the subset of training data for the machine learning model. </p>"""
    evaluation_data_start_time: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>Indicates the time reference in the dataset that should be used to begin the subset of evaluation data for the machine learning model. </p>"""
    evaluation_data_end_time: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p> Indicates the time reference in the dataset that should be used to end the subset of evaluation data for the machine learning model. </p>"""
    role_arn: NotRequired["capo_lookoutequipment.types.iam_role_arn.IamRoleArn"]
    """<p> The Amazon Resource Name (ARN) of a role with permission to access the data source being used to create the machine learning model. </p>"""
    data_pre_processing_configuration: NotRequired[
        "capo_lookoutequipment.types.data_pre_processing_configuration.DataPreProcessingConfiguration"
    ]
    """<p>The configuration is the <code>TargetSamplingRate</code>, which is the sampling rate of the data after post processing by Amazon Lookout for Equipment. For example, if you provide data that has been collected at a 1 second level and you want the system to resample the data at a 1 minute rate before training, the <code>TargetSamplingRate</code> is 1 minute.</p> <p>When providing a value for the <code>TargetSamplingRate</code>, you must attach the prefix "PT" to the rate you want. The value for a 1 second rate is therefore <i>PT1S</i>, the value for a 15 minute rate is <i>PT15M</i>, and the value for a 1 hour rate is <i>PT1H</i> </p>"""
    server_side_kms_key_id: NotRequired[
        "capo_lookoutequipment.types.name_or_arn.NameOrArn"
    ]
    """<p>Provides the identifier of the KMS key used to encrypt model data by Amazon Lookout for Equipment. </p>"""
    tags: NotRequired["capo_lookoutequipment.types.tag_list.TagList"]
    """<p> Any tags associated with the machine learning model being created. </p>"""
    off_condition: NotRequired["capo_lookoutequipment.types.off_condition.OffCondition"]
    """<p>Indicates that the asset associated with this sensor has been shut off. As long as this condition is met, Lookout for Equipment will not use data from this asset for training, evaluation, or inference.</p>"""
    model_diagnostics_output_configuration: NotRequired[
        "capo_lookoutequipment.types.model_diagnostics_output_configuration.ModelDiagnosticsOutputConfiguration"
    ]
    """<p>The Amazon S3 location where you want Amazon Lookout for Equipment to save the pointwise model diagnostics. You must also specify the <code>RoleArn</code> request parameter.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateModelRequest) -> dict:
    out: dict = {}
    out["ModelName"] = value["model_name"]
    out["DatasetName"] = value["dataset_name"]
    if "dataset_schema" in value:
        import capo_lookoutequipment.types.dataset_schema

        out["DatasetSchema"] = (
            capo_lookoutequipment.types.dataset_schema.serialize_aws_json_1_0(
                value["dataset_schema"]
            )
        )
    if "labels_input_configuration" in value:
        import capo_lookoutequipment.types.labels_input_configuration

        out["LabelsInputConfiguration"] = (
            capo_lookoutequipment.types.labels_input_configuration.serialize_aws_json_1_0(
                value["labels_input_configuration"]
            )
        )
    out["ClientToken"] = value["client_token"]
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
    if "server_side_kms_key_id" in value:
        out["ServerSideKmsKeyId"] = value["server_side_kms_key_id"]
    if "tags" in value:
        import capo_lookoutequipment.types.tag_list

        out["Tags"] = capo_lookoutequipment.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "off_condition" in value:
        out["OffCondition"] = value["off_condition"]
    if "model_diagnostics_output_configuration" in value:
        import capo_lookoutequipment.types.model_diagnostics_output_configuration

        out["ModelDiagnosticsOutputConfiguration"] = (
            capo_lookoutequipment.types.model_diagnostics_output_configuration.serialize_aws_json_1_0(
                value["model_diagnostics_output_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateModelRequest:
    out: CreateModelRequest = {}  # type: ignore[typeddict-item]
    if data.get("ModelName") is not None:
        out["model_name"] = data["ModelName"]
    else:
        raise DeserializationError("CreateModelRequest.model_name required")
    if data.get("DatasetName") is not None:
        out["dataset_name"] = data["DatasetName"]
    else:
        raise DeserializationError("CreateModelRequest.dataset_name required")
    if data.get("DatasetSchema") is not None:
        import capo_lookoutequipment.types.dataset_schema

        out["dataset_schema"] = (
            capo_lookoutequipment.types.dataset_schema.deserialize_aws_json_1_0(
                data["DatasetSchema"]
            )
        )
    if data.get("LabelsInputConfiguration") is not None:
        import capo_lookoutequipment.types.labels_input_configuration

        out["labels_input_configuration"] = (
            capo_lookoutequipment.types.labels_input_configuration.deserialize_aws_json_1_0(
                data["LabelsInputConfiguration"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError("CreateModelRequest.client_token required")
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
    if data.get("ServerSideKmsKeyId") is not None:
        out["server_side_kms_key_id"] = data["ServerSideKmsKeyId"]
    if data.get("Tags") is not None:
        import capo_lookoutequipment.types.tag_list

        out["tags"] = capo_lookoutequipment.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if data.get("OffCondition") is not None:
        out["off_condition"] = data["OffCondition"]
    if data.get("ModelDiagnosticsOutputConfiguration") is not None:
        import capo_lookoutequipment.types.model_diagnostics_output_configuration

        out["model_diagnostics_output_configuration"] = (
            capo_lookoutequipment.types.model_diagnostics_output_configuration.deserialize_aws_json_1_0(
                data["ModelDiagnosticsOutputConfiguration"]
            )
        )
    return out
