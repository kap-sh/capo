"""Generated from Smithy shape ``com.amazonaws.mediaconvert#JobSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min1_max150
    import capo_mediaconvert.types.__integer_min_negative1000_max1000
    import capo_mediaconvert.types.__list_of_color_conversion3_dlut_setting
    import capo_mediaconvert.types.__list_of_input
    import capo_mediaconvert.types.__list_of_motion_image_inserter
    import capo_mediaconvert.types.__list_of_output_group
    import capo_mediaconvert.types.avail_blanking
    import capo_mediaconvert.types.esam_settings
    import capo_mediaconvert.types.extended_data_services
    import capo_mediaconvert.types.kantar_watermark_settings
    import capo_mediaconvert.types.motion_image_inserter
    import capo_mediaconvert.types.nielsen_configuration
    import capo_mediaconvert.types.nielsen_non_linear_watermark_settings
    import capo_mediaconvert.types.timecode_config
    import capo_mediaconvert.types.timed_metadata_insertion


class JobSettings(TypedDict, closed=True):
    ad_avail_offset: NotRequired[
        "capo_mediaconvert.types.__integer_min_negative1000_max1000.__integerMinNegative1000Max1000"
    ]
    """When specified, this offset (in milliseconds) is added to the input Ad Avail PTS time."""
    avail_blanking: NotRequired["capo_mediaconvert.types.avail_blanking.AvailBlanking"]
    """Settings for ad avail blanking. Video can be blanked or overlaid with an image, and audio muted during SCTE-35 triggered ad avails."""
    color_conversion3_dlut_settings: NotRequired[
        "capo_mediaconvert.types.__list_of_color_conversion3_dlut_setting.__listOfColorConversion3DLUTSetting"
    ]
    """Use 3D LUTs to specify custom color mapping behavior when you convert from one color space into another. You can include up to 8 different 3D LUTs. For more information, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/3d-luts.html"""
    esam: NotRequired["capo_mediaconvert.types.esam_settings.EsamSettings"]
    """Settings for Event Signaling And Messaging (ESAM). If you don't do ad insertion, you can ignore these settings."""
    extended_data_services: NotRequired[
        "capo_mediaconvert.types.extended_data_services.ExtendedDataServices"
    ]
    """If your source content has EIA-608 Line 21 Data Services, enable this feature to specify what MediaConvert does with the Extended Data Services (XDS) packets. You can choose to pass through XDS packets, or remove them from the output. For more information about XDS, see EIA-608 Line Data Services, section 9.5.1.5 05h Content Advisory."""
    follow_source: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max150.__integerMin1Max150"
    ]
    """Specify the input that MediaConvert references for your default output settings. MediaConvert uses this input's Resolution, Frame rate, and Pixel aspect ratio for all outputs that you don't manually specify different output settings for. Enabling this setting will disable "Follow source" for all other inputs. If MediaConvert cannot follow your source, for example if you specify an audio-only input, MediaConvert uses the first followable input instead. In your JSON job specification, enter an integer from 1 to 150 corresponding to the order of your inputs."""
    inputs: NotRequired["capo_mediaconvert.types.__list_of_input.__listOfInput"]
    """Use Inputs to define source file used in the transcode job. There can be multiple inputs add in a job. These inputs will be concantenated together to create the output."""
    kantar_watermark: NotRequired[
        "capo_mediaconvert.types.kantar_watermark_settings.KantarWatermarkSettings"
    ]
    """Use these settings only when you use Kantar watermarking. Specify the values that MediaConvert uses to generate and place Kantar watermarks in your output audio. These settings apply to every output in your job. In addition to specifying these values, you also need to store your Kantar credentials in AWS Secrets Manager. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/kantar-watermarking.html."""
    motion_image_inserter: NotRequired[
        "capo_mediaconvert.types.motion_image_inserter.MotionImageInserter"
    ]
    """Overlay motion graphics on top of your video. The motion graphics that you specify here appear on all outputs in all output groups. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/motion-graphic-overlay.html."""
    motion_image_inserters: NotRequired[
        "capo_mediaconvert.types.__list_of_motion_image_inserter.__listOfMotionImageInserter"
    ]
    """Array of motion image inserters for overlaying multiple independent motion graphics. Compositing order follows array index. Mutually exclusive with motionImageInserter."""
    nielsen_configuration: NotRequired[
        "capo_mediaconvert.types.nielsen_configuration.NielsenConfiguration"
    ]
    """Settings for your Nielsen configuration. If you don't do Nielsen measurement and analytics, ignore these settings. When you enable Nielsen configuration, MediaConvert enables PCM to ID3 tagging for all outputs in the job."""
    nielsen_non_linear_watermark: NotRequired[
        "capo_mediaconvert.types.nielsen_non_linear_watermark_settings.NielsenNonLinearWatermarkSettings"
    ]
    """Ignore these settings unless you are using Nielsen non-linear watermarking. Specify the values that MediaConvert uses to generate and place Nielsen watermarks in your output audio. In addition to specifying these values, you also need to set up your cloud TIC server. These settings apply to every output in your job. The MediaConvert implementation is currently with the following Nielsen versions: Nielsen Watermark SDK Version 6.0.13 Nielsen NLM Watermark Engine Version 1.3.3 Nielsen Watermark Authenticator [SID_TIC] Version [7.0.0]"""
    output_groups: NotRequired[
        "capo_mediaconvert.types.__list_of_output_group.__listOfOutputGroup"
    ]
    """Contains one group of settings for each set of outputs that share a common package type. All unpackaged files (MPEG-4, MPEG-2 TS, Quicktime, MXF, and no container) are grouped in a single output group as well. Required in is a group of settings that apply to the whole group. This required object depends on the value you set for Type. Type, settings object pairs are as follows. * FILE_GROUP_SETTINGS, FileGroupSettings * HLS_GROUP_SETTINGS, HlsGroupSettings * DASH_ISO_GROUP_SETTINGS, DashIsoGroupSettings * MS_SMOOTH_GROUP_SETTINGS, MsSmoothGroupSettings * CMAF_GROUP_SETTINGS, CmafGroupSettings"""
    timecode_config: NotRequired[
        "capo_mediaconvert.types.timecode_config.TimecodeConfig"
    ]
    """These settings control how the service handles timecodes throughout the job. These settings don't affect input clipping."""
    timed_metadata_insertion: NotRequired[
        "capo_mediaconvert.types.timed_metadata_insertion.TimedMetadataInsertion"
    ]
    """Insert user-defined custom ID3 metadata at timecodes that you specify. In each output that you want to include this metadata, you must set ID3 metadata to Passthrough."""


