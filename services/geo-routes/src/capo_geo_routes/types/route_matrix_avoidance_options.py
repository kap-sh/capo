"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixAvoidanceOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_matrix_avoidance_area_list
    import capo_geo_routes.types.route_matrix_avoidance_zone_category_list
    import capo_geo_routes.types.sensitive_boolean
    import capo_geo_routes.types.truck_road_type_list


class RouteMatrixAvoidanceOptions(TypedDict, closed=True):
    areas: NotRequired[
        "capo_geo_routes.types.route_matrix_avoidance_area_list.RouteMatrixAvoidanceAreaList"
    ]
    """<p>Areas to be avoided.</p>"""
    car_shuttle_trains: NotRequired[
        "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Avoid car-shuttle-trains while calculating the route.</p>"""
    controlled_access_highways: NotRequired[
        "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Avoid controlled access highways while calculating the route.</p>"""
    dirt_roads: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Avoid dirt roads while calculating the route.</p>"""
    ferries: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Avoid ferries while calculating the route.</p>"""
    toll_roads: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Avoids roads where the specified toll transponders are the only mode of payment.</p>"""
    toll_transponders: NotRequired[
        "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Avoids roads where the specified toll transponders are the only mode of payment.</p>"""
    truck_road_types: NotRequired[
        "capo_geo_routes.types.truck_road_type_list.TruckRoadTypeList"
    ]
    """<p>Truck road type identifiers. <code>BK1</code> through <code>BK4</code> apply only to Sweden. <code>A2,A4,B2,B4,C,D,ET2,ET4</code> apply only to Mexico.</p> <note> <p>There are currently no other supported values as of 26th April 2024.</p> </note>"""
    tunnels: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Avoid tunnels while calculating the route.</p>"""
    u_turns: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Avoid U-turns for calculation on highways and motorways.</p>"""
    zone_categories: NotRequired[
        "capo_geo_routes.types.route_matrix_avoidance_zone_category_list.RouteMatrixAvoidanceZoneCategoryList"
    ]
    """<p>Zone categories to be avoided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixAvoidanceOptions) -> dict:
    out: dict = {}
    if "areas" in value:
        import capo_geo_routes.types.route_matrix_avoidance_area_list

        out["Areas"] = (
            capo_geo_routes.types.route_matrix_avoidance_area_list.serialize_json(
                value["areas"]
            )
        )
    if "car_shuttle_trains" in value:
        out["CarShuttleTrains"] = value["car_shuttle_trains"]
    if "controlled_access_highways" in value:
        out["ControlledAccessHighways"] = value["controlled_access_highways"]
    if "dirt_roads" in value:
        out["DirtRoads"] = value["dirt_roads"]
    if "ferries" in value:
        out["Ferries"] = value["ferries"]
    if "toll_roads" in value:
        out["TollRoads"] = value["toll_roads"]
    if "toll_transponders" in value:
        out["TollTransponders"] = value["toll_transponders"]
    if "truck_road_types" in value:
        import capo_geo_routes.types.truck_road_type_list

        out["TruckRoadTypes"] = (
            capo_geo_routes.types.truck_road_type_list.serialize_json(
                value["truck_road_types"]
            )
        )
    if "tunnels" in value:
        out["Tunnels"] = value["tunnels"]
    if "u_turns" in value:
        out["UTurns"] = value["u_turns"]
    if "zone_categories" in value:
        import capo_geo_routes.types.route_matrix_avoidance_zone_category_list

        out["ZoneCategories"] = (
            capo_geo_routes.types.route_matrix_avoidance_zone_category_list.serialize_json(
                value["zone_categories"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteMatrixAvoidanceOptions:
    out: RouteMatrixAvoidanceOptions = {}  # type: ignore[typeddict-item]
    if data.get("Areas") is not None:
        import capo_geo_routes.types.route_matrix_avoidance_area_list

        out["areas"] = (
            capo_geo_routes.types.route_matrix_avoidance_area_list.deserialize_json(
                data["Areas"]
            )
        )
    if data.get("CarShuttleTrains") is not None:
        out["car_shuttle_trains"] = data["CarShuttleTrains"]
    if data.get("ControlledAccessHighways") is not None:
        out["controlled_access_highways"] = data["ControlledAccessHighways"]
    if data.get("DirtRoads") is not None:
        out["dirt_roads"] = data["DirtRoads"]
    if data.get("Ferries") is not None:
        out["ferries"] = data["Ferries"]
    if data.get("TollRoads") is not None:
        out["toll_roads"] = data["TollRoads"]
    if data.get("TollTransponders") is not None:
        out["toll_transponders"] = data["TollTransponders"]
    if data.get("TruckRoadTypes") is not None:
        import capo_geo_routes.types.truck_road_type_list

        out["truck_road_types"] = (
            capo_geo_routes.types.truck_road_type_list.deserialize_json(
                data["TruckRoadTypes"]
            )
        )
    if data.get("Tunnels") is not None:
        out["tunnels"] = data["Tunnels"]
    if data.get("UTurns") is not None:
        out["u_turns"] = data["UTurns"]
    if data.get("ZoneCategories") is not None:
        import capo_geo_routes.types.route_matrix_avoidance_zone_category_list

        out["zone_categories"] = (
            capo_geo_routes.types.route_matrix_avoidance_zone_category_list.deserialize_json(
                data["ZoneCategories"]
            )
        )
    return out


def redact_sensitive(value: RouteMatrixAvoidanceOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "areas" in value:
        import capo_geo_routes.types.route_matrix_avoidance_area_list

        out["areas"] = (
            capo_geo_routes.types.route_matrix_avoidance_area_list.redact_sensitive(
                value["areas"]
            )
        )
    if "car_shuttle_trains" in value:
        out["car_shuttle_trains"] = "*** Sensitive Data Redacted ***"
    if "controlled_access_highways" in value:
        out["controlled_access_highways"] = "*** Sensitive Data Redacted ***"
    if "dirt_roads" in value:
        out["dirt_roads"] = "*** Sensitive Data Redacted ***"
    if "ferries" in value:
        out["ferries"] = "*** Sensitive Data Redacted ***"
    if "toll_roads" in value:
        out["toll_roads"] = "*** Sensitive Data Redacted ***"
    if "toll_transponders" in value:
        out["toll_transponders"] = "*** Sensitive Data Redacted ***"
    if "truck_road_types" in value:
        import capo_geo_routes.types.truck_road_type_list

        out["truck_road_types"] = (
            capo_geo_routes.types.truck_road_type_list.redact_sensitive(
                value["truck_road_types"]
            )
        )
    if "tunnels" in value:
        out["tunnels"] = "*** Sensitive Data Redacted ***"
    if "u_turns" in value:
        out["u_turns"] = "*** Sensitive Data Redacted ***"
    if "zone_categories" in value:
        import capo_geo_routes.types.route_matrix_avoidance_zone_category_list

        out["zone_categories"] = (
            capo_geo_routes.types.route_matrix_avoidance_zone_category_list.redact_sensitive(
                value["zone_categories"]
            )
        )
    return out
