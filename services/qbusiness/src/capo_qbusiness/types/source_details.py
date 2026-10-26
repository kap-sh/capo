"""Generated from Smithy shape ``com.amazonaws.qbusiness#SourceDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError
from capo_qbusiness.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qbusiness.types.audio_source_details
    import capo_qbusiness.types.image_source_details
    import capo_qbusiness.types.video_source_details


class _SourceDetails_imageSourceDetails(TypedDict, closed=True):
    imageSourceDetails: "capo_qbusiness.types.image_source_details.ImageSourceDetails"


class _SourceDetails_audioSourceDetails(TypedDict, closed=True):
    audioSourceDetails: "capo_qbusiness.types.audio_source_details.AudioSourceDetails"


class _SourceDetails_videoSourceDetails(TypedDict, closed=True):
    videoSourceDetails: "capo_qbusiness.types.video_source_details.VideoSourceDetails"


SourceDetails: TypeAlias = (
    _SourceDetails_imageSourceDetails
    | _SourceDetails_audioSourceDetails
    | _SourceDetails_videoSourceDetails
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SourceDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SourceDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "imageSourceDetails" in value:
        import capo_qbusiness.types.image_source_details

        return {
            "imageSourceDetails": capo_qbusiness.types.image_source_details.serialize_json(
                value["imageSourceDetails"]
            )
        }
    elif "audioSourceDetails" in value:
        import capo_qbusiness.types.audio_source_details

        return {
            "audioSourceDetails": capo_qbusiness.types.audio_source_details.serialize_json(
                value["audioSourceDetails"]
            )
        }
    elif "videoSourceDetails" in value:
        import capo_qbusiness.types.video_source_details

        return {
            "videoSourceDetails": capo_qbusiness.types.video_source_details.serialize_json(
                value["videoSourceDetails"]
            )
        }
    else:
        raise SerializationError("SourceDetails: no variant present")


def deserialize_json(data: dict) -> SourceDetails:
    if data.get("imageSourceDetails") is not None:
        import capo_qbusiness.types.image_source_details

        return {
            "imageSourceDetails": capo_qbusiness.types.image_source_details.deserialize_json(
                data["imageSourceDetails"]
            )
        }
    elif data.get("audioSourceDetails") is not None:
        import capo_qbusiness.types.audio_source_details

        return {
            "audioSourceDetails": capo_qbusiness.types.audio_source_details.deserialize_json(
                data["audioSourceDetails"]
            )
        }
    elif data.get("videoSourceDetails") is not None:
        import capo_qbusiness.types.video_source_details

        return {
            "videoSourceDetails": capo_qbusiness.types.video_source_details.deserialize_json(
                data["videoSourceDetails"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SourceDetails: no recognized variant key")
