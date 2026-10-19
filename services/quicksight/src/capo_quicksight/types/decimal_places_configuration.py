"""Generated from Smithy shape ``com.amazonaws.quicksight#DecimalPlacesConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.decimal_places


class DecimalPlacesConfiguration(TypedDict, closed=True):
    decimal_places: "capo_quicksight.types.decimal_places.DecimalPlaces"
    """<p>The values of the decimal places.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DecimalPlacesConfiguration) -> dict:
    out: dict = {}
    out["DecimalPlaces"] = value["decimal_places"]
    return out


def deserialize_json(data: dict) -> DecimalPlacesConfiguration:
    out: DecimalPlacesConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("DecimalPlaces") is not None:
        out["decimal_places"] = data["DecimalPlaces"]
    else:
        out["decimal_places"] = 0
    return out
