"""Generated from Smithy shape ``com.amazonaws.connect#ChatStreamingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.chat_streaming_endpoint_arn


class ChatStreamingConfiguration(TypedDict, closed=True):
    streaming_endpoint_arn: (
        "capo_connect.types.chat_streaming_endpoint_arn.ChatStreamingEndpointARN"
    )
    """<p>The Amazon Resource Name (ARN) of the standard Amazon SNS topic. The Amazon Resource Name (ARN) of the streaming endpoint that is used to publish real-time message streaming for chat conversations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChatStreamingConfiguration) -> dict:
    out: dict = {}
    out["StreamingEndpointArn"] = value["streaming_endpoint_arn"]
    return out


def deserialize_json(data: dict) -> ChatStreamingConfiguration:
    out: ChatStreamingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("StreamingEndpointArn") is not None:
        out["streaming_endpoint_arn"] = data["StreamingEndpointArn"]
    else:
        out["streaming_endpoint_arn"] = ""
    return out
