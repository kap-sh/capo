"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#MediaStorageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.media_storage_configuration_status
    import capo_kinesis_video.types.resource_arn


class MediaStorageConfiguration(TypedDict, closed=True):
    stream_arn: NotRequired["capo_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the stream. </p>"""
    status: "capo_kinesis_video.types.media_storage_configuration_status.MediaStorageConfigurationStatus"
    """<p>The status of the media storage configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaStorageConfiguration) -> dict:
    out: dict = {}
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    import capo_kinesis_video.types.media_storage_configuration_status

    out["Status"] = (
        capo_kinesis_video.types.media_storage_configuration_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> MediaStorageConfiguration:
    out: MediaStorageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    if data.get("Status") is not None:
        import capo_kinesis_video.types.media_storage_configuration_status

        out["status"] = (
            capo_kinesis_video.types.media_storage_configuration_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_kinesis_video.types.media_storage_configuration_status.MediaStorageConfigurationStatus",
            "",
        )
    return out
