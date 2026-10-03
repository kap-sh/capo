"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#CreateStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_video.types.data_retention_in_hours
    import capo_kinesis_video.types.device_name
    import capo_kinesis_video.types.kms_key_id
    import capo_kinesis_video.types.media_type
    import capo_kinesis_video.types.resource_tags
    import capo_kinesis_video.types.stream_name
    import capo_kinesis_video.types.stream_storage_configuration


class CreateStreamInput(TypedDict, closed=True):
    device_name: NotRequired["capo_kinesis_video.types.device_name.DeviceName"]
    """<p>The name of the device that is writing to the stream. </p> <note> <p>In the current implementation, Kinesis Video Streams doesn't use this name.</p> </note>"""
    stream_name: "capo_kinesis_video.types.stream_name.StreamName"
    """<p>A name for the stream that you are creating.</p> <p>The stream name is an identifier for the stream, and must be unique for each account and region.</p>"""
    media_type: NotRequired["capo_kinesis_video.types.media_type.MediaType"]
    """<p>The media type of the stream. Consumers of the stream can use this information when processing the stream. For more information about media types, see <a href="http://www.iana.org/assignments/media-types/media-types.xhtml">Media Types</a>. If you choose to specify the <code>MediaType</code>, see <a href="https://tools.ietf.org/html/rfc6838#section-4.2">Naming Requirements</a> for guidelines.</p> <p>Example valid values include "video/h264" and "video/h264,audio/aac".</p> <p>This parameter is optional; the default value is <code>null</code> (or empty in JSON).</p>"""
    kms_key_id: NotRequired["capo_kinesis_video.types.kms_key_id.KmsKeyId"]
    """<p>The ID of the Key Management Service (KMS) key that you want Kinesis Video Streams to use to encrypt stream data.</p> <p>If no key ID is specified, the default, Kinesis Video-managed key (<code>aws/kinesisvideo</code>) is used.</p> <p> For more information, see <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters">DescribeKey</a>. </p>"""
    data_retention_in_hours: NotRequired[
        "capo_kinesis_video.types.data_retention_in_hours.DataRetentionInHours"
    ]
    """<p>The number of hours that you want to retain the data in the stream. Kinesis Video Streams retains the data in a data store that is associated with the stream.</p> <p>The default value is 0, indicating that the stream does not persist data. The minimum is 1 hour.</p> <p>When the <code>DataRetentionInHours</code> value is 0, consumers can still consume the fragments that remain in the service host buffer, which has a retention time limit of 5 minutes and a retention memory limit of 200 MB. Fragments are removed from the buffer when either limit is reached.</p>"""
    tags: NotRequired["capo_kinesis_video.types.resource_tags.ResourceTags"]
    """<p>A list of tags to associate with the specified stream. Each tag is a key-value pair (the value is optional).</p>"""
    stream_storage_configuration: NotRequired[
        "capo_kinesis_video.types.stream_storage_configuration.StreamStorageConfiguration"
    ]
    """<p>The configuration for the stream's storage, including the default storage tier for stream data. This configuration determines how stream data is stored and accessed, with different tiers offering varying levels of performance and cost optimization.</p> <p>If not specified, the stream will use the default storage configuration with HOT tier for optimal performance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateStreamInput) -> dict:
    out: dict = {}
    if "device_name" in value:
        out["DeviceName"] = value["device_name"]
    out["StreamName"] = value["stream_name"]
    if "media_type" in value:
        out["MediaType"] = value["media_type"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "data_retention_in_hours" in value:
        out["DataRetentionInHours"] = value["data_retention_in_hours"]
    if "tags" in value:
        import capo_kinesis_video.types.resource_tags

        out["Tags"] = capo_kinesis_video.types.resource_tags.serialize_json(
            value["tags"]
        )
    if "stream_storage_configuration" in value:
        import capo_kinesis_video.types.stream_storage_configuration

        out["StreamStorageConfiguration"] = (
            capo_kinesis_video.types.stream_storage_configuration.serialize_json(
                value["stream_storage_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateStreamInput:
    out: CreateStreamInput = {}  # type: ignore[typeddict-item]
    if data.get("DeviceName") is not None:
        out["device_name"] = data["DeviceName"]
    if data.get("StreamName") is not None:
        out["stream_name"] = data["StreamName"]
    else:
        raise DeserializationError("CreateStreamInput.stream_name required")
    if data.get("MediaType") is not None:
        out["media_type"] = data["MediaType"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("DataRetentionInHours") is not None:
        out["data_retention_in_hours"] = data["DataRetentionInHours"]
    if data.get("Tags") is not None:
        import capo_kinesis_video.types.resource_tags

        out["tags"] = capo_kinesis_video.types.resource_tags.deserialize_json(
            data["Tags"]
        )
    if data.get("StreamStorageConfiguration") is not None:
        import capo_kinesis_video.types.stream_storage_configuration

        out["stream_storage_configuration"] = (
            capo_kinesis_video.types.stream_storage_configuration.deserialize_json(
                data["StreamStorageConfiguration"]
            )
        )
    return out
