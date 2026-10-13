"""Generated from Smithy shape ``com.amazonaws.location#ForecastedEventsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.forecasted_event

ForecastedEventsList: TypeAlias = list[
    "capo_location.types.forecasted_event.ForecastedEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: ForecastedEventsList) -> list:
    import capo_location.types.forecasted_event

    out: list = []
    for item in value:
        out.append(capo_location.types.forecasted_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> ForecastedEventsList:
    import capo_location.types.forecasted_event

    out: ForecastedEventsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_location.types.forecasted_event.deserialize_json(item))
    return out


def redact_sensitive(value: ForecastedEventsList) -> list[Any]:
    import capo_location.types.forecasted_event

    return [
        capo_location.types.forecasted_event.redact_sensitive(item) for item in value
    ]
