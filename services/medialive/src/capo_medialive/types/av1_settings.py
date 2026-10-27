"""Generated from Smithy shape ``com.amazonaws.medialive#Av1Settings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__double_min0
    import capo_medialive.types.__integer_min0_max30
    import capo_medialive.types.__integer_min0_max8000000
    import capo_medialive.types.__integer_min1
    import capo_medialive.types.__integer_min1_max10
    import capo_medialive.types.__integer_min1_max3003
    import capo_medialive.types.__integer_min50000_max12000000
    import capo_medialive.types.__integer_min50000_max24000000
    import capo_medialive.types.afd_signaling
    import capo_medialive.types.av1_bit_depth
    import capo_medialive.types.av1_color_space_settings
    import capo_medialive.types.av1_filter_settings
    import capo_medialive.types.av1_gop_size_units
    import capo_medialive.types.av1_level
    import capo_medialive.types.av1_look_ahead_rate_control
    import capo_medialive.types.av1_rate_control_mode
    import capo_medialive.types.av1_scene_change_detect
    import capo_medialive.types.av1_spatial_aq
    import capo_medialive.types.av1_temporal_aq
    import capo_medialive.types.av1_timecode_insertion_behavior
    import capo_medialive.types.fixed_afd
    import capo_medialive.types.timecode_burnin_settings


class Av1Settings(TypedDict, closed=True):
    afd_signaling: NotRequired["capo_medialive.types.afd_signaling.AfdSignaling"]
    """Configures whether MediaLive will write AFD values into the video. AUTO: MediaLive will try to preserve the input AFD value (in cases where multiple AFD values are valid). FIXED: the AFD value will be the value configured in the fixedAfd parameter. NONE: MediaLive won't write AFD into the video"""
    buf_size: NotRequired[
        "capo_medialive.types.__integer_min50000_max24000000.__integerMin50000Max24000000"
    ]
    """The size of the buffer (HRD buffer model) in bits."""
    color_space_settings: NotRequired[
        "capo_medialive.types.av1_color_space_settings.Av1ColorSpaceSettings"
    ]
    """Specify the type of color space to apply or choose to pass through. The default is to pass through the color space that is in the source."""
    fixed_afd: NotRequired["capo_medialive.types.fixed_afd.FixedAfd"]
    """Complete this property only if you set the afdSignaling property to FIXED. Choose the AFD value (4 bits) to write on all frames of the video encode."""
    framerate_denominator: NotRequired[
        "capo_medialive.types.__integer_min1_max3003.__integerMin1Max3003"
    ]
    """The denominator for the framerate. Framerate is a fraction, for example, 24000 / 1001."""
    framerate_numerator: NotRequired[
        "capo_medialive.types.__integer_min1.__integerMin1"
    ]
    """The numerator for the framerate. Framerate is a fraction, for example, 24000 / 1001."""
    gop_size: NotRequired["capo_medialive.types.__double_min0.__doubleMin0"]
    """The GOP size (keyframe interval). If GopSizeUnits is frames, GopSize must be a whole number and must be greater than or equal to 1. If GopSizeUnits is seconds, GopSize must be greater than 0, but it can be a decimal."""
    gop_size_units: NotRequired[
        "capo_medialive.types.av1_gop_size_units.Av1GopSizeUnits"
    ]
    """Choose the units for the GOP size: FRAMES or SECONDS. For SECONDS, MediaLive converts the size into a frame count at run time."""
    level: NotRequired["capo_medialive.types.av1_level.Av1Level"]
    """Sets the level. This parameter is one of the properties of the encoding scheme for AV1."""
    look_ahead_rate_control: NotRequired[
        "capo_medialive.types.av1_look_ahead_rate_control.Av1LookAheadRateControl"
    ]
    """Sets the amount of lookahead. A value of LOW can decrease latency and memory usage. A value of HIGH can produce better quality for certain content."""
    max_bitrate: NotRequired[
        "capo_medialive.types.__integer_min50000_max12000000.__integerMin50000Max12000000"
    ]
    """The maximum bitrate to assign. For recommendations, see the description for qvbrQualityLevel."""
    min_i_interval: NotRequired[
        "capo_medialive.types.__integer_min0_max30.__integerMin0Max30"
    ]
    """Applies only if you enable SceneChangeDetect. Sets the interval between frames. This property ensures a minimum separation between repeated (cadence) I-frames and any I-frames inserted by scene change detection (SCD frames). Enter a number for the interval, measured in number of frames. If an SCD frame and a cadence frame are closer than the specified number of frames, MediaLive shrinks or stretches the GOP to include the SCD frame. Then normal cadence resumes in the next GOP. For GOP stretch to succeed, you must enable LookAheadRateControl. Note that the maximum GOP stretch = (GOP size) + (Minimum I-interval) - 1"""
    par_denominator: NotRequired["capo_medialive.types.__integer_min1.__integerMin1"]
    """The denominator for the output pixel aspect ratio (PAR)."""
    par_numerator: NotRequired["capo_medialive.types.__integer_min1.__integerMin1"]
    """The numerator for the output pixel aspect ratio (PAR)."""
    qvbr_quality_level: NotRequired[
        "capo_medialive.types.__integer_min1_max10.__integerMin1Max10"
    ]
    """Controls the target quality for the video encode. With QVBR rate control mode, the final quality is the target quality, constrained by the maxBitrate. Set values for the qvbrQualityLevel property and maxBitrate property that suit your most important viewing devices. To let MediaLive set the quality level (AUTO mode), leave the qvbrQualityLevel field empty. In this case, MediaLive uses the maximum bitrate, and the quality follows from that: more complex content might have a lower quality. Or set a target quality level and a maximum bitrate. With more complex content, MediaLive will try to achieve the target quality, but it won't exceed the maximum bitrate. With less complex content, This option will use only the bitrate needed to reach the target quality. Recommended values are: Primary screen: qvbrQualityLevel: Leave empty. maxBitrate: 4,000,000 PC or tablet: qvbrQualityLevel: Leave empty. maxBitrate: 1,500,000 to 3,000,000 Smartphone: qvbrQualityLevel: Leave empty. maxBitrate: 1,000,000 to 1,500,000"""
    scene_change_detect: NotRequired[
        "capo_medialive.types.av1_scene_change_detect.Av1SceneChangeDetect"
    ]
    """Controls whether MediaLive inserts I-frames when it detects a scene change. ENABLED or DISABLED."""
    timecode_burnin_settings: NotRequired[
        "capo_medialive.types.timecode_burnin_settings.TimecodeBurninSettings"
    ]
    """Configures the timecode burn-in feature. If you enable this feature, the timecode will become part of the video."""
    bitrate: NotRequired[
        "capo_medialive.types.__integer_min50000_max12000000.__integerMin50000Max12000000"
    ]
    """Average bitrate in bits/second. Required when the rate control mode is CBR. Not used for QVBR."""
    rate_control_mode: NotRequired[
        "capo_medialive.types.av1_rate_control_mode.Av1RateControlMode"
    ]
    """Rate control mode. QVBR: Quality will match the specified quality level except when it is constrained by the maximum bitrate. Recommended if you or your viewers pay for bandwidth. CBR: Quality varies, depending on the video complexity. Recommended only if you distribute your assets to devices that cannot handle variable bitrates."""
    min_bitrate: NotRequired[
        "capo_medialive.types.__integer_min0_max8000000.__integerMin0Max8000000"
    ]
    """Used for QVBR rate control mode only. Optional. Enter a minimum bitrate if you want to keep the output bitrate about a threshold, in order to prevent the downstream system from de-allocating network bandwidth for this output."""
    spatial_aq: NotRequired["capo_medialive.types.av1_spatial_aq.Av1SpatialAq"]
    """Spatial AQ makes adjustments within each frame based on spatial variation of content complexity. Enabled: MediaLive will determine the appropriate level of spatial AQ to apply. Disabled: No spatial AQ. For more information, see the topic about video adaptive quantization in the MediaLive user guide."""
    temporal_aq: NotRequired["capo_medialive.types.av1_temporal_aq.Av1TemporalAq"]
    """Temporal AQ makes adjustments within each frame based on variations in content complexity over time. Enabled: MediaLive will determine the appropriate level of temporal AQ to apply. Disabled: No temporal AQ. For more information, see the topic about video adaptive quantization in the MediaLive user guide."""
    timecode_insertion: NotRequired[
        "capo_medialive.types.av1_timecode_insertion_behavior.Av1TimecodeInsertionBehavior"
    ]
    """Controls how MediaLive inserts timecodes into the video output encode. DISABLED: Do not insert timecodes. METADATA_OBU: Include timecodes. MediaLive inserts timecode metadata based on the timecode from the source specified in the Timecode Config property. The timecode metadata is a metadata OBU (Open Bitstream Unit) of type METADATA_TYPE_TIMECODE, in accordance with https://aomediacodec.github.io/av1-spec/#metadata-timecode-syntax."""
    bit_depth: NotRequired["capo_medialive.types.av1_bit_depth.Av1BitDepth"]
    """Specifies the bit depth for the output encode. Choose a value. Or leave the field empty to use the default, which is 8 bit."""
    filter_settings: NotRequired[
        "capo_medialive.types.av1_filter_settings.Av1FilterSettings"
    ]
    """Optional filters that you can apply to an encode."""


