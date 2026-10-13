"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRampStepDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.localized_string_list
    import capo_geo_routes.types.route_steering_direction
    import capo_geo_routes.types.route_turn_intensity
    import capo_geo_routes.types.turn_angle


class RouteRampStepDetails(TypedDict, closed=True):
    intersection: "capo_geo_routes.types.localized_string_list.LocalizedStringList"
    """<p>Name of the intersection, if applicable to the step.</p>"""
    steering_direction: NotRequired[
        "capo_geo_routes.types.route_steering_direction.RouteSteeringDirection"
    ]
    """<p>Steering direction for the step.</p>"""
    turn_angle: "capo_geo_routes.types.turn_angle.TurnAngle"
    """<p>Angle of the turn.</p>"""
    turn_intensity: NotRequired[
        "capo_geo_routes.types.route_turn_intensity.RouteTurnIntensity"
    ]
    """<p>Intensity of the turn.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteRampStepDetails) -> dict:
    out: dict = {}
    import capo_geo_routes.types.localized_string_list

    out["Intersection"] = capo_geo_routes.types.localized_string_list.serialize_json(
        value["intersection"]
    )
    if "steering_direction" in value:
        import capo_geo_routes.types.route_steering_direction

        out["SteeringDirection"] = (
            capo_geo_routes.types.route_steering_direction.serialize_json(
                value["steering_direction"]
            )
        )
    out["TurnAngle"] = (
        "NaN"
        if value.get("turn_angle", 0) != value.get("turn_angle", 0)
        else "Infinity"
        if value.get("turn_angle", 0) == float("inf")
        else "-Infinity"
        if value.get("turn_angle", 0) == float("-inf")
        else value.get("turn_angle", 0)
    )
    if "turn_intensity" in value:
        import capo_geo_routes.types.route_turn_intensity

        out["TurnIntensity"] = (
            capo_geo_routes.types.route_turn_intensity.serialize_json(
                value["turn_intensity"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteRampStepDetails:
    out: RouteRampStepDetails = {}  # type: ignore[typeddict-item]
    if data.get("Intersection") is not None:
        import capo_geo_routes.types.localized_string_list

        out["intersection"] = (
            capo_geo_routes.types.localized_string_list.deserialize_json(
                data["Intersection"]
            )
        )
    else:
        raise DeserializationError("RouteRampStepDetails.intersection required")
    if data.get("SteeringDirection") is not None:
        import capo_geo_routes.types.route_steering_direction

        out["steering_direction"] = (
            capo_geo_routes.types.route_steering_direction.deserialize_json(
                data["SteeringDirection"]
            )
        )
    if data.get("TurnAngle") is not None:
        out["turn_angle"] = float(data["TurnAngle"])
    else:
        out["turn_angle"] = 0
    if data.get("TurnIntensity") is not None:
        import capo_geo_routes.types.route_turn_intensity

        out["turn_intensity"] = (
            capo_geo_routes.types.route_turn_intensity.deserialize_json(
                data["TurnIntensity"]
            )
        )
    return out


def redact_sensitive(value: RouteRampStepDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "intersection" in value:
        import capo_geo_routes.types.localized_string_list

        out["intersection"] = (
            capo_geo_routes.types.localized_string_list.redact_sensitive(
                value["intersection"]
            )
        )
    if "steering_direction" in value:
        out["steering_direction"] = "*** Sensitive Data Redacted ***"
    if "turn_intensity" in value:
        out["turn_intensity"] = "*** Sensitive Data Redacted ***"
    return out
