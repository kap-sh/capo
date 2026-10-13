"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineTruckOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.dimension_centimeters
    import capo_geo_routes.types.isoline_engine_type
    import capo_geo_routes.types.isoline_hazardous_cargo_type_list
    import capo_geo_routes.types.isoline_trailer_options
    import capo_geo_routes.types.isoline_truck_type
    import capo_geo_routes.types.isoline_vehicle_license_plate
    import capo_geo_routes.types.sensitive_integer
    import capo_geo_routes.types.speed_kilometers_per_hour
    import capo_geo_routes.types.tunnel_restriction_code
    import capo_geo_routes.types.weight_kilograms
    import capo_geo_routes.types.weight_per_axle_group


class IsolineTruckOptions(TypedDict, closed=True):
    axle_count: NotRequired["capo_geo_routes.types.sensitive_integer.SensitiveInteger"]
    """<p>The total number of axles on the vehicle. Required for certain road restrictions and weight limit calculations.</p>"""
    engine_type: NotRequired[
        "capo_geo_routes.types.isoline_engine_type.IsolineEngineType"
    ]
    """<p>The type of engine powering the vehicle, which may affect route calculation due to road restrictions or vehicle characteristics.</p> <ul> <li> <p> <code>INTERNAL_COMBUSTION</code>—Standard gasoline or diesel engine.</p> </li> <li> <p> <code>ELECTRIC</code>—Battery electric vehicle.</p> </li> <li> <p> <code>PLUGIN_HYBRID</code>—Combination of electric and internal combustion engines with plug-in charging capability.</p> </li> </ul>"""
    gross_weight: "capo_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>The gross vehicle weight (the maximum weight a vehicle can safely operate at, as specified by the manufacturer) in kilograms. Used to avoid roads with weight restrictions and ensure compliance with maximum allowed vehicle weight regulations.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    hazardous_cargos: NotRequired[
        "capo_geo_routes.types.isoline_hazardous_cargo_type_list.IsolineHazardousCargoTypeList"
    ]
    """<p>Types of hazardous materials being transported. This affects which roads and tunnels can be used based on local regulations.</p> <ul> <li> <p> <code>Combustible</code>—Materials that can burn readily</p> </li> <li> <p> <code>Corrosive</code>—Materials that can destroy or irreversibly damage other substances</p> </li> <li> <p> <code>Explosive</code>—Materials that can produce an explosion by chemical reaction</p> </li> <li> <p> <code>Flammable</code>—Materials that can easily ignite</p> </li> <li> <p> <code>Gas</code>—Hazardous materials in gaseous form</p> </li> <li> <p> <code>HarmfulToWater</code>—Materials that pose a risk to water sources if released</p> </li> <li> <p> <code>Organic</code>—Hazardous organic compounds</p> </li> <li> <p> <code>Other</code>—Hazardous materials not covered by other categories</p> </li> <li> <p> <code>Poison</code>—Toxic materials</p> </li> <li> <p> <code>PoisonousInhalation</code>—Materials that are toxic when inhaled</p> </li> <li> <p> <code>Radioactive</code>—Materials that emit ionizing radiation</p> </li> </ul>"""
    height: "capo_geo_routes.types.dimension_centimeters.DimensionCentimeters"
    """<p>The vehicle height in centimeters. Used to avoid routes with low bridges or other height restrictions.</p> <p> <b>Unit</b>: <code>centimeters</code> </p>"""
    height_above_first_axle: (
        "capo_geo_routes.types.dimension_centimeters.DimensionCentimeters"
    )
    """<p>The height in centimeters measured from the ground to the highest point above the first axle. Used for specific bridge and tunnel clearance restrictions.</p> <p> <b>Unit</b>: <code>centimeters</code> </p>"""
    kpra_length: "capo_geo_routes.types.dimension_centimeters.DimensionCentimeters"
    """<p>The kingpin to rear axle (KPRA) length in centimeters. Used to determine if the vehicle can safely navigate turns and intersections.</p> <p> <b>Unit</b>: <code>centimeters</code> </p>"""
    length: "capo_geo_routes.types.dimension_centimeters.DimensionCentimeters"
    """<p>The total vehicle length in centimeters. Used to avoid roads with length restrictions and determine if the vehicle can safely navigate turns.</p> <p> <b>Unit</b>: <code>centimeters</code> </p>"""
    license_plate: NotRequired[
        "capo_geo_routes.types.isoline_vehicle_license_plate.IsolineVehicleLicensePlate"
    ]
    """<p>License plate information used in regions where road access or routing restrictions are based on license plate numbers.</p>"""
    max_speed: NotRequired[
        "capo_geo_routes.types.speed_kilometers_per_hour.SpeedKilometersPerHour"
    ]
    """<p>The maximum speed in kilometers per hour at which the vehicle can or is permitted to travel. This affects travel time calculations and may result in different reachable areas compared to using default speed limits. Value must be between 3.6 and 252 kilometers per hour.</p> <p> <b>Unit</b>: <code>kilometers per hour</code> </p>"""
    occupancy: NotRequired["capo_geo_routes.types.sensitive_integer.SensitiveInteger"]
    """<p>The number of occupants in the vehicle. This can affect route calculations by enabling the use of high-occupancy vehicle (HOV) lanes where minimum occupancy requirements are met.</p> <p>Default value: <code>1</code> </p>"""
    payload_capacity: "capo_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>The maximum cargo weight in kilograms that the vehicle (including attached trailers) is rated to carry.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    tire_count: NotRequired["capo_geo_routes.types.sensitive_integer.SensitiveInteger"]
    """<p>The total number of tires on the vehicle.</p>"""
    trailer: NotRequired[
        "capo_geo_routes.types.isoline_trailer_options.IsolineTrailerOptions"
    ]
    """<p>Optional specifications for attached trailers. When provided, trailer characteristics affect route calculations to ensure compliance with trailer-specific restrictions such as length limits, weight distribution requirements, and access restrictions for multi-trailer configurations.</p>"""
    truck_type: NotRequired["capo_geo_routes.types.isoline_truck_type.IsolineTruckType"]
    """<p>The type of truck: <code>LightTruck</code> for smaller delivery vehicles, <code> StraightTruck </code> for rigid body trucks, or <code>Tractor</code> for tractor-trailer combinations.</p>"""
    tunnel_restriction_code: NotRequired[
        "capo_geo_routes.types.tunnel_restriction_code.TunnelRestrictionCode"
    ]
    """<p>The tunnel restriction code.</p> <p>Tunnel categories in this list indicate the restrictions which apply to certain tunnels in Great Britain. They relate to the types of dangerous goods that can be transported through them.</p> <ul> <li> <p> <i>Tunnel Category B</i> </p> <ul> <li> <p> <i>Risk Level</i>: Limited risk</p> </li> <li> <p> <i>Restrictions</i>: Few restrictions</p> </li> </ul> </li> <li> <p> <i>Tunnel Category C</i> </p> <ul> <li> <p> <i>Risk Level</i>: Medium risk</p> </li> <li> <p> <i>Restrictions</i>: Some restrictions</p> </li> </ul> </li> <li> <p> <i>Tunnel Category D</i> </p> <ul> <li> <p> <i>Risk Level</i>: High risk</p> </li> <li> <p> <i>Restrictions</i>: Many restrictions occur</p> </li> </ul> </li> <li> <p> <i>Tunnel Category E</i> </p> <ul> <li> <p> <i>Risk Level</i>: Very high risk</p> </li> <li> <p> <i>Restrictions</i>: Restricted tunnel</p> </li> </ul> </li> </ul>"""
    weight_per_axle: "capo_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>The heaviest weight per axle in kilograms, regardless of axle type or grouping. Used for roads with axle-weight restrictions in regions where regulations don't distinguish between different axle configurations.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    weight_per_axle_group: NotRequired[
        "capo_geo_routes.types.weight_per_axle_group.WeightPerAxleGroup"
    ]
    """<p>Specifies the total weight for different axle group configurations. Used in regions where regulations set different weight limits based on axle group types.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    width: "capo_geo_routes.types.dimension_centimeters.DimensionCentimeters"
    """<p>The vehicle width in centimeters. Used to avoid routes with width restrictions.</p> <p> <b>Unit</b>: <code>centimeters</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsolineTruckOptions) -> dict:
    out: dict = {}
    if "axle_count" in value:
        out["AxleCount"] = value["axle_count"]
    if "engine_type" in value:
        import capo_geo_routes.types.isoline_engine_type

        out["EngineType"] = capo_geo_routes.types.isoline_engine_type.serialize_json(
            value["engine_type"]
        )
    out["GrossWeight"] = value.get("gross_weight", 0)
    if "hazardous_cargos" in value:
        import capo_geo_routes.types.isoline_hazardous_cargo_type_list

        out["HazardousCargos"] = (
            capo_geo_routes.types.isoline_hazardous_cargo_type_list.serialize_json(
                value["hazardous_cargos"]
            )
        )
    out["Height"] = value.get("height", 0)
    out["HeightAboveFirstAxle"] = value.get("height_above_first_axle", 0)
    out["KpraLength"] = value.get("kpra_length", 0)
    out["Length"] = value.get("length", 0)
    if "license_plate" in value:
        import capo_geo_routes.types.isoline_vehicle_license_plate

        out["LicensePlate"] = (
            capo_geo_routes.types.isoline_vehicle_license_plate.serialize_json(
                value["license_plate"]
            )
        )
    if "max_speed" in value:
        out["MaxSpeed"] = (
            "NaN"
            if value["max_speed"] != value["max_speed"]
            else "Infinity"
            if value["max_speed"] == float("inf")
            else "-Infinity"
            if value["max_speed"] == float("-inf")
            else value["max_speed"]
        )
    if "occupancy" in value:
        out["Occupancy"] = value["occupancy"]
    out["PayloadCapacity"] = value.get("payload_capacity", 0)
    if "tire_count" in value:
        out["TireCount"] = value["tire_count"]
    if "trailer" in value:
        import capo_geo_routes.types.isoline_trailer_options

        out["Trailer"] = capo_geo_routes.types.isoline_trailer_options.serialize_json(
            value["trailer"]
        )
    if "truck_type" in value:
        import capo_geo_routes.types.isoline_truck_type

        out["TruckType"] = capo_geo_routes.types.isoline_truck_type.serialize_json(
            value["truck_type"]
        )
    if "tunnel_restriction_code" in value:
        out["TunnelRestrictionCode"] = value["tunnel_restriction_code"]
    out["WeightPerAxle"] = value.get("weight_per_axle", 0)
    if "weight_per_axle_group" in value:
        import capo_geo_routes.types.weight_per_axle_group

        out["WeightPerAxleGroup"] = (
            capo_geo_routes.types.weight_per_axle_group.serialize_json(
                value["weight_per_axle_group"]
            )
        )
    out["Width"] = value.get("width", 0)
    return out


