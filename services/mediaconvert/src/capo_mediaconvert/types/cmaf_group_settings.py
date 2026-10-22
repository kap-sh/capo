"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmafGroupSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__double_min0_max2147483647
    import capo_mediaconvert.types.__integer_min0_max2147483647
    import capo_mediaconvert.types.__integer_min1_max2147483647
    import capo_mediaconvert.types.__list_of_cmaf_additional_manifest
    import capo_mediaconvert.types.__list_of_cmaf_image_based_trick_play_variant
    import capo_mediaconvert.types.__list_of_dash_adaptation_set_grouping
    import capo_mediaconvert.types.__string
    import capo_mediaconvert.types.__string_min1_max256
    import capo_mediaconvert.types.__string_pattern_s3
    import capo_mediaconvert.types.cmaf_client_cache
    import capo_mediaconvert.types.cmaf_codec_specification
    import capo_mediaconvert.types.cmaf_encryption_settings
    import capo_mediaconvert.types.cmaf_image_based_trick_play
    import capo_mediaconvert.types.cmaf_image_based_trick_play_settings
    import capo_mediaconvert.types.cmaf_manifest_compression
    import capo_mediaconvert.types.cmaf_manifest_duration_format
    import capo_mediaconvert.types.cmaf_mpd_manifest_bandwidth_type
    import capo_mediaconvert.types.cmaf_mpd_profile
    import capo_mediaconvert.types.cmaf_pts_offset_handling_for_b_frames
    import capo_mediaconvert.types.cmaf_segment_control
    import capo_mediaconvert.types.cmaf_segment_length_control
    import capo_mediaconvert.types.cmaf_stream_inf_resolution
    import capo_mediaconvert.types.cmaf_target_duration_compatibility_mode
    import capo_mediaconvert.types.cmaf_video_composition_offsets
    import capo_mediaconvert.types.cmaf_write_dash_manifest
    import capo_mediaconvert.types.cmaf_write_hls_manifest
    import capo_mediaconvert.types.cmaf_write_segment_timeline_in_representation
    import capo_mediaconvert.types.dash_manifest_style
    import capo_mediaconvert.types.destination_settings


