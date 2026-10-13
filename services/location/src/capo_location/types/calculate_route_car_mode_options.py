"""Generated from Smithy shape ``com.amazonaws.location#CalculateRouteCarModeOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.sensitive_boolean


class CalculateRouteCarModeOptions(TypedDict, closed=True):
    avoid_ferries: NotRequired["capo_location.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Avoids ferries when calculating routes.</p> <p>Default Value: <code>false</code> </p> <p>Valid Values: <code>false</code> | <code>true</code> </p>"""
    avoid_tolls: NotRequired["capo_location.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Avoids tolls when calculating routes.</p> <p>Default Value: <code>false</code> </p> <p>Valid Values: <code>false</code> | <code>true</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculateRouteCarModeOptions) -> dict:
    out: dict = {}
    if "avoid_ferries" in value:
        out["AvoidFerries"] = value["avoid_ferries"]
    if "avoid_tolls" in value:
        out["AvoidTolls"] = value["avoid_tolls"]
    return out


def deserialize_json(data: dict) -> CalculateRouteCarModeOptions:
    out: CalculateRouteCarModeOptions = {}  # type: ignore[typeddict-item]
    if data.get("AvoidFerries") is not None:
        out["avoid_ferries"] = data["AvoidFerries"]
    if data.get("AvoidTolls") is not None:
        out["avoid_tolls"] = data["AvoidTolls"]
    return out


def redact_sensitive(value: CalculateRouteCarModeOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "avoid_ferries" in value:
        out["avoid_ferries"] = "*** Sensitive Data Redacted ***"
    if "avoid_tolls" in value:
        out["avoid_tolls"] = "*** Sensitive Data Redacted ***"
    return out
