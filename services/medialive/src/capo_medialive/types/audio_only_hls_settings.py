"""Generated from Smithy shape ``com.amazonaws.medialive#AudioOnlyHlsSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.audio_only_hls_segment_type
    import capo_medialive.types.audio_only_hls_track_type
    import capo_medialive.types.input_location


class AudioOnlyHlsSettings(TypedDict, closed=True):
    audio_group_id: NotRequired["capo_medialive.types.__string.__string"]
    """Specifies the group to which the audio Rendition belongs."""
    audio_only_image: NotRequired["capo_medialive.types.input_location.InputLocation"]
    """Optional. Specifies the .jpg or .png image to use as the cover art for an audio-only output. We recommend a low bit-size file because the image increases the output audio bandwidth. The image is attached to the audio as an ID3 tag, frame type APIC, picture type 0x10, as per the "ID3 tag version 2.4.0 - Native Frames" standard."""
    audio_track_type: NotRequired[
        "capo_medialive.types.audio_only_hls_track_type.AudioOnlyHlsTrackType"
    ]
    """Four types of audio-only tracks are supported: Audio-Only Variant Stream The client can play back this audio-only stream instead of video in low-bandwidth scenarios. Represented as an EXT-X-STREAM-INF in the HLS manifest. Alternate Audio, Auto Select, Default Alternate rendition that the client should try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=YES, AUTOSELECT=YES Alternate Audio, Auto Select, Not Default Alternate rendition that the client may try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=YES Alternate Audio, not Auto Select Alternate rendition that the client will not try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=NO"""
    segment_type: NotRequired[
        "capo_medialive.types.audio_only_hls_segment_type.AudioOnlyHlsSegmentType"
    ]
    """Specifies the segment type."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioOnlyHlsSettings) -> dict:
    out: dict = {}
    if "audio_group_id" in value:
        out["audioGroupId"] = value["audio_group_id"]
    if "audio_only_image" in value:
        import capo_medialive.types.input_location

        out["audioOnlyImage"] = capo_medialive.types.input_location.serialize_json(
            value["audio_only_image"]
        )
    if "audio_track_type" in value:
        import capo_medialive.types.audio_only_hls_track_type

        out["audioTrackType"] = (
            capo_medialive.types.audio_only_hls_track_type.serialize_json(
                value["audio_track_type"]
            )
        )
    if "segment_type" in value:
        import capo_medialive.types.audio_only_hls_segment_type

        out["segmentType"] = (
            capo_medialive.types.audio_only_hls_segment_type.serialize_json(
                value["segment_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioOnlyHlsSettings:
    out: AudioOnlyHlsSettings = {}  # type: ignore[typeddict-item]
    if data.get("audioGroupId") is not None:
        out["audio_group_id"] = data["audioGroupId"]
    if data.get("audioOnlyImage") is not None:
        import capo_medialive.types.input_location

        out["audio_only_image"] = capo_medialive.types.input_location.deserialize_json(
            data["audioOnlyImage"]
        )
    if data.get("audioTrackType") is not None:
        import capo_medialive.types.audio_only_hls_track_type

        out["audio_track_type"] = (
            capo_medialive.types.audio_only_hls_track_type.deserialize_json(
                data["audioTrackType"]
            )
        )
    if data.get("segmentType") is not None:
        import capo_medialive.types.audio_only_hls_segment_type

        out["segment_type"] = (
            capo_medialive.types.audio_only_hls_segment_type.deserialize_json(
                data["segmentType"]
            )
        )
    return out
