"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutePedestrianSpan``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.country_code3
    import capo_geo_routes.types.distance_meters
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.index_list
    import capo_geo_routes.types.localized_string_list
    import capo_geo_routes.types.route_number_list
    import capo_geo_routes.types.route_span_dynamic_speed_details
    import capo_geo_routes.types.route_span_pedestrian_access_attribute_list
    import capo_geo_routes.types.route_span_road_attribute_list
    import capo_geo_routes.types.route_span_speed_limit_details
    import capo_geo_routes.types.sensitive_integer
    import capo_geo_routes.types.sensitive_string


class RoutePedestrianSpan(TypedDict, closed=True):
    best_case_duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the computed span without traffic congestion.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    country: NotRequired["capo_geo_routes.types.country_code3.CountryCode3"]
    """<p>3 letter Country code corresponding to the Span.</p>"""
    distance: "capo_geo_routes.types.distance_meters.DistanceMeters"
    """<p>Distance of the computed span. This feature doesn't split a span, but is always computed on a span split by other properties.</p>"""
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the computed span. This feature doesn't split a span, but is always computed on a span split by other properties.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    dynamic_speed: NotRequired[
        "capo_geo_routes.types.route_span_dynamic_speed_details.RouteSpanDynamicSpeedDetails"
    ]
    """<p>Dynamic speed details corresponding to the span.</p> <p> <b>Unit</b>: <code>kilometers per hour</code> </p>"""
    functional_classification: NotRequired[
        "capo_geo_routes.types.sensitive_integer.SensitiveInteger"
    ]
    """<p>A numerical value indicating the functional classification of the road segment corresponding to the span.</p> <p>Classification values are part of the hierarchical network that helps determine a logical and efficient route, and have the following definitions:</p> <ol> <li> <p>Roads that allow for high volume, maximum speed traffic movement between and through major metropolitan areas.</p> </li> <li> <p>Roads that are used to channel traffic to functional class 1 roads for travel between and through cities in the shortest amount of time.</p> </li> <li> <p>Roads that intersect functional class 2 roads and provide a high volume of traffic movement at a lower level of mobility than functional class 2 roads.</p> </li> <li> <p>Roads that provide for a high volume of traffic movement at moderate speeds between neighborhoods.</p> </li> <li> <p>Roads with volume and traffic movement below the level of any other functional class.</p> </li> </ol>"""
    geometry_offset: NotRequired["int"]
    """<p>Offset in the leg geometry corresponding to the start of this span.</p>"""
    incidents: NotRequired["capo_geo_routes.types.index_list.IndexList"]
    """<p>Incidents corresponding to the span. These index into the Incidents in the parent Leg.</p>"""
    names: NotRequired[
        "capo_geo_routes.types.localized_string_list.LocalizedStringList"
    ]
    """<p>Provides an array of names of the pedestrian span in available languages.</p>"""
    pedestrian_access: NotRequired[
        "capo_geo_routes.types.route_span_pedestrian_access_attribute_list.RouteSpanPedestrianAccessAttributeList"
    ]
    """<p>Access attributes for a pedestrian corresponding to the span.</p>"""
    region: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>2-3 letter Region code corresponding to the Span. This is either a province or a state.</p>"""
    road_attributes: NotRequired[
        "capo_geo_routes.types.route_span_road_attribute_list.RouteSpanRoadAttributeList"
    ]
    """<p>Attributes for the road segment corresponding to the span. </p>"""
    route_numbers: NotRequired[
        "capo_geo_routes.types.route_number_list.RouteNumberList"
    ]
    """<p>Designated route name or number corresponding to the span.</p>"""
    speed_limit: NotRequired[
        "capo_geo_routes.types.route_span_speed_limit_details.RouteSpanSpeedLimitDetails"
    ]
    """<p>Speed limit details corresponding to the span.</p> <p> <b>Unit</b>: <code>kilometers per hour</code> </p>"""
    typical_duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the computed span under typical traffic congestion.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutePedestrianSpan) -> dict:
    out: dict = {}
    out["BestCaseDuration"] = value.get("best_case_duration", 0)
    if "country" in value:
        out["Country"] = value["country"]
    out["Distance"] = value.get("distance", 0)
    out["Duration"] = value.get("duration", 0)
    if "dynamic_speed" in value:
        import capo_geo_routes.types.route_span_dynamic_speed_details

        out["DynamicSpeed"] = (
            capo_geo_routes.types.route_span_dynamic_speed_details.serialize_json(
                value["dynamic_speed"]
            )
        )
    if "functional_classification" in value:
        out["FunctionalClassification"] = value["functional_classification"]
    if "geometry_offset" in value:
        out["GeometryOffset"] = value["geometry_offset"]
    if "incidents" in value:
        import capo_geo_routes.types.index_list

        out["Incidents"] = capo_geo_routes.types.index_list.serialize_json(
            value["incidents"]
        )
    if "names" in value:
        import capo_geo_routes.types.localized_string_list

        out["Names"] = capo_geo_routes.types.localized_string_list.serialize_json(
            value["names"]
        )
    if "pedestrian_access" in value:
        import capo_geo_routes.types.route_span_pedestrian_access_attribute_list

        out["PedestrianAccess"] = (
            capo_geo_routes.types.route_span_pedestrian_access_attribute_list.serialize_json(
                value["pedestrian_access"]
            )
        )
    if "region" in value:
        out["Region"] = value["region"]
    if "road_attributes" in value:
        import capo_geo_routes.types.route_span_road_attribute_list

        out["RoadAttributes"] = (
            capo_geo_routes.types.route_span_road_attribute_list.serialize_json(
                value["road_attributes"]
            )
        )
    if "route_numbers" in value:
        import capo_geo_routes.types.route_number_list

        out["RouteNumbers"] = capo_geo_routes.types.route_number_list.serialize_json(
            value["route_numbers"]
        )
    if "speed_limit" in value:
        import capo_geo_routes.types.route_span_speed_limit_details

        out["SpeedLimit"] = (
            capo_geo_routes.types.route_span_speed_limit_details.serialize_json(
                value["speed_limit"]
            )
        )
    out["TypicalDuration"] = value.get("typical_duration", 0)
    return out


def deserialize_json(data: dict) -> RoutePedestrianSpan:
    out: RoutePedestrianSpan = {}  # type: ignore[typeddict-item]
    if data.get("BestCaseDuration") is not None:
        out["best_case_duration"] = data["BestCaseDuration"]
    else:
        out["best_case_duration"] = 0
    if data.get("Country") is not None:
        out["country"] = data["Country"]
    if data.get("Distance") is not None:
        out["distance"] = data["Distance"]
    else:
        out["distance"] = 0
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    if data.get("DynamicSpeed") is not None:
        import capo_geo_routes.types.route_span_dynamic_speed_details

        out["dynamic_speed"] = (
            capo_geo_routes.types.route_span_dynamic_speed_details.deserialize_json(
                data["DynamicSpeed"]
            )
        )
    if data.get("FunctionalClassification") is not None:
        out["functional_classification"] = data["FunctionalClassification"]
    if data.get("GeometryOffset") is not None:
        out["geometry_offset"] = data["GeometryOffset"]
    if data.get("Incidents") is not None:
        import capo_geo_routes.types.index_list

        out["incidents"] = capo_geo_routes.types.index_list.deserialize_json(
            data["Incidents"]
        )
    if data.get("Names") is not None:
        import capo_geo_routes.types.localized_string_list

        out["names"] = capo_geo_routes.types.localized_string_list.deserialize_json(
            data["Names"]
        )
    if data.get("PedestrianAccess") is not None:
        import capo_geo_routes.types.route_span_pedestrian_access_attribute_list

        out["pedestrian_access"] = (
            capo_geo_routes.types.route_span_pedestrian_access_attribute_list.deserialize_json(
                data["PedestrianAccess"]
            )
        )
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("RoadAttributes") is not None:
        import capo_geo_routes.types.route_span_road_attribute_list

        out["road_attributes"] = (
            capo_geo_routes.types.route_span_road_attribute_list.deserialize_json(
                data["RoadAttributes"]
            )
        )
    if data.get("RouteNumbers") is not None:
        import capo_geo_routes.types.route_number_list

        out["route_numbers"] = capo_geo_routes.types.route_number_list.deserialize_json(
            data["RouteNumbers"]
        )
    if data.get("SpeedLimit") is not None:
        import capo_geo_routes.types.route_span_speed_limit_details

        out["speed_limit"] = (
            capo_geo_routes.types.route_span_speed_limit_details.deserialize_json(
                data["SpeedLimit"]
            )
        )
    if data.get("TypicalDuration") is not None:
        out["typical_duration"] = data["TypicalDuration"]
    else:
        out["typical_duration"] = 0
    return out


def redact_sensitive(value: RoutePedestrianSpan) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "best_case_duration" in value:
        out["best_case_duration"] = "*** Sensitive Data Redacted ***"
    if "country" in value:
        out["country"] = "*** Sensitive Data Redacted ***"
    if "distance" in value:
        out["distance"] = "*** Sensitive Data Redacted ***"
    if "duration" in value:
        out["duration"] = "*** Sensitive Data Redacted ***"
    if "dynamic_speed" in value:
        import capo_geo_routes.types.route_span_dynamic_speed_details

        out["dynamic_speed"] = (
            capo_geo_routes.types.route_span_dynamic_speed_details.redact_sensitive(
                value["dynamic_speed"]
            )
        )
    if "functional_classification" in value:
        out["functional_classification"] = "*** Sensitive Data Redacted ***"
    if "names" in value:
        import capo_geo_routes.types.localized_string_list

        out["names"] = capo_geo_routes.types.localized_string_list.redact_sensitive(
            value["names"]
        )
    if "pedestrian_access" in value:
        import capo_geo_routes.types.route_span_pedestrian_access_attribute_list

        out["pedestrian_access"] = (
            capo_geo_routes.types.route_span_pedestrian_access_attribute_list.redact_sensitive(
                value["pedestrian_access"]
            )
        )
    if "region" in value:
        out["region"] = "*** Sensitive Data Redacted ***"
    if "road_attributes" in value:
        import capo_geo_routes.types.route_span_road_attribute_list

        out["road_attributes"] = (
            capo_geo_routes.types.route_span_road_attribute_list.redact_sensitive(
                value["road_attributes"]
            )
        )
    if "route_numbers" in value:
        import capo_geo_routes.types.route_number_list

        out["route_numbers"] = capo_geo_routes.types.route_number_list.redact_sensitive(
            value["route_numbers"]
        )
    if "speed_limit" in value:
        import capo_geo_routes.types.route_span_speed_limit_details

        out["speed_limit"] = (
            capo_geo_routes.types.route_span_speed_limit_details.redact_sensitive(
                value["speed_limit"]
            )
        )
    if "typical_duration" in value:
        out["typical_duration"] = "*** Sensitive Data Redacted ***"
    return out
