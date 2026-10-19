"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledBaselineParameterSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.enabled_baseline_parameter_document


class EnabledBaselineParameterSummary(TypedDict, closed=True):
    key: "str"
    """<p>A string denoting the parameter key.</p>"""
    value: "capo_controltower.types.enabled_baseline_parameter_document.EnabledBaselineParameterDocument"
    """<p>A low-level document object of any type (for example, a Java Object).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnabledBaselineParameterSummary) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> EnabledBaselineParameterSummary:
    out: EnabledBaselineParameterSummary = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = None
    return out
