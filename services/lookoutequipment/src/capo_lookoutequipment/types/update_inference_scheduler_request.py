"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#UpdateInferenceSchedulerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.data_delay_offset_in_minutes
    import capo_lookoutequipment.types.data_upload_frequency
    import capo_lookoutequipment.types.iam_role_arn
    import capo_lookoutequipment.types.inference_input_configuration
    import capo_lookoutequipment.types.inference_output_configuration
    import capo_lookoutequipment.types.inference_scheduler_identifier


class UpdateInferenceSchedulerRequest(TypedDict, closed=True):
    inference_scheduler_name: "capo_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier"
    """<p>The name of the inference scheduler to be updated. </p>"""
    data_delay_offset_in_minutes: NotRequired[
        "capo_lookoutequipment.types.data_delay_offset_in_minutes.DataDelayOffsetInMinutes"
    ]
    """<p> A period of time (in minutes) by which inference on the data is delayed after the data starts. For instance, if you select an offset delay time of five minutes, inference will not begin on the data until the first data measurement after the five minute mark. For example, if five minutes is selected, the inference scheduler will wake up at the configured frequency with the additional five minute delay time to check the customer S3 bucket. The customer can upload data at the same frequency and they don't need to stop and restart the scheduler when uploading new data.</p>"""
    data_upload_frequency: NotRequired[
        "capo_lookoutequipment.types.data_upload_frequency.DataUploadFrequency"
    ]
    """<p>How often data is uploaded to the source S3 bucket for the input data. The value chosen is the length of time between data uploads. For instance, if you select 5 minutes, Amazon Lookout for Equipment will upload the real-time data to the source bucket once every 5 minutes. This frequency also determines how often Amazon Lookout for Equipment starts a scheduled inference on your data. In this example, it starts once every 5 minutes. </p>"""
    data_input_configuration: NotRequired[
        "capo_lookoutequipment.types.inference_input_configuration.InferenceInputConfiguration"
    ]
    """<p> Specifies information for the input data for the inference scheduler, including delimiter, format, and dataset location. </p>"""
    data_output_configuration: NotRequired[
        "capo_lookoutequipment.types.inference_output_configuration.InferenceOutputConfiguration"
    ]
    """<p> Specifies information for the output results from the inference scheduler, including the output S3 location. </p>"""
    role_arn: NotRequired["capo_lookoutequipment.types.iam_role_arn.IamRoleArn"]
    """<p> The Amazon Resource Name (ARN) of a role with permission to access the data source for the inference scheduler. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateInferenceSchedulerRequest) -> dict:
    out: dict = {}
    out["InferenceSchedulerName"] = value["inference_scheduler_name"]
    if "data_delay_offset_in_minutes" in value:
        out["DataDelayOffsetInMinutes"] = value["data_delay_offset_in_minutes"]
    if "data_upload_frequency" in value:
        import capo_lookoutequipment.types.data_upload_frequency

        out["DataUploadFrequency"] = (
            capo_lookoutequipment.types.data_upload_frequency.serialize_aws_json_1_0(
                value["data_upload_frequency"]
            )
        )
    if "data_input_configuration" in value:
        import capo_lookoutequipment.types.inference_input_configuration

        out["DataInputConfiguration"] = (
            capo_lookoutequipment.types.inference_input_configuration.serialize_aws_json_1_0(
                value["data_input_configuration"]
            )
        )
    if "data_output_configuration" in value:
        import capo_lookoutequipment.types.inference_output_configuration

        out["DataOutputConfiguration"] = (
            capo_lookoutequipment.types.inference_output_configuration.serialize_aws_json_1_0(
                value["data_output_configuration"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateInferenceSchedulerRequest:
    out: UpdateInferenceSchedulerRequest = {}  # type: ignore[typeddict-item]
    if data.get("InferenceSchedulerName") is not None:
        out["inference_scheduler_name"] = data["InferenceSchedulerName"]
    else:
        out["inference_scheduler_name"] = ""
    if data.get("DataDelayOffsetInMinutes") is not None:
        out["data_delay_offset_in_minutes"] = data["DataDelayOffsetInMinutes"]
    if data.get("DataUploadFrequency") is not None:
        import capo_lookoutequipment.types.data_upload_frequency

        out["data_upload_frequency"] = (
            capo_lookoutequipment.types.data_upload_frequency.deserialize_aws_json_1_0(
                data["DataUploadFrequency"]
            )
        )
    if data.get("DataInputConfiguration") is not None:
        import capo_lookoutequipment.types.inference_input_configuration

        out["data_input_configuration"] = (
            capo_lookoutequipment.types.inference_input_configuration.deserialize_aws_json_1_0(
                data["DataInputConfiguration"]
            )
        )
    if data.get("DataOutputConfiguration") is not None:
        import capo_lookoutequipment.types.inference_output_configuration

        out["data_output_configuration"] = (
            capo_lookoutequipment.types.inference_output_configuration.deserialize_aws_json_1_0(
                data["DataOutputConfiguration"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    return out
