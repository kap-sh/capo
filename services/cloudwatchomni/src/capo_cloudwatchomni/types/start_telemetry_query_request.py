"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#StartTelemetryQueryRequest``."""

from typing_extensions import TypedDict


class StartTelemetryQueryRequest(TypedDict, closed=True):
    query_string: "str"
    """The query string to execute."""
    session_id: "str"
    """The unique ID of the session."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartTelemetryQueryRequest) -> dict:
    out: dict = {}
    out["queryString"] = value["query_string"]
    out["sessionId"] = value["session_id"]
    return out


def deserialize_cbor(data: dict) -> StartTelemetryQueryRequest:
    out: StartTelemetryQueryRequest = {}  # type: ignore[typeddict-item]
    if data.get("queryString") is not None:
        out["query_string"] = data["queryString"]
    else:
        out["query_string"] = ""
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    return out