# --- restJson1 ser/de ---
def serialize_json(value: JobSettings) -> dict:
    out: dict = {}
    if "ad_avail_offset" in value:
        out["adAvailOffset"] = value["ad_avail_offset"]
    if "avail_blanking" in value:
        import capo_mediaconvert.types.avail_blanking

        out["availBlanking"] = capo_mediaconvert.types.avail_blanking.serialize_json(
            value["avail_blanking"]
        )
    if "color_conversion3_dlut_settings" in value:
        import capo_mediaconvert.types.__list_of_color_conversion3_dlut_setting

        out["colorConversion3DLUTSettings"] = (
            capo_mediaconvert.types.__list_of_color_conversion3_dlut_setting.serialize_json(
                value["color_conversion3_dlut_settings"]
            )
        )
    if "esam" in value:
        import capo_mediaconvert.types.esam_settings

        out["esam"] = capo_mediaconvert.types.esam_settings.serialize_json(
            value["esam"]
        )
    if "extended_data_services" in value:
        import capo_mediaconvert.types.extended_data_services

        out["extendedDataServices"] = (
            capo_mediaconvert.types.extended_data_services.serialize_json(
                value["extended_data_services"]
            )
        )
    if "follow_source" in value:
        out["followSource"] = value["follow_source"]
    if "inputs" in value:
        import capo_mediaconvert.types.__list_of_input

        out["inputs"] = capo_mediaconvert.types.__list_of_input.serialize_json(
            value["inputs"]
        )
    if "kantar_watermark" in value:
        import capo_mediaconvert.types.kantar_watermark_settings

        out["kantarWatermark"] = (
            capo_mediaconvert.types.kantar_watermark_settings.serialize_json(
                value["kantar_watermark"]
            )
        )
    if "motion_image_inserter" in value:
        import capo_mediaconvert.types.motion_image_inserter

        out["motionImageInserter"] = (
            capo_mediaconvert.types.motion_image_inserter.serialize_json(
                value["motion_image_inserter"]
            )
        )
    if "motion_image_inserters" in value:
        import capo_mediaconvert.types.__list_of_motion_image_inserter

        out["motionImageInserters"] = (
            capo_mediaconvert.types.__list_of_motion_image_inserter.serialize_json(
                value["motion_image_inserters"]
            )
        )
    if "nielsen_configuration" in value:
        import capo_mediaconvert.types.nielsen_configuration

        out["nielsenConfiguration"] = (
            capo_mediaconvert.types.nielsen_configuration.serialize_json(
                value["nielsen_configuration"]
            )
        )
    if "nielsen_non_linear_watermark" in value:
        import capo_mediaconvert.types.nielsen_non_linear_watermark_settings

        out["nielsenNonLinearWatermark"] = (
            capo_mediaconvert.types.nielsen_non_linear_watermark_settings.serialize_json(
                value["nielsen_non_linear_watermark"]
            )
        )
    if "output_groups" in value:
        import capo_mediaconvert.types.__list_of_output_group

        out["outputGroups"] = (
            capo_mediaconvert.types.__list_of_output_group.serialize_json(
                value["output_groups"]
            )
        )
    if "timecode_config" in value:
        import capo_mediaconvert.types.timecode_config

        out["timecodeConfig"] = capo_mediaconvert.types.timecode_config.serialize_json(
            value["timecode_config"]
        )
    if "timed_metadata_insertion" in value:
        import capo_mediaconvert.types.timed_metadata_insertion

        out["timedMetadataInsertion"] = (
            capo_mediaconvert.types.timed_metadata_insertion.serialize_json(
                value["timed_metadata_insertion"]
            )
        )
    return out


