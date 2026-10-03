"""Generated from Smithy shape ``com.amazonaws.medialive#H265Settings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__double
    import capo_medialive.types.__integer_min0
    import capo_medialive.types.__integer_min0_max3
    import capo_medialive.types.__integer_min0_max30
    import capo_medialive.types.__integer_min0_max40000000
    import capo_medialive.types.__integer_min1
    import capo_medialive.types.__integer_min1_max10
    import capo_medialive.types.__integer_min1_max16
    import capo_medialive.types.__integer_min1_max51
    import capo_medialive.types.__integer_min1_max3003
    import capo_medialive.types.__integer_min64_max2160
    import capo_medialive.types.__integer_min256_max3840
    import capo_medialive.types.__integer_min100000_max40000000
    import capo_medialive.types.__integer_min100000_max80000000
    import capo_medialive.types.afd_signaling
    import capo_medialive.types.fixed_afd
    import capo_medialive.types.h265_adaptive_quantization
    import capo_medialive.types.h265_alternative_transfer_function
    import capo_medialive.types.h265_color_metadata
    import capo_medialive.types.h265_color_space_settings
    import capo_medialive.types.h265_deblocking
    import capo_medialive.types.h265_filter_settings
    import capo_medialive.types.h265_flicker_aq
    import capo_medialive.types.h265_gop_b_reference
    import capo_medialive.types.h265_gop_size_units
    import capo_medialive.types.h265_level
    import capo_medialive.types.h265_look_ahead_rate_control
    import capo_medialive.types.h265_mv_over_picture_boundaries
    import capo_medialive.types.h265_mv_temporal_predictor
    import capo_medialive.types.h265_profile
    import capo_medialive.types.h265_rate_control_mode
    import capo_medialive.types.h265_scan_type
    import capo_medialive.types.h265_scene_change_detect
    import capo_medialive.types.h265_sub_gop_length
    import capo_medialive.types.h265_tier
    import capo_medialive.types.h265_tile_padding
    import capo_medialive.types.h265_timecode_insertion_behavior
    import capo_medialive.types.h265_treeblock_size
    import capo_medialive.types.timecode_burnin_settings


class H265Settings(TypedDict, closed=True):
    adaptive_quantization: NotRequired[
        "capo_medialive.types.h265_adaptive_quantization.H265AdaptiveQuantization"
    ]
    """Enables or disables adaptive quantization (AQ), which is a technique MediaLive can apply to video on a frame-by-frame basis to produce more compression without losing quality. There are three types of adaptive quantization: spatial, temporal, and flicker. Flicker is the only type that you can customize. We recommend that you set the field to Auto. For more information about all the options, see the topic about video adaptive quantization in the MediaLive user guide."""
    afd_signaling: NotRequired["capo_medialive.types.afd_signaling.AfdSignaling"]
    """Indicates that AFD values will be written into the output stream. If afdSignaling is "auto", the system will try to preserve the input AFD value (in cases where multiple AFD values are valid). If set to "fixed", the AFD value will be the value configured in the fixedAfd parameter."""
    alternative_transfer_function: NotRequired[
        "capo_medialive.types.h265_alternative_transfer_function.H265AlternativeTransferFunction"
    ]
    """Whether or not EML should insert an Alternative Transfer Function SEI message to support backwards compatibility with non-HDR decoders and displays."""
    bitrate: NotRequired[
        "capo_medialive.types.__integer_min100000_max40000000.__integerMin100000Max40000000"
    ]
    """Average bitrate in bits/second. Required when the rate control mode is VBR or CBR. Not used for QVBR. In an MS Smooth output group, each output must have a unique value when its bitrate is rounded down to the nearest multiple of 1000."""
    buf_size: NotRequired[
        "capo_medialive.types.__integer_min100000_max80000000.__integerMin100000Max80000000"
    ]
    """Size of buffer (HRD buffer model) in bits."""
    color_metadata: NotRequired[
        "capo_medialive.types.h265_color_metadata.H265ColorMetadata"
    ]
    """Includes colorspace metadata in the output."""
    color_space_settings: NotRequired[
        "capo_medialive.types.h265_color_space_settings.H265ColorSpaceSettings"
    ]
    """Specify the type of color space to apply or choose to pass through. The default is to pass through the color space that is in the source."""
    filter_settings: NotRequired[
        "capo_medialive.types.h265_filter_settings.H265FilterSettings"
    ]
    """Optional. Both filters reduce bandwidth by removing imperceptible details. You can enable one of the filters. We recommend that you try both filters and observe the results to decide which one to use. The Temporal Filter reduces bandwidth by removing imperceptible details in the content. It combines perceptual filtering and motion compensated temporal filtering (MCTF). It operates independently of the compression level. The Bandwidth Reduction filter is a perceptual filter located within the encoding loop. It adapts to the current compression level to filter imperceptible signals. This filter works only when the resolution is 1080p or lower."""
    fixed_afd: NotRequired["capo_medialive.types.fixed_afd.FixedAfd"]
    """Four bit AFD value to write on all frames of video in the output stream. Only valid when afdSignaling is set to 'Fixed'."""
    flicker_aq: NotRequired["capo_medialive.types.h265_flicker_aq.H265FlickerAq"]
    """Flicker AQ makes adjustments within each frame to reduce flicker or 'pop' on I-frames. The value to enter in this field depends on the value in the Adaptive quantization field. For more information, see the topic about video adaptive quantization in the MediaLive user guide."""
    framerate_denominator: NotRequired[
        "capo_medialive.types.__integer_min1_max3003.__integerMin1Max3003"
    ]
    """Framerate denominator."""
    framerate_numerator: NotRequired[
        "capo_medialive.types.__integer_min1.__integerMin1"
    ]
    """Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976 fps."""
    gop_closed_cadence: NotRequired["capo_medialive.types.__integer_min0.__integerMin0"]
    """Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting."""
    gop_size: NotRequired["capo_medialive.types.__double.__double"]
    """GOP size (keyframe interval) in units of either frames or seconds per gopSizeUnits. If gopSizeUnits is frames, gopSize must be an integer and must be greater than or equal to 1. If gopSizeUnits is seconds, gopSize must be greater than 0, but need not be an integer."""
    gop_size_units: NotRequired[
        "capo_medialive.types.h265_gop_size_units.H265GopSizeUnits"
    ]
    """Indicates if the gopSize is specified in frames or seconds. If seconds the system will convert the gopSize into a frame count at run time."""
    level: NotRequired["capo_medialive.types.h265_level.H265Level"]
    """H.265 Level."""
    look_ahead_rate_control: NotRequired[
        "capo_medialive.types.h265_look_ahead_rate_control.H265LookAheadRateControl"
    ]
    """Amount of lookahead. A value of low can decrease latency and memory usage, while high can produce better quality for certain content."""
    max_bitrate: NotRequired[
        "capo_medialive.types.__integer_min100000_max40000000.__integerMin100000Max40000000"
    ]
    """For QVBR: See the tooltip for Quality level"""
    min_i_interval: NotRequired[
        "capo_medialive.types.__integer_min0_max30.__integerMin0Max30"
    ]
    """Only meaningful if sceneChangeDetect is set to enabled. Defaults to 5 if multiplex rate control is used. Enforces separation between repeated (cadence) I-frames and I-frames inserted by Scene Change Detection. If a scene change I-frame is within I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch requires enabling lookahead as well as setting I-interval. The normal cadence resumes for the next GOP. Note: Maximum GOP stretch = GOP size + Min-I-interval - 1"""
    par_denominator: NotRequired["capo_medialive.types.__integer_min1.__integerMin1"]
    """Pixel Aspect Ratio denominator."""
    par_numerator: NotRequired["capo_medialive.types.__integer_min1.__integerMin1"]
    """Pixel Aspect Ratio numerator."""
    profile: NotRequired["capo_medialive.types.h265_profile.H265Profile"]
    """H.265 Profile."""
    qvbr_quality_level: NotRequired[
        "capo_medialive.types.__integer_min1_max10.__integerMin1Max10"
    ]
    """Controls the target quality for the video encode. Applies only when the rate control mode is QVBR. Set values for the QVBR quality level field and Max bitrate field that suit your most important viewing devices. Recommended values are: - Primary screen: Quality level: 8 to 10. Max bitrate: 4M - PC or tablet: Quality level: 7. Max bitrate: 1.5M to 3M - Smartphone: Quality level: 6. Max bitrate: 1M to 1.5M"""
    rate_control_mode: NotRequired[
        "capo_medialive.types.h265_rate_control_mode.H265RateControlMode"
    ]
    """Rate control mode. QVBR: Quality will match the specified quality level except when it is constrained by the maximum bitrate. Recommended if you or your viewers pay for bandwidth. CBR: Quality varies, depending on the video complexity. Recommended only if you distribute your assets to devices that cannot handle variable bitrates. Multiplex: This rate control mode is only supported (and is required) when the video is being delivered to a MediaLive Multiplex in which case the rate control configuration is controlled by the properties within the Multiplex Program."""
    scan_type: NotRequired["capo_medialive.types.h265_scan_type.H265ScanType"]
    """Sets the scan type of the output to progressive or top-field-first interlaced."""
    scene_change_detect: NotRequired[
        "capo_medialive.types.h265_scene_change_detect.H265SceneChangeDetect"
    ]
    """Scene change detection."""
    slices: NotRequired["capo_medialive.types.__integer_min1_max16.__integerMin1Max16"]
    """Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures. This field is optional; when no value is specified the encoder will choose the number of slices based on encode resolution."""
    tier: NotRequired["capo_medialive.types.h265_tier.H265Tier"]
    """H.265 Tier."""
    timecode_insertion: NotRequired[
        "capo_medialive.types.h265_timecode_insertion_behavior.H265TimecodeInsertionBehavior"
    ]
    """Determines how timecodes should be inserted into the video elementary stream. - 'disabled': Do not include timecodes - 'picTimingSei': Pass through picture timing SEI messages from the source specified in Timecode Config"""
    timecode_burnin_settings: NotRequired[
        "capo_medialive.types.timecode_burnin_settings.TimecodeBurninSettings"
    ]
    """Timecode burn-in settings"""
    mv_over_picture_boundaries: NotRequired[
        "capo_medialive.types.h265_mv_over_picture_boundaries.H265MvOverPictureBoundaries"
    ]
    """If you are setting up the picture as a tile, you must set this to "disabled". In all other configurations, you typically enter "enabled"."""
    mv_temporal_predictor: NotRequired[
        "capo_medialive.types.h265_mv_temporal_predictor.H265MvTemporalPredictor"
    ]
    """If you are setting up the picture as a tile, you must set this to "disabled". In other configurations, you typically enter "enabled"."""
    tile_height: NotRequired[
        "capo_medialive.types.__integer_min64_max2160.__integerMin64Max2160"
    ]
    """Set this field to set up the picture as a tile. You must also set tileWidth. The tile height must result in 22 or fewer rows in the frame. The tile width must result in 20 or fewer columns in the frame. And finally, the product of the column count and row count must be 64 of less. If the tile width and height are specified, MediaLive will override the video codec slices field with a value that MediaLive calculates"""
    tile_padding: NotRequired["capo_medialive.types.h265_tile_padding.H265TilePadding"]
    """Set to "padded" to force MediaLive to add padding to the frame, to obtain a frame that is a whole multiple of the tile size. If you are setting up the picture as a tile, you must enter "padded". In all other configurations, you typically enter "none"."""
    tile_width: NotRequired[
        "capo_medialive.types.__integer_min256_max3840.__integerMin256Max3840"
    ]
    """Set this field to set up the picture as a tile. See tileHeight for more information."""
    treeblock_size: NotRequired[
        "capo_medialive.types.h265_treeblock_size.H265TreeblockSize"
    ]
    """Select the tree block size used for encoding. If you enter "auto", the encoder will pick the best size. If you are setting up the picture as a tile, you must set this to 32x32. In all other configurations, you typically enter "auto"."""
    min_qp: NotRequired["capo_medialive.types.__integer_min1_max51.__integerMin1Max51"]
    """Sets the minimum QP. If you aren't familiar with quantization adjustment, leave the field empty. MediaLive will apply an appropriate value."""
    deblocking: NotRequired["capo_medialive.types.h265_deblocking.H265Deblocking"]
    """Enable or disable the deblocking filter for this codec. The filter reduces blocking artifacts at block boundaries, which improves overall video quality. If the filter is disabled, visible block edges might appear in the output, especially at lower bitrates."""
    gop_b_reference: NotRequired[
        "capo_medialive.types.h265_gop_b_reference.H265GopBReference"
    ]
    """Allows the encoder to use a B-Frame as a reference frame as well. ENABLED: B-frames will also serve as reference frames. DISABLED: B-frames won't be reference frames. Must be DISABLED if resolution is greater than 1080p or when using tiled hevc encoding."""
    gop_num_b_frames: NotRequired[
        "capo_medialive.types.__integer_min0_max3.__integerMin0Max3"
    ]
    """Sets the number of B-frames between reference frames. Set to 2 if resolution is greater than 1080p or when using tiled hevc encoding."""
    min_bitrate: NotRequired[
        "capo_medialive.types.__integer_min0_max40000000.__integerMin0Max40000000"
    ]
    """Used for QVBR rate control mode only. Optional. Enter a minimum bitrate if you want to keep the output bitrate about a threshold, in order to prevent the downstream system from de-allocating network bandwidth for this output."""
    subgop_length: NotRequired[
        "capo_medialive.types.h265_sub_gop_length.H265SubGopLength"
    ]
    """Sets the number of B-frames in each sub-GOP. FIXED: Use the value in Num B-frames. DYNAMIC: Optimizes the number of B-frames in each sub-GOP to improve visual quality. Must be FIXED if resolution is greater than 1080p or when using tiled hevc encoding."""


