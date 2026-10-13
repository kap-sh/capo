"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationFailedConstraint``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.sensitive_string
    import capo_geo_routes.types.waypoint_optimization_constraint


class WaypointOptimizationFailedConstraint(TypedDict, closed=True):
    constraint: NotRequired[
        "capo_geo_routes.types.waypoint_optimization_constraint.WaypointOptimizationConstraint"
    ]
    """<p>The failed constraint.</p>"""
    reason: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Reason for the failed constraint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationFailedConstraint) -> dict:
    out: dict = {}
    if "constraint" in value:
        import capo_geo_routes.types.waypoint_optimization_constraint

        out["Constraint"] = (
            capo_geo_routes.types.waypoint_optimization_constraint.serialize_json(
                value["constraint"]
            )
        )
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> WaypointOptimizationFailedConstraint:
    out: WaypointOptimizationFailedConstraint = {}  # type: ignore[typeddict-item]
    if data.get("Constraint") is not None:
        import capo_geo_routes.types.waypoint_optimization_constraint

        out["constraint"] = (
            capo_geo_routes.types.waypoint_optimization_constraint.deserialize_json(
                data["Constraint"]
            )
        )
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    return out


def redact_sensitive(value: WaypointOptimizationFailedConstraint) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "constraint" in value:
        out["constraint"] = "*** Sensitive Data Redacted ***"
    if "reason" in value:
        out["reason"] = "*** Sensitive Data Redacted ***"
    return out
