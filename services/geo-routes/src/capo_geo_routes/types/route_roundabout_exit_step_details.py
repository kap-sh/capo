"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRoundaboutExitStepDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.localized_string_list
    import capo_geo_routes.types.roundabout_angle
    import capo_geo_routes.types.route_steering_direction
    import capo_geo_routes.types.sensitive_integer


class RouteRoundaboutExitStepDetails(TypedDict, closed=True):
    intersection: "capo_geo_routes.types.localized_string_list.LocalizedStringList"
    """<p>Name of the intersection, if applicable to the step.</p>"""
    relative_exit: NotRequired[
        "capo_geo_routes.types.sensitive_integer.SensitiveInteger"
    ]
    """<p>Exit to be taken.</p>"""
    roundabout_angle: "capo_geo_routes.types.roundabout_angle.RoundaboutAngle"
    """<p>Angle of the roundabout.</p>"""
    steering_direction: NotRequired[
        "capo_geo_routes.types.route_steering_direction.RouteSteeringDirection"
    ]
    """<p>Steering direction for the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteRoundaboutExitStepDetails) -> dict:
    out: dict = {}
    import capo_geo_routes.types.localized_string_list

    out["Intersection"] = capo_geo_routes.types.localized_string_list.serialize_json(
        value["intersection"]
    )
    if "relative_exit" in value:
        out["RelativeExit"] = value["relative_exit"]
    out["RoundaboutAngle"] = (
        "NaN"
        if value.get("roundabout_angle", 0) != value.get("roundabout_angle", 0)
        else "Infinity"
        if value.get("roundabout_angle", 0) == float("inf")
        else "-Infinity"
        if value.get("roundabout_angle", 0) == float("-inf")
        else value.get("roundabout_angle", 0)
    )
    if "steering_direction" in value:
        import capo_geo_routes.types.route_steering_direction

        out["SteeringDirection"] = (
            capo_geo_routes.types.route_steering_direction.serialize_json(
                value["steering_direction"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteRoundaboutExitStepDetails:
    out: RouteRoundaboutExitStepDetails = {}  # type: ignore[typeddict-item]
    if data.get("Intersection") is not None:
        import capo_geo_routes.types.localized_string_list

        out["intersection"] = (
            capo_geo_routes.types.localized_string_list.deserialize_json(
                data["Intersection"]
            )
        )
    else:
        raise DeserializationError(
            "RouteRoundaboutExitStepDetails.intersection required"
        )
    if data.get("RelativeExit") is not None:
        out["relative_exit"] = data["RelativeExit"]
    if data.get("RoundaboutAngle") is not None:
        out["roundabout_angle"] = float(data["RoundaboutAngle"])
    else:
        out["roundabout_angle"] = 0
    if data.get("SteeringDirection") is not None:
        import capo_geo_routes.types.route_steering_direction

        out["steering_direction"] = (
            capo_geo_routes.types.route_steering_direction.deserialize_json(
                data["SteeringDirection"]
            )
        )
    return out


def redact_sensitive(value: RouteRoundaboutExitStepDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "intersection" in value:
        import capo_geo_routes.types.localized_string_list

        out["intersection"] = (
            capo_geo_routes.types.localized_string_list.redact_sensitive(
                value["intersection"]
            )
        )
    if "relative_exit" in value:
        out["relative_exit"] = "*** Sensitive Data Redacted ***"
    if "steering_direction" in value:
        out["steering_direction"] = "*** Sensitive Data Redacted ***"
    return out
