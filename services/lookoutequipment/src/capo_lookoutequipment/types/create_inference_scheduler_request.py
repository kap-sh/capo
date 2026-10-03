"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#CreateInferenceSchedulerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lookoutequipment.types.data_delay_offset_in_minutes
    import capo_lookoutequipment.types.data_upload_frequency
    import capo_lookoutequipment.types.iam_role_arn
    import capo_lookoutequipment.types.idempotence_token
    import capo_lookoutequipment.types.inference_input_configuration
    import capo_lookoutequipment.types.inference_output_configuration
    import capo_lookoutequipment.types.inference_scheduler_name
    import capo_lookoutequipment.types.model_name
    import capo_lookoutequipment.types.name_or_arn
    import capo_lookoutequipment.types.tag_list


class CreateInferenceSchedulerRequest(TypedDict, closed=True):
    model_name: "capo_lookoutequipment.types.model_name.ModelName"
    """<p>The name of the previously trained machine learning model being used to create the inference scheduler. </p>"""
    inference_scheduler_name: (
        "capo_lookoutequipment.types.inference_scheduler_name.InferenceSchedulerName"
    )
    """<p>The name of the inference scheduler being created. </p>"""
    data_delay_offset_in_minutes: NotRequired[
        "capo_lookoutequipment.types.data_delay_offset_in_minutes.DataDelayOffsetInMinutes"
    ]
    """<p>The interval (in minutes) of planned delay at the start of each inference segment. For example, if inference is set to run every ten minutes, the delay is set to five minutes and the time is 09:08. The inference scheduler will wake up at the configured interval (which, without a delay configured, would be 09:10) plus the additional five minute delay time (so 09:15) to check your Amazon S3 bucket. The delay provides a buffer for you to upload data at the same frequency, so that you don't have to stop and restart the scheduler when uploading new data.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/understanding-inference-process.html">Understanding the inference process</a>.</p>"""
    data_upload_frequency: (
        "capo_lookoutequipment.types.data_upload_frequency.DataUploadFrequency"
    )
    """<p> How often data is uploaded to the source Amazon S3 bucket for the input data. The value chosen is the length of time between data uploads. For instance, if you select 5 minutes, Amazon Lookout for Equipment will upload the real-time data to the source bucket once every 5 minutes. This frequency also determines how often Amazon Lookout for Equipment runs inference on your data.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/understanding-inference-process.html">Understanding the inference process</a>.</p>"""
    data_input_configuration: "capo_lookoutequipment.types.inference_input_configuration.InferenceInputConfiguration"
    """<p>Specifies configuration information for the input data for the inference scheduler, including delimiter, format, and dataset location. </p>"""
    data_output_configuration: "capo_lookoutequipment.types.inference_output_configuration.InferenceOutputConfiguration"
    """<p>Specifies configuration information for the output results for the inference scheduler, including the S3 location for the output. </p>"""
    role_arn: "capo_lookoutequipment.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of a role with permission to access the data source being used for the inference. </p>"""
    server_side_kms_key_id: NotRequired[
        "capo_lookoutequipment.types.name_or_arn.NameOrArn"
    ]
    """<p>Provides the identifier of the KMS key used to encrypt inference scheduler data by Amazon Lookout for Equipment. </p>"""
    client_token: "capo_lookoutequipment.types.idempotence_token.IdempotenceToken"
    """<p> A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>"""
    tags: NotRequired["capo_lookoutequipment.types.tag_list.TagList"]
    """<p>Any tags associated with the inference scheduler. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateInferenceSchedulerRequest) -> dict:
    out: dict = {}
    out["ModelName"] = value["model_name"]
    out["InferenceSchedulerName"] = value["inference_scheduler_name"]
    if "data_delay_offset_in_minutes" in value:
        out["DataDelayOffsetInMinutes"] = value["data_delay_offset_in_minutes"]
    import capo_lookoutequipment.types.data_upload_frequency

    out["DataUploadFrequency"] = (
        capo_lookoutequipment.types.data_upload_frequency.serialize_aws_json_1_0(
            value["data_upload_frequency"]
        )
    )
    import capo_lookoutequipment.types.inference_input_configuration

    out["DataInputConfiguration"] = (
        capo_lookoutequipment.types.inference_input_configuration.serialize_aws_json_1_0(
            value["data_input_configuration"]
        )
    )
    import capo_lookoutequipment.types.inference_output_configuration

    out["DataOutputConfiguration"] = (
        capo_lookoutequipment.types.inference_output_configuration.serialize_aws_json_1_0(
            value["data_output_configuration"]
        )
    )
    out["RoleArn"] = value["role_arn"]
    if "server_side_kms_key_id" in value:
        out["ServerSideKmsKeyId"] = value["server_side_kms_key_id"]
    out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_lookoutequipment.types.tag_list

        out["Tags"] = capo_lookoutequipment.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateInferenceSchedulerRequest:
    out: CreateInferenceSchedulerRequest = {}  # type: ignore[typeddict-item]
    if data.get("ModelName") is not None:
        out["model_name"] = data["ModelName"]
    else:
        raise DeserializationError(
            "CreateInferenceSchedulerRequest.model_name required"
        )
    if data.get("InferenceSchedulerName") is not None:
        out["inference_scheduler_name"] = data["InferenceSchedulerName"]
    else:
        raise DeserializationError(
            "CreateInferenceSchedulerRequest.inference_scheduler_name required"
        )
    if data.get("DataDelayOffsetInMinutes") is not None:
        out["data_delay_offset_in_minutes"] = data["DataDelayOffsetInMinutes"]
    if data.get("DataUploadFrequency") is not None:
        import capo_lookoutequipment.types.data_upload_frequency

        out["data_upload_frequency"] = (
            capo_lookoutequipment.types.data_upload_frequency.deserialize_aws_json_1_0(
                data["DataUploadFrequency"]
            )
        )
    else:
        raise DeserializationError(
            "CreateInferenceSchedulerRequest.data_upload_frequency required"
        )
    if data.get("DataInputConfiguration") is not None:
        import capo_lookoutequipment.types.inference_input_configuration

        out["data_input_configuration"] = (
            capo_lookoutequipment.types.inference_input_configuration.deserialize_aws_json_1_0(
                data["DataInputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateInferenceSchedulerRequest.data_input_configuration required"
        )
    if data.get("DataOutputConfiguration") is not None:
        import capo_lookoutequipment.types.inference_output_configuration

        out["data_output_configuration"] = (
            capo_lookoutequipment.types.inference_output_configuration.deserialize_aws_json_1_0(
                data["DataOutputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateInferenceSchedulerRequest.data_output_configuration required"
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("CreateInferenceSchedulerRequest.role_arn required")
    if data.get("ServerSideKmsKeyId") is not None:
        out["server_side_kms_key_id"] = data["ServerSideKmsKeyId"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError(
            "CreateInferenceSchedulerRequest.client_token required"
        )
    if data.get("Tags") is not None:
        import capo_lookoutequipment.types.tag_list

        out["tags"] = capo_lookoutequipment.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
