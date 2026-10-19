"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#GetDataEndpointInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.api_name
    import capo_kinesis_video.types.resource_arn
    import capo_kinesis_video.types.stream_name


class GetDataEndpointInput(TypedDict, closed=True):
    stream_name: NotRequired["capo_kinesis_video.types.stream_name.StreamName"]
    """<p>The name of the stream that you want to get the endpoint for. You must specify either this parameter or a <code>StreamARN</code> in the request.</p>"""
    stream_arn: NotRequired["capo_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the stream that you want to get the endpoint for. You must specify either this parameter or a <code>StreamName</code> in the request. </p>"""
    api_name: "capo_kinesis_video.types.api_name.APIName"
    """<p>The name of the API action for which to get an endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataEndpointInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    import capo_kinesis_video.types.api_name

    out["APIName"] = capo_kinesis_video.types.api_name.serialize_json(value["api_name"])
    return out


def deserialize_json(data: dict) -> GetDataEndpointInput:
    out: GetDataEndpointInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamName") is not None:
        out["stream_name"] = data["StreamName"]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    if data.get("APIName") is not None:
        import capo_kinesis_video.types.api_name

        out["api_name"] = capo_kinesis_video.types.api_name.deserialize_json(
            data["APIName"]
        )
    else:
        import typing

        out["api_name"] = typing.cast("capo_kinesis_video.types.api_name.APIName", "")
    return out
