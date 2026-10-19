"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#UpdateStreamStorageConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_video.types.resource_arn
    import capo_kinesis_video.types.stream_name
    import capo_kinesis_video.types.stream_storage_configuration
    import capo_kinesis_video.types.version


class UpdateStreamStorageConfigurationInput(TypedDict, closed=True):
    stream_name: NotRequired["capo_kinesis_video.types.stream_name.StreamName"]
    """<p>The name of the stream for which you want to update the storage configuration.</p>"""
    stream_arn: NotRequired["capo_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the stream for which you want to update the storage configuration.</p>"""
    current_version: "capo_kinesis_video.types.version.Version"
    """<p>The version of the stream whose storage configuration you want to change. To get the version, call either the <code>DescribeStream</code> or the <code>ListStreams</code> API.</p>"""
    stream_storage_configuration: "capo_kinesis_video.types.stream_storage_configuration.StreamStorageConfiguration"
    """<p>The new storage configuration for the stream. This includes the default storage tier that determines how stream data is stored and accessed.</p> <p>Different storage tiers offer varying levels of performance and cost optimization to match your specific use case requirements.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateStreamStorageConfigurationInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    out["CurrentVersion"] = value["current_version"]
    import capo_kinesis_video.types.stream_storage_configuration

    out["StreamStorageConfiguration"] = (
        capo_kinesis_video.types.stream_storage_configuration.serialize_json(
            value["stream_storage_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateStreamStorageConfigurationInput:
    out: UpdateStreamStorageConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamName") is not None:
        out["stream_name"] = data["StreamName"]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    if data.get("CurrentVersion") is not None:
        out["current_version"] = data["CurrentVersion"]
    else:
        out["current_version"] = ""
    if data.get("StreamStorageConfiguration") is not None:
        import capo_kinesis_video.types.stream_storage_configuration

        out["stream_storage_configuration"] = (
            capo_kinesis_video.types.stream_storage_configuration.deserialize_json(
                data["StreamStorageConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateStreamStorageConfigurationInput.stream_storage_configuration required"
        )
    return out