class CmafGroupSettings(TypedDict, closed=True):
    additional_manifests: NotRequired[
        "capo_mediaconvert.types.__list_of_cmaf_additional_manifest.__listOfCmafAdditionalManifest"
    ]
    """By default, the service creates one top-level .m3u8 HLS manifest and one top -level .mpd DASH manifest for each CMAF output group in your job. These default manifests reference every output in the output group. To create additional top-level manifests that reference a subset of the outputs in the output group, specify a list of them here. For each additional manifest that you specify, the service creates one HLS manifest and one DASH manifest."""
    base_url: NotRequired["capo_mediaconvert.types.__string.__string"]
    """A partial URI prefix that will be put in the manifest file at the top level BaseURL element. Can be used if streams are delivered from a different URL than the manifest file."""
    client_cache: NotRequired[
        "capo_mediaconvert.types.cmaf_client_cache.CmafClientCache"
    ]
    """Disable this setting only when your workflow requires the #EXT-X-ALLOW-CACHE:no tag. Otherwise, keep the default value Enabled and control caching in your video distribution set up. For example, use the Cache-Control http header."""
    codec_specification: NotRequired[
        "capo_mediaconvert.types.cmaf_codec_specification.CmafCodecSpecification"
    ]
    """Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist generation."""
    dash_adaptation_set_grouping: NotRequired[
        "capo_mediaconvert.types.__list_of_dash_adaptation_set_grouping.__listOfDashAdaptationSetGrouping"
    ]
    """Specify additional criteria for partitioning video outputs into separate AdaptationSets. These criteria are applied on top of the grouping produced by DashManifestStyle."""
    dash_i_frame_trick_play_name_modifier: NotRequired[
        "capo_mediaconvert.types.__string_min1_max256.__stringMin1Max256"
    ]
    """Specify whether MediaConvert generates I-frame only video segments for DASH trick play, also known as trick mode. When specified, the I-frame only video segments are included within an additional AdaptationSet in your DASH output manifest. To generate I-frame only video segments: Enter a name as a text string, up to 256 character long. This name is appended to the end of this output group's base filename, that you specify as part of your destination URI, and used for the I-frame only video segment files. You may also include format identifiers. For more information, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/using-variables-in-your-job-settings.html#using-settings-variables-with-streaming-outputs To not generate I-frame only video segments: Leave blank."""
    dash_manifest_style: NotRequired[
        "capo_mediaconvert.types.dash_manifest_style.DashManifestStyle"
    ]
    """Specify how MediaConvert writes SegmentTimeline in your output DASH manifest. To write a SegmentTimeline for outputs that you also specify a Name modifier for: Keep the default value, Basic. Note that if you do not specify a name modifier for an output, MediaConvert will not write a SegmentTimeline for it. To write a common SegmentTimeline in the video AdaptationSet: Choose Compact. Note that MediaConvert will still write a SegmentTimeline in any Representation that does not share a common timeline. To write a video AdaptationSet for each different output framerate, and a common SegmentTimeline in each AdaptationSet: Choose Distinct. To write a SegmentTimeline in each AdaptationSet: Choose Full."""
    destination: NotRequired[
        "capo_mediaconvert.types.__string_pattern_s3.__stringPatternS3"
    ]
    """Use Destination to specify the S3 output location and the output filename base. Destination accepts format identifiers. If you do not specify the base filename in the URI, the service will use the filename of the input file. If your job has multiple inputs, the service uses the filename of the first input file."""
    destination_settings: NotRequired[
        "capo_mediaconvert.types.destination_settings.DestinationSettings"
    ]
    """Settings associated with the destination. Will vary based on the type of destination"""
    encryption: NotRequired[
        "capo_mediaconvert.types.cmaf_encryption_settings.CmafEncryptionSettings"
    ]
    """DRM settings."""
    fragment_length: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """Specify the length, in whole seconds, of the mp4 fragments. When you don't specify a value, MediaConvert defaults to 2. Related setting: Use Fragment length control to specify whether the encoder enforces this value strictly."""
    image_based_trick_play: NotRequired[
        "capo_mediaconvert.types.cmaf_image_based_trick_play.CmafImageBasedTrickPlay"
    ]
    """Specify whether MediaConvert generates images for trick play. Keep the default value, None, to not generate any images. Choose Thumbnail to generate tiled thumbnails. Choose Thumbnail and full frame to generate tiled thumbnails and full-resolution images of single frames. Choose Advanced to customize thumbnail and tile settings for a single trick play variant. Choose Variants to specify multiple trick play variants, each with its own thumbnail and tile settings. When you enable Write HLS manifest, MediaConvert creates a child manifest for each set of images that you generate and adds corresponding entries to the parent manifest. When you enable Write DASH manifest, MediaConvert adds an entry in the .mpd manifest for each set of images that you generate. A common application for these images is Roku trick mode. The thumbnails and full-frame images that MediaConvert creates with this feature are compatible with this Roku specification: https://developer.roku.com/docs/developer-program/media-playback/trick-mode/hls-and-dash.md"""
    image_based_trick_play_settings: NotRequired[
        "capo_mediaconvert.types.cmaf_image_based_trick_play_settings.CmafImageBasedTrickPlaySettings"
    ]
    """Tile and thumbnail settings applicable when imageBasedTrickPlay is ADVANCED"""
    image_based_trick_play_variants: NotRequired[
        "capo_mediaconvert.types.__list_of_cmaf_image_based_trick_play_variant.__listOfCmafImageBasedTrickPlayVariant"
    ]
    """Specify multiple image-based trick play variants. Each entry creates a separate set of JPEG tile images with its own resolution, tile layout, and cadence settings. Set imageBasedTrickPlay to VARIANTS when using this setting."""
    manifest_compression: NotRequired[
        "capo_mediaconvert.types.cmaf_manifest_compression.CmafManifestCompression"
    ]
    """When set to GZIP, compresses HLS playlist."""
    manifest_duration_format: NotRequired[
        "capo_mediaconvert.types.cmaf_manifest_duration_format.CmafManifestDurationFormat"
    ]
    """Indicates whether the output manifest should use floating point values for segment duration."""
    min_buffer_time: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Minimum time of initially buffered media that is needed to ensure smooth playout."""
    min_final_segment_length: NotRequired[
        "capo_mediaconvert.types.__double_min0_max2147483647.__doubleMin0Max2147483647"
    ]
    """Keep this setting at the default value of 0, unless you are troubleshooting a problem with how devices play back the end of your video asset. If you know that player devices are hanging on the final segment of your video because the length of your final segment is too short, use this setting to specify a minimum final segment length, in seconds. Choose a value that is greater than or equal to 1 and less than your segment length. When you specify a value for this setting, the encoder will combine any final segment that is shorter than the length that you specify with the previous segment. For example, your segment length is 3 seconds and your final segment is .5 seconds without a minimum final segment length; when you set the minimum final segment length to 1, your final segment is 3.5 seconds."""
    mpd_manifest_bandwidth_type: NotRequired[
        "capo_mediaconvert.types.cmaf_mpd_manifest_bandwidth_type.CmafMpdManifestBandwidthType"
    ]
    """Specify how the value for bandwidth is determined for each video Representation in your output MPD manifest. We recommend that you choose a MPD manifest bandwidth type that is compatible with your downstream player configuration. Max: Use the same value that you specify for Max bitrate in the video output, in bits per second. Average: Use the calculated average bitrate of the encoded video output, in bits per second."""
    mpd_profile: NotRequired["capo_mediaconvert.types.cmaf_mpd_profile.CmafMpdProfile"]
    """Specify whether your DASH profile is on-demand or main. When you choose Main profile, the service signals urn:mpeg:dash:profile:isoff-main:2011 in your .mpd DASH manifest. When you choose On-demand, the service signals urn:mpeg:dash:profile:isoff-on-demand:2011 in your .mpd. When you choose On-demand, you must also set the output group setting Segment control to Single file."""
    pts_offset_handling_for_b_frames: NotRequired[
        "capo_mediaconvert.types.cmaf_pts_offset_handling_for_b_frames.CmafPtsOffsetHandlingForBFrames"
    ]
    """Use this setting only when your output video stream has B-frames, which causes the initial presentation time stamp (PTS) to be offset from the initial decode time stamp (DTS). Specify how MediaConvert handles PTS when writing time stamps in output DASH manifests. Choose Match initial PTS when you want MediaConvert to use the initial PTS as the first time stamp in the manifest. Choose Zero-based to have MediaConvert ignore the initial PTS in the video stream and instead write the initial time stamp as zero in the manifest. For outputs that don't have B-frames, the time stamps in your DASH manifests start at zero regardless of your choice here."""
    segment_control: NotRequired[
        "capo_mediaconvert.types.cmaf_segment_control.CmafSegmentControl"
    ]
    """When set to SINGLE_FILE, a single output file is generated, which is internally segmented using the Fragment Length and Segment Length. When set to SEGMENTED_FILES, separate segment files will be created."""
    segment_length: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """Specify the length, in whole seconds, of each segment. When you don't specify a value, MediaConvert defaults to 10. Related settings: Use Segment length control to specify whether the encoder enforces this value strictly. Use Segment control to specify whether MediaConvert creates separate segment files or one content file that has metadata to mark the segment boundaries."""
    segment_length_control: NotRequired[
        "capo_mediaconvert.types.cmaf_segment_length_control.CmafSegmentLengthControl"
    ]
    """Specify how you want MediaConvert to determine segment lengths in this output group. To use the exact value that you specify under Segment length: Choose Exact. Note that this might result in additional I-frames in the output GOP. To create segment lengths that are a multiple of the GOP: Choose Multiple of GOP. MediaConvert will round up the segment lengths to match the next GOP boundary. To have MediaConvert automatically determine a segment duration that is a multiple of both the audio packets and the frame rates: Choose Match. When you do, also specify a target segment duration under Segment length. This is useful for some ad-insertion or segment replacement workflows. Note that Match has the following requirements: - Output containers: Include at least one video output and at least one audio output. Audio-only outputs are not supported. - Output frame rate: Follow source is not supported. - Multiple output frame rates: When you specify multiple outputs, we recommend they share a similar frame rate (as in X/3, X/2, X, or 2X). For example: 5, 15, 30 and 60. Or: 25 and 50. (Outputs must share an integer multiple.) - Output audio codec: Specify Advanced Audio Coding (AAC). - Output sample rate: Choose 48kHz."""
    stream_inf_resolution: NotRequired[
        "capo_mediaconvert.types.cmaf_stream_inf_resolution.CmafStreamInfResolution"
    ]
    """Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of variant manifest."""
    target_duration_compatibility_mode: NotRequired[
        "capo_mediaconvert.types.cmaf_target_duration_compatibility_mode.CmafTargetDurationCompatibilityMode"
    ]
    r"""When set to LEGACY, the segment target duration is always rounded up to the nearest integer value above its current value in seconds. When set to SPEC\\_COMPLIANT, the segment target duration is rounded up to the nearest integer value if fraction seconds are greater than or equal to 0.5 (>= 0.5) and rounded down if less than 0.5 (< 0.5). You may need to use LEGACY if your client needs to ensure that the target duration is always longer than the actual duration of the segment. Some older players may experience interrupted playback when the actual duration of a track in a segment is longer than the target duration."""
    video_composition_offsets: NotRequired[
        "capo_mediaconvert.types.cmaf_video_composition_offsets.CmafVideoCompositionOffsets"
    ]
    """Specify the video sample composition time offset mode in the output fMP4 TRUN box. For wider player compatibility, set Video composition offsets to Unsigned or leave blank. The earliest presentation time may be greater than zero, and sample composition time offsets will increment using unsigned integers. For strict fMP4 video and audio timing, set Video composition offsets to Signed. The earliest presentation time will be equal to zero, and sample composition time offsets will increment using signed integers."""
    write_dash_manifest: NotRequired[
        "capo_mediaconvert.types.cmaf_write_dash_manifest.CmafWriteDASHManifest"
    ]
    """When set to ENABLED, a DASH MPD manifest will be generated for this output."""
    write_hls_manifest: NotRequired[
        "capo_mediaconvert.types.cmaf_write_hls_manifest.CmafWriteHLSManifest"
    ]
    """When set to ENABLED, an Apple HLS manifest will be generated for this output."""
    write_segment_timeline_in_representation: NotRequired[
        "capo_mediaconvert.types.cmaf_write_segment_timeline_in_representation.CmafWriteSegmentTimelineInRepresentation"
    ]
    """When you enable Precise segment duration in DASH manifests, your DASH manifest shows precise segment durations. The segment duration information appears inside the SegmentTimeline element, inside SegmentTemplate at the Representation level. When this feature isn't enabled, the segment durations in your DASH manifest are approximate. The segment duration information appears in the duration attribute of the SegmentTemplate element."""


