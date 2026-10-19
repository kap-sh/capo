"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#StartTelemetryQuerySessionResponse``."""

from typing_extensions import TypedDict


class StartTelemetryQuerySessionResponse(TypedDict, closed=True):
    session_id: "str"
    """The unique ID of the session."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartTelemetryQuerySessionResponse) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    return out


def deserialize_cbor(data: dict) -> StartTelemetryQuerySessionResponse:
    out: StartTelemetryQuerySessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    return out
