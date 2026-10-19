"""Generated from Smithy shape ``com.amazonaws.connect#StartContactStreamingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.streaming_id


class StartContactStreamingResponse(TypedDict, closed=True):
    streaming_id: "capo_connect.types.streaming_id.StreamingId"
    """<p>The identifier of the streaming configuration enabled. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartContactStreamingResponse) -> dict:
    out: dict = {}
    out["StreamingId"] = value["streaming_id"]
    return out


def deserialize_json(data: dict) -> StartContactStreamingResponse:
    out: StartContactStreamingResponse = {}  # type: ignore[typeddict-item]
    if data.get("StreamingId") is not None:
        out["streaming_id"] = data["StreamingId"]
    else:
        out["streaming_id"] = ""
    return out