# --- restJson1 ser/de ---
def serialize_json(value: CmafGroupSettings) -> dict:
    out: dict = {}
    if "additional_manifests" in value:
        import capo_mediaconvert.types.__list_of_cmaf_additional_manifest

        out["additionalManifests"] = (
            capo_mediaconvert.types.__list_of_cmaf_additional_manifest.serialize_json(
                value["additional_manifests"]
            )
        )
    if "base_url" in value:
        out["baseUrl"] = value["base_url"]
    if "client_cache" in value:
        import capo_mediaconvert.types.cmaf_client_cache

        out["clientCache"] = capo_mediaconvert.types.cmaf_client_cache.serialize_json(
            value["client_cache"]
        )
    if "codec_specification" in value:
        import capo_mediaconvert.types.cmaf_codec_specification

        out["codecSpecification"] = (
            capo_mediaconvert.types.cmaf_codec_specification.serialize_json(
                value["codec_specification"]
            )
        )
    if "dash_adaptation_set_grouping" in value:
        import capo_mediaconvert.types.__list_of_dash_adaptation_set_grouping

        out["dashAdaptationSetGrouping"] = (
            capo_mediaconvert.types.__list_of_dash_adaptation_set_grouping.serialize_json(
                value["dash_adaptation_set_grouping"]
            )
        )
    if "dash_i_frame_trick_play_name_modifier" in value:
        out["dashIFrameTrickPlayNameModifier"] = value[
            "dash_i_frame_trick_play_name_modifier"
        ]
    if "dash_manifest_style" in value:
        import capo_mediaconvert.types.dash_manifest_style

        out["dashManifestStyle"] = (
            capo_mediaconvert.types.dash_manifest_style.serialize_json(
                value["dash_manifest_style"]
            )
        )
    if "destination" in value:
        out["destination"] = value["destination"]
    if "destination_settings" in value:
        import capo_mediaconvert.types.destination_settings

        out["destinationSettings"] = (
            capo_mediaconvert.types.destination_settings.serialize_json(
                value["destination_settings"]
            )
        )
    if "encryption" in value:
        import capo_mediaconvert.types.cmaf_encryption_settings

        out["encryption"] = (
            capo_mediaconvert.types.cmaf_encryption_settings.serialize_json(
                value["encryption"]
            )
        )
    if "fragment_length" in value:
        out["fragmentLength"] = value["fragment_length"]
    if "image_based_trick_play" in value:
        import capo_mediaconvert.types.cmaf_image_based_trick_play

        out["imageBasedTrickPlay"] = (
            capo_mediaconvert.types.cmaf_image_based_trick_play.serialize_json(
                value["image_based_trick_play"]
            )
        )
    if "image_based_trick_play_settings" in value:
        import capo_mediaconvert.types.cmaf_image_based_trick_play_settings

        out["imageBasedTrickPlaySettings"] = (
            capo_mediaconvert.types.cmaf_image_based_trick_play_settings.serialize_json(
                value["image_based_trick_play_settings"]
            )
        )
    if "image_based_trick_play_variants" in value:
        import capo_mediaconvert.types.__list_of_cmaf_image_based_trick_play_variant

        out["imageBasedTrickPlayVariants"] = (
            capo_mediaconvert.types.__list_of_cmaf_image_based_trick_play_variant.serialize_json(
                value["image_based_trick_play_variants"]
            )
        )
    if "manifest_compression" in value:
        import capo_mediaconvert.types.cmaf_manifest_compression

        out["manifestCompression"] = (
            capo_mediaconvert.types.cmaf_manifest_compression.serialize_json(
                value["manifest_compression"]
            )
        )
    if "manifest_duration_format" in value:
        import capo_mediaconvert.types.cmaf_manifest_duration_format

        out["manifestDurationFormat"] = (
            capo_mediaconvert.types.cmaf_manifest_duration_format.serialize_json(
                value["manifest_duration_format"]
            )
        )
    if "min_buffer_time" in value:
        out["minBufferTime"] = value["min_buffer_time"]
    if "min_final_segment_length" in value:
        out["minFinalSegmentLength"] = (
            "NaN"
            if value["min_final_segment_length"] != value["min_final_segment_length"]
            else "Infinity"
            if value["min_final_segment_length"] == float("inf")
            else "-Infinity"
            if value["min_final_segment_length"] == float("-inf")
            else value["min_final_segment_length"]
        )
    if "mpd_manifest_bandwidth_type" in value:
        import capo_mediaconvert.types.cmaf_mpd_manifest_bandwidth_type

        out["mpdManifestBandwidthType"] = (
            capo_mediaconvert.types.cmaf_mpd_manifest_bandwidth_type.serialize_json(
                value["mpd_manifest_bandwidth_type"]
            )
        )
    if "mpd_profile" in value:
        import capo_mediaconvert.types.cmaf_mpd_profile

        out["mpdProfile"] = capo_mediaconvert.types.cmaf_mpd_profile.serialize_json(
            value["mpd_profile"]
        )
    if "pts_offset_handling_for_b_frames" in value:
        import capo_mediaconvert.types.cmaf_pts_offset_handling_for_b_frames

        out["ptsOffsetHandlingForBFrames"] = (
            capo_mediaconvert.types.cmaf_pts_offset_handling_for_b_frames.serialize_json(
                value["pts_offset_handling_for_b_frames"]
            )
        )
    if "segment_control" in value:
        import capo_mediaconvert.types.cmaf_segment_control

        out["segmentControl"] = (
            capo_mediaconvert.types.cmaf_segment_control.serialize_json(
                value["segment_control"]
            )
        )
    if "segment_length" in value:
        out["segmentLength"] = value["segment_length"]
    if "segment_length_control" in value:
        import capo_mediaconvert.types.cmaf_segment_length_control

        out["segmentLengthControl"] = (
            capo_mediaconvert.types.cmaf_segment_length_control.serialize_json(
                value["segment_length_control"]
            )
        )
    if "stream_inf_resolution" in value:
        import capo_mediaconvert.types.cmaf_stream_inf_resolution

        out["streamInfResolution"] = (
            capo_mediaconvert.types.cmaf_stream_inf_resolution.serialize_json(
                value["stream_inf_resolution"]
            )
        )
    if "target_duration_compatibility_mode" in value:
        import capo_mediaconvert.types.cmaf_target_duration_compatibility_mode

        out["targetDurationCompatibilityMode"] = (
            capo_mediaconvert.types.cmaf_target_duration_compatibility_mode.serialize_json(
                value["target_duration_compatibility_mode"]
            )
        )
    if "video_composition_offsets" in value:
        import capo_mediaconvert.types.cmaf_video_composition_offsets

        out["videoCompositionOffsets"] = (
            capo_mediaconvert.types.cmaf_video_composition_offsets.serialize_json(
                value["video_composition_offsets"]
            )
        )
    if "write_dash_manifest" in value:
        import capo_mediaconvert.types.cmaf_write_dash_manifest

        out["writeDashManifest"] = (
            capo_mediaconvert.types.cmaf_write_dash_manifest.serialize_json(
                value["write_dash_manifest"]
            )
        )
    if "write_hls_manifest" in value:
        import capo_mediaconvert.types.cmaf_write_hls_manifest

        out["writeHlsManifest"] = (
            capo_mediaconvert.types.cmaf_write_hls_manifest.serialize_json(
                value["write_hls_manifest"]
            )
        )
    if "write_segment_timeline_in_representation" in value:
        import capo_mediaconvert.types.cmaf_write_segment_timeline_in_representation

        out["writeSegmentTimelineInRepresentation"] = (
            capo_mediaconvert.types.cmaf_write_segment_timeline_in_representation.serialize_json(
                value["write_segment_timeline_in_representation"]
            )
        )
    return out


