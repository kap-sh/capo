"""Generated from Smithy shape ``com.amazonaws.groundstation#Frequency``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.frequency_units


class Frequency(TypedDict, closed=True):
    value: "float"
    """<p>Frequency value. Valid values are between 2200 to 2300 MHz and 7750 to 8400 MHz for downlink and 2025 to 2120 MHz for uplink.</p>"""
    units: "capo_groundstation.types.frequency_units.FrequencyUnits"
    """<p>Frequency units.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Frequency) -> dict:
    out: dict = {}
    out["value"] = (
        "NaN"
        if value["value"] != value["value"]
        else "Infinity"
        if value["value"] == float("inf")
        else "-Infinity"
        if value["value"] == float("-inf")
        else value["value"]
    )
    import capo_groundstation.types.frequency_units

    out["units"] = capo_groundstation.types.frequency_units.serialize_json(
        value["units"]
    )
    return out


def deserialize_json(data: dict) -> Frequency:
    out: Frequency = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = float(data["value"])
    else:
        out["value"] = 0.0
    if data.get("units") is not None:
        import capo_groundstation.types.frequency_units

        out["units"] = capo_groundstation.types.frequency_units.deserialize_json(
            data["units"]
        )
    else:
        import typing

        out["units"] = typing.cast(
            "capo_groundstation.types.frequency_units.FrequencyUnits", ""
        )
    return out
