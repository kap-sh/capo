"""Generated from Smithy shape ``com.amazonaws.groundstation#GroundStationReservationListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_groundstation.types.antenna_name
    import capo_groundstation.types.ground_station_name
    import capo_groundstation.types.reservation_details
    import capo_groundstation.types.reservation_type


class GroundStationReservationListItem(TypedDict, closed=True):
    reservation_type: "capo_groundstation.types.reservation_type.ReservationType"
    """<p>Type of a ground station reservation.</p>"""
    ground_station_id: "capo_groundstation.types.ground_station_name.GroundStationName"
    """<p>ID of a ground station.</p>"""
    antenna_name: "capo_groundstation.types.antenna_name.AntennaName"
    """<p>Name of an antenna.</p>"""
    start_time: "datetime.datetime"
    """<p>Start time of a ground station reservation in UTC.</p>"""
    end_time: "datetime.datetime"
    """<p>End time of a ground station reservation in UTC.</p>"""
    reservation_details: (
        "capo_groundstation.types.reservation_details.ReservationDetails"
    )
    """<p>Details of a ground station reservation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroundStationReservationListItem) -> dict:
    out: dict = {}
    import capo_groundstation.types.reservation_type

    out["reservationType"] = capo_groundstation.types.reservation_type.serialize_json(
        value["reservation_type"]
    )
    out["groundStationId"] = value["ground_station_id"]
    out["antennaName"] = value["antenna_name"]
    import capo_groundstation.types._prelude.timestamp

    out["startTime"] = capo_groundstation.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    import capo_groundstation.types._prelude.timestamp

    out["endTime"] = capo_groundstation.types._prelude.timestamp.serialize_json(
        value["end_time"]
    )
    import capo_groundstation.types.reservation_details

    out["reservationDetails"] = (
        capo_groundstation.types.reservation_details.serialize_json(
            value["reservation_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> GroundStationReservationListItem:
    out: GroundStationReservationListItem = {}  # type: ignore[typeddict-item]
    if data.get("reservationType") is not None:
        import capo_groundstation.types.reservation_type

        out["reservation_type"] = (
            capo_groundstation.types.reservation_type.deserialize_json(
                data["reservationType"]
            )
        )
    else:
        import typing

        out["reservation_type"] = typing.cast(
            "capo_groundstation.types.reservation_type.ReservationType", ""
        )
    if data.get("groundStationId") is not None:
        out["ground_station_id"] = data["groundStationId"]
    else:
        out["ground_station_id"] = ""
    if data.get("antennaName") is not None:
        out["antenna_name"] = data["antennaName"]
    else:
        out["antenna_name"] = ""
    if data.get("startTime") is not None:
        import capo_groundstation.types._prelude.timestamp

        out["start_time"] = (
            capo_groundstation.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endTime") is not None:
        import capo_groundstation.types._prelude.timestamp

        out["end_time"] = capo_groundstation.types._prelude.timestamp.deserialize_json(
            data["endTime"]
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("reservationDetails") is not None:
        import capo_groundstation.types.reservation_details

        out["reservation_details"] = (
            capo_groundstation.types.reservation_details.deserialize_json(
                data["reservationDetails"]
            )
        )
    else:
        out["reservation_details"] = {"$unknown": {"name": ""}}
    return out
