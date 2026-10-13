"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteViolatedConstraints``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.dimension_centimeters
    import capo_geo_routes.types.route_hazardous_cargo_type_list
    import capo_geo_routes.types.route_notice_detail_range
    import capo_geo_routes.types.route_truck_type
    import capo_geo_routes.types.route_weight_constraint
    import capo_geo_routes.types.sensitive_boolean
    import capo_geo_routes.types.tunnel_restriction_code
    import capo_geo_routes.types.weight_kilograms
    import capo_geo_routes.types.weight_per_axle_group


class RouteViolatedConstraints(TypedDict, closed=True):
    all_hazards_restricted: NotRequired[
        "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>This restriction applies to truck cargo, where the resulting route excludes roads on which hazardous materials are prohibited from being transported.</p>"""
    axle_count: NotRequired[
        "capo_geo_routes.types.route_notice_detail_range.RouteNoticeDetailRange"
    ]
    """<p>Total number of axles of the vehicle.</p>"""
    hazardous_cargos: "capo_geo_routes.types.route_hazardous_cargo_type_list.RouteHazardousCargoTypeList"
    """<p>List of Hazardous cargo contained in the vehicle.</p>"""
    max_height: "capo_geo_routes.types.dimension_centimeters.DimensionCentimeters"
    """<p>The maximum height of the vehicle.</p>"""
    max_kpra_length: "capo_geo_routes.types.dimension_centimeters.DimensionCentimeters"
    """<p>The maximum Kpra length of the vehicle.</p> <p> <b>Unit</b>: <code>centimeters</code> </p>"""
    max_length: "capo_geo_routes.types.dimension_centimeters.DimensionCentimeters"
    """<p>The maximum length of the vehicle.</p>"""
    max_payload_capacity: "capo_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>The maximum load capacity of the vehicle.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    max_weight: NotRequired[
        "capo_geo_routes.types.route_weight_constraint.RouteWeightConstraint"
    ]
    """<p>The maximum weight of the route.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    max_weight_per_axle: "capo_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>The maximum weight per axle of the vehicle.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    max_weight_per_axle_group: NotRequired[
        "capo_geo_routes.types.weight_per_axle_group.WeightPerAxleGroup"
    ]
    """<p>The maximum weight per axle group of the vehicle.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    max_width: "capo_geo_routes.types.dimension_centimeters.DimensionCentimeters"
    """<p>The maximum width of the vehicle.</p>"""
    occupancy: NotRequired[
        "capo_geo_routes.types.route_notice_detail_range.RouteNoticeDetailRange"
    ]
    """<p>The number of occupants in the vehicle.</p> <p>Default value: <code>1</code> </p>"""
    restricted_times: NotRequired["str"]
    """<p>Access radius restrictions based on time.</p>"""
    time_dependent: NotRequired[
        "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>The time dependent constraint.</p>"""
    trailer_count: NotRequired[
        "capo_geo_routes.types.route_notice_detail_range.RouteNoticeDetailRange"
    ]
    """<p>Number of trailers attached to the vehicle.</p> <p>Default value: <code>0</code> </p>"""
    travel_mode: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Travel mode corresponding to the leg.</p>"""
    truck_road_type: NotRequired["str"]
    """<p>Truck road type identifiers. <code>BK1</code> through <code>BK4</code> apply only to Sweden. <code>A2,A4,B2,B4,C,D,ET2,ET4</code> apply only to Mexico.</p> <note> <p>There are currently no other supported values as of 26th April 2024.</p> </note>"""
    truck_type: NotRequired["capo_geo_routes.types.route_truck_type.RouteTruckType"]
    """<p>The type of truck: <code>LightTruck</code> for smaller delivery vehicles, <code> StraightTruck</code> for rigid body trucks, or <code>Tractor</code> for tractor-trailer combinations.</p>"""
    tunnel_restriction_code: NotRequired[
        "capo_geo_routes.types.tunnel_restriction_code.TunnelRestrictionCode"
    ]
    """<p>The tunnel restriction code.</p> <p>Tunnel categories in this list indicate the restrictions which apply to certain tunnels in Great Britain. They relate to the types of dangerous goods that can be transported through them.</p> <ul> <li> <p> <i>Tunnel Category B</i> </p> <ul> <li> <p> <i>Risk Level</i>: Limited risk</p> </li> <li> <p> <i>Restrictions</i>: Few restrictions</p> </li> </ul> </li> <li> <p> <i>Tunnel Category C</i> </p> <ul> <li> <p> <i>Risk Level</i>: Medium risk</p> </li> <li> <p> <i>Restrictions</i>: Some restrictions</p> </li> </ul> </li> <li> <p> <i>Tunnel Category D</i> </p> <ul> <li> <p> <i>Risk Level</i>: High risk</p> </li> <li> <p> <i>Restrictions</i>: Many restrictions occur</p> </li> </ul> </li> <li> <p> <i>Tunnel Category E</i> </p> <ul> <li> <p> <i>Risk Level</i>: Very high risk</p> </li> <li> <p> <i>Restrictions</i>: Restricted tunnel</p> </li> </ul> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteViolatedConstraints) -> dict:
    out: dict = {}
    if "all_hazards_restricted" in value:
        out["AllHazardsRestricted"] = value["all_hazards_restricted"]
    if "axle_count" in value:
        import capo_geo_routes.types.route_notice_detail_range

        out["AxleCount"] = (
            capo_geo_routes.types.route_notice_detail_range.serialize_json(
                value["axle_count"]
            )
        )
    import capo_geo_routes.types.route_hazardous_cargo_type_list

    out["HazardousCargos"] = (
        capo_geo_routes.types.route_hazardous_cargo_type_list.serialize_json(
            value["hazardous_cargos"]
        )
    )
    out["MaxHeight"] = value.get("max_height", 0)
    out["MaxKpraLength"] = value.get("max_kpra_length", 0)
    out["MaxLength"] = value.get("max_length", 0)
    out["MaxPayloadCapacity"] = value.get("max_payload_capacity", 0)
    if "max_weight" in value:
        import capo_geo_routes.types.route_weight_constraint

        out["MaxWeight"] = capo_geo_routes.types.route_weight_constraint.serialize_json(
            value["max_weight"]
        )
    out["MaxWeightPerAxle"] = value.get("max_weight_per_axle", 0)
    if "max_weight_per_axle_group" in value:
        import capo_geo_routes.types.weight_per_axle_group

        out["MaxWeightPerAxleGroup"] = (
            capo_geo_routes.types.weight_per_axle_group.serialize_json(
                value["max_weight_per_axle_group"]
            )
        )
    out["MaxWidth"] = value.get("max_width", 0)
    if "occupancy" in value:
        import capo_geo_routes.types.route_notice_detail_range

        out["Occupancy"] = (
            capo_geo_routes.types.route_notice_detail_range.serialize_json(
                value["occupancy"]
            )
        )
    if "restricted_times" in value:
        out["RestrictedTimes"] = value["restricted_times"]
    if "time_dependent" in value:
        out["TimeDependent"] = value["time_dependent"]
    if "trailer_count" in value:
        import capo_geo_routes.types.route_notice_detail_range

        out["TrailerCount"] = (
            capo_geo_routes.types.route_notice_detail_range.serialize_json(
                value["trailer_count"]
            )
        )
    if "travel_mode" in value:
        out["TravelMode"] = value["travel_mode"]
    if "truck_road_type" in value:
        out["TruckRoadType"] = value["truck_road_type"]
    if "truck_type" in value:
        import capo_geo_routes.types.route_truck_type

        out["TruckType"] = capo_geo_routes.types.route_truck_type.serialize_json(
            value["truck_type"]
        )
    if "tunnel_restriction_code" in value:
        out["TunnelRestrictionCode"] = value["tunnel_restriction_code"]
    return out


