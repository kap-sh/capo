"""Generated from Smithy shape ``com.amazonaws.billingconductor#FreeTierConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.tiering_activated


class FreeTierConfig(TypedDict, closed=True):
    activated: "capo_billingconductor.types.tiering_activated.TieringActivated"
    """<p> Activate or deactivate Amazon Web Services Free Tier application. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FreeTierConfig) -> dict:
    out: dict = {}
    out["Activated"] = value["activated"]
    return out


def deserialize_json(data: dict) -> FreeTierConfig:
    out: FreeTierConfig = {}  # type: ignore[typeddict-item]
    if data.get("Activated") is not None:
        out["activated"] = data["Activated"]
    else:
        out["activated"] = False
    return out
