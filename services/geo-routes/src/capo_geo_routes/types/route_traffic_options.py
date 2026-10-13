"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTrafficOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.traffic_usage


class RouteTrafficOptions(TypedDict, closed=True):
    flow_event_threshold_override: (
        "capo_geo_routes.types.duration_seconds.DurationSeconds"
    )
    """<p>Duration for which flow traffic is considered valid. For this period, the flow traffic is used over historical traffic data. Flow traffic refers to congestion, which changes very quickly. Duration in seconds for which flow traffic event would be considered valid. While flow traffic event is valid it will be used over the historical traffic data. </p>"""
    usage: NotRequired["capo_geo_routes.types.traffic_usage.TrafficUsage"]
    """<p>Specifies how traffic data should be used when calculating routes.</p> <p>Default Value: <code>UseTrafficData</code> </p> <note> <p>Traffic data usage depends on the time parameters in your route request:</p> <ul> <li> <p>When <code>Usage</code> is set to <code>UseTrafficData</code>:</p> <ul> <li> <p>If <code>DepartNow</code> is set to <code>true</code>, or if you specify <code>DepartureTime</code> or <code>ArrivalTime</code>, then all traffic data is considered (including live traffic and closures).</p> </li> <li> <p>If <code>DepartNow</code>, <code>DepartureTime</code>, and <code>ArrivalTime</code> are all unspecified, then only long-term closures are considered, regardless of this setting.</p> </li> </ul> </li> <li> <p>When <code>Usage</code> is set to <code>IgnoreTrafficData</code>, then all traffic data is ignored regardless of the time parameters in your route request.</p> </li> </ul> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTrafficOptions) -> dict:
    out: dict = {}
    out["FlowEventThresholdOverride"] = value.get("flow_event_threshold_override", 0)
    if "usage" in value:
        import capo_geo_routes.types.traffic_usage

        out["Usage"] = capo_geo_routes.types.traffic_usage.serialize_json(
            value["usage"]
        )
    return out


def deserialize_json(data: dict) -> RouteTrafficOptions:
    out: RouteTrafficOptions = {}  # type: ignore[typeddict-item]
    if data.get("FlowEventThresholdOverride") is not None:
        out["flow_event_threshold_override"] = data["FlowEventThresholdOverride"]
    else:
        out["flow_event_threshold_override"] = 0
    if data.get("Usage") is not None:
        import capo_geo_routes.types.traffic_usage

        out["usage"] = capo_geo_routes.types.traffic_usage.deserialize_json(
            data["Usage"]
        )
    return out


def redact_sensitive(value: RouteTrafficOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "flow_event_threshold_override" in value:
        out["flow_event_threshold_override"] = "*** Sensitive Data Redacted ***"
    return out
