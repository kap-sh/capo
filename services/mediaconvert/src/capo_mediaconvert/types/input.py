"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Input``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min0_max5
    import capo_mediaconvert.types.__integer_min1_max2147483647
    import capo_mediaconvert.types.__list_of__string_pattern_s3_assetmap_xml
    import capo_mediaconvert.types.__list_of_input_clipping
    import capo_mediaconvert.types.__list_of_multi_view_settings
    import capo_mediaconvert.types.__list_of_video_overlay
    import capo_mediaconvert.types.__map_of_audio_selector
    import capo_mediaconvert.types.__map_of_audio_selector_group
    import capo_mediaconvert.types.__map_of_caption_selector
    import capo_mediaconvert.types.__map_of_dynamic_audio_selector
    import capo_mediaconvert.types.__string_max2048_pattern_s3_https
    import capo_mediaconvert.types.__string_min11_max11_pattern01_d20305_d205_d
    import capo_mediaconvert.types.__string_min14_pattern_s3_xml_xml_https_xml_xml
    import capo_mediaconvert.types.advanced_input_filter
    import capo_mediaconvert.types.advanced_input_filter_settings
    import capo_mediaconvert.types.image_inserter
    import capo_mediaconvert.types.input_deblock_filter
    import capo_mediaconvert.types.input_decryption_settings
    import capo_mediaconvert.types.input_denoise_filter
    import capo_mediaconvert.types.input_filter_enable
    import capo_mediaconvert.types.input_psi_control
    import capo_mediaconvert.types.input_scan_type
    import capo_mediaconvert.types.input_tams_settings
    import capo_mediaconvert.types.input_timecode_source
    import capo_mediaconvert.types.input_video_generator
    import capo_mediaconvert.types.rectangle
    import capo_mediaconvert.types.video_selector


