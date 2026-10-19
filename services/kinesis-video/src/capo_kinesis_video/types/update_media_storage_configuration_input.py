"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#UpdateMediaStorageConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_video.types.media_storage_configuration
    import capo_kinesis_video.types.resource_arn


class UpdateMediaStorageConfigurationInput(TypedDict, closed=True):
    channel_arn: "capo_kinesis_video.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the channel.</p>"""
    media_storage_configuration: (
        "capo_kinesis_video.types.media_storage_configuration.MediaStorageConfiguration"
    )
    """<p>A structure that encapsulates, or contains, the media storage configuration properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMediaStorageConfigurationInput) -> dict:
    out: dict = {}
    out["ChannelARN"] = value["channel_arn"]
    import capo_kinesis_video.types.media_storage_configuration

    out["MediaStorageConfiguration"] = (
        capo_kinesis_video.types.media_storage_configuration.serialize_json(
            value["media_storage_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateMediaStorageConfigurationInput:
    out: UpdateMediaStorageConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("ChannelARN") is not None:
        out["channel_arn"] = data["ChannelARN"]
    else:
        out["channel_arn"] = ""
    if data.get("MediaStorageConfiguration") is not None:
        import capo_kinesis_video.types.media_storage_configuration

        out["media_storage_configuration"] = (
            capo_kinesis_video.types.media_storage_configuration.deserialize_json(
                data["MediaStorageConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateMediaStorageConfigurationInput.media_storage_configuration required"
        )
    return out
