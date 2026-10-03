"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265Settings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__double_min0
    import capo_mediaconvert.types.__integer_min0_max7
    import capo_mediaconvert.types.__integer_min0_max30
    import capo_mediaconvert.types.__integer_min0_max100
    import capo_mediaconvert.types.__integer_min0_max1466400000
    import capo_mediaconvert.types.__integer_min0_max2147483647
    import capo_mediaconvert.types.__integer_min1_max6
    import capo_mediaconvert.types.__integer_min1_max32
    import capo_mediaconvert.types.__integer_min1_max2147483647
    import capo_mediaconvert.types.__integer_min64_max2160
    import capo_mediaconvert.types.__integer_min256_max3840
    import capo_mediaconvert.types.__integer_min1000_max1466400000
    import capo_mediaconvert.types.__list_of_frame_metric_type
    import capo_mediaconvert.types.bandwidth_reduction_filter
    import capo_mediaconvert.types.h265_adaptive_quantization
    import capo_mediaconvert.types.h265_alternate_transfer_function_sei
    import capo_mediaconvert.types.h265_codec_level
    import capo_mediaconvert.types.h265_codec_profile
    import capo_mediaconvert.types.h265_deblocking
    import capo_mediaconvert.types.h265_dynamic_sub_gop
    import capo_mediaconvert.types.h265_end_of_stream_markers
    import capo_mediaconvert.types.h265_flicker_adaptive_quantization
    import capo_mediaconvert.types.h265_framerate_control
    import capo_mediaconvert.types.h265_framerate_conversion_algorithm
    import capo_mediaconvert.types.h265_gop_b_reference
    import capo_mediaconvert.types.h265_gop_size_units
    import capo_mediaconvert.types.h265_interlace_mode
    import capo_mediaconvert.types.h265_mv_over_picture_boundaries
    import capo_mediaconvert.types.h265_mv_temporal_predictor
    import capo_mediaconvert.types.h265_par_control
    import capo_mediaconvert.types.h265_quality_tuning_level
    import capo_mediaconvert.types.h265_qvbr_settings
    import capo_mediaconvert.types.h265_rate_control_mode
    import capo_mediaconvert.types.h265_sample_adaptive_offset_filter_mode
    import capo_mediaconvert.types.h265_scan_type_conversion_mode
    import capo_mediaconvert.types.h265_scene_change_detect
    import capo_mediaconvert.types.h265_slow_pal
    import capo_mediaconvert.types.h265_spatial_adaptive_quantization
    import capo_mediaconvert.types.h265_telecine
    import capo_mediaconvert.types.h265_temporal_adaptive_quantization
    import capo_mediaconvert.types.h265_temporal_ids
    import capo_mediaconvert.types.h265_tile_padding
    import capo_mediaconvert.types.h265_tiles
    import capo_mediaconvert.types.h265_tree_block_size
    import capo_mediaconvert.types.h265_unregistered_sei_timecode
    import capo_mediaconvert.types.h265_write_mp4_packaging_type


