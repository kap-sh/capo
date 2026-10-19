"""Generated from Smithy shape ``com.amazonaws.rekognition#CreateStreamProcessorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.kms_key_id
    import capo_rekognition.types.regions_of_interest
    import capo_rekognition.types.role_arn
    import capo_rekognition.types.stream_processor_data_sharing_preference
    import capo_rekognition.types.stream_processor_input
    import capo_rekognition.types.stream_processor_name
    import capo_rekognition.types.stream_processor_notification_channel
    import capo_rekognition.types.stream_processor_output
    import capo_rekognition.types.stream_processor_settings
    import capo_rekognition.types.tag_map


class CreateStreamProcessorRequest(TypedDict, closed=True):
    input: "capo_rekognition.types.stream_processor_input.StreamProcessorInput"
    """<p>Kinesis video stream stream that provides the source streaming video. If you are using the AWS CLI, the parameter name is <code>StreamProcessorInput</code>. This is required for both face search and label detection stream processors.</p>"""
    output: "capo_rekognition.types.stream_processor_output.StreamProcessorOutput"
    """<p>Kinesis data stream stream or Amazon S3 bucket location to which Amazon Rekognition Video puts the analysis results. If you are using the AWS CLI, the parameter name is <code>StreamProcessorOutput</code>. This must be a <a>S3Destination</a> of an Amazon S3 bucket that you own for a label detection stream processor or a Kinesis data stream ARN for a face search stream processor.</p>"""
    name: "capo_rekognition.types.stream_processor_name.StreamProcessorName"
    """<p>An identifier you assign to the stream processor. You can use <code>Name</code> to manage the stream processor. For example, you can get the current status of the stream processor by calling <a>DescribeStreamProcessor</a>. <code>Name</code> is idempotent. This is required for both face search and label detection stream processors. </p>"""
    settings: "capo_rekognition.types.stream_processor_settings.StreamProcessorSettings"
    """<p>Input parameters used in a streaming video analyzed by a stream processor. You can use <code>FaceSearch</code> to recognize faces in a streaming video, or you can use <code>ConnectedHome</code> to detect labels.</p>"""
    role_arn: "capo_rekognition.types.role_arn.RoleArn"
    """<p>The Amazon Resource Number (ARN) of the IAM role that allows access to the stream processor. The IAM role provides Rekognition read permissions for a Kinesis stream. It also provides write permissions to an Amazon S3 bucket and Amazon Simple Notification Service topic for a label detection stream processor. This is required for both face search and label detection stream processors.</p>"""
    tags: NotRequired["capo_rekognition.types.tag_map.TagMap"]
    """<p> A set of tags (key-value pairs) that you want to attach to the stream processor. </p>"""
    notification_channel: NotRequired[
        "capo_rekognition.types.stream_processor_notification_channel.StreamProcessorNotificationChannel"
    ]
    kms_key_id: NotRequired["capo_rekognition.types.kms_key_id.KmsKeyId"]
    """<p> The identifier for your AWS Key Management Service key (AWS KMS key). This is an optional parameter for label detection stream processors and should not be used to create a face search stream processor. You can supply the Amazon Resource Name (ARN) of your KMS key, the ID of your KMS key, an alias for your KMS key, or an alias ARN. The key is used to encrypt results and data published to your Amazon S3 bucket, which includes image frames and hero images. Your source images are unaffected. </p> <p> </p>"""
    regions_of_interest: NotRequired[
        "capo_rekognition.types.regions_of_interest.RegionsOfInterest"
    ]
    """<p> Specifies locations in the frames where Amazon Rekognition checks for objects or people. You can specify up to 10 regions of interest, and each region has either a polygon or a bounding box. This is an optional parameter for label detection stream processors and should not be used to create a face search stream processor. </p>"""
    data_sharing_preference: NotRequired[
        "capo_rekognition.types.stream_processor_data_sharing_preference.StreamProcessorDataSharingPreference"
    ]
    """<p> Shows whether you are sharing data with Rekognition to improve model performance. You can choose this option at the account level or on a per-stream basis. Note that if you opt out at the account level this setting is ignored on individual streams. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateStreamProcessorRequest) -> dict:
    out: dict = {}
    import capo_rekognition.types.stream_processor_input

    out["Input"] = capo_rekognition.types.stream_processor_input.serialize_aws_json_1_1(
        value["input"]
    )
    import capo_rekognition.types.stream_processor_output

    out["Output"] = (
        capo_rekognition.types.stream_processor_output.serialize_aws_json_1_1(
            value["output"]
        )
    )
    out["Name"] = value["name"]
    import capo_rekognition.types.stream_processor_settings

    out["Settings"] = (
        capo_rekognition.types.stream_processor_settings.serialize_aws_json_1_1(
            value["settings"]
        )
    )
    out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_rekognition.types.tag_map

        out["Tags"] = capo_rekognition.types.tag_map.serialize_aws_json_1_1(
            value["tags"]
        )
    if "notification_channel" in value:
        import capo_rekognition.types.stream_processor_notification_channel

        out["NotificationChannel"] = (
            capo_rekognition.types.stream_processor_notification_channel.serialize_aws_json_1_1(
                value["notification_channel"]
            )
        )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "regions_of_interest" in value:
        import capo_rekognition.types.regions_of_interest

        out["RegionsOfInterest"] = (
            capo_rekognition.types.regions_of_interest.serialize_aws_json_1_1(
                value["regions_of_interest"]
            )
        )
    if "data_sharing_preference" in value:
        import capo_rekognition.types.stream_processor_data_sharing_preference

        out["DataSharingPreference"] = (
            capo_rekognition.types.stream_processor_data_sharing_preference.serialize_aws_json_1_1(
                value["data_sharing_preference"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateStreamProcessorRequest:
    out: CreateStreamProcessorRequest = {}  # type: ignore[typeddict-item]
    if data.get("Input") is not None:
        import capo_rekognition.types.stream_processor_input

        out["input"] = (
            capo_rekognition.types.stream_processor_input.deserialize_aws_json_1_1(
                data["Input"]
            )
        )
    else:
        raise DeserializationError("CreateStreamProcessorRequest.input required")
    if data.get("Output") is not None:
        import capo_rekognition.types.stream_processor_output

        out["output"] = (
            capo_rekognition.types.stream_processor_output.deserialize_aws_json_1_1(
                data["Output"]
            )
        )
    else:
        raise DeserializationError("CreateStreamProcessorRequest.output required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Settings") is not None:
        import capo_rekognition.types.stream_processor_settings

        out["settings"] = (
            capo_rekognition.types.stream_processor_settings.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    else:
        raise DeserializationError("CreateStreamProcessorRequest.settings required")
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    if data.get("Tags") is not None:
        import capo_rekognition.types.tag_map

        out["tags"] = capo_rekognition.types.tag_map.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("NotificationChannel") is not None:
        import capo_rekognition.types.stream_processor_notification_channel

        out["notification_channel"] = (
            capo_rekognition.types.stream_processor_notification_channel.deserialize_aws_json_1_1(
                data["NotificationChannel"]
            )
        )
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("RegionsOfInterest") is not None:
        import capo_rekognition.types.regions_of_interest

        out["regions_of_interest"] = (
            capo_rekognition.types.regions_of_interest.deserialize_aws_json_1_1(
                data["RegionsOfInterest"]
            )
        )
    if data.get("DataSharingPreference") is not None:
        import capo_rekognition.types.stream_processor_data_sharing_preference

        out["data_sharing_preference"] = (
            capo_rekognition.types.stream_processor_data_sharing_preference.deserialize_aws_json_1_1(
                data["DataSharingPreference"]
            )
        )
    return out
