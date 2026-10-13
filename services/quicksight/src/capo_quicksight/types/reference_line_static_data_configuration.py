"""Generated from Smithy shape ``com.amazonaws.quicksight#ReferenceLineStaticDataConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.sensitive_double


class ReferenceLineStaticDataConfiguration(TypedDict, closed=True):
    value: "capo_quicksight.types.sensitive_double.SensitiveDouble"
    """<p>The double input of the static data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceLineStaticDataConfiguration) -> dict:
    out: dict = {}
    out["Value"] = (
        "NaN"
        if value.get("value", 0) != value.get("value", 0)
        else "Infinity"
        if value.get("value", 0) == float("inf")
        else "-Infinity"
        if value.get("value", 0) == float("-inf")
        else value.get("value", 0)
    )
    return out


def deserialize_json(data: dict) -> ReferenceLineStaticDataConfiguration:
    out: ReferenceLineStaticDataConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = float(data["Value"])
    else:
        out["value"] = 0
    return out


def redact_sensitive(value: ReferenceLineStaticDataConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    return out