def deserialize_json(data: dict) -> IsolineTruckOptions:
    out: IsolineTruckOptions = {}  # type: ignore[typeddict-item]
    if data.get("AxleCount") is not None:
        out["axle_count"] = data["AxleCount"]
    if data.get("EngineType") is not None:
        import capo_geo_routes.types.isoline_engine_type

        out["engine_type"] = capo_geo_routes.types.isoline_engine_type.deserialize_json(
            data["EngineType"]
        )
    if data.get("GrossWeight") is not None:
        out["gross_weight"] = data["GrossWeight"]
    else:
        out["gross_weight"] = 0
    if data.get("HazardousCargos") is not None:
        import capo_geo_routes.types.isoline_hazardous_cargo_type_list

        out["hazardous_cargos"] = (
            capo_geo_routes.types.isoline_hazardous_cargo_type_list.deserialize_json(
                data["HazardousCargos"]
            )
        )
    if data.get("Height") is not None:
        out["height"] = data["Height"]
    else:
        out["height"] = 0
    if data.get("HeightAboveFirstAxle") is not None:
        out["height_above_first_axle"] = data["HeightAboveFirstAxle"]
    else:
        out["height_above_first_axle"] = 0
    if data.get("KpraLength") is not None:
        out["kpra_length"] = data["KpraLength"]
    else:
        out["kpra_length"] = 0
    if data.get("Length") is not None:
        out["length"] = data["Length"]
    else:
        out["length"] = 0
    if data.get("LicensePlate") is not None:
        import capo_geo_routes.types.isoline_vehicle_license_plate

        out["license_plate"] = (
            capo_geo_routes.types.isoline_vehicle_license_plate.deserialize_json(
                data["LicensePlate"]
            )
        )
    if data.get("MaxSpeed") is not None:
        out["max_speed"] = float(data["MaxSpeed"])
    if data.get("Occupancy") is not None:
        out["occupancy"] = data["Occupancy"]
    if data.get("PayloadCapacity") is not None:
        out["payload_capacity"] = data["PayloadCapacity"]
    else:
        out["payload_capacity"] = 0
    if data.get("TireCount") is not None:
        out["tire_count"] = data["TireCount"]
    if data.get("Trailer") is not None:
        import capo_geo_routes.types.isoline_trailer_options

        out["trailer"] = capo_geo_routes.types.isoline_trailer_options.deserialize_json(
            data["Trailer"]
        )
    if data.get("TruckType") is not None:
        import capo_geo_routes.types.isoline_truck_type

        out["truck_type"] = capo_geo_routes.types.isoline_truck_type.deserialize_json(
            data["TruckType"]
        )
    if data.get("TunnelRestrictionCode") is not None:
        out["tunnel_restriction_code"] = data["TunnelRestrictionCode"]
    if data.get("WeightPerAxle") is not None:
        out["weight_per_axle"] = data["WeightPerAxle"]
    else:
        out["weight_per_axle"] = 0
    if data.get("WeightPerAxleGroup") is not None:
        import capo_geo_routes.types.weight_per_axle_group

        out["weight_per_axle_group"] = (
            capo_geo_routes.types.weight_per_axle_group.deserialize_json(
                data["WeightPerAxleGroup"]
            )
        )
    if data.get("Width") is not None:
        out["width"] = data["Width"]
    else:
        out["width"] = 0
    return out


