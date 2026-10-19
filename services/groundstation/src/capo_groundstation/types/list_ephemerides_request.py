"""Generated from Smithy shape ``com.amazonaws.groundstation#ListEphemeridesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_groundstation.types.ephemeris_status_list
    import capo_groundstation.types.ephemeris_type
    import capo_groundstation.types.pagination_max_results
    import capo_groundstation.types.pagination_token
    import capo_groundstation.types.uuid


class ListEphemeridesRequest(TypedDict, closed=True):
    satellite_id: NotRequired["capo_groundstation.types.uuid.Uuid"]
    """<p>The AWS Ground Station satellite ID to list ephemeris for.</p>"""
    ephemeris_type: NotRequired["capo_groundstation.types.ephemeris_type.EphemerisType"]
    """<p>Filter ephemerides by type. If not specified, all ephemeris types will be returned.</p>"""
    start_time: "datetime.datetime"
    """<p>The start time for the list operation in UTC. Returns ephemerides with expiration times within your specified time range.</p>"""
    end_time: "datetime.datetime"
    """<p>The end time for the list operation in UTC. Returns ephemerides with expiration times within your specified time range.</p>"""
    status_list: NotRequired[
        "capo_groundstation.types.ephemeris_status_list.EphemerisStatusList"
    ]
    """<p>The list of ephemeris status to return.</p>"""
    max_results: NotRequired[
        "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
    ]
    """<p>Maximum number of ephemerides to return.</p>"""
    next_token: NotRequired["capo_groundstation.types.pagination_token.PaginationToken"]
    """<p>Pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEphemeridesRequest) -> dict:
    out: dict = {}
    if "satellite_id" in value:
        out["satelliteId"] = value["satellite_id"]
    if "ephemeris_type" in value:
        import capo_groundstation.types.ephemeris_type

        out["ephemerisType"] = capo_groundstation.types.ephemeris_type.serialize_json(
            value["ephemeris_type"]
        )
    import capo_groundstation.types._prelude.timestamp

    out["startTime"] = capo_groundstation.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    import capo_groundstation.types._prelude.timestamp

    out["endTime"] = capo_groundstation.types._prelude.timestamp.serialize_json(
        value["end_time"]
    )
    if "status_list" in value:
        import capo_groundstation.types.ephemeris_status_list

        out["statusList"] = (
            capo_groundstation.types.ephemeris_status_list.serialize_json(
                value["status_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListEphemeridesRequest:
    out: ListEphemeridesRequest = {}  # type: ignore[typeddict-item]
    if data.get("satelliteId") is not None:
        out["satellite_id"] = data["satelliteId"]
    if data.get("ephemerisType") is not None:
        import capo_groundstation.types.ephemeris_type

        out["ephemeris_type"] = (
            capo_groundstation.types.ephemeris_type.deserialize_json(
                data["ephemerisType"]
            )
        )
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
    if data.get("statusList") is not None:
        import capo_groundstation.types.ephemeris_status_list

        out["status_list"] = (
            capo_groundstation.types.ephemeris_status_list.deserialize_json(
                data["statusList"]
            )
        )
    return out
