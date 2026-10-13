"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationTruckOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.dimension_centimeters
    import capo_geo_routes.types.tunnel_restriction_code
    import capo_geo_routes.types.waypoint_optimization_hazardous_cargo_type_list
    import capo_geo_routes.types.waypoint_optimization_trailer_options
    import capo_geo_routes.types.waypoint_optimization_truck_type
    import capo_geo_routes.types.weight_kilograms


class WaypointOptimizationTruckOptions(TypedDict, closed=True):
    gross_weight: "capo_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>Gross weight of the vehicle including trailers, and goods at capacity.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    hazardous_cargos: NotRequired[
        "capo_geo_routes.types.waypoint_optimization_hazardous_cargo_type_list.WaypointOptimizationHazardousCargoTypeList"
    ]
    """<p>List of Hazardous cargo contained in the vehicle.</p>"""
    height: "capo_geo_routes.types.dimension_centimeters.DimensionCentimeters"
    """<p>Height of the vehicle.</p> <p> <b>Unit</b>: <code>centimeters</code> </p>"""
    length: "capo_geo_routes.types.dimension_centimeters.DimensionCentimeters"
    """<p>Length of the vehicle.</p> <p> <b>Unit</b>: <code>centimeters</code> </p>"""
    trailer: NotRequired[
        "capo_geo_routes.types.waypoint_optimization_trailer_options.WaypointOptimizationTrailerOptions"
    ]
    """<p>Trailer options corresponding to the vehicle.</p>"""
    truck_type: NotRequired[
        "capo_geo_routes.types.waypoint_optimization_truck_type.WaypointOptimizationTruckType"
    ]
    """<p>The type of truck: <code>LightTruck</code> for smaller delivery vehicles, <code> StraightTruck</code> for rigid body trucks, or <code>Tractor</code> for tractor-trailer combinations.</p>"""
    tunnel_restriction_code: NotRequired[
        "capo_geo_routes.types.tunnel_restriction_code.TunnelRestrictionCode"
    ]
    """<p>The tunnel restriction code.</p> <p>Tunnel categories in this list indicate the restrictions which apply to certain tunnels in Great Britain. They relate to the types of dangerous goods that can be transported through them.</p> <ul> <li> <p> <i>Tunnel Category B</i> </p> <ul> <li> <p> <i>Risk Level</i>: Limited risk</p> </li> <li> <p> <i>Restrictions</i>: Few restrictions</p> </li> </ul> </li> <li> <p> <i>Tunnel Category C</i> </p> <ul> <li> <p> <i>Risk Level</i>: Medium risk</p> </li> <li> <p> <i>Restrictions</i>: Some restrictions</p> </li> </ul> </li> <li> <p> <i>Tunnel Category D</i> </p> <ul> <li> <p> <i>Risk Level</i>: High risk</p> </li> <li> <p> <i>Restrictions</i>: Many restrictions occur</p> </li> </ul> </li> <li> <p> <i>Tunnel Category E</i> </p> <ul> <li> <p> <i>Risk Level</i>: Very high risk</p> </li> <li> <p> <i>Restrictions</i>: Restricted tunnel</p> </li> </ul> </li> </ul>"""
    weight_per_axle: "capo_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>Heaviest weight per axle irrespective of the axle type or the axle group. Meant for usage in countries where the differences in axle types or axle groups are not distinguished.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    width: "capo_geo_routes.types.dimension_centimeters.DimensionCentimeters"
    """<p>Width of the vehicle.</p> <p> <b>Unit</b>: <code>centimeters</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationTruckOptions) -> dict:
    out: dict = {}
    out["GrossWeight"] = value.get("gross_weight", 0)
    if "hazardous_cargos" in value:
        import capo_geo_routes.types.waypoint_optimization_hazardous_cargo_type_list

        out["HazardousCargos"] = (
            capo_geo_routes.types.waypoint_optimization_hazardous_cargo_type_list.serialize_json(
                value["hazardous_cargos"]
            )
        )
    out["Height"] = value.get("height", 0)
    out["Length"] = value.get("length", 0)
    if "trailer" in value:
        import capo_geo_routes.types.waypoint_optimization_trailer_options

        out["Trailer"] = (
            capo_geo_routes.types.waypoint_optimization_trailer_options.serialize_json(
                value["trailer"]
            )
        )
    if "truck_type" in value:
        import capo_geo_routes.types.waypoint_optimization_truck_type

        out["TruckType"] = (
            capo_geo_routes.types.waypoint_optimization_truck_type.serialize_json(
                value["truck_type"]
            )
        )
    if "tunnel_restriction_code" in value:
        out["TunnelRestrictionCode"] = value["tunnel_restriction_code"]
    out["WeightPerAxle"] = value.get("weight_per_axle", 0)
    out["Width"] = value.get("width", 0)
    return out


def deserialize_json(data: dict) -> WaypointOptimizationTruckOptions:
    out: WaypointOptimizationTruckOptions = {}  # type: ignore[typeddict-item]
    if data.get("GrossWeight") is not None:
        out["gross_weight"] = data["GrossWeight"]
    else:
        out["gross_weight"] = 0
    if data.get("HazardousCargos") is not None:
        import capo_geo_routes.types.waypoint_optimization_hazardous_cargo_type_list

        out["hazardous_cargos"] = (
            capo_geo_routes.types.waypoint_optimization_hazardous_cargo_type_list.deserialize_json(
                data["HazardousCargos"]
            )
        )
    if data.get("Height") is not None:
        out["height"] = data["Height"]
    else:
        out["height"] = 0
    if data.get("Length") is not None:
        out["length"] = data["Length"]
    else:
        out["length"] = 0
    if data.get("Trailer") is not None:
        import capo_geo_routes.types.waypoint_optimization_trailer_options

        out["trailer"] = (
            capo_geo_routes.types.waypoint_optimization_trailer_options.deserialize_json(
                data["Trailer"]
            )
        )
    if data.get("TruckType") is not None:
        import capo_geo_routes.types.waypoint_optimization_truck_type

        out["truck_type"] = (
            capo_geo_routes.types.waypoint_optimization_truck_type.deserialize_json(
                data["TruckType"]
            )
        )
    if data.get("TunnelRestrictionCode") is not None:
        out["tunnel_restriction_code"] = data["TunnelRestrictionCode"]
    if data.get("WeightPerAxle") is not None:
        out["weight_per_axle"] = data["WeightPerAxle"]
    else:
        out["weight_per_axle"] = 0
    if data.get("Width") is not None:
        out["width"] = data["Width"]
    else:
        out["width"] = 0
    return out


def redact_sensitive(value: WaypointOptimizationTruckOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "gross_weight" in value:
        out["gross_weight"] = "*** Sensitive Data Redacted ***"
    if "hazardous_cargos" in value:
        import capo_geo_routes.types.waypoint_optimization_hazardous_cargo_type_list

        out["hazardous_cargos"] = (
            capo_geo_routes.types.waypoint_optimization_hazardous_cargo_type_list.redact_sensitive(
                value["hazardous_cargos"]
            )
        )
    if "height" in value:
        out["height"] = "*** Sensitive Data Redacted ***"
    if "length" in value:
        out["length"] = "*** Sensitive Data Redacted ***"
    if "trailer" in value:
        import capo_geo_routes.types.waypoint_optimization_trailer_options

        out["trailer"] = (
            capo_geo_routes.types.waypoint_optimization_trailer_options.redact_sensitive(
                value["trailer"]
            )
        )
    if "truck_type" in value:
        out["truck_type"] = "*** Sensitive Data Redacted ***"
    if "tunnel_restriction_code" in value:
        out["tunnel_restriction_code"] = "*** Sensitive Data Redacted ***"
    if "weight_per_axle" in value:
        out["weight_per_axle"] = "*** Sensitive Data Redacted ***"
    if "width" in value:
        out["width"] = "*** Sensitive Data Redacted ***"
    return out