# --- restJson1 ser/de ---
def serialize_json(value: Av1Settings) -> dict:
    out: dict = {}
    if "afd_signaling" in value:
        import capo_medialive.types.afd_signaling

        out["afdSignaling"] = capo_medialive.types.afd_signaling.serialize_json(
            value["afd_signaling"]
        )
    if "buf_size" in value:
        out["bufSize"] = value["buf_size"]
    if "color_space_settings" in value:
        import capo_medialive.types.av1_color_space_settings

        out["colorSpaceSettings"] = (
            capo_medialive.types.av1_color_space_settings.serialize_json(
                value["color_space_settings"]
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
        import capo_medialive.types.av1_gop_size_units

        out["gopSizeUnits"] = capo_medialive.types.av1_gop_size_units.serialize_json(
            value["gop_size_units"]
        )
    if "level" in value:
        import capo_medialive.types.av1_level

        out["level"] = capo_medialive.types.av1_level.serialize_json(value["level"])
    if "look_ahead_rate_control" in value:
        import capo_medialive.types.av1_look_ahead_rate_control

        out["lookAheadRateControl"] = (
            capo_medialive.types.av1_look_ahead_rate_control.serialize_json(
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
    if "qvbr_quality_level" in value:
        out["qvbrQualityLevel"] = value["qvbr_quality_level"]
    if "scene_change_detect" in value:
        import capo_medialive.types.av1_scene_change_detect

        out["sceneChangeDetect"] = (
            capo_medialive.types.av1_scene_change_detect.serialize_json(
                value["scene_change_detect"]
            )
        )
    if "timecode_burnin_settings" in value:
        import capo_medialive.types.timecode_burnin_settings

        out["timecodeBurninSettings"] = (
            capo_medialive.types.timecode_burnin_settings.serialize_json(
                value["timecode_burnin_settings"]
            )
        )
    if "bitrate" in value:
        out["bitrate"] = value["bitrate"]
    if "rate_control_mode" in value:
        import capo_medialive.types.av1_rate_control_mode

        out["rateControlMode"] = (
            capo_medialive.types.av1_rate_control_mode.serialize_json(
                value["rate_control_mode"]
            )
        )
    if "min_bitrate" in value:
        out["minBitrate"] = value["min_bitrate"]
    if "spatial_aq" in value:
        import capo_medialive.types.av1_spatial_aq

        out["spatialAq"] = capo_medialive.types.av1_spatial_aq.serialize_json(
            value["spatial_aq"]
        )
    if "temporal_aq" in value:
        import capo_medialive.types.av1_temporal_aq

        out["temporalAq"] = capo_medialive.types.av1_temporal_aq.serialize_json(
            value["temporal_aq"]
        )
    if "timecode_insertion" in value:
        import capo_medialive.types.av1_timecode_insertion_behavior

        out["timecodeInsertion"] = (
            capo_medialive.types.av1_timecode_insertion_behavior.serialize_json(
                value["timecode_insertion"]
            )
        )
    if "bit_depth" in value:
        import capo_medialive.types.av1_bit_depth

        out["bitDepth"] = capo_medialive.types.av1_bit_depth.serialize_json(
            value["bit_depth"]
        )
    if "filter_settings" in value:
        import capo_medialive.types.av1_filter_settings

        out["filterSettings"] = capo_medialive.types.av1_filter_settings.serialize_json(
            value["filter_settings"]
        )
    return out


def deserialize_json(data: dict) -> Av1Settings:
    out: Av1Settings = {}  # type: ignore[typeddict-item]
    if data.get("afdSignaling") is not None:
        import capo_medialive.types.afd_signaling

        out["afd_signaling"] = capo_medialive.types.afd_signaling.deserialize_json(
            data["afdSignaling"]
        )
    if data.get("bufSize") is not None:
        out["buf_size"] = data["bufSize"]
    if data.get("colorSpaceSettings") is not None:
        import capo_medialive.types.av1_color_space_settings

        out["color_space_settings"] = (
            capo_medialive.types.av1_color_space_settings.deserialize_json(
                data["colorSpaceSettings"]
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
    if data.get("gopSize") is not None:
        out["gop_size"] = float(data["gopSize"])
    if data.get("gopSizeUnits") is not None:
        import capo_medialive.types.av1_gop_size_units

        out["gop_size_units"] = (
            capo_medialive.types.av1_gop_size_units.deserialize_json(
                data["gopSizeUnits"]
            )
        )
    if data.get("level") is not None:
        import capo_medialive.types.av1_level

        out["level"] = capo_medialive.types.av1_level.deserialize_json(data["level"])
    if data.get("lookAheadRateControl") is not None:
        import capo_medialive.types.av1_look_ahead_rate_control

        out["look_ahead_rate_control"] = (
            capo_medialive.types.av1_look_ahead_rate_control.deserialize_json(
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
    if data.get("qvbrQualityLevel") is not None:
        out["qvbr_quality_level"] = data["qvbrQualityLevel"]
    if data.get("sceneChangeDetect") is not None:
        import capo_medialive.types.av1_scene_change_detect

        out["scene_change_detect"] = (
            capo_medialive.types.av1_scene_change_detect.deserialize_json(
                data["sceneChangeDetect"]
            )
        )
    if data.get("timecodeBurninSettings") is not None:
        import capo_medialive.types.timecode_burnin_settings

        out["timecode_burnin_settings"] = (
            capo_medialive.types.timecode_burnin_settings.deserialize_json(
                data["timecodeBurninSettings"]
            )
        )
    if data.get("bitrate") is not None:
        out["bitrate"] = data["bitrate"]
    if data.get("rateControlMode") is not None:
        import capo_medialive.types.av1_rate_control_mode

        out["rate_control_mode"] = (
            capo_medialive.types.av1_rate_control_mode.deserialize_json(
                data["rateControlMode"]
            )
        )
    if data.get("minBitrate") is not None:
        out["min_bitrate"] = data["minBitrate"]
    if data.get("spatialAq") is not None:
        import capo_medialive.types.av1_spatial_aq

        out["spatial_aq"] = capo_medialive.types.av1_spatial_aq.deserialize_json(
            data["spatialAq"]
        )
    if data.get("temporalAq") is not None:
        import capo_medialive.types.av1_temporal_aq

        out["temporal_aq"] = capo_medialive.types.av1_temporal_aq.deserialize_json(
            data["temporalAq"]
        )
    if data.get("timecodeInsertion") is not None:
        import capo_medialive.types.av1_timecode_insertion_behavior

        out["timecode_insertion"] = (
            capo_medialive.types.av1_timecode_insertion_behavior.deserialize_json(
                data["timecodeInsertion"]
            )
        )
    if data.get("bitDepth") is not None:
        import capo_medialive.types.av1_bit_depth

        out["bit_depth"] = capo_medialive.types.av1_bit_depth.deserialize_json(
            data["bitDepth"]
        )
    if data.get("filterSettings") is not None:
        import capo_medialive.types.av1_filter_settings

        out["filter_settings"] = (
            capo_medialive.types.av1_filter_settings.deserialize_json(
                data["filterSettings"]
            )
        )
    return out
