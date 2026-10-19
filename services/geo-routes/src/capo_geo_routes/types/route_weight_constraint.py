"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteWeightConstraint``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_weight_constraint_type
    import capo_geo_routes.types.weight_kilograms


class RouteWeightConstraint(TypedDict, closed=True):
    type: "capo_geo_routes.types.route_weight_constraint_type.RouteWeightConstraintType"
    """<p>The type of constraint.</p>"""
    value: "capo_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>The constraint value.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteWeightConstraint) -> dict:
    out: dict = {}
    import capo_geo_routes.types.route_weight_constraint_type

    out["Type"] = capo_geo_routes.types.route_weight_constraint_type.serialize_json(
        value["type"]
    )
    out["Value"] = value.get("value", 0)
    return out


def deserialize_json(data: dict) -> RouteWeightConstraint:
    out: RouteWeightConstraint = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_geo_routes.types.route_weight_constraint_type

        out["type"] = (
            capo_geo_routes.types.route_weight_constraint_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_geo_routes.types.route_weight_constraint_type.RouteWeightConstraintType",
            "",
        )
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = 0
    return out


def redact_sensitive(value: RouteWeightConstraint) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    return out
