"""Generated from Smithy shape ``com.amazonaws.medialive#Mpeg2Settings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__double
    import capo_medialive.types.__integer_min0
    import capo_medialive.types.__integer_min0_max7
    import capo_medialive.types.__integer_min1
    import capo_medialive.types.afd_signaling
    import capo_medialive.types.fixed_afd
    import capo_medialive.types.mpeg2_adaptive_quantization
    import capo_medialive.types.mpeg2_color_metadata
    import capo_medialive.types.mpeg2_color_space
    import capo_medialive.types.mpeg2_display_ratio
    import capo_medialive.types.mpeg2_filter_settings
    import capo_medialive.types.mpeg2_gop_size_units
    import capo_medialive.types.mpeg2_scan_type
    import capo_medialive.types.mpeg2_sub_gop_length
    import capo_medialive.types.mpeg2_timecode_insertion_behavior
    import capo_medialive.types.timecode_burnin_settings


class Mpeg2Settings(TypedDict, closed=True):
    adaptive_quantization: NotRequired[
        "capo_medialive.types.mpeg2_adaptive_quantization.Mpeg2AdaptiveQuantization"
    ]
    """Choose Off to disable adaptive quantization. Or choose another value to enable the quantizer and set its strength. The strengths are: Auto, Off, Low, Medium, High. When you enable this field, MediaLive allows intra-frame quantizers to vary, which might improve visual quality."""
    afd_signaling: NotRequired["capo_medialive.types.afd_signaling.AfdSignaling"]
    """Indicates the AFD values that MediaLive will write into the video encode. If you do not know what AFD signaling is, or if your downstream system has not given you guidance, choose AUTO. AUTO: MediaLive will try to preserve the input AFD value (in cases where multiple AFD values are valid). FIXED: MediaLive will use the value you specify in fixedAFD."""
    color_metadata: NotRequired[
        "capo_medialive.types.mpeg2_color_metadata.Mpeg2ColorMetadata"
    ]
    """Specifies whether to include the color space metadata. The metadata describes the color space that applies to the video (the colorSpace field). We recommend that you insert the metadata."""
    color_space: NotRequired["capo_medialive.types.mpeg2_color_space.Mpeg2ColorSpace"]
    r"""Choose the type of color space conversion to apply to the output. For detailed information on setting up both the input and the output to obtain the desired color space in the output, see the section on \"MediaLive Features - Video - color space\" in the MediaLive User Guide. PASSTHROUGH: Keep the color space of the input content - do not convert it. AUTO:Convert all content that is SD to rec 601, and convert all content that is HD to rec 709."""
    display_aspect_ratio: NotRequired[
        "capo_medialive.types.mpeg2_display_ratio.Mpeg2DisplayRatio"
    ]
    """Sets the pixel aspect ratio for the encode."""
    filter_settings: NotRequired[
        "capo_medialive.types.mpeg2_filter_settings.Mpeg2FilterSettings"
    ]
    """Optionally specify a noise reduction filter, which can improve quality of compressed content. If you do not choose a filter, no filter will be applied. TEMPORAL: This filter is useful for both source content that is noisy (when it has excessive digital artifacts) and source content that is clean. When the content is noisy, the filter cleans up the source content before the encoding phase, with these two effects: First, it improves the output video quality because the content has been cleaned up. Secondly, it decreases the bandwidth because MediaLive does not waste bits on encoding noise. When the content is reasonably clean, the filter tends to decrease the bitrate."""
    fixed_afd: NotRequired["capo_medialive.types.fixed_afd.FixedAfd"]
    """Complete this field only when afdSignaling is set to FIXED. Enter the AFD value (4 bits) to write on all frames of the video encode."""
    framerate_denominator: NotRequired[
        "capo_medialive.types.__integer_min1.__integerMin1"
    ]
    """description": "The framerate denominator. For example, 1001. The framerate is the numerator divided by the denominator. For example, 24000 / 1001 = 23.976 FPS."""
    framerate_numerator: NotRequired[
        "capo_medialive.types.__integer_min1.__integerMin1"
    ]
    """The framerate numerator. For example, 24000. The framerate is the numerator divided by the denominator. For example, 24000 / 1001 = 23.976 FPS."""
    gop_closed_cadence: NotRequired["capo_medialive.types.__integer_min0.__integerMin0"]
    """MPEG2: default is open GOP."""
    gop_num_b_frames: NotRequired[
        "capo_medialive.types.__integer_min0_max7.__integerMin0Max7"
    ]
    """Relates to the GOP structure. The number of B-frames between reference frames. If you do not know what a B-frame is, use the default."""
    gop_size: NotRequired["capo_medialive.types.__double.__double"]
    """Relates to the GOP structure. The GOP size (keyframe interval) in the units specified in gopSizeUnits. If you do not know what GOP is, use the default. If gopSizeUnits is frames, then the gopSize must be an integer and must be greater than or equal to 1. If gopSizeUnits is seconds, the gopSize must be greater than 0, but does not need to be an integer."""
    gop_size_units: NotRequired[
        "capo_medialive.types.mpeg2_gop_size_units.Mpeg2GopSizeUnits"
    ]
    """Relates to the GOP structure. Specifies whether the gopSize is specified in frames or seconds. If you do not plan to change the default gopSize, leave the default. If you specify SECONDS, MediaLive will internally convert the gop size to a frame count."""
    scan_type: NotRequired["capo_medialive.types.mpeg2_scan_type.Mpeg2ScanType"]
    """Set the scan type of the output to PROGRESSIVE or INTERLACED (top field first)."""
    subgop_length: NotRequired[
        "capo_medialive.types.mpeg2_sub_gop_length.Mpeg2SubGopLength"
    ]
    """Relates to the GOP structure. If you do not know what GOP is, use the default. FIXED: Set the number of B-frames in each sub-GOP to the value in gopNumBFrames. DYNAMIC: Let MediaLive optimize the number of B-frames in each sub-GOP, to improve visual quality."""
    timecode_insertion: NotRequired[
        "capo_medialive.types.mpeg2_timecode_insertion_behavior.Mpeg2TimecodeInsertionBehavior"
    ]
    r"""Determines how MediaLive inserts timecodes in the output video. For detailed information about setting up the input and the output for a timecode, see the section on \"MediaLive Features - Timecode configuration\" in the MediaLive User Guide. DISABLED: do not include timecodes. GOP_TIMECODE: Include timecode metadata in the GOP header."""
    timecode_burnin_settings: NotRequired[
        "capo_medialive.types.timecode_burnin_settings.TimecodeBurninSettings"
    ]
    """Timecode burn-in settings"""


