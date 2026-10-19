"""Generated from Smithy shape ``com.amazonaws.location#InferredState``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.position
    import capo_location.types.positional_accuracy


class InferredState(TypedDict, closed=True):
    position: NotRequired["capo_location.types.position.Position"]
    """<p>The device position inferred by the provided position, IP address, cellular signals, and Wi-Fi- access points.</p>"""
    accuracy: NotRequired["capo_location.types.positional_accuracy.PositionalAccuracy"]
    """<p>The level of certainty of the inferred position.</p>"""
    deviation_distance: NotRequired["float"]
    """<p>The distance between the inferred position and the device's self-reported position.</p>"""
    proxy_detected: "bool"
    """<p>Indicates if a proxy was used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InferredState) -> dict:
    out: dict = {}
    if "position" in value:
        import capo_location.types.position

        out["Position"] = capo_location.types.position.serialize_json(value["position"])
    if "accuracy" in value:
        import capo_location.types.positional_accuracy

        out["Accuracy"] = capo_location.types.positional_accuracy.serialize_json(
            value["accuracy"]
        )
    if "deviation_distance" in value:
        out["DeviationDistance"] = (
            "NaN"
            if value["deviation_distance"] != value["deviation_distance"]
            else "Infinity"
            if value["deviation_distance"] == float("inf")
            else "-Infinity"
            if value["deviation_distance"] == float("-inf")
            else value["deviation_distance"]
        )
    out["ProxyDetected"] = value["proxy_detected"]
    return out


def deserialize_json(data: dict) -> InferredState:
    out: InferredState = {}  # type: ignore[typeddict-item]
    if data.get("Position") is not None:
        import capo_location.types.position

        out["position"] = capo_location.types.position.deserialize_json(
            data["Position"]
        )
    if data.get("Accuracy") is not None:
        import capo_location.types.positional_accuracy

        out["accuracy"] = capo_location.types.positional_accuracy.deserialize_json(
            data["Accuracy"]
        )
    if data.get("DeviationDistance") is not None:
        out["deviation_distance"] = float(data["DeviationDistance"])
    if data.get("ProxyDetected") is not None:
        out["proxy_detected"] = data["ProxyDetected"]
    else:
        out["proxy_detected"] = False
    return out


def redact_sensitive(value: InferredState) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "position" in value:
        out["position"] = "*** Sensitive Data Redacted ***"
    if "accuracy" in value:
        import capo_location.types.positional_accuracy

        out["accuracy"] = capo_location.types.positional_accuracy.redact_sensitive(
            value["accuracy"]
        )
    return out
