"""Generated from Smithy shape ``com.amazonaws.medialive#H264Settings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__double
    import capo_medialive.types.__integer_min0
    import capo_medialive.types.__integer_min0_max7
    import capo_medialive.types.__integer_min0_max30
    import capo_medialive.types.__integer_min0_max100
    import capo_medialive.types.__integer_min0_max128
    import capo_medialive.types.__integer_min1
    import capo_medialive.types.__integer_min1_max6
    import capo_medialive.types.__integer_min1_max10
    import capo_medialive.types.__integer_min1_max32
    import capo_medialive.types.__integer_min1_max51
    import capo_medialive.types.__integer_min1000
    import capo_medialive.types.afd_signaling
    import capo_medialive.types.fixed_afd
    import capo_medialive.types.h264_adaptive_quantization
    import capo_medialive.types.h264_color_metadata
    import capo_medialive.types.h264_color_space_settings
    import capo_medialive.types.h264_entropy_encoding
    import capo_medialive.types.h264_filter_settings
    import capo_medialive.types.h264_flicker_aq
    import capo_medialive.types.h264_force_field_pictures
    import capo_medialive.types.h264_framerate_control
    import capo_medialive.types.h264_gop_b_reference
    import capo_medialive.types.h264_gop_size_units
    import capo_medialive.types.h264_level
    import capo_medialive.types.h264_look_ahead_rate_control
    import capo_medialive.types.h264_par_control
    import capo_medialive.types.h264_profile
    import capo_medialive.types.h264_quality_level
    import capo_medialive.types.h264_rate_control_mode
    import capo_medialive.types.h264_scan_type
    import capo_medialive.types.h264_scene_change_detect
    import capo_medialive.types.h264_spatial_aq
    import capo_medialive.types.h264_sub_gop_length
    import capo_medialive.types.h264_syntax
    import capo_medialive.types.h264_temporal_aq
    import capo_medialive.types.h264_timecode_insertion_behavior
    import capo_medialive.types.timecode_burnin_settings


class H264Settings(TypedDict, closed=True):
    adaptive_quantization: NotRequired[
        "capo_medialive.types.h264_adaptive_quantization.H264AdaptiveQuantization"
    ]
    """Enables or disables adaptive quantization (AQ), which is a technique MediaLive can apply to video on a frame-by-frame basis to produce more compression without losing quality. There are three types of adaptive quantization: spatial, temporal, and flicker. We recommend that you set the field to Auto. For more information about all the options, see the topic about video adaptive quantization in the MediaLive user guide."""
    afd_signaling: NotRequired["capo_medialive.types.afd_signaling.AfdSignaling"]
    """Indicates that AFD values will be written into the output stream. If afdSignaling is "auto", the system will try to preserve the input AFD value (in cases where multiple AFD values are valid). If set to "fixed", the AFD value will be the value configured in the fixedAfd parameter."""
    bitrate: NotRequired["capo_medialive.types.__integer_min1000.__integerMin1000"]
    """Average bitrate in bits/second. Required when the rate control mode is VBR or CBR. Not used for QVBR. In an MS Smooth output group, each output must have a unique value when its bitrate is rounded down to the nearest multiple of 1000."""
    buf_fill_pct: NotRequired[
        "capo_medialive.types.__integer_min0_max100.__integerMin0Max100"
    ]
    """Percentage of the buffer that should initially be filled (HRD buffer model)."""
    buf_size: NotRequired["capo_medialive.types.__integer_min0.__integerMin0"]
    """Size of buffer (HRD buffer model) in bits."""
    color_metadata: NotRequired[
        "capo_medialive.types.h264_color_metadata.H264ColorMetadata"
    ]
    """Includes colorspace metadata in the output."""
    color_space_settings: NotRequired[
        "capo_medialive.types.h264_color_space_settings.H264ColorSpaceSettings"
    ]
    """Specify the type of color space to apply or choose to pass through. The default is to pass through the color space that is in the source."""
    entropy_encoding: NotRequired[
        "capo_medialive.types.h264_entropy_encoding.H264EntropyEncoding"
    ]
    """Entropy encoding mode. Use cabac (must be in Main or High profile) or cavlc."""
    filter_settings: NotRequired[
        "capo_medialive.types.h264_filter_settings.H264FilterSettings"
    ]
    """Optional. Both filters reduce bandwidth by removing imperceptible details. You can enable one of the filters. We recommend that you try both filters and observe the results to decide which one to use. The Temporal Filter reduces bandwidth by removing imperceptible details in the content. It combines perceptual filtering and motion compensated temporal filtering (MCTF). It operates independently of the compression level. The Bandwidth Reduction filter is a perceptual filter located within the encoding loop. It adapts to the current compression level to filter imperceptible signals. This filter works only when the resolution is 1080p or lower."""
    fixed_afd: NotRequired["capo_medialive.types.fixed_afd.FixedAfd"]
    """Four bit AFD value to write on all frames of video in the output stream. Only valid when afdSignaling is set to 'Fixed'."""
    flicker_aq: NotRequired["capo_medialive.types.h264_flicker_aq.H264FlickerAq"]
    """Flicker AQ makes adjustments within each frame to reduce flicker or 'pop' on I-frames. The value to enter in this field depends on the value in the Adaptive quantization field. For more information, see the topic about video adaptive quantization in the MediaLive user guide."""
    force_field_pictures: NotRequired[
        "capo_medialive.types.h264_force_field_pictures.H264ForceFieldPictures"
    ]
    """This setting applies only when scan type is "interlaced." It controls whether coding is performed on a field basis or on a frame basis. (When the video is progressive, the coding is always performed on a frame basis.) enabled: Force MediaLive to code on a field basis, so that odd and even sets of fields are coded separately. disabled: Code the two sets of fields separately (on a field basis) or together (on a frame basis using PAFF), depending on what is most appropriate for the content."""
    framerate_control: NotRequired[
        "capo_medialive.types.h264_framerate_control.H264FramerateControl"
    ]
    """This field indicates how the output video frame rate is specified. If "specified" is selected then the output video frame rate is determined by framerateNumerator and framerateDenominator, else if "initializeFromSource" is selected then the output video frame rate will be set equal to the input video frame rate of the first input."""
    framerate_denominator: NotRequired[
        "capo_medialive.types.__integer_min1.__integerMin1"
    ]
    """Framerate denominator."""
    framerate_numerator: NotRequired[
        "capo_medialive.types.__integer_min1.__integerMin1"
    ]
    """Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976 fps."""
    gop_b_reference: NotRequired[
        "capo_medialive.types.h264_gop_b_reference.H264GopBReference"
    ]
    """Documentation update needed"""
    gop_closed_cadence: NotRequired["capo_medialive.types.__integer_min0.__integerMin0"]
    """Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting."""
    gop_num_b_frames: NotRequired[
        "capo_medialive.types.__integer_min0_max7.__integerMin0Max7"
    ]
    """Number of B-frames between reference frames."""
    gop_size: NotRequired["capo_medialive.types.__double.__double"]
    """GOP size (keyframe interval) in units of either frames or seconds per gopSizeUnits. If gopSizeUnits is frames, gopSize must be an integer and must be greater than or equal to 1. If gopSizeUnits is seconds, gopSize must be greater than 0, but need not be an integer."""
    gop_size_units: NotRequired[
        "capo_medialive.types.h264_gop_size_units.H264GopSizeUnits"
    ]
    """Indicates if the gopSize is specified in frames or seconds. If seconds the system will convert the gopSize into a frame count at run time."""
    level: NotRequired["capo_medialive.types.h264_level.H264Level"]
    """H.264 Level."""
    look_ahead_rate_control: NotRequired[
        "capo_medialive.types.h264_look_ahead_rate_control.H264LookAheadRateControl"
    ]
    """Amount of lookahead. A value of low can decrease latency and memory usage, while high can produce better quality for certain content."""
    max_bitrate: NotRequired["capo_medialive.types.__integer_min1000.__integerMin1000"]
    """For QVBR: See the tooltip for Quality level For VBR: Set the maximum bitrate in order to accommodate expected spikes in the complexity of the video."""
    min_i_interval: NotRequired[
        "capo_medialive.types.__integer_min0_max30.__integerMin0Max30"
    ]
    """Only meaningful if sceneChangeDetect is set to enabled. Defaults to 5 if multiplex rate control is used. Enforces separation between repeated (cadence) I-frames and I-frames inserted by Scene Change Detection. If a scene change I-frame is within I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch requires enabling lookahead as well as setting I-interval. The normal cadence resumes for the next GOP. Note: Maximum GOP stretch = GOP size + Min-I-interval - 1"""
    num_ref_frames: NotRequired[
        "capo_medialive.types.__integer_min1_max6.__integerMin1Max6"
    ]
    """Number of reference frames to use. The encoder may use more than requested if using B-frames and/or interlaced encoding."""
    par_control: NotRequired["capo_medialive.types.h264_par_control.H264ParControl"]
    """This field indicates how the output pixel aspect ratio is specified. If "specified" is selected then the output video pixel aspect ratio is determined by parNumerator and parDenominator, else if "initializeFromSource" is selected then the output pixsel aspect ratio will be set equal to the input video pixel aspect ratio of the first input."""
    par_denominator: NotRequired["capo_medialive.types.__integer_min1.__integerMin1"]
    """Pixel Aspect Ratio denominator."""
    par_numerator: NotRequired["capo_medialive.types.__integer_min1.__integerMin1"]
    """Pixel Aspect Ratio numerator."""
    profile: NotRequired["capo_medialive.types.h264_profile.H264Profile"]
    """H.264 Profile."""
    quality_level: NotRequired[
        "capo_medialive.types.h264_quality_level.H264QualityLevel"
    ]
    """Leave as STANDARD_QUALITY or choose a different value (which might result in additional costs to run the channel). - ENHANCED_QUALITY: Produces a slightly better video quality without an increase in the bitrate. Has an effect only when the Rate control mode is QVBR or CBR. If this channel is in a MediaLive multiplex, the value must be ENHANCED_QUALITY. - STANDARD_QUALITY: Valid for any Rate control mode."""
    qvbr_quality_level: NotRequired[
        "capo_medialive.types.__integer_min1_max10.__integerMin1Max10"
    ]
    """Controls the target quality for the video encode. Applies only when the rate control mode is QVBR. You can set a target quality or you can let MediaLive determine the best quality. To set a target quality, enter values in the QVBR quality level field and the Max bitrate field. Enter values that suit your most important viewing devices. Recommended values are: - Primary screen: Quality level: 8 to 10. Max bitrate: 4M - PC or tablet: Quality level: 7. Max bitrate: 1.5M to 3M - Smartphone: Quality level: 6. Max bitrate: 1M to 1.5M To let MediaLive decide, leave the QVBR quality level field empty, and in Max bitrate enter the maximum rate you want in the video. For more information, see the section called "Video - rate control mode" in the MediaLive user guide"""
    rate_control_mode: NotRequired[
        "capo_medialive.types.h264_rate_control_mode.H264RateControlMode"
    ]
    """Rate control mode. QVBR: Quality will match the specified quality level except when it is constrained by the maximum bitrate. Recommended if you or your viewers pay for bandwidth. VBR: Quality and bitrate vary, depending on the video complexity. Recommended instead of QVBR if you want to maintain a specific average bitrate over the duration of the channel. CBR: Quality varies, depending on the video complexity. Recommended only if you distribute your assets to devices that cannot handle variable bitrates. Multiplex: This rate control mode is only supported (and is required) when the video is being delivered to a MediaLive Multiplex in which case the rate control configuration is controlled by the properties within the Multiplex Program."""
    scan_type: NotRequired["capo_medialive.types.h264_scan_type.H264ScanType"]
    """Sets the scan type of the output to progressive or top-field-first interlaced."""
    scene_change_detect: NotRequired[
        "capo_medialive.types.h264_scene_change_detect.H264SceneChangeDetect"
    ]
    """Scene change detection. - On: inserts I-frames when scene change is detected. - Off: does not force an I-frame when scene change is detected."""
    slices: NotRequired["capo_medialive.types.__integer_min1_max32.__integerMin1Max32"]
    """Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures. This field is optional; when no value is specified the encoder will choose the number of slices based on encode resolution."""
    softness: NotRequired[
        "capo_medialive.types.__integer_min0_max128.__integerMin0Max128"
    ]
    """Softness. Selects quantizer matrix, larger values reduce high-frequency content in the encoded image. If not set to zero, must be greater than 15."""
    spatial_aq: NotRequired["capo_medialive.types.h264_spatial_aq.H264SpatialAq"]
    """Spatial AQ makes adjustments within each frame based on spatial variation of content complexity. The value to enter in this field depends on the value in the Adaptive quantization field. For more information, see the topic about video adaptive quantization in the MediaLive user guide."""
    subgop_length: NotRequired[
        "capo_medialive.types.h264_sub_gop_length.H264SubGopLength"
    ]
    """If set to fixed, use gopNumBFrames B-frames per sub-GOP. If set to dynamic, optimize the number of B-frames used for each sub-GOP to improve visual quality."""
    syntax: NotRequired["capo_medialive.types.h264_syntax.H264Syntax"]
    """Produces a bitstream compliant with SMPTE RP-2027."""
    temporal_aq: NotRequired["capo_medialive.types.h264_temporal_aq.H264TemporalAq"]
    """Temporal makes adjustments within each frame based on variations in content complexity over time. The value to enter in this field depends on the value in the Adaptive quantization field. For more information, see the topic about video adaptive quantization in the MediaLive user guide."""
    timecode_insertion: NotRequired[
        "capo_medialive.types.h264_timecode_insertion_behavior.H264TimecodeInsertionBehavior"
    ]
    """Determines how timecodes should be inserted into the video elementary stream. - 'disabled': Do not include timecodes - 'picTimingSei': Pass through picture timing SEI messages from the source specified in Timecode Config"""
    timecode_burnin_settings: NotRequired[
        "capo_medialive.types.timecode_burnin_settings.TimecodeBurninSettings"
    ]
    """Timecode burn-in settings"""
    min_qp: NotRequired["capo_medialive.types.__integer_min1_max51.__integerMin1Max51"]
    """Sets the minimum QP. If you aren't familiar with quantization adjustment, leave the field empty. MediaLive will apply an appropriate value."""
    min_bitrate: NotRequired["capo_medialive.types.__integer_min0.__integerMin0"]
    """Used for QVBR rate control mode only. Optional. Enter a minimum bitrate if you want to keep the output bitrate about a threshold, in order to prevent the downstream system from de-allocating network bandwidth for this output."""


