"""Generated from Smithy shape ``com.amazonaws.groundstation#ListContactsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_groundstation.types.ephemeris_filter
    import capo_groundstation.types.ground_station_name
    import capo_groundstation.types.mission_profile_arn
    import capo_groundstation.types.pagination_max_results
    import capo_groundstation.types.pagination_token
    import capo_groundstation.types.satellite_arn
    import capo_groundstation.types.status_list


class ListContactsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
    ]
    """<p>Maximum number of contacts returned.</p>"""
    next_token: NotRequired["capo_groundstation.types.pagination_token.PaginationToken"]
    """<p>Next token returned in the request of a previous <code>ListContacts</code> call. Used to get the next page of results.</p>"""
    status_list: "capo_groundstation.types.status_list.StatusList"
    """<p>Status of a contact reservation.</p>"""
    start_time: "datetime.datetime"
    """<p>Start time of a contact in UTC.</p>"""
    end_time: "datetime.datetime"
    """<p>End time of a contact in UTC.</p>"""
    ground_station: NotRequired[
        "capo_groundstation.types.ground_station_name.GroundStationName"
    ]
    """<p>Name of a ground station.</p>"""
    satellite_arn: NotRequired["capo_groundstation.types.satellite_arn.satelliteArn"]
    """<p>ARN of a satellite.</p>"""
    mission_profile_arn: NotRequired[
        "capo_groundstation.types.mission_profile_arn.MissionProfileArn"
    ]
    """<p>ARN of a mission profile.</p>"""
    ephemeris: NotRequired["capo_groundstation.types.ephemeris_filter.EphemerisFilter"]
    """<p>Filter for selecting contacts that use a specific ephemeris".</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContactsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_groundstation.types.status_list

    out["statusList"] = capo_groundstation.types.status_list.serialize_json(
        value["status_list"]
    )
    import capo_groundstation.types._prelude.timestamp

    out["startTime"] = capo_groundstation.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    import capo_groundstation.types._prelude.timestamp

    out["endTime"] = capo_groundstation.types._prelude.timestamp.serialize_json(
        value["end_time"]
    )
    if "ground_station" in value:
        out["groundStation"] = value["ground_station"]
    if "satellite_arn" in value:
        out["satelliteArn"] = value["satellite_arn"]
    if "mission_profile_arn" in value:
        out["missionProfileArn"] = value["mission_profile_arn"]
    if "ephemeris" in value:
        import capo_groundstation.types.ephemeris_filter

        out["ephemeris"] = capo_groundstation.types.ephemeris_filter.serialize_json(
            value["ephemeris"]
        )
    return out


def deserialize_json(data: dict) -> ListContactsRequest:
    out: ListContactsRequest = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("statusList") is not None:
        import capo_groundstation.types.status_list

        out["status_list"] = capo_groundstation.types.status_list.deserialize_json(
            data["statusList"]
        )
    else:
        raise DeserializationError("ListContactsRequest.status_list required")
    if data.get("startTime") is not None:
        import capo_groundstation.types._prelude.timestamp

        out["start_time"] = (
            capo_groundstation.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError("ListContactsRequest.start_time required")
    if data.get("endTime") is not None:
        import capo_groundstation.types._prelude.timestamp

        out["end_time"] = capo_groundstation.types._prelude.timestamp.deserialize_json(
            data["endTime"]
        )
    else:
        raise DeserializationError("ListContactsRequest.end_time required")
    if data.get("groundStation") is not None:
        out["ground_station"] = data["groundStation"]
    if data.get("satelliteArn") is not None:
        out["satellite_arn"] = data["satelliteArn"]
    if data.get("missionProfileArn") is not None:
        out["mission_profile_arn"] = data["missionProfileArn"]
    if data.get("ephemeris") is not None:
        import capo_groundstation.types.ephemeris_filter

        out["ephemeris"] = capo_groundstation.types.ephemeris_filter.deserialize_json(
            data["ephemeris"]
        )
    return out
