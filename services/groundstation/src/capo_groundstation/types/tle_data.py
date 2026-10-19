"""Generated from Smithy shape ``com.amazonaws.groundstation#TLEData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_groundstation.types.time_range
    import capo_groundstation.types.tle_line_one
    import capo_groundstation.types.tle_line_two


class TLEData(TypedDict, closed=True):
    tle_line1: "capo_groundstation.types.tle_line_one.TleLineOne"
    """<p>First line of two-line element set (TLE) data.</p>"""
    tle_line2: "capo_groundstation.types.tle_line_two.TleLineTwo"
    """<p>Second line of two-line element set (TLE) data.</p>"""
    valid_time_range: "capo_groundstation.types.time_range.TimeRange"
    """<p>The valid time range for the TLE. Time ranges must be continuous without gaps or overlaps.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TLEData) -> dict:
    out: dict = {}
    out["tleLine1"] = value["tle_line1"]
    out["tleLine2"] = value["tle_line2"]
    import capo_groundstation.types.time_range

    out["validTimeRange"] = capo_groundstation.types.time_range.serialize_json(
        value["valid_time_range"]
    )
    return out


def deserialize_json(data: dict) -> TLEData:
    out: TLEData = {}  # type: ignore[typeddict-item]
    if data.get("tleLine1") is not None:
        out["tle_line1"] = data["tleLine1"]
    else:
        out["tle_line1"] = ""
    if data.get("tleLine2") is not None:
        out["tle_line2"] = data["tleLine2"]
    else:
        out["tle_line2"] = ""
    if data.get("validTimeRange") is not None:
        import capo_groundstation.types.time_range

        out["valid_time_range"] = capo_groundstation.types.time_range.deserialize_json(
            data["validTimeRange"]
        )
    else:
        raise DeserializationError("TLEData.valid_time_range required")
    return out
