"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#CreateStreamSessionConnectionOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.signal_response


class CreateStreamSessionConnectionOutput(TypedDict, closed=True):
    signal_response: NotRequired[
        "capo_gameliftstreams.types.signal_response.SignalResponse"
    ]
    """<p>The WebRTC answer string that the stream server generates in response to the <code>SignalRequest</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateStreamSessionConnectionOutput) -> dict:
    out: dict = {}
    if "signal_response" in value:
        out["SignalResponse"] = value["signal_response"]
    return out


def deserialize_json(data: dict) -> CreateStreamSessionConnectionOutput:
    out: CreateStreamSessionConnectionOutput = {}  # type: ignore[typeddict-item]
    if data.get("SignalResponse") is not None:
        out["signal_response"] = data["SignalResponse"]
    return out


def redact_sensitive(value: CreateStreamSessionConnectionOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "signal_response" in value:
        out["signal_response"] = "*** Sensitive Data Redacted ***"
    return out