class H265Settings(TypedDict, closed=True):
    adaptive_quantization: NotRequired[
        "capo_mediaconvert.types.h265_adaptive_quantization.H265AdaptiveQuantization"
    ]
    """When you set Adaptive Quantization to Auto, or leave blank, MediaConvert automatically applies quantization to improve the video quality of your output. Set Adaptive Quantization to Low, Medium, High, Higher, or Max to manually control the strength of the quantization filter. When you do, you can specify a value for Spatial Adaptive Quantization, Temporal Adaptive Quantization, and Flicker Adaptive Quantization, to further control the quantization filter. Set Adaptive Quantization to Off to apply no quantization to your output."""
    alternate_transfer_function_sei: NotRequired[
        "capo_mediaconvert.types.h265_alternate_transfer_function_sei.H265AlternateTransferFunctionSei"
    ]
    """Enables Alternate Transfer Function SEI message for outputs using Hybrid Log Gamma (HLG) Electro-Optical Transfer Function (EOTF)."""
    bandwidth_reduction_filter: NotRequired[
        "capo_mediaconvert.types.bandwidth_reduction_filter.BandwidthReductionFilter"
    ]
    """The Bandwidth reduction filter increases the video quality of your output relative to its bitrate. Use to lower the bitrate of your constant quality QVBR output, with little or no perceptual decrease in quality. Or, use to increase the video quality of outputs with other rate control modes relative to the bitrate that you specify. Bandwidth reduction increases further when your input is low quality or noisy. Outputs that use this feature incur pro-tier pricing. When you include Bandwidth reduction filter, you cannot include the Noise reducer preprocessor."""
    bitrate: NotRequired[
        "capo_mediaconvert.types.__integer_min1000_max1466400000.__integerMin1000Max1466400000"
    ]
    """Specify the average bitrate in bits per second. Required for VBR and CBR. For MS Smooth outputs, bitrates must be unique when rounded down to the nearest multiple of 1000."""
    codec_level: NotRequired["capo_mediaconvert.types.h265_codec_level.H265CodecLevel"]
    """H.265 Level."""
    codec_profile: NotRequired[
        "capo_mediaconvert.types.h265_codec_profile.H265CodecProfile"
    ]
    """Represents the Profile and Tier, per the HEVC (H.265) specification. Selections are grouped as [Profile] / [Tier], so "Main/High" represents Main Profile with High Tier. 4:2:2 profiles are only available with the HEVC 4:2:2 License."""
    deblocking: NotRequired["capo_mediaconvert.types.h265_deblocking.H265Deblocking"]
    """Use Deblocking to improve the video quality of your output by smoothing the edges of macroblock artifacts created during video compression. To reduce blocking artifacts at block boundaries, and improve overall video quality: Keep the default value, Enabled. To not apply any deblocking: Choose Disabled. Visible block edge artifacts might appear in the output, especially at lower bitrates."""
    dynamic_sub_gop: NotRequired[
        "capo_mediaconvert.types.h265_dynamic_sub_gop.H265DynamicSubGop"
    ]
    """Specify whether to allow the number of B-frames in your output GOP structure to vary or not depending on your input video content. To improve the subjective video quality of your output that has high-motion content: Leave blank or keep the default value Adaptive. MediaConvert will use fewer B-frames for high-motion video content than low-motion content. The maximum number of B- frames is limited by the value that you choose for B-frames between reference frames. To use the same number B-frames for all types of content: Choose Static."""
    end_of_stream_markers: NotRequired[
        "capo_mediaconvert.types.h265_end_of_stream_markers.H265EndOfStreamMarkers"
    ]
    """Optionally include or suppress markers at the end of your output that signal the end of the video stream. To include end of stream markers: Leave blank or keep the default value, Include. To not include end of stream markers: Choose Suppress. This is useful when your output will be inserted into another stream."""
    flicker_adaptive_quantization: NotRequired[
        "capo_mediaconvert.types.h265_flicker_adaptive_quantization.H265FlickerAdaptiveQuantization"
    ]
    """Enable this setting to have the encoder reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. This setting is disabled by default. Related setting: In addition to enabling this setting, you must also set adaptiveQuantization to a value other than Off."""
    framerate_control: NotRequired[
        "capo_mediaconvert.types.h265_framerate_control.H265FramerateControl"
    ]
    """Use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction."""
    framerate_conversion_algorithm: NotRequired[
        "capo_mediaconvert.types.h265_framerate_conversion_algorithm.H265FramerateConversionAlgorithm"
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
    gop_b_reference: NotRequired[
        "capo_mediaconvert.types.h265_gop_b_reference.H265GopBReference"
    ]
    """Specify whether to allow B-frames to be referenced by other frame types. To use reference B-frames when your GOP structure has 1 or more B-frames: Leave blank or keep the default value Enabled. We recommend that you choose Enabled to help improve the video quality of your output relative to its bitrate. To not use reference B-frames: Choose Disabled."""
    gop_closed_cadence: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Specify the relative frequency of open to closed GOPs in this output. For example, if you want to allow four open GOPs and then require a closed GOP, set this value to 5. We recommend that you have the transcoder automatically choose this value for you based on characteristics of your input video. To enable this automatic behavior, do this by keeping the default empty value. If you do explicitly specify a value, for segmented outputs, don't set this value to 0."""
    gop_size: NotRequired["capo_mediaconvert.types.__double_min0.__doubleMin0"]
    """Use this setting only when you set GOP mode control to Specified, frames or Specified, seconds. Specify the GOP length using a whole number of frames or a decimal value of seconds. MediaConvert will interpret this value as frames or seconds depending on the value you choose for GOP mode control. If you want to allow MediaConvert to automatically determine GOP size, leave GOP size blank and set GOP mode control to Auto. If your output group specifies HLS, DASH, or CMAF, leave GOP size blank and set GOP mode control to Auto in each output in your output group."""
    gop_size_units: NotRequired[
        "capo_mediaconvert.types.h265_gop_size_units.H265GopSizeUnits"
    ]
    """Specify how the transcoder determines GOP size for this output. We recommend that you have the transcoder automatically choose this value for you based on characteristics of your input video. To enable this automatic behavior, choose Auto and and leave GOP size blank. By default, if you don't specify GOP mode control, MediaConvert will use automatic behavior. If your output group specifies HLS, DASH, or CMAF, set GOP mode control to Auto and leave GOP size blank in each output in your output group. To explicitly specify the GOP length, choose Specified, frames or Specified, seconds and then provide the GOP length in the related setting GOP size."""
    hrd_buffer_final_fill_percentage: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max100.__integerMin0Max100"
    ]
    """If your downstream systems have strict buffer requirements: Specify the minimum percentage of the HRD buffer that's available at the end of each encoded video segment. For the best video quality: Set to 0 or leave blank to automatically determine the final buffer fill percentage."""
    hrd_buffer_initial_fill_percentage: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max100.__integerMin0Max100"
    ]
    """Percentage of the buffer that should initially be filled (HRD buffer model)."""
    hrd_buffer_size: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max1466400000.__integerMin0Max1466400000"
    ]
    """Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000."""
    interlace_mode: NotRequired[
        "capo_mediaconvert.types.h265_interlace_mode.H265InterlaceMode"
    ]
    """Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose."""
    max_bitrate: NotRequired[
        "capo_mediaconvert.types.__integer_min1000_max1466400000.__integerMin1000Max1466400000"
    ]
    """Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. Required when Rate control mode is QVBR."""
    min_i_interval: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max30.__integerMin0Max30"
    ]
    """Specify the minimum number of frames allowed between two IDR-frames in your output. This includes frames created at the start of a GOP or a scene change. Use Min I-Interval to improve video compression by varying GOP size when two IDR-frames would be created near each other. For example, if a regular cadence-driven IDR-frame would fall within 5 frames of a scene-change IDR-frame, and you set Min I-interval to 5, then the encoder would only write an IDR-frame for the scene-change. In this way, one GOP is shortened or extended. If a cadence-driven IDR-frame would be further than 5 frames from a scene-change IDR-frame, then the encoder leaves all IDR-frames in place. To use an automatically determined interval: We recommend that you keep this value blank. This allows for MediaConvert to use an optimal setting according to the characteristics of your input video, and results in better video compression. To manually specify an interval: Enter a value from 1 to 30. Use when your downstream systems have specific GOP size requirements. To disable GOP size variance: Enter 0. MediaConvert will only create IDR-frames at the start of your output's cadence-driven GOP. Use when your downstream systems require a regular GOP size."""
    mv_over_picture_boundaries: NotRequired[
        "capo_mediaconvert.types.h265_mv_over_picture_boundaries.H265MvOverPictureBoundaries"
    ]
    """If you are setting up the picture as a tile, you must set this to "disabled". In all other configurations, you typically enter "enabled"."""
    mv_temporal_predictor: NotRequired[
        "capo_mediaconvert.types.h265_mv_temporal_predictor.H265MvTemporalPredictor"
    ]
    """If you are setting up the picture as a tile, you must set this to "disabled". In other configurations, you typically enter "enabled"."""
    number_b_frames_between_reference_frames: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max7.__integerMin0Max7"
    ]
    """Specify the number of B-frames between reference frames in this output. For the best video quality: Leave blank. MediaConvert automatically determines the number of B-frames to use based on the characteristics of your input video. To manually specify the number of B-frames between reference frames: Enter an integer from 0 to 7."""
    number_reference_frames: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max6.__integerMin1Max6"
    ]
    """Number of reference frames to use. The encoder may use more than requested if using B-frames and/or interlaced encoding."""
    par_control: NotRequired["capo_mediaconvert.types.h265_par_control.H265ParControl"]
    """Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings."""
    par_denominator: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parDenominator is 33."""
    par_numerator: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parNumerator is 40."""
    per_frame_metrics: NotRequired[
        "capo_mediaconvert.types.__list_of_frame_metric_type.__listOfFrameMetricType"
    ]
    """Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: * PSNR: Peak Signal-to-Noise Ratio * SSIM: Structural Similarity Index Measure * MS_SSIM: Multi-Scale Similarity Index Measure * PSNR_HVS: Peak Signal-to-Noise Ratio, Human Visual System * VMAF: Video Multi-Method Assessment Fusion * QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. * SHOT_CHANGE: Shot Changes"""
    quality_tuning_level: NotRequired[
        "capo_mediaconvert.types.h265_quality_tuning_level.H265QualityTuningLevel"
    ]
    """Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding."""
    qvbr_settings: NotRequired[
        "capo_mediaconvert.types.h265_qvbr_settings.H265QvbrSettings"
    ]
    """Settings for quality-defined variable bitrate encoding with the H.265 codec. Use these settings only when you set QVBR for Rate control mode."""
    rate_control_mode: NotRequired[
        "capo_mediaconvert.types.h265_rate_control_mode.H265RateControlMode"
    ]
    """Use this setting to specify whether this output has a variable bitrate (VBR), constant bitrate (CBR) or quality-defined variable bitrate (QVBR)."""
    sample_adaptive_offset_filter_mode: NotRequired[
        "capo_mediaconvert.types.h265_sample_adaptive_offset_filter_mode.H265SampleAdaptiveOffsetFilterMode"
    ]
    """Specify Sample Adaptive Offset (SAO) filter strength. Adaptive mode dynamically selects best strength based on content"""
    scan_type_conversion_mode: NotRequired[
        "capo_mediaconvert.types.h265_scan_type_conversion_mode.H265ScanTypeConversionMode"
    ]
    """Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive."""
    scene_change_detect: NotRequired[
        "capo_mediaconvert.types.h265_scene_change_detect.H265SceneChangeDetect"
    ]
    """Enable this setting to insert I-frames at scene changes that the service automatically detects. This improves video quality and is enabled by default. If this output uses QVBR, choose Transition detection for further video quality improvement. For more information about QVBR, see https://docs.aws.amazon.com/console/mediaconvert/cbr-vbr-qvbr."""
    slices: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max32.__integerMin1Max32"
    ]
    """Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures."""
    slow_pal: NotRequired["capo_mediaconvert.types.h265_slow_pal.H265SlowPal"]
    """Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25."""
    spatial_adaptive_quantization: NotRequired[
        "capo_mediaconvert.types.h265_spatial_adaptive_quantization.H265SpatialAdaptiveQuantization"
    ]
    """Keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher."""
    telecine: NotRequired["capo_mediaconvert.types.h265_telecine.H265Telecine"]
    """This field applies only if the Streams > Advanced > Framerate field is set to 29.970. This field works with the Streams > Advanced > Preprocessors > Deinterlacer field and the Streams > Advanced > Interlaced Mode field to identify the scan type for the output: Progressive, Interlaced, Hard Telecine or Soft Telecine. - Hard: produces 29.97i output from 23.976 input. - Soft: produces 23.976; the player converts this output to 29.97i."""
    temporal_adaptive_quantization: NotRequired[
        "capo_mediaconvert.types.h265_temporal_adaptive_quantization.H265TemporalAdaptiveQuantization"
    ]
    """Keep the default value, Enabled, to adjust quantization within each frame based on temporal variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas of the frame that aren't moving and uses more bits on complex objects with sharp edges that move a lot. For example, this feature improves the readability of text tickers on newscasts and scoreboards on sports matches. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen that doesn't have moving objects with sharp edges, such as sports athletes' faces, you might choose to disable this feature. Related setting: When you enable temporal quantization, adjust the strength of the filter with the setting Adaptive quantization."""
    temporal_ids: NotRequired[
        "capo_mediaconvert.types.h265_temporal_ids.H265TemporalIds"
    ]
    """Enables temporal layer identifiers in the encoded bitstream. Up to 3 layers are supported depending on GOP structure: I- and P-frames form one layer, reference B-frames can form a second layer and non-reference b-frames can form a third layer. Decoders can optionally decode only the lower temporal layers to generate a lower frame rate output. For example, given a bitstream with temporal IDs and with b-frames = 1 (i.e. IbPbPb display order), a decoder could decode all the frames for full frame rate output or only the I and P frames (lowest temporal layer) for a half frame rate output."""
    tile_height: NotRequired[
        "capo_mediaconvert.types.__integer_min64_max2160.__integerMin64Max2160"
    ]
    """Set this field to set up the picture as a tile. You must also set TileWidth. The tile height must result in 22 or fewer rows in the frame. The tile width must result in 20 or fewer columns in the frame. And finally, the product of the column count and row count must be 64 or less. If the tile width and height are specified, MediaConvert will override the video codec slices field with a value that MediaConvert calculates."""
    tile_padding: NotRequired[
        "capo_mediaconvert.types.h265_tile_padding.H265TilePadding"
    ]
    """Set to "padded" to force MediaConvert to add padding to the frame, to obtain a frame that is a whole multiple of the tile size. If you are setting up the picture as a tile, you must enter "padded". In all other configurations, you typically enter "none"."""
    tile_width: NotRequired[
        "capo_mediaconvert.types.__integer_min256_max3840.__integerMin256Max3840"
    ]
    """Set this field to set up the picture as a tile. See TileHeight for more information."""
    tiles: NotRequired["capo_mediaconvert.types.h265_tiles.H265Tiles"]
    """Enable use of tiles, allowing horizontal as well as vertical subdivision of the encoded pictures."""
    tree_block_size: NotRequired[
        "capo_mediaconvert.types.h265_tree_block_size.H265TreeBlockSize"
    ]
    """Select the tree block size used for encoding. If you enter "auto", the encoder will pick the best size. If you are setting up the picture as a tile, you must set this to 32x32. In all other configurations, you typically enter "auto"."""
    unregistered_sei_timecode: NotRequired[
        "capo_mediaconvert.types.h265_unregistered_sei_timecode.H265UnregisteredSeiTimecode"
    ]
    """Inserts timecode for each frame as 4 bytes of an unregistered SEI message."""
    write_mp4_packaging_type: NotRequired[
        "capo_mediaconvert.types.h265_write_mp4_packaging_type.H265WriteMp4PackagingType"
    ]
    """If the location of parameter set NAL units doesn't matter in your workflow, ignore this setting. Use this setting only with CMAF or DASH outputs, or with standalone file outputs in an MPEG-4 container (MP4 outputs). Choose HVC1 to mark your output as HVC1. This makes your output compliant with the following specification: ISO IECJTC1 SC29 N13798 Text ISO/IEC FDIS 14496-15 3rd Edition. For these outputs, the service stores parameter set NAL units in the sample headers but not in the samples directly. For MP4 outputs, when you choose HVC1, your output video might not work properly with some downstream systems and video players. The service defaults to marking your output as HEV1. For these outputs, the service writes parameter set NAL units directly into the samples."""