def redact_sensitive(value: IsolineTruckOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "axle_count" in value:
        out["axle_count"] = "*** Sensitive Data Redacted ***"
    if "engine_type" in value:
        out["engine_type"] = "*** Sensitive Data Redacted ***"
    if "gross_weight" in value:
        out["gross_weight"] = "*** Sensitive Data Redacted ***"
    if "hazardous_cargos" in value:
        import capo_geo_routes.types.isoline_hazardous_cargo_type_list

        out["hazardous_cargos"] = (
            capo_geo_routes.types.isoline_hazardous_cargo_type_list.redact_sensitive(
                value["hazardous_cargos"]
            )
        )
    if "height" in value:
        out["height"] = "*** Sensitive Data Redacted ***"
    if "height_above_first_axle" in value:
        out["height_above_first_axle"] = "*** Sensitive Data Redacted ***"
    if "kpra_length" in value:
        out["kpra_length"] = "*** Sensitive Data Redacted ***"
    if "length" in value:
        out["length"] = "*** Sensitive Data Redacted ***"
    if "license_plate" in value:
        out["license_plate"] = "*** Sensitive Data Redacted ***"
    if "max_speed" in value:
        out["max_speed"] = "*** Sensitive Data Redacted ***"
    if "occupancy" in value:
        out["occupancy"] = "*** Sensitive Data Redacted ***"
    if "payload_capacity" in value:
        out["payload_capacity"] = "*** Sensitive Data Redacted ***"
    if "tire_count" in value:
        out["tire_count"] = "*** Sensitive Data Redacted ***"
    if "trailer" in value:
        import capo_geo_routes.types.isoline_trailer_options

        out["trailer"] = capo_geo_routes.types.isoline_trailer_options.redact_sensitive(
            value["trailer"]
        )
    if "tunnel_restriction_code" in value:
        out["tunnel_restriction_code"] = "*** Sensitive Data Redacted ***"
    if "weight_per_axle" in value:
        out["weight_per_axle"] = "*** Sensitive Data Redacted ***"
    if "weight_per_axle_group" in value:
        import capo_geo_routes.types.weight_per_axle_group

        out["weight_per_axle_group"] = (
            capo_geo_routes.types.weight_per_axle_group.redact_sensitive(
                value["weight_per_axle_group"]
            )
        )
    if "width" in value:
        out["width"] = "*** Sensitive Data Redacted ***"
    return out
