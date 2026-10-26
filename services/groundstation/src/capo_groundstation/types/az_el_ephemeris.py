"""Generated from Smithy shape ``com.amazonaws.groundstation#AzElEphemeris``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.az_el_segments_data
    import capo_groundstation.types.ground_station_name


class AzElEphemeris(TypedDict, closed=True):
    ground_station: "capo_groundstation.types.ground_station_name.GroundStationName"
    """<p>The ground station name for which you're providing azimuth elevation data.</p> <p>This ephemeris is specific to this ground station and can't be used at other locations.</p>"""
    data: "capo_groundstation.types.az_el_segments_data.AzElSegmentsData"
    """<p>Azimuth elevation segment data.</p> <p>You can provide data inline in the request or through an Amazon S3 object reference.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzElEphemeris) -> dict:
    out: dict = {}
    out["groundStation"] = value["ground_station"]
    import capo_groundstation.types.az_el_segments_data

    out["data"] = capo_groundstation.types.az_el_segments_data.serialize_json(
        value["data"]
    )
    return out


def deserialize_json(data: dict) -> AzElEphemeris:
    out: AzElEphemeris = {}  # type: ignore[typeddict-item]
    if data.get("groundStation") is not None:
        out["ground_station"] = data["groundStation"]
    else:
        out["ground_station"] = ""
    if data.get("data") is not None:
        import capo_groundstation.types.az_el_segments_data

        out["data"] = capo_groundstation.types.az_el_segments_data.deserialize_json(
            data["data"]
        )
    else:
        out["data"] = {"$unknown": {"name": ""}}
    return out
