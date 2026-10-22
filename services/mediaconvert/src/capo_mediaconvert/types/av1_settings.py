"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Av1Settings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__double_min0
    import capo_mediaconvert.types.__integer_min0_max15
    import capo_mediaconvert.types.__integer_min1_max32
    import capo_mediaconvert.types.__integer_min1_max2147483647
    import capo_mediaconvert.types.__integer_min1000_max3000
    import capo_mediaconvert.types.__integer_min1000_max1152000000
    import capo_mediaconvert.types.__list_of_frame_metric_type
    import capo_mediaconvert.types.av1_adaptive_quantization
    import capo_mediaconvert.types.av1_bit_depth
    import capo_mediaconvert.types.av1_film_grain_synthesis
    import capo_mediaconvert.types.av1_framerate_control
    import capo_mediaconvert.types.av1_framerate_conversion_algorithm
    import capo_mediaconvert.types.av1_qvbr_settings
    import capo_mediaconvert.types.av1_rate_control_mode
    import capo_mediaconvert.types.av1_scene_change_detect
    import capo_mediaconvert.types.av1_spatial_adaptive_quantization


class Av1Settings(TypedDict, closed=True):
    adaptive_quantization: NotRequired[
        "capo_mediaconvert.types.av1_adaptive_quantization.Av1AdaptiveQuantization"
    ]
    """Specify the strength of any adaptive quantization filters that you enable. The value that you choose here applies to Spatial adaptive quantization."""
    bit_depth: NotRequired["capo_mediaconvert.types.av1_bit_depth.Av1BitDepth"]
    """Specify the Bit depth. You can choose 8-bit or 10-bit."""
    bitrate: NotRequired[
        "capo_mediaconvert.types.__integer_min1000_max1152000000.__integerMin1000Max1152000000"
    ]
    """Specify the average bitrate in bits per second. Required when Rate control mode is CBR."""
    film_grain_synthesis: NotRequired[
        "capo_mediaconvert.types.av1_film_grain_synthesis.Av1FilmGrainSynthesis"
    ]
    """Film grain synthesis replaces film grain present in your content with similar quality synthesized AV1 film grain. We recommend that you choose Enabled to reduce the bandwidth of your QVBR quality level 5, 6, 7, or 8 outputs. For QVBR quality level 9 or 10 outputs we recommend that you keep the default value, Disabled. When you include Film grain synthesis, you cannot include the Noise reducer preprocessor."""
    framerate_control: NotRequired[
        "capo_mediaconvert.types.av1_framerate_control.Av1FramerateControl"
    ]
    """Use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction."""
    framerate_conversion_algorithm: NotRequired[
        "capo_mediaconvert.types.av1_framerate_conversion_algorithm.Av1FramerateConversionAlgorithm"
    ]
    """Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates."""
    framerate_denominator: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976."""
    framerate_numerator: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976."""
    gop_size: NotRequired["capo_mediaconvert.types.__double_min0.__doubleMin0"]
    """Specify the GOP length (keyframe interval) in frames. With AV1, MediaConvert doesn't support GOP length in seconds. This value must be greater than zero and preferably equal to 1 + ((numberBFrames + 1) * x), where x is an integer value."""
    max_bitrate: NotRequired[
        "capo_mediaconvert.types.__integer_min1000_max1152000000.__integerMin1000Max1152000000"
    ]
    """Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. Required when Rate control mode is QVBR."""
    number_b_frames_between_reference_frames: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max15.__integerMin0Max15"
    ]
    """Specify from the number of B-frames, in the range of 0-15. For AV1 encoding, we recommend using 7 or 15. Choose a larger number for a lower bitrate and smaller file size; choose a smaller number for better video quality."""
    per_frame_metrics: NotRequired[
        "capo_mediaconvert.types.__list_of_frame_metric_type.__listOfFrameMetricType"
    ]
    """Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: * PSNR: Peak Signal-to-Noise Ratio * SSIM: Structural Similarity Index Measure * MS_SSIM: Multi-Scale Similarity Index Measure * PSNR_HVS: Peak Signal-to-Noise Ratio, Human Visual System * VMAF: Video Multi-Method Assessment Fusion * QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. * SHOT_CHANGE: Shot Changes"""
    qvbr_settings: NotRequired[
        "capo_mediaconvert.types.av1_qvbr_settings.Av1QvbrSettings"
    ]
    """Settings for quality-defined variable bitrate encoding with the AV1 codec. Use these settings only when you set QVBR for Rate control mode."""
    rate_control_mode: NotRequired[
        "capo_mediaconvert.types.av1_rate_control_mode.Av1RateControlMode"
    ]
    """'With AV1 outputs, for rate control mode, MediaConvert supports quality-defined variable bitrate (QVBR) and constant bitrate (CBR). You can''t use VBR.'"""
    scene_change_detect: NotRequired[
        "capo_mediaconvert.types.av1_scene_change_detect.Av1SceneChangeDetect"
    ]
    """Optional. Use this setting to have the service insert I-frames at scene changes that it automatically detects. For AV1, scene change detection is disabled by default. Choose Enabled to insert I-frames at detected scene changes, which can improve video quality. If this output uses QVBR, you can instead choose Transition detection for further video quality improvement. For more information about QVBR, see https://docs.aws.amazon.com/console/mediaconvert/cbr-vbr-qvbr."""
    slices: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max32.__integerMin1Max32"
    ]
    """Specify the number of slices per picture. This value must be 1, 2, 4, 8, 16, or 32. For progressive pictures, this value must be less than or equal to the number of macroblock rows. For interlaced pictures, this value must be less than or equal to half the number of macroblock rows."""
    sliding_window_ms: NotRequired[
        "capo_mediaconvert.types.__integer_min1000_max3000.__integerMin1000Max3000"
    ]
    """Optional. Specify the duration, in milliseconds, of the sliding window over which MediaConvert enforces your Peak bitrate. When you specify a Peak bitrate but omit this value, MediaConvert uses a default sliding window of 1000."""
    sliding_window_peak_bitrate: NotRequired[
        "capo_mediaconvert.types.__integer_min1000_max1152000000.__integerMin1000Max1152000000"
    ]
    """Optional. Specify an instantaneous peak bitrate ceiling, in bits/second, that MediaConvert enforces over the sliding window set by Peak bitrate window. For example, enter fifty megabits per second as 50000000. Applies in the QVBR rate control mode. When you specify a value below Max bitrate, MediaConvert raises it to Max bitrate."""
    spatial_adaptive_quantization: NotRequired[
        "capo_mediaconvert.types.av1_spatial_adaptive_quantization.Av1SpatialAdaptiveQuantization"
    ]
    """Keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher."""


