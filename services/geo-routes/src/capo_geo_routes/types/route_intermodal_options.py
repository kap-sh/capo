"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteIntermodalOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_accessibility_attribute_list
    import capo_geo_routes.types.route_intermodal_pedestrian_options
    import capo_geo_routes.types.route_intermodal_rental_options
    import capo_geo_routes.types.route_intermodal_taxi_options
    import capo_geo_routes.types.route_intermodal_transit_options
    import capo_geo_routes.types.route_intermodal_vehicle_options


class RouteIntermodalOptions(TypedDict, closed=True):
    accessibility_attributes: NotRequired[
        "capo_geo_routes.types.route_accessibility_attribute_list.RouteAccessibilityAttributeList"
    ]
    """<p>Accessibility attributes to consider when calculating the route.</p>"""
    max_transfers: NotRequired["int"]
    """<p>Maximum number of transfers allowed when calculating the route.</p>"""
    pedestrian: NotRequired[
        "capo_geo_routes.types.route_intermodal_pedestrian_options.RouteIntermodalPedestrianOptions"
    ]
    """<p>Options for the pedestrian leg of the intermodal route.</p>"""
    rental: NotRequired[
        "capo_geo_routes.types.route_intermodal_rental_options.RouteIntermodalRentalOptions"
    ]
    """<p>Options for the rental leg of the intermodal route.</p>"""
    taxi: NotRequired[
        "capo_geo_routes.types.route_intermodal_taxi_options.RouteIntermodalTaxiOptions"
    ]
    """<p>Options for the taxi leg of the intermodal route.</p>"""
    transit: NotRequired[
        "capo_geo_routes.types.route_intermodal_transit_options.RouteIntermodalTransitOptions"
    ]
    """<p>Options for the transit leg of the intermodal route.</p>"""
    vehicle: NotRequired[
        "capo_geo_routes.types.route_intermodal_vehicle_options.RouteIntermodalVehicleOptions"
    ]
    """<p>Options for the vehicle leg of the intermodal route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteIntermodalOptions) -> dict:
    out: dict = {}
    if "accessibility_attributes" in value:
        import capo_geo_routes.types.route_accessibility_attribute_list

        out["AccessibilityAttributes"] = (
            capo_geo_routes.types.route_accessibility_attribute_list.serialize_json(
                value["accessibility_attributes"]
            )
        )
    if "max_transfers" in value:
        out["MaxTransfers"] = value["max_transfers"]
    if "pedestrian" in value:
        import capo_geo_routes.types.route_intermodal_pedestrian_options

        out["Pedestrian"] = (
            capo_geo_routes.types.route_intermodal_pedestrian_options.serialize_json(
                value["pedestrian"]
            )
        )
    if "rental" in value:
        import capo_geo_routes.types.route_intermodal_rental_options

        out["Rental"] = (
            capo_geo_routes.types.route_intermodal_rental_options.serialize_json(
                value["rental"]
            )
        )
    if "taxi" in value:
        import capo_geo_routes.types.route_intermodal_taxi_options

        out["Taxi"] = (
            capo_geo_routes.types.route_intermodal_taxi_options.serialize_json(
                value["taxi"]
            )
        )
    if "transit" in value:
        import capo_geo_routes.types.route_intermodal_transit_options

        out["Transit"] = (
            capo_geo_routes.types.route_intermodal_transit_options.serialize_json(
                value["transit"]
            )
        )
    if "vehicle" in value:
        import capo_geo_routes.types.route_intermodal_vehicle_options

        out["Vehicle"] = (
            capo_geo_routes.types.route_intermodal_vehicle_options.serialize_json(
                value["vehicle"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteIntermodalOptions:
    out: RouteIntermodalOptions = {}  # type: ignore[typeddict-item]
    if data.get("AccessibilityAttributes") is not None:
        import capo_geo_routes.types.route_accessibility_attribute_list

        out["accessibility_attributes"] = (
            capo_geo_routes.types.route_accessibility_attribute_list.deserialize_json(
                data["AccessibilityAttributes"]
            )
        )
    if data.get("MaxTransfers") is not None:
        out["max_transfers"] = data["MaxTransfers"]
    if data.get("Pedestrian") is not None:
        import capo_geo_routes.types.route_intermodal_pedestrian_options

        out["pedestrian"] = (
            capo_geo_routes.types.route_intermodal_pedestrian_options.deserialize_json(
                data["Pedestrian"]
            )
        )
    if data.get("Rental") is not None:
        import capo_geo_routes.types.route_intermodal_rental_options

        out["rental"] = (
            capo_geo_routes.types.route_intermodal_rental_options.deserialize_json(
                data["Rental"]
            )
        )
    if data.get("Taxi") is not None:
        import capo_geo_routes.types.route_intermodal_taxi_options

        out["taxi"] = (
            capo_geo_routes.types.route_intermodal_taxi_options.deserialize_json(
                data["Taxi"]
            )
        )
    if data.get("Transit") is not None:
        import capo_geo_routes.types.route_intermodal_transit_options

        out["transit"] = (
            capo_geo_routes.types.route_intermodal_transit_options.deserialize_json(
                data["Transit"]
            )
        )
    if data.get("Vehicle") is not None:
        import capo_geo_routes.types.route_intermodal_vehicle_options

        out["vehicle"] = (
            capo_geo_routes.types.route_intermodal_vehicle_options.deserialize_json(
                data["Vehicle"]
            )
        )
    return out


def redact_sensitive(value: RouteIntermodalOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "accessibility_attributes" in value:
        import capo_geo_routes.types.route_accessibility_attribute_list

        out["accessibility_attributes"] = (
            capo_geo_routes.types.route_accessibility_attribute_list.redact_sensitive(
                value["accessibility_attributes"]
            )
        )
    if "pedestrian" in value:
        import capo_geo_routes.types.route_intermodal_pedestrian_options

        out["pedestrian"] = (
            capo_geo_routes.types.route_intermodal_pedestrian_options.redact_sensitive(
                value["pedestrian"]
            )
        )
    if "rental" in value:
        import capo_geo_routes.types.route_intermodal_rental_options

        out["rental"] = (
            capo_geo_routes.types.route_intermodal_rental_options.redact_sensitive(
                value["rental"]
            )
        )
    if "taxi" in value:
        import capo_geo_routes.types.route_intermodal_taxi_options

        out["taxi"] = (
            capo_geo_routes.types.route_intermodal_taxi_options.redact_sensitive(
                value["taxi"]
            )
        )
    if "transit" in value:
        import capo_geo_routes.types.route_intermodal_transit_options

        out["transit"] = (
            capo_geo_routes.types.route_intermodal_transit_options.redact_sensitive(
                value["transit"]
            )
        )
    if "vehicle" in value:
        import capo_geo_routes.types.route_intermodal_vehicle_options

        out["vehicle"] = (
            capo_geo_routes.types.route_intermodal_vehicle_options.redact_sensitive(
                value["vehicle"]
            )
        )
    return out
