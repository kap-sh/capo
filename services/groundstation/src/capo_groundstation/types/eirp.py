"""Generated from Smithy shape ``com.amazonaws.groundstation#Eirp``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.eirp_units


class Eirp(TypedDict, closed=True):
    value: "float"
    """<p>Value of an EIRP. Valid values are between 20.0 to 50.0 dBW.</p>"""
    units: "capo_groundstation.types.eirp_units.EirpUnits"
    """<p>Units of an EIRP.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Eirp) -> dict:
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
    import capo_groundstation.types.eirp_units

    out["units"] = capo_groundstation.types.eirp_units.serialize_json(value["units"])
    return out


def deserialize_json(data: dict) -> Eirp:
    out: Eirp = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = float(data["value"])
    else:
        out["value"] = 0.0
    if data.get("units") is not None:
        import capo_groundstation.types.eirp_units

        out["units"] = capo_groundstation.types.eirp_units.deserialize_json(
            data["units"]
        )
    else:
        import typing

        out["units"] = typing.cast("capo_groundstation.types.eirp_units.EirpUnits", "")
    return out