# --- restJson1 ser/de ---
def serialize_json(value: Mpeg2Settings) -> dict:
    out: dict = {}
    if "adaptive_quantization" in value:
        import capo_medialive.types.mpeg2_adaptive_quantization

        out["adaptiveQuantization"] = (
            capo_medialive.types.mpeg2_adaptive_quantization.serialize_json(
                value["adaptive_quantization"]
            )
        )
    if "afd_signaling" in value:
        import capo_medialive.types.afd_signaling

        out["afdSignaling"] = capo_medialive.types.afd_signaling.serialize_json(
            value["afd_signaling"]
        )
    if "color_metadata" in value:
        import capo_medialive.types.mpeg2_color_metadata

        out["colorMetadata"] = capo_medialive.types.mpeg2_color_metadata.serialize_json(
            value["color_metadata"]
        )
    if "color_space" in value:
        import capo_medialive.types.mpeg2_color_space

        out["colorSpace"] = capo_medialive.types.mpeg2_color_space.serialize_json(
            value["color_space"]
        )
    if "display_aspect_ratio" in value:
        import capo_medialive.types.mpeg2_display_ratio

        out["displayAspectRatio"] = (
            capo_medialive.types.mpeg2_display_ratio.serialize_json(
                value["display_aspect_ratio"]
            )
        )
    if "filter_settings" in value:
        import capo_medialive.types.mpeg2_filter_settings

        out["filterSettings"] = (
            capo_medialive.types.mpeg2_filter_settings.serialize_json(
                value["filter_settings"]
            )
        )
    if "fixed_afd" in value:
        import capo_medialive.types.fixed_afd

        out["fixedAfd"] = capo_medialive.types.fixed_afd.serialize_json(
            value["fixed_afd"]
        )
    if "framerate_denominator" in value:
        out["framerateDenominator"] = value["framerate_denominator"]
    if "framerate_numerator" in value:
        out["framerateNumerator"] = value["framerate_numerator"]
    if "gop_closed_cadence" in value:
        out["gopClosedCadence"] = value["gop_closed_cadence"]
    if "gop_num_b_frames" in value:
        out["gopNumBFrames"] = value["gop_num_b_frames"]
    if "gop_size" in value:
        out["gopSize"] = (
            "NaN"
            if value["gop_size"] != value["gop_size"]
            else "Infinity"
            if value["gop_size"] == float("inf")
            else "-Infinity"
            if value["gop_size"] == float("-inf")
            else value["gop_size"]
        )
    if "gop_size_units" in value:
        import capo_medialive.types.mpeg2_gop_size_units

        out["gopSizeUnits"] = capo_medialive.types.mpeg2_gop_size_units.serialize_json(
            value["gop_size_units"]
        )
    if "scan_type" in value:
        import capo_medialive.types.mpeg2_scan_type

        out["scanType"] = capo_medialive.types.mpeg2_scan_type.serialize_json(
            value["scan_type"]
        )
    if "subgop_length" in value:
        import capo_medialive.types.mpeg2_sub_gop_length

        out["subgopLength"] = capo_medialive.types.mpeg2_sub_gop_length.serialize_json(
            value["subgop_length"]
        )
    if "timecode_insertion" in value:
        import capo_medialive.types.mpeg2_timecode_insertion_behavior

        out["timecodeInsertion"] = (
            capo_medialive.types.mpeg2_timecode_insertion_behavior.serialize_json(
                value["timecode_insertion"]
            )
        )
    if "timecode_burnin_settings" in value:
        import capo_medialive.types.timecode_burnin_settings

        out["timecodeBurninSettings"] = (
            capo_medialive.types.timecode_burnin_settings.serialize_json(
                value["timecode_burnin_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> Mpeg2Settings:
    out: Mpeg2Settings = {}  # type: ignore[typeddict-item]
    if data.get("adaptiveQuantization") is not None:
        import capo_medialive.types.mpeg2_adaptive_quantization

        out["adaptive_quantization"] = (
            capo_medialive.types.mpeg2_adaptive_quantization.deserialize_json(
                data["adaptiveQuantization"]
            )
        )
    if data.get("afdSignaling") is not None:
        import capo_medialive.types.afd_signaling

        out["afd_signaling"] = capo_medialive.types.afd_signaling.deserialize_json(
            data["afdSignaling"]
        )
    if data.get("colorMetadata") is not None:
        import capo_medialive.types.mpeg2_color_metadata

        out["color_metadata"] = (
            capo_medialive.types.mpeg2_color_metadata.deserialize_json(
                data["colorMetadata"]
            )
        )
    if data.get("colorSpace") is not None:
        import capo_medialive.types.mpeg2_color_space

        out["color_space"] = capo_medialive.types.mpeg2_color_space.deserialize_json(
            data["colorSpace"]
        )
    if data.get("displayAspectRatio") is not None:
        import capo_medialive.types.mpeg2_display_ratio

        out["display_aspect_ratio"] = (
            capo_medialive.types.mpeg2_display_ratio.deserialize_json(
                data["displayAspectRatio"]
            )
        )
    if data.get("filterSettings") is not None:
        import capo_medialive.types.mpeg2_filter_settings

        out["filter_settings"] = (
            capo_medialive.types.mpeg2_filter_settings.deserialize_json(
                data["filterSettings"]
            )
        )
    if data.get("fixedAfd") is not None:
        import capo_medialive.types.fixed_afd

        out["fixed_afd"] = capo_medialive.types.fixed_afd.deserialize_json(
            data["fixedAfd"]
        )
    if data.get("framerateDenominator") is not None:
        out["framerate_denominator"] = data["framerateDenominator"]
    if data.get("framerateNumerator") is not None:
        out["framerate_numerator"] = data["framerateNumerator"]
    if data.get("gopClosedCadence") is not None:
        out["gop_closed_cadence"] = data["gopClosedCadence"]
    if data.get("gopNumBFrames") is not None:
        out["gop_num_b_frames"] = data["gopNumBFrames"]
    if data.get("gopSize") is not None:
        out["gop_size"] = float(data["gopSize"])
    if data.get("gopSizeUnits") is not None:
        import capo_medialive.types.mpeg2_gop_size_units

        out["gop_size_units"] = (
            capo_medialive.types.mpeg2_gop_size_units.deserialize_json(
                data["gopSizeUnits"]
            )
        )
    if data.get("scanType") is not None:
        import capo_medialive.types.mpeg2_scan_type

        out["scan_type"] = capo_medialive.types.mpeg2_scan_type.deserialize_json(
            data["scanType"]
        )
    if data.get("subgopLength") is not None:
        import capo_medialive.types.mpeg2_sub_gop_length

        out["subgop_length"] = (
            capo_medialive.types.mpeg2_sub_gop_length.deserialize_json(
                data["subgopLength"]
            )
        )
    if data.get("timecodeInsertion") is not None:
        import capo_medialive.types.mpeg2_timecode_insertion_behavior

        out["timecode_insertion"] = (
            capo_medialive.types.mpeg2_timecode_insertion_behavior.deserialize_json(
                data["timecodeInsertion"]
            )
        )
    if data.get("timecodeBurninSettings") is not None:
        import capo_medialive.types.timecode_burnin_settings

        out["timecode_burnin_settings"] = (
            capo_medialive.types.timecode_burnin_settings.deserialize_json(
                data["timecodeBurninSettings"]
            )
        )
    return out
