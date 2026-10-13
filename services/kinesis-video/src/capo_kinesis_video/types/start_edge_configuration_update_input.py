"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#StartEdgeConfigurationUpdateInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_video.types.edge_config
    import capo_kinesis_video.types.resource_arn
    import capo_kinesis_video.types.stream_name


class StartEdgeConfigurationUpdateInput(TypedDict, closed=True):
    stream_name: NotRequired["capo_kinesis_video.types.stream_name.StreamName"]
    """<p>The name of the stream whose edge configuration you want to update. Specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>"""
    stream_arn: NotRequired["capo_kinesis_video.types.resource_arn.ResourceARN"]
    """<p> The Amazon Resource Name (ARN) of the stream. Specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>"""
    edge_config: "capo_kinesis_video.types.edge_config.EdgeConfig"
    """<p>The edge configuration details required to invoke the update process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartEdgeConfigurationUpdateInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    import capo_kinesis_video.types.edge_config

    out["EdgeConfig"] = capo_kinesis_video.types.edge_config.serialize_json(
        value["edge_config"]
    )
    return out


def deserialize_json(data: dict) -> StartEdgeConfigurationUpdateInput:
    out: StartEdgeConfigurationUpdateInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamName") is not None:
        out["stream_name"] = data["StreamName"]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    if data.get("EdgeConfig") is not None:
        import capo_kinesis_video.types.edge_config

        out["edge_config"] = capo_kinesis_video.types.edge_config.deserialize_json(
            data["EdgeConfig"]
        )
    else:
        raise DeserializationError(
            "StartEdgeConfigurationUpdateInput.edge_config required"
        )
    return out


def redact_sensitive(value: StartEdgeConfigurationUpdateInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "edge_config" in value:
        import capo_kinesis_video.types.edge_config

        out["edge_config"] = capo_kinesis_video.types.edge_config.redact_sensitive(
            value["edge_config"]
        )
    return out