# --- restJson1 ser/de ---
def serialize_json(value: H264Settings) -> dict:
    out: dict = {}
    if "adaptive_quantization" in value:
        import capo_medialive.types.h264_adaptive_quantization

        out["adaptiveQuantization"] = (
            capo_medialive.types.h264_adaptive_quantization.serialize_json(
                value["adaptive_quantization"]
            )
        )
    if "afd_signaling" in value:
        import capo_medialive.types.afd_signaling

        out["afdSignaling"] = capo_medialive.types.afd_signaling.serialize_json(
            value["afd_signaling"]
        )
    if "bitrate" in value:
        out["bitrate"] = value["bitrate"]
    if "buf_fill_pct" in value:
        out["bufFillPct"] = value["buf_fill_pct"]
    if "buf_size" in value:
        out["bufSize"] = value["buf_size"]
    if "color_metadata" in value:
        import capo_medialive.types.h264_color_metadata

        out["colorMetadata"] = capo_medialive.types.h264_color_metadata.serialize_json(
            value["color_metadata"]
        )
    if "color_space_settings" in value:
        import capo_medialive.types.h264_color_space_settings

        out["colorSpaceSettings"] = (
            capo_medialive.types.h264_color_space_settings.serialize_json(
                value["color_space_settings"]
            )
        )
    if "entropy_encoding" in value:
        import capo_medialive.types.h264_entropy_encoding

        out["entropyEncoding"] = (
            capo_medialive.types.h264_entropy_encoding.serialize_json(
                value["entropy_encoding"]
            )
        )
    if "filter_settings" in value:
        import capo_medialive.types.h264_filter_settings

        out["filterSettings"] = (
            capo_medialive.types.h264_filter_settings.serialize_json(
                value["filter_settings"]
            )
        )
    if "fixed_afd" in value:
        import capo_medialive.types.fixed_afd

        out["fixedAfd"] = capo_medialive.types.fixed_afd.serialize_json(
            value["fixed_afd"]
        )
    if "flicker_aq" in value:
        import capo_medialive.types.h264_flicker_aq

        out["flickerAq"] = capo_medialive.types.h264_flicker_aq.serialize_json(
            value["flicker_aq"]
        )
    if "force_field_pictures" in value:
        import capo_medialive.types.h264_force_field_pictures

        out["forceFieldPictures"] = (
            capo_medialive.types.h264_force_field_pictures.serialize_json(
                value["force_field_pictures"]
            )
        )
    if "framerate_control" in value:
        import capo_medialive.types.h264_framerate_control

        out["framerateControl"] = (
            capo_medialive.types.h264_framerate_control.serialize_json(
                value["framerate_control"]
            )
        )
    if "framerate_denominator" in value:
        out["framerateDenominator"] = value["framerate_denominator"]
    if "framerate_numerator" in value:
        out["framerateNumerator"] = value["framerate_numerator"]
    if "gop_b_reference" in value:
        import capo_medialive.types.h264_gop_b_reference

        out["gopBReference"] = capo_medialive.types.h264_gop_b_reference.serialize_json(
            value["gop_b_reference"]
        )
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
        import capo_medialive.types.h264_gop_size_units

        out["gopSizeUnits"] = capo_medialive.types.h264_gop_size_units.serialize_json(
            value["gop_size_units"]
        )
    if "level" in value:
        import capo_medialive.types.h264_level

        out["level"] = capo_medialive.types.h264_level.serialize_json(value["level"])
    if "look_ahead_rate_control" in value:
        import capo_medialive.types.h264_look_ahead_rate_control

        out["lookAheadRateControl"] = (
            capo_medialive.types.h264_look_ahead_rate_control.serialize_json(
                value["look_ahead_rate_control"]
            )
        )
    if "max_bitrate" in value:
        out["maxBitrate"] = value["max_bitrate"]
    if "min_i_interval" in value:
        out["minIInterval"] = value["min_i_interval"]
    if "num_ref_frames" in value:
        out["numRefFrames"] = value["num_ref_frames"]
    if "par_control" in value:
        import capo_medialive.types.h264_par_control

        out["parControl"] = capo_medialive.types.h264_par_control.serialize_json(
            value["par_control"]
        )
    if "par_denominator" in value:
        out["parDenominator"] = value["par_denominator"]
    if "par_numerator" in value:
        out["parNumerator"] = value["par_numerator"]
    if "profile" in value:
        import capo_medialive.types.h264_profile

        out["profile"] = capo_medialive.types.h264_profile.serialize_json(
            value["profile"]
        )
    if "quality_level" in value:
        import capo_medialive.types.h264_quality_level

        out["qualityLevel"] = capo_medialive.types.h264_quality_level.serialize_json(
            value["quality_level"]
        )
    if "qvbr_quality_level" in value:
        out["qvbrQualityLevel"] = value["qvbr_quality_level"]
    if "rate_control_mode" in value:
        import capo_medialive.types.h264_rate_control_mode

        out["rateControlMode"] = (
            capo_medialive.types.h264_rate_control_mode.serialize_json(
                value["rate_control_mode"]
            )
        )
    if "scan_type" in value:
        import capo_medialive.types.h264_scan_type

        out["scanType"] = capo_medialive.types.h264_scan_type.serialize_json(
            value["scan_type"]
        )
    if "scene_change_detect" in value:
        import capo_medialive.types.h264_scene_change_detect

        out["sceneChangeDetect"] = (
            capo_medialive.types.h264_scene_change_detect.serialize_json(
                value["scene_change_detect"]
            )
        )
    if "slices" in value:
        out["slices"] = value["slices"]
    if "softness" in value:
        out["softness"] = value["softness"]
    if "spatial_aq" in value:
        import capo_medialive.types.h264_spatial_aq

        out["spatialAq"] = capo_medialive.types.h264_spatial_aq.serialize_json(
            value["spatial_aq"]
        )
    if "subgop_length" in value:
        import capo_medialive.types.h264_sub_gop_length

        out["subgopLength"] = capo_medialive.types.h264_sub_gop_length.serialize_json(
            value["subgop_length"]
        )
    if "syntax" in value:
        import capo_medialive.types.h264_syntax

        out["syntax"] = capo_medialive.types.h264_syntax.serialize_json(value["syntax"])
    if "temporal_aq" in value:
        import capo_medialive.types.h264_temporal_aq

        out["temporalAq"] = capo_medialive.types.h264_temporal_aq.serialize_json(
            value["temporal_aq"]
        )
    if "timecode_insertion" in value:
        import capo_medialive.types.h264_timecode_insertion_behavior

        out["timecodeInsertion"] = (
            capo_medialive.types.h264_timecode_insertion_behavior.serialize_json(
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
    if "min_qp" in value:
        out["minQp"] = value["min_qp"]
    if "min_bitrate" in value:
        out["minBitrate"] = value["min_bitrate"]
    return out


def deserialize_json(data: dict) -> H264Settings:
    out: H264Settings = {}  # type: ignore[typeddict-item]
    if data.get("adaptiveQuantization") is not None:
        import capo_medialive.types.h264_adaptive_quantization

        out["adaptive_quantization"] = (
            capo_medialive.types.h264_adaptive_quantization.deserialize_json(
                data["adaptiveQuantization"]
            )
        )
    if data.get("afdSignaling") is not None:
        import capo_medialive.types.afd_signaling

        out["afd_signaling"] = capo_medialive.types.afd_signaling.deserialize_json(
            data["afdSignaling"]
        )
    if data.get("bitrate") is not None:
        out["bitrate"] = data["bitrate"]
    if data.get("bufFillPct") is not None:
        out["buf_fill_pct"] = data["bufFillPct"]
    if data.get("bufSize") is not None:
        out["buf_size"] = data["bufSize"]
    if data.get("colorMetadata") is not None:
        import capo_medialive.types.h264_color_metadata

        out["color_metadata"] = (
            capo_medialive.types.h264_color_metadata.deserialize_json(
                data["colorMetadata"]
            )
        )
    if data.get("colorSpaceSettings") is not None:
        import capo_medialive.types.h264_color_space_settings

        out["color_space_settings"] = (
            capo_medialive.types.h264_color_space_settings.deserialize_json(
                data["colorSpaceSettings"]
            )
        )
    if data.get("entropyEncoding") is not None:
        import capo_medialive.types.h264_entropy_encoding

        out["entropy_encoding"] = (
            capo_medialive.types.h264_entropy_encoding.deserialize_json(
                data["entropyEncoding"]
            )
        )
    if data.get("filterSettings") is not None:
        import capo_medialive.types.h264_filter_settings

        out["filter_settings"] = (
            capo_medialive.types.h264_filter_settings.deserialize_json(
                data["filterSettings"]
            )
        )
    if data.get("fixedAfd") is not None:
        import capo_medialive.types.fixed_afd

        out["fixed_afd"] = capo_medialive.types.fixed_afd.deserialize_json(
            data["fixedAfd"]
        )
    if data.get("flickerAq") is not None:
        import capo_medialive.types.h264_flicker_aq

        out["flicker_aq"] = capo_medialive.types.h264_flicker_aq.deserialize_json(
            data["flickerAq"]
        )
    if data.get("forceFieldPictures") is not None:
        import capo_medialive.types.h264_force_field_pictures

        out["force_field_pictures"] = (
            capo_medialive.types.h264_force_field_pictures.deserialize_json(
                data["forceFieldPictures"]
            )
        )
    if data.get("framerateControl") is not None:
        import capo_medialive.types.h264_framerate_control

        out["framerate_control"] = (
            capo_medialive.types.h264_framerate_control.deserialize_json(
                data["framerateControl"]
            )
        )
    if data.get("framerateDenominator") is not None:
        out["framerate_denominator"] = data["framerateDenominator"]
    if data.get("framerateNumerator") is not None:
        out["framerate_numerator"] = data["framerateNumerator"]
    if data.get("gopBReference") is not None:
        import capo_medialive.types.h264_gop_b_reference

        out["gop_b_reference"] = (
            capo_medialive.types.h264_gop_b_reference.deserialize_json(
                data["gopBReference"]
            )
        )
    if data.get("gopClosedCadence") is not None:
        out["gop_closed_cadence"] = data["gopClosedCadence"]
    if data.get("gopNumBFrames") is not None:
        out["gop_num_b_frames"] = data["gopNumBFrames"]
    if data.get("gopSize") is not None:
        out["gop_size"] = float(data["gopSize"])
    if data.get("gopSizeUnits") is not None:
        import capo_medialive.types.h264_gop_size_units

        out["gop_size_units"] = (
            capo_medialive.types.h264_gop_size_units.deserialize_json(
                data["gopSizeUnits"]
            )
        )
    if data.get("level") is not None:
        import capo_medialive.types.h264_level

        out["level"] = capo_medialive.types.h264_level.deserialize_json(data["level"])
    if data.get("lookAheadRateControl") is not None:
        import capo_medialive.types.h264_look_ahead_rate_control

        out["look_ahead_rate_control"] = (
            capo_medialive.types.h264_look_ahead_rate_control.deserialize_json(
                data["lookAheadRateControl"]
            )
        )
    if data.get("maxBitrate") is not None:
        out["max_bitrate"] = data["maxBitrate"]
    if data.get("minIInterval") is not None:
        out["min_i_interval"] = data["minIInterval"]
    if data.get("numRefFrames") is not None:
        out["num_ref_frames"] = data["numRefFrames"]
    if data.get("parControl") is not None:
        import capo_medialive.types.h264_par_control

        out["par_control"] = capo_medialive.types.h264_par_control.deserialize_json(
            data["parControl"]
        )
    if data.get("parDenominator") is not None:
        out["par_denominator"] = data["parDenominator"]
    if data.get("parNumerator") is not None:
        out["par_numerator"] = data["parNumerator"]
    if data.get("profile") is not None:
        import capo_medialive.types.h264_profile

        out["profile"] = capo_medialive.types.h264_profile.deserialize_json(
            data["profile"]
        )
    if data.get("qualityLevel") is not None:
        import capo_medialive.types.h264_quality_level

        out["quality_level"] = capo_medialive.types.h264_quality_level.deserialize_json(
            data["qualityLevel"]
        )
    if data.get("qvbrQualityLevel") is not None:
        out["qvbr_quality_level"] = data["qvbrQualityLevel"]
    if data.get("rateControlMode") is not None:
        import capo_medialive.types.h264_rate_control_mode

        out["rate_control_mode"] = (
            capo_medialive.types.h264_rate_control_mode.deserialize_json(
                data["rateControlMode"]
            )
        )
    if data.get("scanType") is not None:
        import capo_medialive.types.h264_scan_type

        out["scan_type"] = capo_medialive.types.h264_scan_type.deserialize_json(
            data["scanType"]
        )
    if data.get("sceneChangeDetect") is not None:
        import capo_medialive.types.h264_scene_change_detect

        out["scene_change_detect"] = (
            capo_medialive.types.h264_scene_change_detect.deserialize_json(
                data["sceneChangeDetect"]
            )
        )
    if data.get("slices") is not None:
        out["slices"] = data["slices"]
    if data.get("softness") is not None:
        out["softness"] = data["softness"]
    if data.get("spatialAq") is not None:
        import capo_medialive.types.h264_spatial_aq

        out["spatial_aq"] = capo_medialive.types.h264_spatial_aq.deserialize_json(
            data["spatialAq"]
        )
    if data.get("subgopLength") is not None:
        import capo_medialive.types.h264_sub_gop_length

        out["subgop_length"] = (
            capo_medialive.types.h264_sub_gop_length.deserialize_json(
                data["subgopLength"]
            )
        )
    if data.get("syntax") is not None:
        import capo_medialive.types.h264_syntax

        out["syntax"] = capo_medialive.types.h264_syntax.deserialize_json(
            data["syntax"]
        )
    if data.get("temporalAq") is not None:
        import capo_medialive.types.h264_temporal_aq

        out["temporal_aq"] = capo_medialive.types.h264_temporal_aq.deserialize_json(
            data["temporalAq"]
        )
    if data.get("timecodeInsertion") is not None:
        import capo_medialive.types.h264_timecode_insertion_behavior

        out["timecode_insertion"] = (
            capo_medialive.types.h264_timecode_insertion_behavior.deserialize_json(
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
    if data.get("minQp") is not None:
        out["min_qp"] = data["minQp"]
    if data.get("minBitrate") is not None:
        out["min_bitrate"] = data["minBitrate"]
    return out