# --- restJson1 ser/de ---
def serialize_json(value: H265Settings) -> dict:
    out: dict = {}
    if "adaptive_quantization" in value:
        import capo_medialive.types.h265_adaptive_quantization

        out["adaptiveQuantization"] = (
            capo_medialive.types.h265_adaptive_quantization.serialize_json(
                value["adaptive_quantization"]
            )
        )
    if "afd_signaling" in value:
        import capo_medialive.types.afd_signaling

        out["afdSignaling"] = capo_medialive.types.afd_signaling.serialize_json(
            value["afd_signaling"]
        )
    if "alternative_transfer_function" in value:
        import capo_medialive.types.h265_alternative_transfer_function

        out["alternativeTransferFunction"] = (
            capo_medialive.types.h265_alternative_transfer_function.serialize_json(
                value["alternative_transfer_function"]
            )
        )
    if "bitrate" in value:
        out["bitrate"] = value["bitrate"]
    if "buf_size" in value:
        out["bufSize"] = value["buf_size"]
    if "color_metadata" in value:
        import capo_medialive.types.h265_color_metadata

        out["colorMetadata"] = capo_medialive.types.h265_color_metadata.serialize_json(
            value["color_metadata"]
        )
    if "color_space_settings" in value:
        import capo_medialive.types.h265_color_space_settings

        out["colorSpaceSettings"] = (
            capo_medialive.types.h265_color_space_settings.serialize_json(
                value["color_space_settings"]
            )
        )
    if "filter_settings" in value:
        import capo_medialive.types.h265_filter_settings

        out["filterSettings"] = (
            capo_medialive.types.h265_filter_settings.serialize_json(
                value["filter_settings"]
            )
        )
    if "fixed_afd" in value:
        import capo_medialive.types.fixed_afd

        out["fixedAfd"] = capo_medialive.types.fixed_afd.serialize_json(
            value["fixed_afd"]
        )
    if "flicker_aq" in value:
        import capo_medialive.types.h265_flicker_aq

        out["flickerAq"] = capo_medialive.types.h265_flicker_aq.serialize_json(
            value["flicker_aq"]
        )
    if "framerate_denominator" in value:
        out["framerateDenominator"] = value["framerate_denominator"]
    if "framerate_numerator" in value:
        out["framerateNumerator"] = value["framerate_numerator"]
    if "gop_closed_cadence" in value:
        out["gopClosedCadence"] = value["gop_closed_cadence"]
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
        import capo_medialive.types.h265_gop_size_units

        out["gopSizeUnits"] = capo_medialive.types.h265_gop_size_units.serialize_json(
            value["gop_size_units"]
        )
    if "level" in value:
        import capo_medialive.types.h265_level

        out["level"] = capo_medialive.types.h265_level.serialize_json(value["level"])
    if "look_ahead_rate_control" in value:
        import capo_medialive.types.h265_look_ahead_rate_control

        out["lookAheadRateControl"] = (
            capo_medialive.types.h265_look_ahead_rate_control.serialize_json(
                value["look_ahead_rate_control"]
            )
        )
    if "max_bitrate" in value:
        out["maxBitrate"] = value["max_bitrate"]
    if "min_i_interval" in value:
        out["minIInterval"] = value["min_i_interval"]
    if "par_denominator" in value:
        out["parDenominator"] = value["par_denominator"]
    if "par_numerator" in value:
        out["parNumerator"] = value["par_numerator"]
    if "profile" in value:
        import capo_medialive.types.h265_profile

        out["profile"] = capo_medialive.types.h265_profile.serialize_json(
            value["profile"]
        )
    if "qvbr_quality_level" in value:
        out["qvbrQualityLevel"] = value["qvbr_quality_level"]
    if "rate_control_mode" in value:
        import capo_medialive.types.h265_rate_control_mode

        out["rateControlMode"] = (
            capo_medialive.types.h265_rate_control_mode.serialize_json(
                value["rate_control_mode"]
            )
        )
    if "scan_type" in value:
        import capo_medialive.types.h265_scan_type

        out["scanType"] = capo_medialive.types.h265_scan_type.serialize_json(
            value["scan_type"]
        )
    if "scene_change_detect" in value:
        import capo_medialive.types.h265_scene_change_detect

        out["sceneChangeDetect"] = (
            capo_medialive.types.h265_scene_change_detect.serialize_json(
                value["scene_change_detect"]
            )
        )
    if "slices" in value:
        out["slices"] = value["slices"]
    if "tier" in value:
        import capo_medialive.types.h265_tier

        out["tier"] = capo_medialive.types.h265_tier.serialize_json(value["tier"])
    if "timecode_insertion" in value:
        import capo_medialive.types.h265_timecode_insertion_behavior

        out["timecodeInsertion"] = (
            capo_medialive.types.h265_timecode_insertion_behavior.serialize_json(
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
    if "mv_over_picture_boundaries" in value:
        import capo_medialive.types.h265_mv_over_picture_boundaries

        out["mvOverPictureBoundaries"] = (
            capo_medialive.types.h265_mv_over_picture_boundaries.serialize_json(
                value["mv_over_picture_boundaries"]
            )
        )
    if "mv_temporal_predictor" in value:
        import capo_medialive.types.h265_mv_temporal_predictor

        out["mvTemporalPredictor"] = (
            capo_medialive.types.h265_mv_temporal_predictor.serialize_json(
                value["mv_temporal_predictor"]
            )
        )
    if "tile_height" in value:
        out["tileHeight"] = value["tile_height"]
    if "tile_padding" in value:
        import capo_medialive.types.h265_tile_padding

        out["tilePadding"] = capo_medialive.types.h265_tile_padding.serialize_json(
            value["tile_padding"]
        )
    if "tile_width" in value:
        out["tileWidth"] = value["tile_width"]
    if "treeblock_size" in value:
        import capo_medialive.types.h265_treeblock_size

        out["treeblockSize"] = capo_medialive.types.h265_treeblock_size.serialize_json(
            value["treeblock_size"]
        )
    if "min_qp" in value:
        out["minQp"] = value["min_qp"]
    if "deblocking" in value:
        import capo_medialive.types.h265_deblocking

        out["deblocking"] = capo_medialive.types.h265_deblocking.serialize_json(
            value["deblocking"]
        )
    if "gop_b_reference" in value:
        import capo_medialive.types.h265_gop_b_reference

        out["gopBReference"] = capo_medialive.types.h265_gop_b_reference.serialize_json(
            value["gop_b_reference"]
        )
    if "gop_num_b_frames" in value:
        out["gopNumBFrames"] = value["gop_num_b_frames"]
    if "min_bitrate" in value:
        out["minBitrate"] = value["min_bitrate"]
    if "subgop_length" in value:
        import capo_medialive.types.h265_sub_gop_length

        out["subgopLength"] = capo_medialive.types.h265_sub_gop_length.serialize_json(
            value["subgop_length"]
        )
    return out


def deserialize_json(data: dict) -> H265Settings:
    out: H265Settings = {}  # type: ignore[typeddict-item]
    if data.get("adaptiveQuantization") is not None:
        import capo_medialive.types.h265_adaptive_quantization

        out["adaptive_quantization"] = (
            capo_medialive.types.h265_adaptive_quantization.deserialize_json(
                data["adaptiveQuantization"]
            )
        )
    if data.get("afdSignaling") is not None:
        import capo_medialive.types.afd_signaling

        out["afd_signaling"] = capo_medialive.types.afd_signaling.deserialize_json(
            data["afdSignaling"]
        )
    if data.get("alternativeTransferFunction") is not None:
        import capo_medialive.types.h265_alternative_transfer_function

        out["alternative_transfer_function"] = (
            capo_medialive.types.h265_alternative_transfer_function.deserialize_json(
                data["alternativeTransferFunction"]
            )
        )
    if data.get("bitrate") is not None:
        out["bitrate"] = data["bitrate"]
    if data.get("bufSize") is not None:
        out["buf_size"] = data["bufSize"]
    if data.get("colorMetadata") is not None:
        import capo_medialive.types.h265_color_metadata

        out["color_metadata"] = (
            capo_medialive.types.h265_color_metadata.deserialize_json(
                data["colorMetadata"]
            )
        )
    if data.get("colorSpaceSettings") is not None:
        import capo_medialive.types.h265_color_space_settings

        out["color_space_settings"] = (
            capo_medialive.types.h265_color_space_settings.deserialize_json(
                data["colorSpaceSettings"]
            )
        )
    if data.get("filterSettings") is not None:
        import capo_medialive.types.h265_filter_settings

        out["filter_settings"] = (
            capo_medialive.types.h265_filter_settings.deserialize_json(
                data["filterSettings"]
            )
        )
    if data.get("fixedAfd") is not None:
        import capo_medialive.types.fixed_afd

        out["fixed_afd"] = capo_medialive.types.fixed_afd.deserialize_json(
            data["fixedAfd"]
        )
    if data.get("flickerAq") is not None:
        import capo_medialive.types.h265_flicker_aq

        out["flicker_aq"] = capo_medialive.types.h265_flicker_aq.deserialize_json(
            data["flickerAq"]
        )
    if data.get("framerateDenominator") is not None:
        out["framerate_denominator"] = data["framerateDenominator"]
    if data.get("framerateNumerator") is not None:
        out["framerate_numerator"] = data["framerateNumerator"]
    if data.get("gopClosedCadence") is not None:
        out["gop_closed_cadence"] = data["gopClosedCadence"]
    if data.get("gopSize") is not None:
        out["gop_size"] = float(data["gopSize"])
    if data.get("gopSizeUnits") is not None:
        import capo_medialive.types.h265_gop_size_units

        out["gop_size_units"] = (
            capo_medialive.types.h265_gop_size_units.deserialize_json(
                data["gopSizeUnits"]
            )
        )
    if data.get("level") is not None:
        import capo_medialive.types.h265_level

        out["level"] = capo_medialive.types.h265_level.deserialize_json(data["level"])
    if data.get("lookAheadRateControl") is not None:
        import capo_medialive.types.h265_look_ahead_rate_control

        out["look_ahead_rate_control"] = (
            capo_medialive.types.h265_look_ahead_rate_control.deserialize_json(
                data["lookAheadRateControl"]
            )
        )
    if data.get("maxBitrate") is not None:
        out["max_bitrate"] = data["maxBitrate"]
    if data.get("minIInterval") is not None:
        out["min_i_interval"] = data["minIInterval"]
    if data.get("parDenominator") is not None:
        out["par_denominator"] = data["parDenominator"]
    if data.get("parNumerator") is not None:
        out["par_numerator"] = data["parNumerator"]
    if data.get("profile") is not None:
        import capo_medialive.types.h265_profile

        out["profile"] = capo_medialive.types.h265_profile.deserialize_json(
            data["profile"]
        )
    if data.get("qvbrQualityLevel") is not None:
        out["qvbr_quality_level"] = data["qvbrQualityLevel"]
    if data.get("rateControlMode") is not None:
        import capo_medialive.types.h265_rate_control_mode

        out["rate_control_mode"] = (
            capo_medialive.types.h265_rate_control_mode.deserialize_json(
                data["rateControlMode"]
            )
        )
    if data.get("scanType") is not None:
        import capo_medialive.types.h265_scan_type

        out["scan_type"] = capo_medialive.types.h265_scan_type.deserialize_json(
            data["scanType"]
        )
    if data.get("sceneChangeDetect") is not None:
        import capo_medialive.types.h265_scene_change_detect

        out["scene_change_detect"] = (
            capo_medialive.types.h265_scene_change_detect.deserialize_json(
                data["sceneChangeDetect"]
            )
        )
    if data.get("slices") is not None:
        out["slices"] = data["slices"]
    if data.get("tier") is not None:
        import capo_medialive.types.h265_tier

        out["tier"] = capo_medialive.types.h265_tier.deserialize_json(data["tier"])
    if data.get("timecodeInsertion") is not None:
        import capo_medialive.types.h265_timecode_insertion_behavior

        out["timecode_insertion"] = (
            capo_medialive.types.h265_timecode_insertion_behavior.deserialize_json(
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
    if data.get("mvOverPictureBoundaries") is not None:
        import capo_medialive.types.h265_mv_over_picture_boundaries

        out["mv_over_picture_boundaries"] = (
            capo_medialive.types.h265_mv_over_picture_boundaries.deserialize_json(
                data["mvOverPictureBoundaries"]
            )
        )
    if data.get("mvTemporalPredictor") is not None:
        import capo_medialive.types.h265_mv_temporal_predictor

        out["mv_temporal_predictor"] = (
            capo_medialive.types.h265_mv_temporal_predictor.deserialize_json(
                data["mvTemporalPredictor"]
            )
        )
    if data.get("tileHeight") is not None:
        out["tile_height"] = data["tileHeight"]
    if data.get("tilePadding") is not None:
        import capo_medialive.types.h265_tile_padding

        out["tile_padding"] = capo_medialive.types.h265_tile_padding.deserialize_json(
            data["tilePadding"]
        )
    if data.get("tileWidth") is not None:
        out["tile_width"] = data["tileWidth"]
    if data.get("treeblockSize") is not None:
        import capo_medialive.types.h265_treeblock_size

        out["treeblock_size"] = (
            capo_medialive.types.h265_treeblock_size.deserialize_json(
                data["treeblockSize"]
            )
        )
    if data.get("minQp") is not None:
        out["min_qp"] = data["minQp"]
    if data.get("deblocking") is not None:
        import capo_medialive.types.h265_deblocking

        out["deblocking"] = capo_medialive.types.h265_deblocking.deserialize_json(
            data["deblocking"]
        )
    if data.get("gopBReference") is not None:
        import capo_medialive.types.h265_gop_b_reference

        out["gop_b_reference"] = (
            capo_medialive.types.h265_gop_b_reference.deserialize_json(
                data["gopBReference"]
            )
        )
    if data.get("gopNumBFrames") is not None:
        out["gop_num_b_frames"] = data["gopNumBFrames"]
    if data.get("minBitrate") is not None:
        out["min_bitrate"] = data["minBitrate"]
    if data.get("subgopLength") is not None:
        import capo_medialive.types.h265_sub_gop_length

        out["subgop_length"] = (
            capo_medialive.types.h265_sub_gop_length.deserialize_json(
                data["subgopLength"]
            )
        )
    return out
