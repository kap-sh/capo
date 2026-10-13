"""Generated from Smithy shape ``com.amazonaws.quicksight#RangeConstant``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.limited_sensitive_string


class RangeConstant(TypedDict, closed=True):
    minimum: NotRequired[
        "capo_quicksight.types.limited_sensitive_string.LimitedSensitiveString"
    ]
    """<p>The minimum value for a range constant.</p>"""
    maximum: NotRequired[
        "capo_quicksight.types.limited_sensitive_string.LimitedSensitiveString"
    ]
    """<p>The maximum value for a range constant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RangeConstant) -> dict:
    out: dict = {}
    if "minimum" in value:
        out["Minimum"] = value["minimum"]
    if "maximum" in value:
        out["Maximum"] = value["maximum"]
    return out


def deserialize_json(data: dict) -> RangeConstant:
    out: RangeConstant = {}  # type: ignore[typeddict-item]
    if data.get("Minimum") is not None:
        out["minimum"] = data["Minimum"]
    if data.get("Maximum") is not None:
        out["maximum"] = data["Maximum"]
    return out


def redact_sensitive(value: RangeConstant) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "minimum" in value:
        out["minimum"] = "*** Sensitive Data Redacted ***"
    if "maximum" in value:
        out["maximum"] = "*** Sensitive Data Redacted ***"
    return out
