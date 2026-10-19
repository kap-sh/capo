"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#GetSignalingChannelEndpointInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.resource_arn
    import capo_kinesis_video.types.single_master_channel_endpoint_configuration


class GetSignalingChannelEndpointInput(TypedDict, closed=True):
    channel_arn: "capo_kinesis_video.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the signalling channel for which you want to get an endpoint.</p>"""
    single_master_channel_endpoint_configuration: NotRequired[
        "capo_kinesis_video.types.single_master_channel_endpoint_configuration.SingleMasterChannelEndpointConfiguration"
    ]
    """<p>A structure containing the endpoint configuration for the <code>SINGLE_MASTER</code> channel type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSignalingChannelEndpointInput) -> dict:
    out: dict = {}
    out["ChannelARN"] = value["channel_arn"]
    if "single_master_channel_endpoint_configuration" in value:
        import capo_kinesis_video.types.single_master_channel_endpoint_configuration

        out["SingleMasterChannelEndpointConfiguration"] = (
            capo_kinesis_video.types.single_master_channel_endpoint_configuration.serialize_json(
                value["single_master_channel_endpoint_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSignalingChannelEndpointInput:
    out: GetSignalingChannelEndpointInput = {}  # type: ignore[typeddict-item]
    if data.get("ChannelARN") is not None:
        out["channel_arn"] = data["ChannelARN"]
    else:
        out["channel_arn"] = ""
    if data.get("SingleMasterChannelEndpointConfiguration") is not None:
        import capo_kinesis_video.types.single_master_channel_endpoint_configuration

        out["single_master_channel_endpoint_configuration"] = (
            capo_kinesis_video.types.single_master_channel_endpoint_configuration.deserialize_json(
                data["SingleMasterChannelEndpointConfiguration"]
            )
        )
    return out
