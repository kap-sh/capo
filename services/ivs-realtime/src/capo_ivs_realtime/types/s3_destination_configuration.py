"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#S3DestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.composition_thumbnail_configuration_list
    import capo_ivs_realtime.types.encoder_configuration_arn_list
    import capo_ivs_realtime.types.recording_configuration
    import capo_ivs_realtime.types.storage_configuration_arn


class S3DestinationConfiguration(TypedDict, closed=True):
    storage_configuration_arn: (
        "capo_ivs_realtime.types.storage_configuration_arn.StorageConfigurationArn"
    )
    """<p>ARN of the <a>StorageConfiguration</a> where recorded videos will be stored.</p>"""
    encoder_configuration_arns: "capo_ivs_realtime.types.encoder_configuration_arn_list.EncoderConfigurationArnList"
    """<p>ARNs of the <a>EncoderConfiguration</a> resource. The encoder configuration and stage resources must be in the same AWS account and region. </p>"""
    recording_configuration: NotRequired[
        "capo_ivs_realtime.types.recording_configuration.RecordingConfiguration"
    ]
    """<p>Array of maps, each of the form <code>string:string (key:value)</code>. This is an optional customer specification, currently used only to specify the recording format for storing a recording in Amazon S3.</p>"""
    thumbnail_configurations: NotRequired[
        "capo_ivs_realtime.types.composition_thumbnail_configuration_list.CompositionThumbnailConfigurationList"
    ]
    """<p>A complex type that allows you to enable/disable the recording of thumbnails for a <a>Composition</a> and modify the interval at which thumbnails are generated for the live session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3DestinationConfiguration) -> dict:
    out: dict = {}
    out["storageConfigurationArn"] = value["storage_configuration_arn"]
    import capo_ivs_realtime.types.encoder_configuration_arn_list

    out["encoderConfigurationArns"] = (
        capo_ivs_realtime.types.encoder_configuration_arn_list.serialize_json(
            value["encoder_configuration_arns"]
        )
    )
    if "recording_configuration" in value:
        import capo_ivs_realtime.types.recording_configuration

        out["recordingConfiguration"] = (
            capo_ivs_realtime.types.recording_configuration.serialize_json(
                value["recording_configuration"]
            )
        )
    if "thumbnail_configurations" in value:
        import capo_ivs_realtime.types.composition_thumbnail_configuration_list

        out["thumbnailConfigurations"] = (
            capo_ivs_realtime.types.composition_thumbnail_configuration_list.serialize_json(
                value["thumbnail_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> S3DestinationConfiguration:
    out: S3DestinationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("storageConfigurationArn") is not None:
        out["storage_configuration_arn"] = data["storageConfigurationArn"]
    else:
        out["storage_configuration_arn"] = ""
    if data.get("encoderConfigurationArns") is not None:
        import capo_ivs_realtime.types.encoder_configuration_arn_list

        out["encoder_configuration_arns"] = (
            capo_ivs_realtime.types.encoder_configuration_arn_list.deserialize_json(
                data["encoderConfigurationArns"]
            )
        )
    else:
        out["encoder_configuration_arns"] = []
    if data.get("recordingConfiguration") is not None:
        import capo_ivs_realtime.types.recording_configuration

        out["recording_configuration"] = (
            capo_ivs_realtime.types.recording_configuration.deserialize_json(
                data["recordingConfiguration"]
            )
        )
    if data.get("thumbnailConfigurations") is not None:
        import capo_ivs_realtime.types.composition_thumbnail_configuration_list

        out["thumbnail_configurations"] = (
            capo_ivs_realtime.types.composition_thumbnail_configuration_list.deserialize_json(
                data["thumbnailConfigurations"]
            )
        )
    return out