# --- restJson1 ser/de ---
def serialize_json(value: H265Settings) -> dict:
    out: dict = {}
    if "adaptive_quantization" in value:
        import capo_mediaconvert.types.h265_adaptive_quantization

        out["adaptiveQuantization"] = (
            capo_mediaconvert.types.h265_adaptive_quantization.serialize_json(
                value["adaptive_quantization"]
            )
        )
    if "alternate_transfer_function_sei" in value:
        import capo_mediaconvert.types.h265_alternate_transfer_function_sei

        out["alternateTransferFunctionSei"] = (
            capo_mediaconvert.types.h265_alternate_transfer_function_sei.serialize_json(
                value["alternate_transfer_function_sei"]
            )
        )
    if "bandwidth_reduction_filter" in value:
        import capo_mediaconvert.types.bandwidth_reduction_filter

        out["bandwidthReductionFilter"] = (
            capo_mediaconvert.types.bandwidth_reduction_filter.serialize_json(
                value["bandwidth_reduction_filter"]
            )
        )
    if "bitrate" in value:
        out["bitrate"] = value["bitrate"]
    if "codec_level" in value:
        import capo_mediaconvert.types.h265_codec_level

        out["codecLevel"] = capo_mediaconvert.types.h265_codec_level.serialize_json(
            value["codec_level"]
        )
    if "codec_profile" in value:
        import capo_mediaconvert.types.h265_codec_profile

        out["codecProfile"] = capo_mediaconvert.types.h265_codec_profile.serialize_json(
            value["codec_profile"]
        )
    if "deblocking" in value:
        import capo_mediaconvert.types.h265_deblocking

        out["deblocking"] = capo_mediaconvert.types.h265_deblocking.serialize_json(
            value["deblocking"]
        )
    if "dynamic_sub_gop" in value:
        import capo_mediaconvert.types.h265_dynamic_sub_gop

        out["dynamicSubGop"] = (
            capo_mediaconvert.types.h265_dynamic_sub_gop.serialize_json(
                value["dynamic_sub_gop"]
            )
        )
    if "end_of_stream_markers" in value:
        import capo_mediaconvert.types.h265_end_of_stream_markers

        out["endOfStreamMarkers"] = (
            capo_mediaconvert.types.h265_end_of_stream_markers.serialize_json(
                value["end_of_stream_markers"]
            )
        )
    if "flicker_adaptive_quantization" in value:
        import capo_mediaconvert.types.h265_flicker_adaptive_quantization

        out["flickerAdaptiveQuantization"] = (
            capo_mediaconvert.types.h265_flicker_adaptive_quantization.serialize_json(
                value["flicker_adaptive_quantization"]
            )
        )
    if "framerate_control" in value:
        import capo_mediaconvert.types.h265_framerate_control

        out["framerateControl"] = (
            capo_mediaconvert.types.h265_framerate_control.serialize_json(
                value["framerate_control"]
            )
        )
    if "framerate_conversion_algorithm" in value:
        import capo_mediaconvert.types.h265_framerate_conversion_algorithm

        out["framerateConversionAlgorithm"] = (
            capo_mediaconvert.types.h265_framerate_conversion_algorithm.serialize_json(
                value["framerate_conversion_algorithm"]
            )
        )
    if "framerate_denominator" in value:
        out["framerateDenominator"] = value["framerate_denominator"]
    if "framerate_numerator" in value:
        out["framerateNumerator"] = value["framerate_numerator"]
    if "gop_b_reference" in value:
        import capo_mediaconvert.types.h265_gop_b_reference

        out["gopBReference"] = (
            capo_mediaconvert.types.h265_gop_b_reference.serialize_json(
                value["gop_b_reference"]
            )
        )
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
        import capo_mediaconvert.types.h265_gop_size_units

        out["gopSizeUnits"] = (
            capo_mediaconvert.types.h265_gop_size_units.serialize_json(
                value["gop_size_units"]
            )
        )
    if "hrd_buffer_final_fill_percentage" in value:
        out["hrdBufferFinalFillPercentage"] = value["hrd_buffer_final_fill_percentage"]
    if "hrd_buffer_initial_fill_percentage" in value:
        out["hrdBufferInitialFillPercentage"] = value[
            "hrd_buffer_initial_fill_percentage"
        ]
    if "hrd_buffer_size" in value:
        out["hrdBufferSize"] = value["hrd_buffer_size"]
    if "interlace_mode" in value:
        import capo_mediaconvert.types.h265_interlace_mode

        out["interlaceMode"] = (
            capo_mediaconvert.types.h265_interlace_mode.serialize_json(
                value["interlace_mode"]
            )
        )
    if "max_bitrate" in value:
        out["maxBitrate"] = value["max_bitrate"]
    if "min_i_interval" in value:
        out["minIInterval"] = value["min_i_interval"]
    if "mv_over_picture_boundaries" in value:
        import capo_mediaconvert.types.h265_mv_over_picture_boundaries

        out["mvOverPictureBoundaries"] = (
            capo_mediaconvert.types.h265_mv_over_picture_boundaries.serialize_json(
                value["mv_over_picture_boundaries"]
            )
        )
    if "mv_temporal_predictor" in value:
        import capo_mediaconvert.types.h265_mv_temporal_predictor

        out["mvTemporalPredictor"] = (
            capo_mediaconvert.types.h265_mv_temporal_predictor.serialize_json(
                value["mv_temporal_predictor"]
            )
        )
    if "number_b_frames_between_reference_frames" in value:
        out["numberBFramesBetweenReferenceFrames"] = value[
            "number_b_frames_between_reference_frames"
        ]
    if "number_reference_frames" in value:
        out["numberReferenceFrames"] = value["number_reference_frames"]
    if "par_control" in value:
        import capo_mediaconvert.types.h265_par_control

        out["parControl"] = capo_mediaconvert.types.h265_par_control.serialize_json(
            value["par_control"]
        )
    if "par_denominator" in value:
        out["parDenominator"] = value["par_denominator"]
    if "par_numerator" in value:
        out["parNumerator"] = value["par_numerator"]
    if "per_frame_metrics" in value:
        import capo_mediaconvert.types.__list_of_frame_metric_type

        out["perFrameMetrics"] = (
            capo_mediaconvert.types.__list_of_frame_metric_type.serialize_json(
                value["per_frame_metrics"]
            )
        )
    if "quality_tuning_level" in value:
        import capo_mediaconvert.types.h265_quality_tuning_level

        out["qualityTuningLevel"] = (
            capo_mediaconvert.types.h265_quality_tuning_level.serialize_json(
                value["quality_tuning_level"]
            )
        )
    if "qvbr_settings" in value:
        import capo_mediaconvert.types.h265_qvbr_settings

        out["qvbrSettings"] = capo_mediaconvert.types.h265_qvbr_settings.serialize_json(
            value["qvbr_settings"]
        )
    if "rate_control_mode" in value:
        import capo_mediaconvert.types.h265_rate_control_mode

        out["rateControlMode"] = (
            capo_mediaconvert.types.h265_rate_control_mode.serialize_json(
                value["rate_control_mode"]
            )
        )
    if "sample_adaptive_offset_filter_mode" in value:
        import capo_mediaconvert.types.h265_sample_adaptive_offset_filter_mode

        out["sampleAdaptiveOffsetFilterMode"] = (
            capo_mediaconvert.types.h265_sample_adaptive_offset_filter_mode.serialize_json(
                value["sample_adaptive_offset_filter_mode"]
            )
        )
    if "scan_type_conversion_mode" in value:
        import capo_mediaconvert.types.h265_scan_type_conversion_mode

        out["scanTypeConversionMode"] = (
            capo_mediaconvert.types.h265_scan_type_conversion_mode.serialize_json(
                value["scan_type_conversion_mode"]
            )
        )
    if "scene_change_detect" in value:
        import capo_mediaconvert.types.h265_scene_change_detect

        out["sceneChangeDetect"] = (
            capo_mediaconvert.types.h265_scene_change_detect.serialize_json(
                value["scene_change_detect"]
            )
        )
    if "slices" in value:
        out["slices"] = value["slices"]
    if "slow_pal" in value:
        import capo_mediaconvert.types.h265_slow_pal

        out["slowPal"] = capo_mediaconvert.types.h265_slow_pal.serialize_json(
            value["slow_pal"]
        )
    if "spatial_adaptive_quantization" in value:
        import capo_mediaconvert.types.h265_spatial_adaptive_quantization

        out["spatialAdaptiveQuantization"] = (
            capo_mediaconvert.types.h265_spatial_adaptive_quantization.serialize_json(
                value["spatial_adaptive_quantization"]
            )
        )
    if "telecine" in value:
        import capo_mediaconvert.types.h265_telecine

        out["telecine"] = capo_mediaconvert.types.h265_telecine.serialize_json(
            value["telecine"]
        )
    if "temporal_adaptive_quantization" in value:
        import capo_mediaconvert.types.h265_temporal_adaptive_quantization

        out["temporalAdaptiveQuantization"] = (
            capo_mediaconvert.types.h265_temporal_adaptive_quantization.serialize_json(
                value["temporal_adaptive_quantization"]
            )
        )
    if "temporal_ids" in value:
        import capo_mediaconvert.types.h265_temporal_ids

        out["temporalIds"] = capo_mediaconvert.types.h265_temporal_ids.serialize_json(
            value["temporal_ids"]
        )
    if "tile_height" in value:
        out["tileHeight"] = value["tile_height"]
    if "tile_padding" in value:
        import capo_mediaconvert.types.h265_tile_padding

        out["tilePadding"] = capo_mediaconvert.types.h265_tile_padding.serialize_json(
            value["tile_padding"]
        )
    if "tile_width" in value:
        out["tileWidth"] = value["tile_width"]
    if "tiles" in value:
        import capo_mediaconvert.types.h265_tiles

        out["tiles"] = capo_mediaconvert.types.h265_tiles.serialize_json(value["tiles"])
    if "tree_block_size" in value:
        import capo_mediaconvert.types.h265_tree_block_size

        out["treeBlockSize"] = (
            capo_mediaconvert.types.h265_tree_block_size.serialize_json(
                value["tree_block_size"]
            )
        )
    if "unregistered_sei_timecode" in value:
        import capo_mediaconvert.types.h265_unregistered_sei_timecode

        out["unregisteredSeiTimecode"] = (
            capo_mediaconvert.types.h265_unregistered_sei_timecode.serialize_json(
                value["unregistered_sei_timecode"]
            )
        )
    if "write_mp4_packaging_type" in value:
        import capo_mediaconvert.types.h265_write_mp4_packaging_type

        out["writeMp4PackagingType"] = (
            capo_mediaconvert.types.h265_write_mp4_packaging_type.serialize_json(
                value["write_mp4_packaging_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> H265Settings:
    out: H265Settings = {}  # type: ignore[typeddict-item]
    if data.get("adaptiveQuantization") is not None:
        import capo_mediaconvert.types.h265_adaptive_quantization

        out["adaptive_quantization"] = (
            capo_mediaconvert.types.h265_adaptive_quantization.deserialize_json(
                data["adaptiveQuantization"]
            )
        )
    if data.get("alternateTransferFunctionSei") is not None:
        import capo_mediaconvert.types.h265_alternate_transfer_function_sei

        out["alternate_transfer_function_sei"] = (
            capo_mediaconvert.types.h265_alternate_transfer_function_sei.deserialize_json(
                data["alternateTransferFunctionSei"]
            )
        )
    if data.get("bandwidthReductionFilter") is not None:
        import capo_mediaconvert.types.bandwidth_reduction_filter

        out["bandwidth_reduction_filter"] = (
            capo_mediaconvert.types.bandwidth_reduction_filter.deserialize_json(
                data["bandwidthReductionFilter"]
            )
        )
    if data.get("bitrate") is not None:
        out["bitrate"] = data["bitrate"]
    if data.get("codecLevel") is not None:
        import capo_mediaconvert.types.h265_codec_level

        out["codec_level"] = capo_mediaconvert.types.h265_codec_level.deserialize_json(
            data["codecLevel"]
        )
    if data.get("codecProfile") is not None:
        import capo_mediaconvert.types.h265_codec_profile

        out["codec_profile"] = (
            capo_mediaconvert.types.h265_codec_profile.deserialize_json(
                data["codecProfile"]
            )
        )
    if data.get("deblocking") is not None:
        import capo_mediaconvert.types.h265_deblocking

        out["deblocking"] = capo_mediaconvert.types.h265_deblocking.deserialize_json(
            data["deblocking"]
        )
    if data.get("dynamicSubGop") is not None:
        import capo_mediaconvert.types.h265_dynamic_sub_gop

        out["dynamic_sub_gop"] = (
            capo_mediaconvert.types.h265_dynamic_sub_gop.deserialize_json(
                data["dynamicSubGop"]
            )
        )
    if data.get("endOfStreamMarkers") is not None:
        import capo_mediaconvert.types.h265_end_of_stream_markers

        out["end_of_stream_markers"] = (
            capo_mediaconvert.types.h265_end_of_stream_markers.deserialize_json(
                data["endOfStreamMarkers"]
            )
        )
    if data.get("flickerAdaptiveQuantization") is not None:
        import capo_mediaconvert.types.h265_flicker_adaptive_quantization

        out["flicker_adaptive_quantization"] = (
            capo_mediaconvert.types.h265_flicker_adaptive_quantization.deserialize_json(
                data["flickerAdaptiveQuantization"]
            )
        )
    if data.get("framerateControl") is not None:
        import capo_mediaconvert.types.h265_framerate_control

        out["framerate_control"] = (
            capo_mediaconvert.types.h265_framerate_control.deserialize_json(
                data["framerateControl"]
            )
        )
    if data.get("framerateConversionAlgorithm") is not None:
        import capo_mediaconvert.types.h265_framerate_conversion_algorithm

        out["framerate_conversion_algorithm"] = (
            capo_mediaconvert.types.h265_framerate_conversion_algorithm.deserialize_json(
                data["framerateConversionAlgorithm"]
            )
        )
    if data.get("framerateDenominator") is not None:
        out["framerate_denominator"] = data["framerateDenominator"]
    if data.get("framerateNumerator") is not None:
        out["framerate_numerator"] = data["framerateNumerator"]
    if data.get("gopBReference") is not None:
        import capo_mediaconvert.types.h265_gop_b_reference

        out["gop_b_reference"] = (
            capo_mediaconvert.types.h265_gop_b_reference.deserialize_json(
                data["gopBReference"]
            )
        )
    if data.get("gopClosedCadence") is not None:
        out["gop_closed_cadence"] = data["gopClosedCadence"]
    if data.get("gopSize") is not None:
        out["gop_size"] = float(data["gopSize"])
    if data.get("gopSizeUnits") is not None:
        import capo_mediaconvert.types.h265_gop_size_units

        out["gop_size_units"] = (
            capo_mediaconvert.types.h265_gop_size_units.deserialize_json(
                data["gopSizeUnits"]
            )
        )
    if data.get("hrdBufferFinalFillPercentage") is not None:
        out["hrd_buffer_final_fill_percentage"] = data["hrdBufferFinalFillPercentage"]
    if data.get("hrdBufferInitialFillPercentage") is not None:
        out["hrd_buffer_initial_fill_percentage"] = data[
            "hrdBufferInitialFillPercentage"
        ]
    if data.get("hrdBufferSize") is not None:
        out["hrd_buffer_size"] = data["hrdBufferSize"]
    if data.get("interlaceMode") is not None:
        import capo_mediaconvert.types.h265_interlace_mode

        out["interlace_mode"] = (
            capo_mediaconvert.types.h265_interlace_mode.deserialize_json(
                data["interlaceMode"]
            )
        )
    if data.get("maxBitrate") is not None:
        out["max_bitrate"] = data["maxBitrate"]
    if data.get("minIInterval") is not None:
        out["min_i_interval"] = data["minIInterval"]
    if data.get("mvOverPictureBoundaries") is not None:
        import capo_mediaconvert.types.h265_mv_over_picture_boundaries

        out["mv_over_picture_boundaries"] = (
            capo_mediaconvert.types.h265_mv_over_picture_boundaries.deserialize_json(
                data["mvOverPictureBoundaries"]
            )
        )
    if data.get("mvTemporalPredictor") is not None:
        import capo_mediaconvert.types.h265_mv_temporal_predictor

        out["mv_temporal_predictor"] = (
            capo_mediaconvert.types.h265_mv_temporal_predictor.deserialize_json(
                data["mvTemporalPredictor"]
            )
        )
    if data.get("numberBFramesBetweenReferenceFrames") is not None:
        out["number_b_frames_between_reference_frames"] = data[
            "numberBFramesBetweenReferenceFrames"
        ]
    if data.get("numberReferenceFrames") is not None:
        out["number_reference_frames"] = data["numberReferenceFrames"]
    if data.get("parControl") is not None:
        import capo_mediaconvert.types.h265_par_control

        out["par_control"] = capo_mediaconvert.types.h265_par_control.deserialize_json(
            data["parControl"]
        )
    if data.get("parDenominator") is not None:
        out["par_denominator"] = data["parDenominator"]
    if data.get("parNumerator") is not None:
        out["par_numerator"] = data["parNumerator"]
    if data.get("perFrameMetrics") is not None:
        import capo_mediaconvert.types.__list_of_frame_metric_type

        out["per_frame_metrics"] = (
            capo_mediaconvert.types.__list_of_frame_metric_type.deserialize_json(
                data["perFrameMetrics"]
            )
        )
    if data.get("qualityTuningLevel") is not None:
        import capo_mediaconvert.types.h265_quality_tuning_level

        out["quality_tuning_level"] = (
            capo_mediaconvert.types.h265_quality_tuning_level.deserialize_json(
                data["qualityTuningLevel"]
            )
        )
    if data.get("qvbrSettings") is not None:
        import capo_mediaconvert.types.h265_qvbr_settings

        out["qvbr_settings"] = (
            capo_mediaconvert.types.h265_qvbr_settings.deserialize_json(
                data["qvbrSettings"]
            )
        )
    if data.get("rateControlMode") is not None:
        import capo_mediaconvert.types.h265_rate_control_mode

        out["rate_control_mode"] = (
            capo_mediaconvert.types.h265_rate_control_mode.deserialize_json(
                data["rateControlMode"]
            )
        )
    if data.get("sampleAdaptiveOffsetFilterMode") is not None:
        import capo_mediaconvert.types.h265_sample_adaptive_offset_filter_mode

        out["sample_adaptive_offset_filter_mode"] = (
            capo_mediaconvert.types.h265_sample_adaptive_offset_filter_mode.deserialize_json(
                data["sampleAdaptiveOffsetFilterMode"]
            )
        )
    if data.get("scanTypeConversionMode") is not None:
        import capo_mediaconvert.types.h265_scan_type_conversion_mode

        out["scan_type_conversion_mode"] = (
            capo_mediaconvert.types.h265_scan_type_conversion_mode.deserialize_json(
                data["scanTypeConversionMode"]
            )
        )
    if data.get("sceneChangeDetect") is not None:
        import capo_mediaconvert.types.h265_scene_change_detect

        out["scene_change_detect"] = (
            capo_mediaconvert.types.h265_scene_change_detect.deserialize_json(
                data["sceneChangeDetect"]
            )
        )
    if data.get("slices") is not None:
        out["slices"] = data["slices"]
    if data.get("slowPal") is not None:
        import capo_mediaconvert.types.h265_slow_pal

        out["slow_pal"] = capo_mediaconvert.types.h265_slow_pal.deserialize_json(
            data["slowPal"]
        )
    if data.get("spatialAdaptiveQuantization") is not None:
        import capo_mediaconvert.types.h265_spatial_adaptive_quantization

        out["spatial_adaptive_quantization"] = (
            capo_mediaconvert.types.h265_spatial_adaptive_quantization.deserialize_json(
                data["spatialAdaptiveQuantization"]
            )
        )
    if data.get("telecine") is not None:
        import capo_mediaconvert.types.h265_telecine

        out["telecine"] = capo_mediaconvert.types.h265_telecine.deserialize_json(
            data["telecine"]
        )
    if data.get("temporalAdaptiveQuantization") is not None:
        import capo_mediaconvert.types.h265_temporal_adaptive_quantization

        out["temporal_adaptive_quantization"] = (
            capo_mediaconvert.types.h265_temporal_adaptive_quantization.deserialize_json(
                data["temporalAdaptiveQuantization"]
            )
        )
    if data.get("temporalIds") is not None:
        import capo_mediaconvert.types.h265_temporal_ids

        out["temporal_ids"] = (
            capo_mediaconvert.types.h265_temporal_ids.deserialize_json(
                data["temporalIds"]
            )
        )
    if data.get("tileHeight") is not None:
        out["tile_height"] = data["tileHeight"]
    if data.get("tilePadding") is not None:
        import capo_mediaconvert.types.h265_tile_padding

        out["tile_padding"] = (
            capo_mediaconvert.types.h265_tile_padding.deserialize_json(
                data["tilePadding"]
            )
        )
    if data.get("tileWidth") is not None:
        out["tile_width"] = data["tileWidth"]
    if data.get("tiles") is not None:
        import capo_mediaconvert.types.h265_tiles

        out["tiles"] = capo_mediaconvert.types.h265_tiles.deserialize_json(
            data["tiles"]
        )
    if data.get("treeBlockSize") is not None:
        import capo_mediaconvert.types.h265_tree_block_size

        out["tree_block_size"] = (
            capo_mediaconvert.types.h265_tree_block_size.deserialize_json(
                data["treeBlockSize"]
            )
        )
    if data.get("unregisteredSeiTimecode") is not None:
        import capo_mediaconvert.types.h265_unregistered_sei_timecode

        out["unregistered_sei_timecode"] = (
            capo_mediaconvert.types.h265_unregistered_sei_timecode.deserialize_json(
                data["unregisteredSeiTimecode"]
            )
        )
    if data.get("writeMp4PackagingType") is not None:
        import capo_mediaconvert.types.h265_write_mp4_packaging_type

        out["write_mp4_packaging_type"] = (
            capo_mediaconvert.types.h265_write_mp4_packaging_type.deserialize_json(
                data["writeMp4PackagingType"]
            )
        )
    return out