class Input(TypedDict, closed=True):
    advanced_input_filter: NotRequired[
        "capo_mediaconvert.types.advanced_input_filter.AdvancedInputFilter"
    ]
    """Use to remove noise, blocking, blurriness, or ringing from your input as a pre-filter step before encoding. The Advanced input filter removes more types of compression artifacts and is an improvement when compared to basic Deblock and Denoise filters. To remove video compression artifacts from your input and improve the video quality: Choose Enabled. Additionally, this filter can help increase the video quality of your output relative to its bitrate, since noisy inputs are more complex and require more bits to encode. To help restore loss of detail after applying the filter, you can optionally add texture or sharpening as an additional step. Jobs that use this feature incur pro-tier pricing. To not apply advanced input filtering: Choose Disabled. Note that you can still apply basic filtering with Deblock and Denoise."""
    advanced_input_filter_settings: NotRequired[
        "capo_mediaconvert.types.advanced_input_filter_settings.AdvancedInputFilterSettings"
    ]
    """Optional settings for Advanced input filter when you set Advanced input filter to Enabled."""
    audio_selector_groups: NotRequired[
        "capo_mediaconvert.types.__map_of_audio_selector_group.__mapOfAudioSelectorGroup"
    ]
    """Use audio selector groups to combine multiple sidecar audio inputs so that you can assign them to a single output audio tab. Note that, if you're working with embedded audio, it's simpler to assign multiple input tracks into a single audio selector rather than use an audio selector group."""
    audio_selectors: NotRequired[
        "capo_mediaconvert.types.__map_of_audio_selector.__mapOfAudioSelector"
    ]
    """Use Audio selectors to specify a track or set of tracks from the input that you will use in your outputs. You can use multiple Audio selectors per input."""
    caption_selectors: NotRequired[
        "capo_mediaconvert.types.__map_of_caption_selector.__mapOfCaptionSelector"
    ]
    """Use captions selectors to specify the captions data from your input that you use in your outputs. You can use up to 100 captions selectors per input."""
    crop: NotRequired["capo_mediaconvert.types.rectangle.Rectangle"]
    """Use Cropping selection to specify the video area that the service will include in the output video frame. If you specify a value here, it will override any value that you specify in the output setting Cropping selection."""
    deblock_filter: NotRequired[
        "capo_mediaconvert.types.input_deblock_filter.InputDeblockFilter"
    ]
    """Enable Deblock to produce smoother motion in the output. Default is disabled. Only manually controllable for MPEG2 and uncompressed video inputs."""
    decryption_settings: NotRequired[
        "capo_mediaconvert.types.input_decryption_settings.InputDecryptionSettings"
    ]
    """Settings for decrypting any input files that you encrypt before you upload them to Amazon S3. MediaConvert can decrypt files only when you use AWS Key Management Service (KMS) to encrypt the data key that you use to encrypt your content."""
    denoise_filter: NotRequired[
        "capo_mediaconvert.types.input_denoise_filter.InputDenoiseFilter"
    ]
    """Enable Denoise to filter noise from the input. Default is disabled. Only applicable to MPEG2, H.264, H.265, and uncompressed video inputs."""
    dolby_vision_metadata_xml: NotRequired[
        "capo_mediaconvert.types.__string_min14_pattern_s3_xml_xml_https_xml_xml.__stringMin14PatternS3XmlXMLHttpsXmlXML"
    ]
    """Use this setting only when your video source has Dolby Vision studio mastering metadata that is carried in a separate XML file. Specify the Amazon S3 location for the metadata XML file. MediaConvert uses this file to provide global and frame-level metadata for Dolby Vision preprocessing. When you specify a file here and your input also has interleaved global and frame level metadata, MediaConvert ignores the interleaved metadata and uses only the the metadata from this external XML file. Note that your IAM service role must grant MediaConvert read permissions to this file. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html."""
    dynamic_audio_selectors: NotRequired[
        "capo_mediaconvert.types.__map_of_dynamic_audio_selector.__mapOfDynamicAudioSelector"
    ]
    """Use Dynamic audio selectors when you do not know the track layout of your source when you submit your job, but want to select multiple audio tracks. When you include an audio track in your output and specify this Dynamic audio selector as the Audio source, MediaConvert creates an output audio track for each dynamically selected track. Note that when you include a Dynamic audio selector for two or more inputs, each input must have the same number of audio tracks and audio channels."""
    file_input: NotRequired[
        "capo_mediaconvert.types.__string_max2048_pattern_s3_https.__stringMax2048PatternS3Https"
    ]
    """Specify the source file for your transcoding job. You can use multiple inputs in a single job. The service concatenates these inputs, in the order that you specify them in the job, to create the outputs. For standard inputs, provide the path to your S3, HTTP, or HTTPS source file. For example, s3://amzn-s3-demo-bucket/input.mp4 for an Amazon S3 input or https://example.com/input.mp4 for an HTTPS input. For TAMS inputs, specify the HTTPS endpoint of your TAMS server. For example, https://tams-server.example.com . When you do, also specify Source ID, Timerange, GAP handling, and the Authorization connection ARN under TAMS settings. (Don't include these parameters in the Input file URL.) For IMF inputs, specify your input by providing the path to your CPL. For example, s3://amzn-s3-demo-bucket/vf/cpl.xml . If the CPL is in an incomplete IMP, make sure to use Supplemental IMPsto specify any supplemental IMPs that contain assets referenced by the CPL."""
    filter_enable: NotRequired[
        "capo_mediaconvert.types.input_filter_enable.InputFilterEnable"
    ]
    """Specify whether to apply input filtering to improve the video quality of your input. To apply filtering depending on your input type and quality: Choose Auto. To apply no filtering: Choose Disable. To apply filtering regardless of your input type and quality: Choose Force. When you do, you must also specify a value for Filter strength."""
    filter_strength: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max5.__integerMin0Max5"
    ]
    """Specify the strength of the input filter. To apply an automatic amount of filtering based the compression artifacts measured in your input: We recommend that you leave Filter strength blank and set Filter enable to Auto. To manually apply filtering: Enter a value from 1 to 5, where 1 is the least amount of filtering and 5 is the most. The value that you enter applies to the strength of the Deblock or Denoise filters, or to the strength of the Advanced input filter."""
    image_inserter: NotRequired["capo_mediaconvert.types.image_inserter.ImageInserter"]
    """Enable the image inserter feature to include a graphic overlay on your video. Enable or disable this feature for each input individually. This setting is disabled by default."""
    input_clippings: NotRequired[
        "capo_mediaconvert.types.__list_of_input_clipping.__listOfInputClipping"
    ]
    """Contains sets of start and end times that together specify a portion of the input to be used in the outputs. If you provide only a start time, the clip will be the entire input from that point to the end. If you provide only an end time, it will be the entire input up to that point. When you specify more than one input clip, the transcoding service creates the job outputs by stringing the clips together in the order you specify them."""
    input_scan_type: NotRequired[
        "capo_mediaconvert.types.input_scan_type.InputScanType"
    ]
    """When you have a progressive segmented frame (PsF) input, use this setting to flag the input as PsF. MediaConvert doesn't automatically detect PsF. Therefore, flagging your input as PsF results in better preservation of video quality when you do deinterlacing and frame rate conversion. If you don't specify, the default value is Auto. Auto is the correct setting for all inputs that are not PsF. Don't set this value to PsF when your input is interlaced. Doing so creates horizontal interlacing artifacts."""
    multi_view_settings: NotRequired[
        "capo_mediaconvert.types.__list_of_multi_view_settings.__listOfMultiViewSettings"
    ]
    """Specify the enhancement layer input video file path for Multi View outputs. The base layer input is treated as the left eye and this Multi View input is treated as the right eye. Only one Multi View input is currently supported. MediaConvert encodes both views into a single MV-HEVC output codec. When you add MultiViewSettings to your job, you can only produce Multi View outputs. Adding any other codec output to the same job is not supported."""
    position: NotRequired["capo_mediaconvert.types.rectangle.Rectangle"]
    """Use Selection placement to define the video area in your output frame. The area outside of the rectangle that you specify here is black. If you specify a value here, it will override any value that you specify in the output setting Selection placement. If you specify a value here, this will override any AFD values in your input, even if you set Respond to AFD to Respond. If you specify a value here, this will ignore anything that you specify for the setting Scaling Behavior."""
    program_number: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """Use Program to select a specific program from within a multi-program transport stream. Note that Quad 4K is not currently supported. Default is the first program within the transport stream. If the program you specify doesn't exist, the transcoding service will use this default."""
    psi_control: NotRequired[
        "capo_mediaconvert.types.input_psi_control.InputPsiControl"
    ]
    """Set PSI control for transport stream inputs to specify which data the demux process to scans. * Ignore PSI - Scan all PIDs for audio and video. * Use PSI - Scan only PSI data."""
    supplemental_imps: NotRequired[
        "capo_mediaconvert.types.__list_of__string_pattern_s3_assetmap_xml.__listOf__stringPatternS3ASSETMAPXml"
    ]
    """Provide a list of any necessary supplemental IMPs. You need supplemental IMPs if the CPL that you're using for your input is in an incomplete IMP. Specify either the supplemental IMP directories with a trailing slash or the ASSETMAP.xml files. For example ["s3://bucket/ov/", "s3://bucket/vf2/ASSETMAP.xml"]. You don't need to specify the IMP that contains your input CPL, because the service automatically detects it."""
    tams_settings: NotRequired[
        "capo_mediaconvert.types.input_tams_settings.InputTamsSettings"
    ]
    """Specify a Time Addressable Media Store (TAMS) server as an input source. TAMS is an open-source API specification that provides access to time-segmented media content. Use TAMS to retrieve specific time ranges from live or archived media streams. When you specify TAMS settings, MediaConvert connects to your TAMS server, retrieves the media segments for your specified time range, and processes them as a single input. This enables workflows like extracting clips from live streams or processing specific portions of archived content. To use TAMS, you must: 1. Have access to a TAMS-compliant server 2. Specify the server URL in the Input file URL field 3. Provide the required SourceId and Timerange parameters 4. Configure authentication, if your TAMS server requires it"""
    timecode_source: NotRequired[
        "capo_mediaconvert.types.input_timecode_source.InputTimecodeSource"
    ]
    """Use this Timecode source setting, located under the input settings, to specify how the service counts input video frames. This input frame count affects only the behavior of features that apply to a single input at a time, such as input clipping and synchronizing some captions formats. Choose Embedded to use the timecodes in your input video. Choose Start at zero to start the first frame at zero. Choose Specified start to start the first frame at the timecode that you specify in the setting Start timecode. If you don't specify a value for Timecode source, the service will use Embedded by default. For more information about timecodes, see https://docs.aws.amazon.com/console/mediaconvert/timecode."""
    timecode_start: NotRequired[
        "capo_mediaconvert.types.__string_min11_max11_pattern01_d20305_d205_d.__stringMin11Max11Pattern01D20305D205D"
    ]
    """Specify the timecode that you want the service to use for this input's initial frame. To use this setting, you must set the Timecode source setting, located under the input settings, to Specified start. For more information about timecodes, see https://docs.aws.amazon.com/console/mediaconvert/timecode."""
    video_generator: NotRequired[
        "capo_mediaconvert.types.input_video_generator.InputVideoGenerator"
    ]
    """When you include Video generator, MediaConvert creates a video input with black frames. Use this setting if you do not have a video input or if you want to add black video frames before, or after, other inputs. You can specify Video generator, or you can specify an Input file, but you cannot specify both. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/video-generator.html"""
    video_overlays: NotRequired[
        "capo_mediaconvert.types.__list_of_video_overlay.__listOfVideoOverlay"
    ]
    """Contains an array of video overlays."""
    video_selector: NotRequired["capo_mediaconvert.types.video_selector.VideoSelector"]
    """Input video selectors contain the video settings for the input. Each of your inputs can have up to one video selector."""


