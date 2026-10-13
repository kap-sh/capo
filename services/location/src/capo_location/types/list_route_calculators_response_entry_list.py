"""Generated from Smithy shape ``com.amazonaws.location#ListRouteCalculatorsResponseEntryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.list_route_calculators_response_entry

ListRouteCalculatorsResponseEntryList: TypeAlias = list[
    "capo_location.types.list_route_calculators_response_entry.ListRouteCalculatorsResponseEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListRouteCalculatorsResponseEntryList) -> list:
    import capo_location.types.list_route_calculators_response_entry

    out: list = []
    for item in value:
        out.append(
            capo_location.types.list_route_calculators_response_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListRouteCalculatorsResponseEntryList:
    import capo_location.types.list_route_calculators_response_entry

    out: ListRouteCalculatorsResponseEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_location.types.list_route_calculators_response_entry.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: ListRouteCalculatorsResponseEntryList) -> list[Any]:
    import capo_location.types.list_route_calculators_response_entry

    return [
        capo_location.types.list_route_calculators_response_entry.redact_sensitive(item)
        for item in value
    ]
