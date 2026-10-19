"""Generated from Smithy shape ``com.amazonaws.groundstation#AzElSegment``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_groundstation.types.iso8601_time_range
    import capo_groundstation.types.time_az_el_list


class AzElSegment(TypedDict, closed=True):
    reference_epoch: "datetime.datetime"
    """<p>The reference time for this segment in ISO 8601 format in Coordinated Universal Time (UTC).</p> <p>All time values within the segment's <a>AzElSegment$azElList</a> are specified as offsets in atomic seconds from this reference epoch.</p> <p>Example: <code>2024-01-15T12:00:00.000Z</code> </p>"""
    valid_time_range: "capo_groundstation.types.iso8601_time_range.ISO8601TimeRange"
    """<p>The valid time range for this segment.</p> <p> Specifies the start and end timestamps in ISO 8601 format in Coordinated Universal Time (UTC). The segment's pointing data must cover this entire time range. </p>"""
    az_el_list: "capo_groundstation.types.time_az_el_list.TimeAzElList"
    """<p>List of time-tagged azimuth elevation data points.</p> <p> Must contain at least five points to support 4th order Lagrange interpolation. Points must be in chronological order with no duplicates. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzElSegment) -> dict:
    out: dict = {}
    import capo_groundstation._protocol.serialize

    out["referenceEpoch"] = capo_groundstation._protocol.serialize.fmt_date_time(
        value["reference_epoch"]
    )
    import capo_groundstation.types.iso8601_time_range

    out["validTimeRange"] = capo_groundstation.types.iso8601_time_range.serialize_json(
        value["valid_time_range"]
    )
    import capo_groundstation.types.time_az_el_list

    out["azElList"] = capo_groundstation.types.time_az_el_list.serialize_json(
        value["az_el_list"]
    )
    return out


def deserialize_json(data: dict) -> AzElSegment:
    out: AzElSegment = {}  # type: ignore[typeddict-item]
    if data.get("referenceEpoch") is not None:
        import datetime

        out["reference_epoch"] = datetime.datetime.fromisoformat(
            data["referenceEpoch"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["reference_epoch"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("validTimeRange") is not None:
        import capo_groundstation.types.iso8601_time_range

        out["valid_time_range"] = (
            capo_groundstation.types.iso8601_time_range.deserialize_json(
                data["validTimeRange"]
            )
        )
    else:
        raise DeserializationError("AzElSegment.valid_time_range required")
    if data.get("azElList") is not None:
        import capo_groundstation.types.time_az_el_list

        out["az_el_list"] = capo_groundstation.types.time_az_el_list.deserialize_json(
            data["azElList"]
        )
    else:
        out["az_el_list"] = []
    return out
