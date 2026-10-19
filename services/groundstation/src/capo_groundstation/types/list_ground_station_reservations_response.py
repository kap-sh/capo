"""Generated from Smithy shape ``com.amazonaws.groundstation#ListGroundStationReservationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.ground_station_reservation_list
    import capo_groundstation.types.pagination_token


class ListGroundStationReservationsResponse(TypedDict, closed=True):
    reservation_list: "capo_groundstation.types.ground_station_reservation_list.GroundStationReservationList"
    """<p>List of ground station reservations.</p>"""
    next_token: NotRequired["capo_groundstation.types.pagination_token.PaginationToken"]
    """<p>Next token to be used in a subsequent <code>ListGroundStationReservations</code> call to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroundStationReservationsResponse) -> dict:
    out: dict = {}
    import capo_groundstation.types.ground_station_reservation_list

    out["reservationList"] = (
        capo_groundstation.types.ground_station_reservation_list.serialize_json(
            value["reservation_list"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGroundStationReservationsResponse:
    out: ListGroundStationReservationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("reservationList") is not None:
        import capo_groundstation.types.ground_station_reservation_list

        out["reservation_list"] = (
            capo_groundstation.types.ground_station_reservation_list.deserialize_json(
                data["reservationList"]
            )
        )
    else:
        out["reservation_list"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
