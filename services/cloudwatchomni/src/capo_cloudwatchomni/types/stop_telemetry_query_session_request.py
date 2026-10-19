"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#StopTelemetryQuerySessionRequest``."""

from typing_extensions import TypedDict


class StopTelemetryQuerySessionRequest(TypedDict, closed=True):
    session_id: "str"
    """The unique ID of the session."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StopTelemetryQuerySessionRequest) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    return out


def deserialize_cbor(data: dict) -> StopTelemetryQuerySessionRequest:
    out: StopTelemetryQuerySessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    return out