def deserialize_json(data: dict) -> RouteViolatedConstraints:
    out: RouteViolatedConstraints = {}  # type: ignore[typeddict-item]
    if data.get("AllHazardsRestricted") is not None:
        out["all_hazards_restricted"] = data["AllHazardsRestricted"]
    if data.get("AxleCount") is not None:
        import capo_geo_routes.types.route_notice_detail_range

        out["axle_count"] = (
            capo_geo_routes.types.route_notice_detail_range.deserialize_json(
                data["AxleCount"]
            )
        )
    if data.get("HazardousCargos") is not None:
        import capo_geo_routes.types.route_hazardous_cargo_type_list

        out["hazardous_cargos"] = (
            capo_geo_routes.types.route_hazardous_cargo_type_list.deserialize_json(
                data["HazardousCargos"]
            )
        )
    else:
        raise DeserializationError("RouteViolatedConstraints.hazardous_cargos required")
    if data.get("MaxHeight") is not None:
        out["max_height"] = data["MaxHeight"]
    else:
        out["max_height"] = 0
    if data.get("MaxKpraLength") is not None:
        out["max_kpra_length"] = data["MaxKpraLength"]
    else:
        out["max_kpra_length"] = 0
    if data.get("MaxLength") is not None:
        out["max_length"] = data["MaxLength"]
    else:
        out["max_length"] = 0
    if data.get("MaxPayloadCapacity") is not None:
        out["max_payload_capacity"] = data["MaxPayloadCapacity"]
    else:
        out["max_payload_capacity"] = 0
    if data.get("MaxWeight") is not None:
        import capo_geo_routes.types.route_weight_constraint

        out["max_weight"] = (
            capo_geo_routes.types.route_weight_constraint.deserialize_json(
                data["MaxWeight"]
            )
        )
    if data.get("MaxWeightPerAxle") is not None:
        out["max_weight_per_axle"] = data["MaxWeightPerAxle"]
    else:
        out["max_weight_per_axle"] = 0
    if data.get("MaxWeightPerAxleGroup") is not None:
        import capo_geo_routes.types.weight_per_axle_group

        out["max_weight_per_axle_group"] = (
            capo_geo_routes.types.weight_per_axle_group.deserialize_json(
                data["MaxWeightPerAxleGroup"]
            )
        )
    if data.get("MaxWidth") is not None:
        out["max_width"] = data["MaxWidth"]
    else:
        out["max_width"] = 0
    if data.get("Occupancy") is not None:
        import capo_geo_routes.types.route_notice_detail_range

        out["occupancy"] = (
            capo_geo_routes.types.route_notice_detail_range.deserialize_json(
                data["Occupancy"]
            )
        )
    if data.get("RestrictedTimes") is not None:
        out["restricted_times"] = data["RestrictedTimes"]
    if data.get("TimeDependent") is not None:
        out["time_dependent"] = data["TimeDependent"]
    if data.get("TrailerCount") is not None:
        import capo_geo_routes.types.route_notice_detail_range

        out["trailer_count"] = (
            capo_geo_routes.types.route_notice_detail_range.deserialize_json(
                data["TrailerCount"]
            )
        )
    if data.get("TravelMode") is not None:
        out["travel_mode"] = data["TravelMode"]
    if data.get("TruckRoadType") is not None:
        out["truck_road_type"] = data["TruckRoadType"]
    if data.get("TruckType") is not None:
        import capo_geo_routes.types.route_truck_type

        out["truck_type"] = capo_geo_routes.types.route_truck_type.deserialize_json(
            data["TruckType"]
        )
    if data.get("TunnelRestrictionCode") is not None:
        out["tunnel_restriction_code"] = data["TunnelRestrictionCode"]
    return out


