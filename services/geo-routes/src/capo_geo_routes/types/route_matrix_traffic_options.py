"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixTrafficOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.traffic_usage


class RouteMatrixTrafficOptions(TypedDict, closed=True):
    flow_event_threshold_override: (
        "capo_geo_routes.types.duration_seconds.DurationSeconds"
    )
    """<p>Duration for which flow traffic is considered valid. For this period, the flow traffic is used over historical traffic data. Flow traffic refers to congestion, which changes very quickly. Duration in seconds for which flow traffic event would be considered valid. While flow traffic event is valid it will be used over the historical traffic data. </p>"""
    usage: NotRequired["capo_geo_routes.types.traffic_usage.TrafficUsage"]
    """<p>Determines if traffic should be used or ignored while calculating the route.</p> <p>Default value: <code>UseTrafficData</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixTrafficOptions) -> dict:
    out: dict = {}
    out["FlowEventThresholdOverride"] = value.get("flow_event_threshold_override", 0)
    if "usage" in value:
        import capo_geo_routes.types.traffic_usage

        out["Usage"] = capo_geo_routes.types.traffic_usage.serialize_json(
            value["usage"]
        )
    return out


def deserialize_json(data: dict) -> RouteMatrixTrafficOptions:
    out: RouteMatrixTrafficOptions = {}  # type: ignore[typeddict-item]
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


def redact_sensitive(value: RouteMatrixTrafficOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "flow_event_threshold_override" in value:
        out["flow_event_threshold_override"] = "*** Sensitive Data Redacted ***"
    return out
