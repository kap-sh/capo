"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.currency_code
    import capo_geo_routes.types.route_emission_type
    import capo_geo_routes.types.route_toll_vehicle_category
    import capo_geo_routes.types.sensitive_boolean


class RouteTollOptions(TypedDict, closed=True):
    all_transponders: NotRequired[
        "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Specifies if the user has valid transponder with access to all toll systems. This impacts toll calculation, and if true the price with transponders is used.</p>"""
    all_vignettes: NotRequired[
        "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Specifies if the user has valid vignettes with access for all toll roads. If a user has a vignette for a toll road, then toll cost for that road is omitted since no further payment is necessary.</p>"""
    currency: NotRequired["capo_geo_routes.types.currency_code.CurrencyCode"]
    """<p>Currency code corresponding to the price. This is the same as Currency specified in the request.</p>"""
    emission_type: NotRequired[
        "capo_geo_routes.types.route_emission_type.RouteEmissionType"
    ]
    """<p>Emission type of the vehicle for toll cost calculation.</p> <p> <b>Valid values</b>: <code>Euro1, Euro2, Euro3, Euro4, Euro5, Euro6, EuroEev</code> </p>"""
    vehicle_category: NotRequired[
        "capo_geo_routes.types.route_toll_vehicle_category.RouteTollVehicleCategory"
    ]
    """<p>Vehicle category for toll cost calculation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollOptions) -> dict:
    out: dict = {}
    if "all_transponders" in value:
        out["AllTransponders"] = value["all_transponders"]
    if "all_vignettes" in value:
        out["AllVignettes"] = value["all_vignettes"]
    if "currency" in value:
        out["Currency"] = value["currency"]
    if "emission_type" in value:
        import capo_geo_routes.types.route_emission_type

        out["EmissionType"] = capo_geo_routes.types.route_emission_type.serialize_json(
            value["emission_type"]
        )
    if "vehicle_category" in value:
        import capo_geo_routes.types.route_toll_vehicle_category

        out["VehicleCategory"] = (
            capo_geo_routes.types.route_toll_vehicle_category.serialize_json(
                value["vehicle_category"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteTollOptions:
    out: RouteTollOptions = {}  # type: ignore[typeddict-item]
    if data.get("AllTransponders") is not None:
        out["all_transponders"] = data["AllTransponders"]
    if data.get("AllVignettes") is not None:
        out["all_vignettes"] = data["AllVignettes"]
    if data.get("Currency") is not None:
        out["currency"] = data["Currency"]
    if data.get("EmissionType") is not None:
        import capo_geo_routes.types.route_emission_type

        out["emission_type"] = (
            capo_geo_routes.types.route_emission_type.deserialize_json(
                data["EmissionType"]
            )
        )
    if data.get("VehicleCategory") is not None:
        import capo_geo_routes.types.route_toll_vehicle_category

        out["vehicle_category"] = (
            capo_geo_routes.types.route_toll_vehicle_category.deserialize_json(
                data["VehicleCategory"]
            )
        )
    return out


def redact_sensitive(value: RouteTollOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "all_transponders" in value:
        out["all_transponders"] = "*** Sensitive Data Redacted ***"
    if "all_vignettes" in value:
        out["all_vignettes"] = "*** Sensitive Data Redacted ***"
    if "emission_type" in value:
        import capo_geo_routes.types.route_emission_type

        out["emission_type"] = (
            capo_geo_routes.types.route_emission_type.redact_sensitive(
                value["emission_type"]
            )
        )
    if "vehicle_category" in value:
        out["vehicle_category"] = "*** Sensitive Data Redacted ***"
    return out
