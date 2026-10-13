"""Generated from Smithy shape ``com.amazonaws.location#RouteMatrixEntry``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.route_matrix_entry_error
    import capo_location.types.sensitive_double


class RouteMatrixEntry(TypedDict, closed=True):
    distance: NotRequired["capo_location.types.sensitive_double.SensitiveDouble"]
    """<p>The total distance of travel for the route.</p>"""
    duration_seconds: NotRequired[
        "capo_location.types.sensitive_double.SensitiveDouble"
    ]
    """<p>The expected duration of travel for the route.</p>"""
    error: NotRequired[
        "capo_location.types.route_matrix_entry_error.RouteMatrixEntryError"
    ]
    """<p>An error corresponding to the calculation of a route between the <code>DeparturePosition</code> and <code>DestinationPosition</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixEntry) -> dict:
    out: dict = {}
    if "distance" in value:
        out["Distance"] = (
            "NaN"
            if value["distance"] != value["distance"]
            else "Infinity"
            if value["distance"] == float("inf")
            else "-Infinity"
            if value["distance"] == float("-inf")
            else value["distance"]
        )
    if "duration_seconds" in value:
        out["DurationSeconds"] = (
            "NaN"
            if value["duration_seconds"] != value["duration_seconds"]
            else "Infinity"
            if value["duration_seconds"] == float("inf")
            else "-Infinity"
            if value["duration_seconds"] == float("-inf")
            else value["duration_seconds"]
        )
    if "error" in value:
        import capo_location.types.route_matrix_entry_error

        out["Error"] = capo_location.types.route_matrix_entry_error.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> RouteMatrixEntry:
    out: RouteMatrixEntry = {}  # type: ignore[typeddict-item]
    if data.get("Distance") is not None:
        out["distance"] = float(data["Distance"])
    if data.get("DurationSeconds") is not None:
        out["duration_seconds"] = float(data["DurationSeconds"])
    if data.get("Error") is not None:
        import capo_location.types.route_matrix_entry_error

        out["error"] = capo_location.types.route_matrix_entry_error.deserialize_json(
            data["Error"]
        )
    return out


def redact_sensitive(value: RouteMatrixEntry) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "distance" in value:
        out["distance"] = "*** Sensitive Data Redacted ***"
    if "duration_seconds" in value:
        out["duration_seconds"] = "*** Sensitive Data Redacted ***"
    return out
