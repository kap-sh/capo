"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string
    import capo_mediaconvert.types.hls_audio_only_container
    import capo_mediaconvert.types.hls_audio_track_type
    import capo_mediaconvert.types.hls_descriptive_video_service_flag
    import capo_mediaconvert.types.hls_i_frame_only_manifest


class HlsSettings(TypedDict, closed=True):
    audio_group_id: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Specifies the group to which the audio rendition belongs."""
    audio_only_container: NotRequired[
        "capo_mediaconvert.types.hls_audio_only_container.HlsAudioOnlyContainer"
    ]
    """Use this setting only in audio-only outputs. Choose MPEG-2 Transport Stream (M2TS) to create a file in an MPEG2-TS container. Keep the default value Automatic to create an audio-only file in a raw container. Regardless of the value that you specify here, if this output has video, the service will place the output into an MPEG2-TS container."""
    audio_rendition_sets: NotRequired["capo_mediaconvert.types.__string.__string"]
    """List all the audio groups that are used with the video output stream. Input all the audio GROUP-IDs that are associated to the video, separate by ','."""
    audio_track_type: NotRequired[
        "capo_mediaconvert.types.hls_audio_track_type.HlsAudioTrackType"
    ]
    """Four types of audio-only tracks are supported: Audio-Only Variant Stream The client can play back this audio-only stream instead of video in low-bandwidth scenarios. Represented as an EXT-X-STREAM-INF in the HLS manifest. Alternate Audio, Auto Select, Default Alternate rendition that the client should try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=YES, AUTOSELECT=YES Alternate Audio, Auto Select, Not Default Alternate rendition that the client may try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=YES Alternate Audio, not Auto Select Alternate rendition that the client will not try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=NO"""
    descriptive_video_service_flag: NotRequired[
        "capo_mediaconvert.types.hls_descriptive_video_service_flag.HlsDescriptiveVideoServiceFlag"
    ]
    """Specify whether to flag this audio track as descriptive video service (DVS) in your HLS parent manifest. When you choose Flag, MediaConvert includes the parameter CHARACTERISTICS="public.accessibility.describes-video" in the EXT-X-MEDIA entry for this track. When you keep the default choice, Don't flag, MediaConvert leaves this parameter out. The DVS flag can help with accessibility on Apple devices. For more information, see the Apple documentation."""
    i_frame_only_manifest: NotRequired[
        "capo_mediaconvert.types.hls_i_frame_only_manifest.HlsIFrameOnlyManifest"
    ]
    """Generate a variant manifest that lists only the I-frames for this rendition. You might use this manifest as part of a workflow that creates preview functions for your video. MediaConvert adds both the I-frame only variant manifest and the regular variant manifest to the multivariant manifest. To have MediaConvert write a variant manifest that references I-frames from your output content using EXT-X-BYTERANGE tags: Choose Include. To have MediaConvert output I-frames as single frame TS files and a corresponding variant manifest that references them: Choose Include as TS. When you don't need the I-frame only variant manifest: Keep the default value, Exclude."""
    segment_modifier: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Use this setting to add an identifying string to the filename of each segment. The service adds this string between the name modifier and segment index number. You can use format identifiers in the string. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/using-variables-in-your-job-settings.html"""


# --- restJson1 ser/de ---
def serialize_json(value: HlsSettings) -> dict:
    out: dict = {}
    if "audio_group_id" in value:
        out["audioGroupId"] = value["audio_group_id"]
    if "audio_only_container" in value:
        import capo_mediaconvert.types.hls_audio_only_container

        out["audioOnlyContainer"] = (
            capo_mediaconvert.types.hls_audio_only_container.serialize_json(
                value["audio_only_container"]
            )
        )
    if "audio_rendition_sets" in value:
        out["audioRenditionSets"] = value["audio_rendition_sets"]
    if "audio_track_type" in value:
        import capo_mediaconvert.types.hls_audio_track_type

        out["audioTrackType"] = (
            capo_mediaconvert.types.hls_audio_track_type.serialize_json(
                value["audio_track_type"]
            )
        )
    if "descriptive_video_service_flag" in value:
        import capo_mediaconvert.types.hls_descriptive_video_service_flag

        out["descriptiveVideoServiceFlag"] = (
            capo_mediaconvert.types.hls_descriptive_video_service_flag.serialize_json(
                value["descriptive_video_service_flag"]
            )
        )
    if "i_frame_only_manifest" in value:
        import capo_mediaconvert.types.hls_i_frame_only_manifest

        out["iFrameOnlyManifest"] = (
            capo_mediaconvert.types.hls_i_frame_only_manifest.serialize_json(
                value["i_frame_only_manifest"]
            )
        )
    if "segment_modifier" in value:
        out["segmentModifier"] = value["segment_modifier"]
    return out


def deserialize_json(data: dict) -> HlsSettings:
    out: HlsSettings = {}  # type: ignore[typeddict-item]
    if data.get("audioGroupId") is not None:
        out["audio_group_id"] = data["audioGroupId"]
    if data.get("audioOnlyContainer") is not None:
        import capo_mediaconvert.types.hls_audio_only_container

        out["audio_only_container"] = (
            capo_mediaconvert.types.hls_audio_only_container.deserialize_json(
                data["audioOnlyContainer"]
            )
        )
    if data.get("audioRenditionSets") is not None:
        out["audio_rendition_sets"] = data["audioRenditionSets"]
    if data.get("audioTrackType") is not None:
        import capo_mediaconvert.types.hls_audio_track_type

        out["audio_track_type"] = (
            capo_mediaconvert.types.hls_audio_track_type.deserialize_json(
                data["audioTrackType"]
            )
        )
    if data.get("descriptiveVideoServiceFlag") is not None:
        import capo_mediaconvert.types.hls_descriptive_video_service_flag

        out["descriptive_video_service_flag"] = (
            capo_mediaconvert.types.hls_descriptive_video_service_flag.deserialize_json(
                data["descriptiveVideoServiceFlag"]
            )
        )
    if data.get("iFrameOnlyManifest") is not None:
        import capo_mediaconvert.types.hls_i_frame_only_manifest

        out["i_frame_only_manifest"] = (
            capo_mediaconvert.types.hls_i_frame_only_manifest.deserialize_json(
                data["iFrameOnlyManifest"]
            )
        )
    if data.get("segmentModifier") is not None:
        out["segment_modifier"] = data["segmentModifier"]
    return out
