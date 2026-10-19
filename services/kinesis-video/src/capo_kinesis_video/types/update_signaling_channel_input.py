"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#UpdateSignalingChannelInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.resource_arn
    import capo_kinesis_video.types.single_master_configuration
    import capo_kinesis_video.types.version


class UpdateSignalingChannelInput(TypedDict, closed=True):
    channel_arn: "capo_kinesis_video.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the signaling channel that you want to update.</p>"""
    current_version: "capo_kinesis_video.types.version.Version"
    """<p>The current version of the signaling channel that you want to update.</p>"""
    single_master_configuration: NotRequired[
        "capo_kinesis_video.types.single_master_configuration.SingleMasterConfiguration"
    ]
    """<p>The structure containing the configuration for the <code>SINGLE_MASTER</code> type of the signaling channel that you want to update. This parameter and the channel message's time-to-live are required for channels with the <code>SINGLE_MASTER</code> channel type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSignalingChannelInput) -> dict:
    out: dict = {}
    out["ChannelARN"] = value["channel_arn"]
    out["CurrentVersion"] = value["current_version"]
    if "single_master_configuration" in value:
        import capo_kinesis_video.types.single_master_configuration

        out["SingleMasterConfiguration"] = (
            capo_kinesis_video.types.single_master_configuration.serialize_json(
                value["single_master_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSignalingChannelInput:
    out: UpdateSignalingChannelInput = {}  # type: ignore[typeddict-item]
    if data.get("ChannelARN") is not None:
        out["channel_arn"] = data["ChannelARN"]
    else:
        out["channel_arn"] = ""
    if data.get("CurrentVersion") is not None:
        out["current_version"] = data["CurrentVersion"]
    else:
        out["current_version"] = ""
    if data.get("SingleMasterConfiguration") is not None:
        import capo_kinesis_video.types.single_master_configuration

        out["single_master_configuration"] = (
            capo_kinesis_video.types.single_master_configuration.deserialize_json(
                data["SingleMasterConfiguration"]
            )
        )
    return out
