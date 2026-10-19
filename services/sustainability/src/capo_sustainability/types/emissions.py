"""Generated from Smithy shape ``com.amazonaws.sustainability#Emissions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sustainability.types.emissions_unit


class Emissions(TypedDict, closed=True):
    value: "float"
    """<p>The numeric value of the emissions quantity.</p>"""
    unit: "capo_sustainability.types.emissions_unit.EmissionsUnit"
    """<p>The unit of measurement for the emissions value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Emissions) -> dict:
    out: dict = {}
    out["Value"] = (
        "NaN"
        if value["value"] != value["value"]
        else "Infinity"
        if value["value"] == float("inf")
        else "-Infinity"
        if value["value"] == float("-inf")
        else value["value"]
    )
    import capo_sustainability.types.emissions_unit

    out["Unit"] = capo_sustainability.types.emissions_unit.serialize_json(value["unit"])
    return out


def deserialize_json(data: dict) -> Emissions:
    out: Emissions = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = float(data["Value"])
    else:
        out["value"] = 0.0
    if data.get("Unit") is not None:
        import capo_sustainability.types.emissions_unit

        out["unit"] = capo_sustainability.types.emissions_unit.deserialize_json(
            data["Unit"]
        )
    else:
        import typing

        out["unit"] = typing.cast(
            "capo_sustainability.types.emissions_unit.EmissionsUnit", ""
        )
    return out
