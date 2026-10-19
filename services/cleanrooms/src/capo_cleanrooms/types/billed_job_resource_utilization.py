"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BilledJobResourceUtilization``."""

from typing_extensions import TypedDict


class BilledJobResourceUtilization(TypedDict, closed=True):
    units: "float"
    """<p> The number of Clean Rooms Processing Unit (CRPU) hours that have been billed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BilledJobResourceUtilization) -> dict:
    out: dict = {}
    out["units"] = (
        "NaN"
        if value["units"] != value["units"]
        else "Infinity"
        if value["units"] == float("inf")
        else "-Infinity"
        if value["units"] == float("-inf")
        else value["units"]
    )
    return out


def deserialize_json(data: dict) -> BilledJobResourceUtilization:
    out: BilledJobResourceUtilization = {}  # type: ignore[typeddict-item]
    if data.get("units") is not None:
        out["units"] = float(data["units"])
    else:
        out["units"] = 0.0
    return out
