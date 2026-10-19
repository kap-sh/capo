"""Generated from Smithy shape ``com.amazonaws.groundstation#AntennaListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.antenna_name
    import capo_groundstation.types.aws_region
    import capo_groundstation.types.ground_station_name


class AntennaListItem(TypedDict, closed=True):
    ground_station_name: (
        "capo_groundstation.types.ground_station_name.GroundStationName"
    )
    """<p>Name of the ground station the antenna is associated with.</p>"""
    antenna_name: "capo_groundstation.types.antenna_name.AntennaName"
    """<p>Name of the antenna.</p>"""
    region: "capo_groundstation.types.aws_region.AWSRegion"
    """<p>Region of the antenna.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AntennaListItem) -> dict:
    out: dict = {}
    out["groundStationName"] = value["ground_station_name"]
    out["antennaName"] = value["antenna_name"]
    out["region"] = value["region"]
    return out


def deserialize_json(data: dict) -> AntennaListItem:
    out: AntennaListItem = {}  # type: ignore[typeddict-item]
    if data.get("groundStationName") is not None:
        out["ground_station_name"] = data["groundStationName"]
    else:
        out["ground_station_name"] = ""
    if data.get("antennaName") is not None:
        out["antenna_name"] = data["antennaName"]
    else:
        out["antenna_name"] = ""
    if data.get("region") is not None:
        out["region"] = data["region"]
    else:
        out["region"] = ""
    return out