# --- restJson1 ser/de ---
def serialize_json(value: Input) -> dict:
    out: dict = {}
    if "advanced_input_filter" in value:
        import capo_mediaconvert.types.advanced_input_filter

        out["advancedInputFilter"] = (
            capo_mediaconvert.types.advanced_input_filter.serialize_json(
                value["advanced_input_filter"]
            )
        )
    if "advanced_input_filter_settings" in value:
        import capo_mediaconvert.types.advanced_input_filter_settings

        out["advancedInputFilterSettings"] = (
            capo_mediaconvert.types.advanced_input_filter_settings.serialize_json(
                value["advanced_input_filter_settings"]
            )
        )
    if "audio_selector_groups" in value:
        import capo_mediaconvert.types.__map_of_audio_selector_group

        out["audioSelectorGroups"] = (
            capo_mediaconvert.types.__map_of_audio_selector_group.serialize_json(
                value["audio_selector_groups"]
            )
        )
    if "audio_selectors" in value:
        import capo_mediaconvert.types.__map_of_audio_selector

        out["audioSelectors"] = (
            capo_mediaconvert.types.__map_of_audio_selector.serialize_json(
                value["audio_selectors"]
            )
        )
    if "caption_selectors" in value:
        import capo_mediaconvert.types.__map_of_caption_selector

        out["captionSelectors"] = (
            capo_mediaconvert.types.__map_of_caption_selector.serialize_json(
                value["caption_selectors"]
            )
        )
    if "crop" in value:
        import capo_mediaconvert.types.rectangle

        out["crop"] = capo_mediaconvert.types.rectangle.serialize_json(value["crop"])
    if "deblock_filter" in value:
        import capo_mediaconvert.types.input_deblock_filter

        out["deblockFilter"] = (
            capo_mediaconvert.types.input_deblock_filter.serialize_json(
                value["deblock_filter"]
            )
        )
    if "decryption_settings" in value:
        import capo_mediaconvert.types.input_decryption_settings

        out["decryptionSettings"] = (
            capo_mediaconvert.types.input_decryption_settings.serialize_json(
                value["decryption_settings"]
            )
        )
    if "denoise_filter" in value:
        import capo_mediaconvert.types.input_denoise_filter

        out["denoiseFilter"] = (
            capo_mediaconvert.types.input_denoise_filter.serialize_json(
                value["denoise_filter"]
            )
        )
    if "dolby_vision_metadata_xml" in value:
        out["dolbyVisionMetadataXml"] = value["dolby_vision_metadata_xml"]
    if "dynamic_audio_selectors" in value:
        import capo_mediaconvert.types.__map_of_dynamic_audio_selector

        out["dynamicAudioSelectors"] = (
            capo_mediaconvert.types.__map_of_dynamic_audio_selector.serialize_json(
                value["dynamic_audio_selectors"]
            )
        )
    if "file_input" in value:
        out["fileInput"] = value["file_input"]
    if "filter_enable" in value:
        import capo_mediaconvert.types.input_filter_enable

        out["filterEnable"] = (
            capo_mediaconvert.types.input_filter_enable.serialize_json(
                value["filter_enable"]
            )
        )
    if "filter_strength" in value:
        out["filterStrength"] = value["filter_strength"]
    if "image_inserter" in value:
        import capo_mediaconvert.types.image_inserter

        out["imageInserter"] = capo_mediaconvert.types.image_inserter.serialize_json(
            value["image_inserter"]
        )
    if "input_clippings" in value:
        import capo_mediaconvert.types.__list_of_input_clipping

        out["inputClippings"] = (
            capo_mediaconvert.types.__list_of_input_clipping.serialize_json(
                value["input_clippings"]
            )
        )
    if "input_scan_type" in value:
        import capo_mediaconvert.types.input_scan_type

        out["inputScanType"] = capo_mediaconvert.types.input_scan_type.serialize_json(
            value["input_scan_type"]
        )
    if "multi_view_settings" in value:
        import capo_mediaconvert.types.__list_of_multi_view_settings

        out["multiViewSettings"] = (
            capo_mediaconvert.types.__list_of_multi_view_settings.serialize_json(
                value["multi_view_settings"]
            )
        )
    if "position" in value:
        import capo_mediaconvert.types.rectangle

        out["position"] = capo_mediaconvert.types.rectangle.serialize_json(
            value["position"]
        )
    if "program_number" in value:
        out["programNumber"] = value["program_number"]
    if "psi_control" in value:
        import capo_mediaconvert.types.input_psi_control

        out["psiControl"] = capo_mediaconvert.types.input_psi_control.serialize_json(
            value["psi_control"]
        )
    if "supplemental_imps" in value:
        import capo_mediaconvert.types.__list_of__string_pattern_s3_assetmap_xml

        out["supplementalImps"] = (
            capo_mediaconvert.types.__list_of__string_pattern_s3_assetmap_xml.serialize_json(
                value["supplemental_imps"]
            )
        )
    if "tams_settings" in value:
        import capo_mediaconvert.types.input_tams_settings

        out["tamsSettings"] = (
            capo_mediaconvert.types.input_tams_settings.serialize_json(
                value["tams_settings"]
            )
        )
    if "timecode_source" in value:
        import capo_mediaconvert.types.input_timecode_source

        out["timecodeSource"] = (
            capo_mediaconvert.types.input_timecode_source.serialize_json(
                value["timecode_source"]
            )
        )
    if "timecode_start" in value:
        out["timecodeStart"] = value["timecode_start"]
    if "video_generator" in value:
        import capo_mediaconvert.types.input_video_generator

        out["videoGenerator"] = (
            capo_mediaconvert.types.input_video_generator.serialize_json(
                value["video_generator"]
            )
        )
    if "video_overlays" in value:
        import capo_mediaconvert.types.__list_of_video_overlay

        out["videoOverlays"] = (
            capo_mediaconvert.types.__list_of_video_overlay.serialize_json(
                value["video_overlays"]
            )
        )
    if "video_selector" in value:
        import capo_mediaconvert.types.video_selector

        out["videoSelector"] = capo_mediaconvert.types.video_selector.serialize_json(
            value["video_selector"]
        )
    return out


