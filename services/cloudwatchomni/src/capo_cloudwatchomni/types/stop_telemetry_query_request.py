"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#StopTelemetryQueryRequest``."""

from typing_extensions import TypedDict


class StopTelemetryQueryRequest(TypedDict, closed=True):
    query_id: "str"
    """The unique ID of the query."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StopTelemetryQueryRequest) -> dict:
    out: dict = {}
    out["queryId"] = value["query_id"]
    return out


def deserialize_cbor(data: dict) -> StopTelemetryQueryRequest:
    out: StopTelemetryQueryRequest = {}  # type: ignore[typeddict-item]
    if data.get("queryId") is not None:
        out["query_id"] = data["queryId"]
    else:
        out["query_id"] = ""
    return out
