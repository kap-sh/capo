"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#EdgeProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.edge_traffic_stats


class EdgeProperties(TypedDict, closed=True):
    protocol: NotRequired["str"]
    """The IANA protocol name for the observed network traffic, such as "tcp"."""
    source_port: NotRequired["str"]
    """The source port of the observed traffic. May be a placeholder when the port is unknown."""
    destination_port: NotRequired["str"]
    """The destination port of the observed traffic. May be a placeholder when the port is unknown."""
    blocked: NotRequired["bool"]
    """Whether the observed network flow was denied. Absent means the edge was not derived from network flow data, which is not the same as allowed."""
    error_code: NotRequired["str"]
    """The error code returned when the call was attempted and refused. Its presence means the edge exists but the dependency is failing."""
    http_status_code: NotRequired["str"]
    """The HTTP status code observed on the request. Distinct from errorCode."""
    http_method: NotRequired["str"]
    """The HTTP method observed on the request."""
    service_initiated: NotRequired["bool"]
    """Whether the caller was an AWS service principal rather than a user or role. Absent means the edge was not derived from a source that reports it."""
    traffic_stats: NotRequired[
        "capo_cloudwatchomni.types.edge_traffic_stats.EdgeTrafficStats"
    ]
    """Traffic counters accumulated over the edge's observation window."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EdgeProperties) -> dict:
    out: dict = {}
    if "protocol" in value:
        out["protocol"] = value["protocol"]
    if "source_port" in value:
        out["sourcePort"] = value["source_port"]
    if "destination_port" in value:
        out["destinationPort"] = value["destination_port"]
    if "blocked" in value:
        out["blocked"] = value["blocked"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "http_status_code" in value:
        out["httpStatusCode"] = value["http_status_code"]
    if "http_method" in value:
        out["httpMethod"] = value["http_method"]
    if "service_initiated" in value:
        out["serviceInitiated"] = value["service_initiated"]
    if "traffic_stats" in value:
        import capo_cloudwatchomni.types.edge_traffic_stats

        out["trafficStats"] = (
            capo_cloudwatchomni.types.edge_traffic_stats.serialize_cbor(
                value["traffic_stats"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> EdgeProperties:
    out: EdgeProperties = {}  # type: ignore[typeddict-item]
    if data.get("protocol") is not None:
        out["protocol"] = data["protocol"]
    if data.get("sourcePort") is not None:
        out["source_port"] = data["sourcePort"]
    if data.get("destinationPort") is not None:
        out["destination_port"] = data["destinationPort"]
    if data.get("blocked") is not None:
        out["blocked"] = data["blocked"]
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    if data.get("httpStatusCode") is not None:
        out["http_status_code"] = data["httpStatusCode"]
    if data.get("httpMethod") is not None:
        out["http_method"] = data["httpMethod"]
    if data.get("serviceInitiated") is not None:
        out["service_initiated"] = data["serviceInitiated"]
    if data.get("trafficStats") is not None:
        import capo_cloudwatchomni.types.edge_traffic_stats

        out["traffic_stats"] = (
            capo_cloudwatchomni.types.edge_traffic_stats.deserialize_cbor(
                data["trafficStats"]
            )
        )
    return out