# --- restJson1 ser/de ---
def serialize_json(value: Av1Settings) -> dict:
    out: dict = {}
    if "adaptive_quantization" in value:
        import capo_mediaconvert.types.av1_adaptive_quantization

        out["adaptiveQuantization"] = (
            capo_mediaconvert.types.av1_adaptive_quantization.serialize_json(
                value["adaptive_quantization"]
            )
        )
    if "bit_depth" in value:
        import capo_mediaconvert.types.av1_bit_depth

        out["bitDepth"] = capo_mediaconvert.types.av1_bit_depth.serialize_json(
            value["bit_depth"]
        )
    if "bitrate" in value:
        out["bitrate"] = value["bitrate"]
    if "film_grain_synthesis" in value:
        import capo_mediaconvert.types.av1_film_grain_synthesis

        out["filmGrainSynthesis"] = (
            capo_mediaconvert.types.av1_film_grain_synthesis.serialize_json(
                value["film_grain_synthesis"]
            )
        )
    if "framerate_control" in value:
        import capo_mediaconvert.types.av1_framerate_control

        out["framerateControl"] = (
            capo_mediaconvert.types.av1_framerate_control.serialize_json(
                value["framerate_control"]
            )
        )
    if "framerate_conversion_algorithm" in value:
        import capo_mediaconvert.types.av1_framerate_conversion_algorithm

        out["framerateConversionAlgorithm"] = (
            capo_mediaconvert.types.av1_framerate_conversion_algorithm.serialize_json(
                value["framerate_conversion_algorithm"]
            )
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
    if "max_bitrate" in value:
        out["maxBitrate"] = value["max_bitrate"]
    if "number_b_frames_between_reference_frames" in value:
        out["numberBFramesBetweenReferenceFrames"] = value[
            "number_b_frames_between_reference_frames"
        ]
    if "per_frame_metrics" in value:
        import capo_mediaconvert.types.__list_of_frame_metric_type

        out["perFrameMetrics"] = (
            capo_mediaconvert.types.__list_of_frame_metric_type.serialize_json(
                value["per_frame_metrics"]
            )
        )
    if "qvbr_settings" in value:
        import capo_mediaconvert.types.av1_qvbr_settings

        out["qvbrSettings"] = capo_mediaconvert.types.av1_qvbr_settings.serialize_json(
            value["qvbr_settings"]
        )
    if "rate_control_mode" in value:
        import capo_mediaconvert.types.av1_rate_control_mode

        out["rateControlMode"] = (
            capo_mediaconvert.types.av1_rate_control_mode.serialize_json(
                value["rate_control_mode"]
            )
        )
    if "scene_change_detect" in value:
        import capo_mediaconvert.types.av1_scene_change_detect

        out["sceneChangeDetect"] = (
            capo_mediaconvert.types.av1_scene_change_detect.serialize_json(
                value["scene_change_detect"]
            )
        )
    if "slices" in value:
        out["slices"] = value["slices"]
    if "sliding_window_ms" in value:
        out["slidingWindowMs"] = value["sliding_window_ms"]
    if "sliding_window_peak_bitrate" in value:
        out["slidingWindowPeakBitrate"] = value["sliding_window_peak_bitrate"]
    if "spatial_adaptive_quantization" in value:
        import capo_mediaconvert.types.av1_spatial_adaptive_quantization

        out["spatialAdaptiveQuantization"] = (
            capo_mediaconvert.types.av1_spatial_adaptive_quantization.serialize_json(
                value["spatial_adaptive_quantization"]
            )
        )
    return out


def deserialize_json(data: dict) -> Av1Settings:
    out: Av1Settings = {}  # type: ignore[typeddict-item]
    if data.get("adaptiveQuantization") is not None:
        import capo_mediaconvert.types.av1_adaptive_quantization

        out["adaptive_quantization"] = (
            capo_mediaconvert.types.av1_adaptive_quantization.deserialize_json(
                data["adaptiveQuantization"]
            )
        )
    if data.get("bitDepth") is not None:
        import capo_mediaconvert.types.av1_bit_depth

        out["bit_depth"] = capo_mediaconvert.types.av1_bit_depth.deserialize_json(
            data["bitDepth"]
        )
    if data.get("bitrate") is not None:
        out["bitrate"] = data["bitrate"]
    if data.get("filmGrainSynthesis") is not None:
        import capo_mediaconvert.types.av1_film_grain_synthesis

        out["film_grain_synthesis"] = (
            capo_mediaconvert.types.av1_film_grain_synthesis.deserialize_json(
                data["filmGrainSynthesis"]
            )
        )
    if data.get("framerateControl") is not None:
        import capo_mediaconvert.types.av1_framerate_control

        out["framerate_control"] = (
            capo_mediaconvert.types.av1_framerate_control.deserialize_json(
                data["framerateControl"]
            )
        )
    if data.get("framerateConversionAlgorithm") is not None:
        import capo_mediaconvert.types.av1_framerate_conversion_algorithm

        out["framerate_conversion_algorithm"] = (
            capo_mediaconvert.types.av1_framerate_conversion_algorithm.deserialize_json(
                data["framerateConversionAlgorithm"]
            )
        )
    if data.get("framerateDenominator") is not None:
        out["framerate_denominator"] = data["framerateDenominator"]
    if data.get("framerateNumerator") is not None:
        out["framerate_numerator"] = data["framerateNumerator"]
    if data.get("gopSize") is not None:
        out["gop_size"] = float(data["gopSize"])
    if data.get("maxBitrate") is not None:
        out["max_bitrate"] = data["maxBitrate"]
    if data.get("numberBFramesBetweenReferenceFrames") is not None:
        out["number_b_frames_between_reference_frames"] = data[
            "numberBFramesBetweenReferenceFrames"
        ]
    if data.get("perFrameMetrics") is not None:
        import capo_mediaconvert.types.__list_of_frame_metric_type

        out["per_frame_metrics"] = (
            capo_mediaconvert.types.__list_of_frame_metric_type.deserialize_json(
                data["perFrameMetrics"]
            )
        )
    if data.get("qvbrSettings") is not None:
        import capo_mediaconvert.types.av1_qvbr_settings

        out["qvbr_settings"] = (
            capo_mediaconvert.types.av1_qvbr_settings.deserialize_json(
                data["qvbrSettings"]
            )
        )
    if data.get("rateControlMode") is not None:
        import capo_mediaconvert.types.av1_rate_control_mode

        out["rate_control_mode"] = (
            capo_mediaconvert.types.av1_rate_control_mode.deserialize_json(
                data["rateControlMode"]
            )
        )
    if data.get("sceneChangeDetect") is not None:
        import capo_mediaconvert.types.av1_scene_change_detect

        out["scene_change_detect"] = (
            capo_mediaconvert.types.av1_scene_change_detect.deserialize_json(
                data["sceneChangeDetect"]
            )
        )
    if data.get("slices") is not None:
        out["slices"] = data["slices"]
    if data.get("slidingWindowMs") is not None:
        out["sliding_window_ms"] = data["slidingWindowMs"]
    if data.get("slidingWindowPeakBitrate") is not None:
        out["sliding_window_peak_bitrate"] = data["slidingWindowPeakBitrate"]
    if data.get("spatialAdaptiveQuantization") is not None:
        import capo_mediaconvert.types.av1_spatial_adaptive_quantization

        out["spatial_adaptive_quantization"] = (
            capo_mediaconvert.types.av1_spatial_adaptive_quantization.deserialize_json(
                data["spatialAdaptiveQuantization"]
            )
        )
    return out
