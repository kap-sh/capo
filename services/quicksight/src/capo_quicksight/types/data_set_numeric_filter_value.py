"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetNumericFilterValue``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.sensitive_double


class DataSetNumericFilterValue(TypedDict, closed=True):
    static_value: NotRequired["capo_quicksight.types.sensitive_double.SensitiveDouble"]
    """<p>A static numeric value used for filtering.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetNumericFilterValue) -> dict:
    out: dict = {}
    if "static_value" in value:
        out["StaticValue"] = (
            "NaN"
            if value["static_value"] != value["static_value"]
            else "Infinity"
            if value["static_value"] == float("inf")
            else "-Infinity"
            if value["static_value"] == float("-inf")
            else value["static_value"]
        )
    return out


def deserialize_json(data: dict) -> DataSetNumericFilterValue:
    out: DataSetNumericFilterValue = {}  # type: ignore[typeddict-item]
    if data.get("StaticValue") is not None:
        out["static_value"] = float(data["StaticValue"])
    return out


def redact_sensitive(value: DataSetNumericFilterValue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "static_value" in value:
        out["static_value"] = "*** Sensitive Data Redacted ***"
    return out
