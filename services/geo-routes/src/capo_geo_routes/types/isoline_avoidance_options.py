"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineAvoidanceOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.isoline_avoidance_area_list
    import capo_geo_routes.types.isoline_avoidance_zone_category_list
    import capo_geo_routes.types.sensitive_boolean
    import capo_geo_routes.types.truck_road_type_list


class IsolineAvoidanceOptions(TypedDict, closed=True):
    areas: NotRequired[
        "capo_geo_routes.types.isoline_avoidance_area_list.IsolineAvoidanceAreaList"
    ]
    """<p>Specifies geographic areas to avoid where possible. Routes may still pass through these areas if no reasonable alternative exists.</p>"""
    car_shuttle_trains: NotRequired[
        "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Indicates a preference to avoid car shuttle trains (auto trains) where possible. These may still be included if no reasonable alternative route exists.</p>"""
    controlled_access_highways: NotRequired[
        "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Indicates a preference to avoid controlled-access highways (such as interstate highways or motorways) where possible. If a viable route cannot be calculated using only local roads, controlled-access highways may still be included.</p>"""
    dirt_roads: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Indicates a preference to avoid unpaved or dirt roads where possible. Routes may still include dirt roads if no reasonable paved alternative exists.</p>"""
    ferries: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Indicates a preference to avoid ferries where possible. If a viable route cannot be calculated without using ferries, they may still be included.</p>"""
    seasonal_closure: NotRequired[
        "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Indicates a preference to avoid roads that may be subject to seasonal closures where possible. These roads may still be included if no reasonable year-round alternative exists.</p>"""
    toll_roads: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Indicates a preference to avoid toll roads where possible. If a viable route cannot be calculated without using toll roads, they may still be included.</p>"""
    toll_transponders: NotRequired[
        "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Indicates a preference to avoid roads that require electronic toll collection transponders where possible. These roads may still be included if no viable alternative route exists.</p>"""
    truck_road_types: NotRequired[
        "capo_geo_routes.types.truck_road_type_list.TruckRoadTypeList"
    ]
    """<p>For truck travel modes, indicates specific road classification types in Sweden (<code> BK1</code> through <code>BK4</code>) and Mexico (<code>A2, A4, B2, B4, C, D, ET2, ET4</code>) to avoid where possible. These road types may still be used if no reasonable alternative exists.</p> <note> <p>There are currently no other supported values as of 26th April 2024.</p> </note>"""
    tunnels: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Indicates a preference to avoid tunnels where possible. If a viable route cannot be calculated without using tunnels, they may still be included.</p>"""
    u_turns: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Indicates a preference to avoid U-turns where possible. U-turns may still be included if necessary to reach certain areas or when no reasonable alternative exists.</p>"""
    zone_categories: NotRequired[
        "capo_geo_routes.types.isoline_avoidance_zone_category_list.IsolineAvoidanceZoneCategoryList"
    ]
    """<p>Indicates types of regulated zones (such as congestion pricing or environmental zones) to avoid where possible. Routes may still pass through these zones if no reasonable alternative exists.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsolineAvoidanceOptions) -> dict:
    out: dict = {}
    if "areas" in value:
        import capo_geo_routes.types.isoline_avoidance_area_list

        out["Areas"] = capo_geo_routes.types.isoline_avoidance_area_list.serialize_json(
            value["areas"]
        )
    if "car_shuttle_trains" in value:
        out["CarShuttleTrains"] = value["car_shuttle_trains"]
    if "controlled_access_highways" in value:
        out["ControlledAccessHighways"] = value["controlled_access_highways"]
    if "dirt_roads" in value:
        out["DirtRoads"] = value["dirt_roads"]
    if "ferries" in value:
        out["Ferries"] = value["ferries"]
    if "seasonal_closure" in value:
        out["SeasonalClosure"] = value["seasonal_closure"]
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
        import capo_geo_routes.types.isoline_avoidance_zone_category_list

        out["ZoneCategories"] = (
            capo_geo_routes.types.isoline_avoidance_zone_category_list.serialize_json(
                value["zone_categories"]
            )
        )
    return out


def deserialize_json(data: dict) -> IsolineAvoidanceOptions:
    out: IsolineAvoidanceOptions = {}  # type: ignore[typeddict-item]
    if data.get("Areas") is not None:
        import capo_geo_routes.types.isoline_avoidance_area_list

        out["areas"] = (
            capo_geo_routes.types.isoline_avoidance_area_list.deserialize_json(
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
    if data.get("SeasonalClosure") is not None:
        out["seasonal_closure"] = data["SeasonalClosure"]
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
        import capo_geo_routes.types.isoline_avoidance_zone_category_list

        out["zone_categories"] = (
            capo_geo_routes.types.isoline_avoidance_zone_category_list.deserialize_json(
                data["ZoneCategories"]
            )
        )
    return out


def redact_sensitive(value: IsolineAvoidanceOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "areas" in value:
        import capo_geo_routes.types.isoline_avoidance_area_list

        out["areas"] = (
            capo_geo_routes.types.isoline_avoidance_area_list.redact_sensitive(
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
    if "seasonal_closure" in value:
        out["seasonal_closure"] = "*** Sensitive Data Redacted ***"
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
    return out