def deserialize_json(data: dict) -> CmafGroupSettings:
    out: CmafGroupSettings = {}  # type: ignore[typeddict-item]
    if data.get("additionalManifests") is not None:
        import capo_mediaconvert.types.__list_of_cmaf_additional_manifest

        out["additional_manifests"] = (
            capo_mediaconvert.types.__list_of_cmaf_additional_manifest.deserialize_json(
                data["additionalManifests"]
            )
        )
    if data.get("baseUrl") is not None:
        out["base_url"] = data["baseUrl"]
    if data.get("clientCache") is not None:
        import capo_mediaconvert.types.cmaf_client_cache

        out["client_cache"] = (
            capo_mediaconvert.types.cmaf_client_cache.deserialize_json(
                data["clientCache"]
            )
        )
    if data.get("codecSpecification") is not None:
        import capo_mediaconvert.types.cmaf_codec_specification

        out["codec_specification"] = (
            capo_mediaconvert.types.cmaf_codec_specification.deserialize_json(
                data["codecSpecification"]
            )
        )
    if data.get("dashAdaptationSetGrouping") is not None:
        import capo_mediaconvert.types.__list_of_dash_adaptation_set_grouping

        out["dash_adaptation_set_grouping"] = (
            capo_mediaconvert.types.__list_of_dash_adaptation_set_grouping.deserialize_json(
                data["dashAdaptationSetGrouping"]
            )
        )
    if data.get("dashIFrameTrickPlayNameModifier") is not None:
        out["dash_i_frame_trick_play_name_modifier"] = data[
            "dashIFrameTrickPlayNameModifier"
        ]
    if data.get("dashManifestStyle") is not None:
        import capo_mediaconvert.types.dash_manifest_style

        out["dash_manifest_style"] = (
            capo_mediaconvert.types.dash_manifest_style.deserialize_json(
                data["dashManifestStyle"]
            )
        )
    if data.get("destination") is not None:
        out["destination"] = data["destination"]
    if data.get("destinationSettings") is not None:
        import capo_mediaconvert.types.destination_settings

        out["destination_settings"] = (
            capo_mediaconvert.types.destination_settings.deserialize_json(
                data["destinationSettings"]
            )
        )
    if data.get("encryption") is not None:
        import capo_mediaconvert.types.cmaf_encryption_settings

        out["encryption"] = (
            capo_mediaconvert.types.cmaf_encryption_settings.deserialize_json(
                data["encryption"]
            )
        )
    if data.get("fragmentLength") is not None:
        out["fragment_length"] = data["fragmentLength"]
    if data.get("imageBasedTrickPlay") is not None:
        import capo_mediaconvert.types.cmaf_image_based_trick_play

        out["image_based_trick_play"] = (
            capo_mediaconvert.types.cmaf_image_based_trick_play.deserialize_json(
                data["imageBasedTrickPlay"]
            )
        )
    if data.get("imageBasedTrickPlaySettings") is not None:
        import capo_mediaconvert.types.cmaf_image_based_trick_play_settings

        out["image_based_trick_play_settings"] = (
            capo_mediaconvert.types.cmaf_image_based_trick_play_settings.deserialize_json(
                data["imageBasedTrickPlaySettings"]
            )
        )
    if data.get("imageBasedTrickPlayVariants") is not None:
        import capo_mediaconvert.types.__list_of_cmaf_image_based_trick_play_variant

        out["image_based_trick_play_variants"] = (
            capo_mediaconvert.types.__list_of_cmaf_image_based_trick_play_variant.deserialize_json(
                data["imageBasedTrickPlayVariants"]
            )
        )
    if data.get("manifestCompression") is not None:
        import capo_mediaconvert.types.cmaf_manifest_compression

        out["manifest_compression"] = (
            capo_mediaconvert.types.cmaf_manifest_compression.deserialize_json(
                data["manifestCompression"]
            )
        )
    if data.get("manifestDurationFormat") is not None:
        import capo_mediaconvert.types.cmaf_manifest_duration_format

        out["manifest_duration_format"] = (
            capo_mediaconvert.types.cmaf_manifest_duration_format.deserialize_json(
                data["manifestDurationFormat"]
            )
        )
    if data.get("minBufferTime") is not None:
        out["min_buffer_time"] = data["minBufferTime"]
    if data.get("minFinalSegmentLength") is not None:
        out["min_final_segment_length"] = float(data["minFinalSegmentLength"])
    if data.get("mpdManifestBandwidthType") is not None:
        import capo_mediaconvert.types.cmaf_mpd_manifest_bandwidth_type

        out["mpd_manifest_bandwidth_type"] = (
            capo_mediaconvert.types.cmaf_mpd_manifest_bandwidth_type.deserialize_json(
                data["mpdManifestBandwidthType"]
            )
        )
    if data.get("mpdProfile") is not None:
        import capo_mediaconvert.types.cmaf_mpd_profile

        out["mpd_profile"] = capo_mediaconvert.types.cmaf_mpd_profile.deserialize_json(
            data["mpdProfile"]
        )
    if data.get("ptsOffsetHandlingForBFrames") is not None:
        import capo_mediaconvert.types.cmaf_pts_offset_handling_for_b_frames

        out["pts_offset_handling_for_b_frames"] = (
            capo_mediaconvert.types.cmaf_pts_offset_handling_for_b_frames.deserialize_json(
                data["ptsOffsetHandlingForBFrames"]
            )
        )
    if data.get("segmentControl") is not None:
        import capo_mediaconvert.types.cmaf_segment_control

        out["segment_control"] = (
            capo_mediaconvert.types.cmaf_segment_control.deserialize_json(
                data["segmentControl"]
            )
        )
    if data.get("segmentLength") is not None:
        out["segment_length"] = data["segmentLength"]
    if data.get("segmentLengthControl") is not None:
        import capo_mediaconvert.types.cmaf_segment_length_control

        out["segment_length_control"] = (
            capo_mediaconvert.types.cmaf_segment_length_control.deserialize_json(
                data["segmentLengthControl"]
            )
        )
    if data.get("streamInfResolution") is not None:
        import capo_mediaconvert.types.cmaf_stream_inf_resolution

        out["stream_inf_resolution"] = (
            capo_mediaconvert.types.cmaf_stream_inf_resolution.deserialize_json(
                data["streamInfResolution"]
            )
        )
    if data.get("targetDurationCompatibilityMode") is not None:
        import capo_mediaconvert.types.cmaf_target_duration_compatibility_mode

        out["target_duration_compatibility_mode"] = (
            capo_mediaconvert.types.cmaf_target_duration_compatibility_mode.deserialize_json(
                data["targetDurationCompatibilityMode"]
            )
        )
    if data.get("videoCompositionOffsets") is not None:
        import capo_mediaconvert.types.cmaf_video_composition_offsets

        out["video_composition_offsets"] = (
            capo_mediaconvert.types.cmaf_video_composition_offsets.deserialize_json(
                data["videoCompositionOffsets"]
            )
        )
    if data.get("writeDashManifest") is not None:
        import capo_mediaconvert.types.cmaf_write_dash_manifest

        out["write_dash_manifest"] = (
            capo_mediaconvert.types.cmaf_write_dash_manifest.deserialize_json(
                data["writeDashManifest"]
            )
        )
    if data.get("writeHlsManifest") is not None:
        import capo_mediaconvert.types.cmaf_write_hls_manifest

        out["write_hls_manifest"] = (
            capo_mediaconvert.types.cmaf_write_hls_manifest.deserialize_json(
                data["writeHlsManifest"]
            )
        )
    if data.get("writeSegmentTimelineInRepresentation") is not None:
        import capo_mediaconvert.types.cmaf_write_segment_timeline_in_representation

        out["write_segment_timeline_in_representation"] = (
            capo_mediaconvert.types.cmaf_write_segment_timeline_in_representation.deserialize_json(
                data["writeSegmentTimelineInRepresentation"]
            )
        )
    return out
