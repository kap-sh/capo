"""Generated from Smithy shape ``com.amazonaws.groundstation#Elevation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.angle_units


class Elevation(TypedDict, closed=True):
    value: "float"
    """<p>Elevation angle value.</p>"""
    unit: "capo_groundstation.types.angle_units.AngleUnits"
    """<p>Elevation angle units.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Elevation) -> dict:
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
    import capo_groundstation.types.angle_units

    out["unit"] = capo_groundstation.types.angle_units.serialize_json(value["unit"])
    return out


def deserialize_json(data: dict) -> Elevation:
    out: Elevation = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = float(data["value"])
    else:
        out["value"] = 0.0
    if data.get("unit") is not None:
        import capo_groundstation.types.angle_units

        out["unit"] = capo_groundstation.types.angle_units.deserialize_json(
            data["unit"]
        )
    else:
        import typing

        out["unit"] = typing.cast("capo_groundstation.types.angle_units.AngleUnits", "")
    return out
