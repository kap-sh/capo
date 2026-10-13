"""Generated from Smithy shape ``com.amazonaws.location#PositionalAccuracy``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.sensitive_double


class PositionalAccuracy(TypedDict, closed=True):
    horizontal: "capo_location.types.sensitive_double.SensitiveDouble"
    """<p>Estimated maximum distance, in meters, between the measured position and the true position of a device, along the Earth's surface.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PositionalAccuracy) -> dict:
    out: dict = {}
    out["Horizontal"] = (
        "NaN"
        if value["horizontal"] != value["horizontal"]
        else "Infinity"
        if value["horizontal"] == float("inf")
        else "-Infinity"
        if value["horizontal"] == float("-inf")
        else value["horizontal"]
    )
    return out


def deserialize_json(data: dict) -> PositionalAccuracy:
    out: PositionalAccuracy = {}  # type: ignore[typeddict-item]
    if data.get("Horizontal") is not None:
        out["horizontal"] = float(data["Horizontal"])
    else:
        raise DeserializationError("PositionalAccuracy.horizontal required")
    return out


def redact_sensitive(value: PositionalAccuracy) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "horizontal" in value:
        out["horizontal"] = "*** Sensitive Data Redacted ***"
    return out
