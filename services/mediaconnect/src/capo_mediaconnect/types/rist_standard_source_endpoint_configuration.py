"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RistStandardSourceEndpointConfiguration``."""

from typing_extensions import TypedDict


class RistStandardSourceEndpointConfiguration(TypedDict, closed=True):
    destination_ingest_port: "int"
    """<p>The port on the destination that receives the content. The valid range is 3000 to 30000.</p>"""
    recovery_latency_milliseconds: "int"
    """<p>The amount of time, in milliseconds, that the source endpoint allows for recovering lost packets. The valid range is 10 to 10000.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RistStandardSourceEndpointConfiguration) -> dict:
    out: dict = {}
    out["destinationIngestPort"] = value["destination_ingest_port"]
    out["recoveryLatencyMilliseconds"] = value["recovery_latency_milliseconds"]
    return out


def deserialize_json(data: dict) -> RistStandardSourceEndpointConfiguration:
    out: RistStandardSourceEndpointConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("destinationIngestPort") is not None:
        out["destination_ingest_port"] = data["destinationIngestPort"]
    else:
        out["destination_ingest_port"] = 0
    if data.get("recoveryLatencyMilliseconds") is not None:
        out["recovery_latency_milliseconds"] = data["recoveryLatencyMilliseconds"]
    else:
        out["recovery_latency_milliseconds"] = 0
    return out
