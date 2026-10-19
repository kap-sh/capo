"""Generated from Smithy shape ``com.amazonaws.groundstation#ReserveContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_groundstation.types.ground_station_name
    import capo_groundstation.types.mission_profile_arn
    import capo_groundstation.types.satellite_arn
    import capo_groundstation.types.tags_map
    import capo_groundstation.types.tracking_overrides


class ReserveContactRequest(TypedDict, closed=True):
    mission_profile_arn: (
        "capo_groundstation.types.mission_profile_arn.MissionProfileArn"
    )
    """<p>ARN of a mission profile.</p>"""
    satellite_arn: NotRequired["capo_groundstation.types.satellite_arn.satelliteArn"]
    """<p>ARN of a satellite</p>"""
    start_time: "datetime.datetime"
    """<p>Start time of a contact in UTC.</p>"""
    end_time: "datetime.datetime"
    """<p>End time of a contact in UTC.</p>"""
    ground_station: "capo_groundstation.types.ground_station_name.GroundStationName"
    """<p>Name of a ground station.</p>"""
    tags: NotRequired["capo_groundstation.types.tags_map.TagsMap"]
    """<p>Tags assigned to a contact.</p>"""
    tracking_overrides: NotRequired[
        "capo_groundstation.types.tracking_overrides.TrackingOverrides"
    ]
    """<p>Tracking configuration overrides for the contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReserveContactRequest) -> dict:
    out: dict = {}
    out["missionProfileArn"] = value["mission_profile_arn"]
    if "satellite_arn" in value:
        out["satelliteArn"] = value["satellite_arn"]
    import capo_groundstation.types._prelude.timestamp

    out["startTime"] = capo_groundstation.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    import capo_groundstation.types._prelude.timestamp

    out["endTime"] = capo_groundstation.types._prelude.timestamp.serialize_json(
        value["end_time"]
    )
    out["groundStation"] = value["ground_station"]
    if "tags" in value:
        import capo_groundstation.types.tags_map

        out["tags"] = capo_groundstation.types.tags_map.serialize_json(value["tags"])
    if "tracking_overrides" in value:
        import capo_groundstation.types.tracking_overrides

        out["trackingOverrides"] = (
            capo_groundstation.types.tracking_overrides.serialize_json(
                value["tracking_overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReserveContactRequest:
    out: ReserveContactRequest = {}  # type: ignore[typeddict-item]
    if data.get("missionProfileArn") is not None:
        out["mission_profile_arn"] = data["missionProfileArn"]
    else:
        out["mission_profile_arn"] = ""
    if data.get("satelliteArn") is not None:
        out["satellite_arn"] = data["satelliteArn"]
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
    if data.get("groundStation") is not None:
        out["ground_station"] = data["groundStation"]
    else:
        out["ground_station"] = ""
    if data.get("tags") is not None:
        import capo_groundstation.types.tags_map

        out["tags"] = capo_groundstation.types.tags_map.deserialize_json(data["tags"])
    if data.get("trackingOverrides") is not None:
        import capo_groundstation.types.tracking_overrides

        out["tracking_overrides"] = (
            capo_groundstation.types.tracking_overrides.deserialize_json(
                data["trackingOverrides"]
            )
        )
    return out
