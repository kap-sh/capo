"""Generated from Smithy shape ``com.amazonaws.kinesis#StreamModeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.stream_mode


class StreamModeDetails(TypedDict, closed=True):
    stream_mode: "capo_kinesis.types.stream_mode.StreamMode"
    """<p> Specifies the capacity mode to which you want to set your data stream. Currently, in Kinesis Data Streams, you can choose between an <b>on-demand</b> capacity mode and a <b>provisioned</b> capacity mode for your data streams. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamModeDetails) -> dict:
    out: dict = {}
    import capo_kinesis.types.stream_mode

    out["StreamMode"] = capo_kinesis.types.stream_mode.serialize_aws_json_1_1(
        value["stream_mode"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StreamModeDetails:
    out: StreamModeDetails = {}  # type: ignore[typeddict-item]
    if data.get("StreamMode") is not None:
        import capo_kinesis.types.stream_mode

        out["stream_mode"] = capo_kinesis.types.stream_mode.deserialize_aws_json_1_1(
            data["StreamMode"]
        )
    else:
        import typing

        out["stream_mode"] = typing.cast(
            "capo_kinesis.types.stream_mode.StreamMode", ""
        )
    return out
