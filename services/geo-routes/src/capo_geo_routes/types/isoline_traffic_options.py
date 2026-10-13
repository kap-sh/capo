"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineTrafficOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.traffic_usage


class IsolineTrafficOptions(TypedDict, closed=True):
    flow_event_threshold_override: (
        "capo_geo_routes.types.duration_seconds.DurationSeconds"
    )
    """<p>The duration in seconds that real-time congestion data is considered valid before reverting to historical traffic patterns. This helps balance between using current conditions and more predictable historical data when calculating travel times.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    usage: NotRequired["capo_geo_routes.types.traffic_usage.TrafficUsage"]
    """<p>Controls whether traffic data is used in calculations. <code>UseTrafficData</code> considers both real-time congestion and historical patterns, while <code>IgnoreTrafficData</code> calculates routes based solely on road types and speed limits. Using traffic data provides more accurate real-world estimates but may produce different results at different times of day.</p> <p>Default value: <code>UseTrafficData</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsolineTrafficOptions) -> dict:
    out: dict = {}
    out["FlowEventThresholdOverride"] = value.get("flow_event_threshold_override", 0)
    if "usage" in value:
        import capo_geo_routes.types.traffic_usage

        out["Usage"] = capo_geo_routes.types.traffic_usage.serialize_json(
            value["usage"]
        )
    return out


def deserialize_json(data: dict) -> IsolineTrafficOptions:
    out: IsolineTrafficOptions = {}  # type: ignore[typeddict-item]
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


def redact_sensitive(value: IsolineTrafficOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "flow_event_threshold_override" in value:
        out["flow_event_threshold_override"] = "*** Sensitive Data Redacted ***"
    return out
