"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#StartTelemetryQueryResponse``."""

from typing_extensions import TypedDict


class StartTelemetryQueryResponse(TypedDict, closed=True):
    query_id: "str"
    """The unique ID of the query."""
    session_id: "str"
    """The unique ID of the session."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartTelemetryQueryResponse) -> dict:
    out: dict = {}
    out["queryId"] = value["query_id"]
    out["sessionId"] = value["session_id"]
    return out


def deserialize_cbor(data: dict) -> StartTelemetryQueryResponse:
    out: StartTelemetryQueryResponse = {}  # type: ignore[typeddict-item]
    if data.get("queryId") is not None:
        out["query_id"] = data["queryId"]
    else:
        out["query_id"] = ""
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    return out
