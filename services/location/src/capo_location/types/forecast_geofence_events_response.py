"""Generated from Smithy shape ``com.amazonaws.location#ForecastGeofenceEventsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.distance_unit
    import capo_location.types.forecasted_events_list
    import capo_location.types.large_token
    import capo_location.types.speed_unit


class ForecastGeofenceEventsResponse(TypedDict, closed=True):
    forecasted_events: "capo_location.types.forecasted_events_list.ForecastedEventsList"
    """<p>The list of forecasted events.</p>"""
    next_token: NotRequired["capo_location.types.large_token.LargeToken"]
    """<p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p>"""
    distance_unit: "capo_location.types.distance_unit.DistanceUnit"
    """<p>The distance unit for the forecasted events.</p>"""
    speed_unit: "capo_location.types.speed_unit.SpeedUnit"
    """<p>The speed unit for the forecasted events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ForecastGeofenceEventsResponse) -> dict:
    out: dict = {}
    import capo_location.types.forecasted_events_list

    out["ForecastedEvents"] = capo_location.types.forecasted_events_list.serialize_json(
        value["forecasted_events"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["DistanceUnit"] = value["distance_unit"]
    out["SpeedUnit"] = value["speed_unit"]
    return out


def deserialize_json(data: dict) -> ForecastGeofenceEventsResponse:
    out: ForecastGeofenceEventsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ForecastedEvents") is not None:
        import capo_location.types.forecasted_events_list

        out["forecasted_events"] = (
            capo_location.types.forecasted_events_list.deserialize_json(
                data["ForecastedEvents"]
            )
        )
    else:
        raise DeserializationError(
            "ForecastGeofenceEventsResponse.forecasted_events required"
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("DistanceUnit") is not None:
        out["distance_unit"] = data["DistanceUnit"]
    else:
        raise DeserializationError(
            "ForecastGeofenceEventsResponse.distance_unit required"
        )
    if data.get("SpeedUnit") is not None:
        out["speed_unit"] = data["SpeedUnit"]
    else:
        raise DeserializationError("ForecastGeofenceEventsResponse.speed_unit required")
    return out


def redact_sensitive(value: ForecastGeofenceEventsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "forecasted_events" in value:
        import capo_location.types.forecasted_events_list

        out["forecasted_events"] = (
            capo_location.types.forecasted_events_list.redact_sensitive(
                value["forecasted_events"]
            )
        )
    return out
