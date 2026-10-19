"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Insight``."""

from typing_extensions import NotRequired, TypedDict


class Insight(TypedDict, closed=True):
    usage_pattern: "str"
    """<p>A description of the usage pattern.</p>"""
    signals_detected: NotRequired["str"]
    """<p>A description of the signals detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Insight) -> dict:
    out: dict = {}
    out["usagePattern"] = value["usage_pattern"]
    if "signals_detected" in value:
        out["signalsDetected"] = value["signals_detected"]
    return out


def deserialize_json(data: dict) -> Insight:
    out: Insight = {}  # type: ignore[typeddict-item]
    if data.get("usagePattern") is not None:
        out["usage_pattern"] = data["usagePattern"]
    else:
        out["usage_pattern"] = ""
    if data.get("signalsDetected") is not None:
        out["signals_detected"] = data["signalsDetected"]
    return out