def deserialize_json(data: dict) -> JobSettings:
    out: JobSettings = {}  # type: ignore[typeddict-item]
    if data.get("adAvailOffset") is not None:
        out["ad_avail_offset"] = data["adAvailOffset"]
    if data.get("availBlanking") is not None:
        import capo_mediaconvert.types.avail_blanking

        out["avail_blanking"] = capo_mediaconvert.types.avail_blanking.deserialize_json(
            data["availBlanking"]
        )
    if data.get("colorConversion3DLUTSettings") is not None:
        import capo_mediaconvert.types.__list_of_color_conversion3_dlut_setting

        out["color_conversion3_dlut_settings"] = (
            capo_mediaconvert.types.__list_of_color_conversion3_dlut_setting.deserialize_json(
                data["colorConversion3DLUTSettings"]
            )
        )
    if data.get("esam") is not None:
        import capo_mediaconvert.types.esam_settings

        out["esam"] = capo_mediaconvert.types.esam_settings.deserialize_json(
            data["esam"]
        )
    if data.get("extendedDataServices") is not None:
        import capo_mediaconvert.types.extended_data_services

        out["extended_data_services"] = (
            capo_mediaconvert.types.extended_data_services.deserialize_json(
                data["extendedDataServices"]
            )
        )
    if data.get("followSource") is not None:
        out["follow_source"] = data["followSource"]
    if data.get("inputs") is not None:
        import capo_mediaconvert.types.__list_of_input

        out["inputs"] = capo_mediaconvert.types.__list_of_input.deserialize_json(
            data["inputs"]
        )
    if data.get("kantarWatermark") is not None:
        import capo_mediaconvert.types.kantar_watermark_settings

        out["kantar_watermark"] = (
            capo_mediaconvert.types.kantar_watermark_settings.deserialize_json(
                data["kantarWatermark"]
            )
        )
    if data.get("motionImageInserter") is not None:
        import capo_mediaconvert.types.motion_image_inserter

        out["motion_image_inserter"] = (
            capo_mediaconvert.types.motion_image_inserter.deserialize_json(
                data["motionImageInserter"]
            )
        )
    if data.get("motionImageInserters") is not None:
        import capo_mediaconvert.types.__list_of_motion_image_inserter

        out["motion_image_inserters"] = (
            capo_mediaconvert.types.__list_of_motion_image_inserter.deserialize_json(
                data["motionImageInserters"]
            )
        )
    if data.get("nielsenConfiguration") is not None:
        import capo_mediaconvert.types.nielsen_configuration

        out["nielsen_configuration"] = (
            capo_mediaconvert.types.nielsen_configuration.deserialize_json(
                data["nielsenConfiguration"]
            )
        )
    if data.get("nielsenNonLinearWatermark") is not None:
        import capo_mediaconvert.types.nielsen_non_linear_watermark_settings

        out["nielsen_non_linear_watermark"] = (
            capo_mediaconvert.types.nielsen_non_linear_watermark_settings.deserialize_json(
                data["nielsenNonLinearWatermark"]
            )
        )
    if data.get("outputGroups") is not None:
        import capo_mediaconvert.types.__list_of_output_group

        out["output_groups"] = (
            capo_mediaconvert.types.__list_of_output_group.deserialize_json(
                data["outputGroups"]
            )
        )
    if data.get("timecodeConfig") is not None:
        import capo_mediaconvert.types.timecode_config

        out["timecode_config"] = (
            capo_mediaconvert.types.timecode_config.deserialize_json(
                data["timecodeConfig"]
            )
        )
    if data.get("timedMetadataInsertion") is not None:
        import capo_mediaconvert.types.timed_metadata_insertion

        out["timed_metadata_insertion"] = (
            capo_mediaconvert.types.timed_metadata_insertion.deserialize_json(
                data["timedMetadataInsertion"]
            )
        )
    return out
