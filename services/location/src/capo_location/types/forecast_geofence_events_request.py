"""Generated from Smithy shape ``com.amazonaws.location#ForecastGeofenceEventsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.distance_unit
    import capo_location.types.forecast_geofence_events_device_state
    import capo_location.types.large_token
    import capo_location.types.resource_name
    import capo_location.types.speed_unit


class ForecastGeofenceEventsRequest(TypedDict, closed=True):
    collection_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the geofence collection.</p>"""
    device_state: "capo_location.types.forecast_geofence_events_device_state.ForecastGeofenceEventsDeviceState"
    """<p>Represents the device's state, including its current position and speed. When speed is omitted, this API performs a <i>containment check</i>. The <i>containment check</i> operation returns <code>IDLE</code> events for geofences where the device is currently inside of, but no other events.</p>"""
    time_horizon_minutes: NotRequired["float"]
    """<p>The forward-looking time window for forecasting, specified in minutes. The API only returns events that are predicted to occur within this time horizon. When no value is specified, this API performs a <i>containment check</i>. The <i>containment check</i> operation returns <code>IDLE</code> events for geofences where the device is currently inside of, but no other events.</p>"""
    distance_unit: NotRequired["capo_location.types.distance_unit.DistanceUnit"]
    """<p>The distance unit used for the <code>NearestDistance</code> property returned in a forecasted event. The measurement system must match for <code>DistanceUnit</code> and <code>SpeedUnit</code>; if <code>Kilometers</code> is specified for <code>DistanceUnit</code>, then <code>SpeedUnit</code> must be <code>KilometersPerHour</code>. </p> <p>Default Value: <code>Kilometers</code> </p>"""
    speed_unit: NotRequired["capo_location.types.speed_unit.SpeedUnit"]
    """<p>The speed unit for the device captured by the device state. The measurement system must match for <code>DistanceUnit</code> and <code>SpeedUnit</code>; if <code>Kilometers</code> is specified for <code>DistanceUnit</code>, then <code>SpeedUnit</code> must be <code>KilometersPerHour</code>.</p> <p>Default Value: <code>KilometersPerHour</code>.</p>"""
    next_token: NotRequired["capo_location.types.large_token.LargeToken"]
    """<p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.</p> <p>Default value: <code>null</code> </p>"""
    max_results: NotRequired["int"]
    """<p>An optional limit for the number of resources returned in a single call.</p> <p>Default value: <code>20</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ForecastGeofenceEventsRequest) -> dict:
    out: dict = {}
    import capo_location.types.forecast_geofence_events_device_state

    out["DeviceState"] = (
        capo_location.types.forecast_geofence_events_device_state.serialize_json(
            value["device_state"]
        )
    )
    if "time_horizon_minutes" in value:
        out["TimeHorizonMinutes"] = (
            "NaN"
            if value["time_horizon_minutes"] != value["time_horizon_minutes"]
            else "Infinity"
            if value["time_horizon_minutes"] == float("inf")
            else "-Infinity"
            if value["time_horizon_minutes"] == float("-inf")
            else value["time_horizon_minutes"]
        )
    if "distance_unit" in value:
        out["DistanceUnit"] = value["distance_unit"]
    if "speed_unit" in value:
        out["SpeedUnit"] = value["speed_unit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ForecastGeofenceEventsRequest:
    out: ForecastGeofenceEventsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DeviceState") is not None:
        import capo_location.types.forecast_geofence_events_device_state

        out["device_state"] = (
            capo_location.types.forecast_geofence_events_device_state.deserialize_json(
                data["DeviceState"]
            )
        )
    else:
        raise DeserializationError(
            "ForecastGeofenceEventsRequest.device_state required"
        )
    if data.get("TimeHorizonMinutes") is not None:
        out["time_horizon_minutes"] = float(data["TimeHorizonMinutes"])
    if data.get("DistanceUnit") is not None:
        out["distance_unit"] = data["DistanceUnit"]
    if data.get("SpeedUnit") is not None:
        out["speed_unit"] = data["SpeedUnit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out


def redact_sensitive(value: ForecastGeofenceEventsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "device_state" in value:
        import capo_location.types.forecast_geofence_events_device_state

        out["device_state"] = (
            capo_location.types.forecast_geofence_events_device_state.redact_sensitive(
                value["device_state"]
            )
        )
    return out
