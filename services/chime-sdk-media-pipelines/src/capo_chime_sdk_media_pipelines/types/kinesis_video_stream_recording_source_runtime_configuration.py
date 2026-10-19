"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#KinesisVideoStreamRecordingSourceRuntimeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.fragment_selector
    import capo_chime_sdk_media_pipelines.types.recording_stream_list


class KinesisVideoStreamRecordingSourceRuntimeConfiguration(TypedDict, closed=True):
    streams: (
        "capo_chime_sdk_media_pipelines.types.recording_stream_list.RecordingStreamList"
    )
    """<p>The stream or streams to be recorded.</p>"""
    fragment_selector: (
        "capo_chime_sdk_media_pipelines.types.fragment_selector.FragmentSelector"
    )
    """<p>Describes the timestamp range and timestamp origin of a range of fragments in the Kinesis video stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: KinesisVideoStreamRecordingSourceRuntimeConfiguration,
) -> dict:
    out: dict = {}
    import capo_chime_sdk_media_pipelines.types.recording_stream_list

    out["Streams"] = (
        capo_chime_sdk_media_pipelines.types.recording_stream_list.serialize_json(
            value["streams"]
        )
    )
    import capo_chime_sdk_media_pipelines.types.fragment_selector

    out["FragmentSelector"] = (
        capo_chime_sdk_media_pipelines.types.fragment_selector.serialize_json(
            value["fragment_selector"]
        )
    )
    return out


def deserialize_json(
    data: dict,
) -> KinesisVideoStreamRecordingSourceRuntimeConfiguration:
    out: KinesisVideoStreamRecordingSourceRuntimeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Streams") is not None:
        import capo_chime_sdk_media_pipelines.types.recording_stream_list

        out["streams"] = (
            capo_chime_sdk_media_pipelines.types.recording_stream_list.deserialize_json(
                data["Streams"]
            )
        )
    else:
        out["streams"] = []
    if data.get("FragmentSelector") is not None:
        import capo_chime_sdk_media_pipelines.types.fragment_selector

        out["fragment_selector"] = (
            capo_chime_sdk_media_pipelines.types.fragment_selector.deserialize_json(
                data["FragmentSelector"]
            )
        )
    else:
        raise DeserializationError(
            "KinesisVideoStreamRecordingSourceRuntimeConfiguration.fragment_selector required"
        )
    return out