def deserialize_json(data: dict) -> Input:
    out: Input = {}  # type: ignore[typeddict-item]
    if data.get("advancedInputFilter") is not None:
        import capo_mediaconvert.types.advanced_input_filter

        out["advanced_input_filter"] = (
            capo_mediaconvert.types.advanced_input_filter.deserialize_json(
                data["advancedInputFilter"]
            )
        )
    if data.get("advancedInputFilterSettings") is not None:
        import capo_mediaconvert.types.advanced_input_filter_settings

        out["advanced_input_filter_settings"] = (
            capo_mediaconvert.types.advanced_input_filter_settings.deserialize_json(
                data["advancedInputFilterSettings"]
            )
        )
    if data.get("audioSelectorGroups") is not None:
        import capo_mediaconvert.types.__map_of_audio_selector_group

        out["audio_selector_groups"] = (
            capo_mediaconvert.types.__map_of_audio_selector_group.deserialize_json(
                data["audioSelectorGroups"]
            )
        )
    if data.get("audioSelectors") is not None:
        import capo_mediaconvert.types.__map_of_audio_selector

        out["audio_selectors"] = (
            capo_mediaconvert.types.__map_of_audio_selector.deserialize_json(
                data["audioSelectors"]
            )
        )
    if data.get("captionSelectors") is not None:
        import capo_mediaconvert.types.__map_of_caption_selector

        out["caption_selectors"] = (
            capo_mediaconvert.types.__map_of_caption_selector.deserialize_json(
                data["captionSelectors"]
            )
        )
    if data.get("crop") is not None:
        import capo_mediaconvert.types.rectangle

        out["crop"] = capo_mediaconvert.types.rectangle.deserialize_json(data["crop"])
    if data.get("deblockFilter") is not None:
        import capo_mediaconvert.types.input_deblock_filter

        out["deblock_filter"] = (
            capo_mediaconvert.types.input_deblock_filter.deserialize_json(
                data["deblockFilter"]
            )
        )
    if data.get("decryptionSettings") is not None:
        import capo_mediaconvert.types.input_decryption_settings

        out["decryption_settings"] = (
            capo_mediaconvert.types.input_decryption_settings.deserialize_json(
                data["decryptionSettings"]
            )
        )
    if data.get("denoiseFilter") is not None:
        import capo_mediaconvert.types.input_denoise_filter

        out["denoise_filter"] = (
            capo_mediaconvert.types.input_denoise_filter.deserialize_json(
                data["denoiseFilter"]
            )
        )
    if data.get("dolbyVisionMetadataXml") is not None:
        out["dolby_vision_metadata_xml"] = data["dolbyVisionMetadataXml"]
    if data.get("dynamicAudioSelectors") is not None:
        import capo_mediaconvert.types.__map_of_dynamic_audio_selector

        out["dynamic_audio_selectors"] = (
            capo_mediaconvert.types.__map_of_dynamic_audio_selector.deserialize_json(
                data["dynamicAudioSelectors"]
            )
        )
    if data.get("fileInput") is not None:
        out["file_input"] = data["fileInput"]
    if data.get("filterEnable") is not None:
        import capo_mediaconvert.types.input_filter_enable

        out["filter_enable"] = (
            capo_mediaconvert.types.input_filter_enable.deserialize_json(
                data["filterEnable"]
            )
        )
    if data.get("filterStrength") is not None:
        out["filter_strength"] = data["filterStrength"]
    if data.get("imageInserter") is not None:
        import capo_mediaconvert.types.image_inserter

        out["image_inserter"] = capo_mediaconvert.types.image_inserter.deserialize_json(
            data["imageInserter"]
        )
    if data.get("inputClippings") is not None:
        import capo_mediaconvert.types.__list_of_input_clipping

        out["input_clippings"] = (
            capo_mediaconvert.types.__list_of_input_clipping.deserialize_json(
                data["inputClippings"]
            )
        )
    if data.get("inputScanType") is not None:
        import capo_mediaconvert.types.input_scan_type

        out["input_scan_type"] = (
            capo_mediaconvert.types.input_scan_type.deserialize_json(
                data["inputScanType"]
            )
        )
    if data.get("multiViewSettings") is not None:
        import capo_mediaconvert.types.__list_of_multi_view_settings

        out["multi_view_settings"] = (
            capo_mediaconvert.types.__list_of_multi_view_settings.deserialize_json(
                data["multiViewSettings"]
            )
        )
    if data.get("position") is not None:
        import capo_mediaconvert.types.rectangle

        out["position"] = capo_mediaconvert.types.rectangle.deserialize_json(
            data["position"]
        )
    if data.get("programNumber") is not None:
        out["program_number"] = data["programNumber"]
    if data.get("psiControl") is not None:
        import capo_mediaconvert.types.input_psi_control

        out["psi_control"] = capo_mediaconvert.types.input_psi_control.deserialize_json(
            data["psiControl"]
        )
    if data.get("supplementalImps") is not None:
        import capo_mediaconvert.types.__list_of__string_pattern_s3_assetmap_xml

        out["supplemental_imps"] = (
            capo_mediaconvert.types.__list_of__string_pattern_s3_assetmap_xml.deserialize_json(
                data["supplementalImps"]
            )
        )
    if data.get("tamsSettings") is not None:
        import capo_mediaconvert.types.input_tams_settings

        out["tams_settings"] = (
            capo_mediaconvert.types.input_tams_settings.deserialize_json(
                data["tamsSettings"]
            )
        )
    if data.get("timecodeSource") is not None:
        import capo_mediaconvert.types.input_timecode_source

        out["timecode_source"] = (
            capo_mediaconvert.types.input_timecode_source.deserialize_json(
                data["timecodeSource"]
            )
        )
    if data.get("timecodeStart") is not None:
        out["timecode_start"] = data["timecodeStart"]
    if data.get("videoGenerator") is not None:
        import capo_mediaconvert.types.input_video_generator

        out["video_generator"] = (
            capo_mediaconvert.types.input_video_generator.deserialize_json(
                data["videoGenerator"]
            )
        )
    if data.get("videoOverlays") is not None:
        import capo_mediaconvert.types.__list_of_video_overlay

        out["video_overlays"] = (
            capo_mediaconvert.types.__list_of_video_overlay.deserialize_json(
                data["videoOverlays"]
            )
        )
    if data.get("videoSelector") is not None:
        import capo_mediaconvert.types.video_selector

        out["video_selector"] = capo_mediaconvert.types.video_selector.deserialize_json(
            data["videoSelector"]
        )
    return out