def redact_sensitive(value: RouteViolatedConstraints) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "all_hazards_restricted" in value:
        out["all_hazards_restricted"] = "*** Sensitive Data Redacted ***"
    if "hazardous_cargos" in value:
        import capo_geo_routes.types.route_hazardous_cargo_type_list

        out["hazardous_cargos"] = (
            capo_geo_routes.types.route_hazardous_cargo_type_list.redact_sensitive(
                value["hazardous_cargos"]
            )
        )
    if "max_height" in value:
        out["max_height"] = "*** Sensitive Data Redacted ***"
    if "max_kpra_length" in value:
        out["max_kpra_length"] = "*** Sensitive Data Redacted ***"
    if "max_length" in value:
        out["max_length"] = "*** Sensitive Data Redacted ***"
    if "max_payload_capacity" in value:
        out["max_payload_capacity"] = "*** Sensitive Data Redacted ***"
    if "max_weight" in value:
        import capo_geo_routes.types.route_weight_constraint

        out["max_weight"] = (
            capo_geo_routes.types.route_weight_constraint.redact_sensitive(
                value["max_weight"]
            )
        )
    if "max_weight_per_axle" in value:
        out["max_weight_per_axle"] = "*** Sensitive Data Redacted ***"
    if "max_weight_per_axle_group" in value:
        import capo_geo_routes.types.weight_per_axle_group

        out["max_weight_per_axle_group"] = (
            capo_geo_routes.types.weight_per_axle_group.redact_sensitive(
                value["max_weight_per_axle_group"]
            )
        )
    if "max_width" in value:
        out["max_width"] = "*** Sensitive Data Redacted ***"
    if "time_dependent" in value:
        out["time_dependent"] = "*** Sensitive Data Redacted ***"
    if "travel_mode" in value:
        out["travel_mode"] = "*** Sensitive Data Redacted ***"
    if "truck_type" in value:
        out["truck_type"] = "*** Sensitive Data Redacted ***"
    if "tunnel_restriction_code" in value:
        out["tunnel_restriction_code"] = "*** Sensitive Data Redacted ***"
    return out
