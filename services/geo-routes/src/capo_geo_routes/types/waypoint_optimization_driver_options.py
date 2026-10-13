"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationDriverOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.waypoint_optimization_rest_cycles
    import capo_geo_routes.types.waypoint_optimization_rest_profile
    import capo_geo_routes.types.waypoint_optimization_service_time_treatment


class WaypointOptimizationDriverOptions(TypedDict, closed=True):
    rest_cycles: NotRequired[
        "capo_geo_routes.types.waypoint_optimization_rest_cycles.WaypointOptimizationRestCycles"
    ]
    """<p>Driver work-rest schedules defined by a short and long cycle. A rest needs to be taken after the short work duration. The short cycle can be repeated until you hit the long work duration, at which point the long rest duration should be taken before restarting.</p>"""
    rest_profile: NotRequired[
        "capo_geo_routes.types.waypoint_optimization_rest_profile.WaypointOptimizationRestProfile"
    ]
    """<p>Pre defined rest profiles for a driver schedule. The only currently supported profile is EU.</p>"""
    treat_service_time_as: NotRequired[
        "capo_geo_routes.types.waypoint_optimization_service_time_treatment.WaypointOptimizationServiceTimeTreatment"
    ]
    """<p>If the service time provided at a waypoint/destination should be considered as rest or work. This contributes to the total time breakdown returned within the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationDriverOptions) -> dict:
    out: dict = {}
    if "rest_cycles" in value:
        import capo_geo_routes.types.waypoint_optimization_rest_cycles

        out["RestCycles"] = (
            capo_geo_routes.types.waypoint_optimization_rest_cycles.serialize_json(
                value["rest_cycles"]
            )
        )
    if "rest_profile" in value:
        import capo_geo_routes.types.waypoint_optimization_rest_profile

        out["RestProfile"] = (
            capo_geo_routes.types.waypoint_optimization_rest_profile.serialize_json(
                value["rest_profile"]
            )
        )
    if "treat_service_time_as" in value:
        import capo_geo_routes.types.waypoint_optimization_service_time_treatment

        out["TreatServiceTimeAs"] = (
            capo_geo_routes.types.waypoint_optimization_service_time_treatment.serialize_json(
                value["treat_service_time_as"]
            )
        )
    return out


def deserialize_json(data: dict) -> WaypointOptimizationDriverOptions:
    out: WaypointOptimizationDriverOptions = {}  # type: ignore[typeddict-item]
    if data.get("RestCycles") is not None:
        import capo_geo_routes.types.waypoint_optimization_rest_cycles

        out["rest_cycles"] = (
            capo_geo_routes.types.waypoint_optimization_rest_cycles.deserialize_json(
                data["RestCycles"]
            )
        )
    if data.get("RestProfile") is not None:
        import capo_geo_routes.types.waypoint_optimization_rest_profile

        out["rest_profile"] = (
            capo_geo_routes.types.waypoint_optimization_rest_profile.deserialize_json(
                data["RestProfile"]
            )
        )
    if data.get("TreatServiceTimeAs") is not None:
        import capo_geo_routes.types.waypoint_optimization_service_time_treatment

        out["treat_service_time_as"] = (
            capo_geo_routes.types.waypoint_optimization_service_time_treatment.deserialize_json(
                data["TreatServiceTimeAs"]
            )
        )
    return out


def redact_sensitive(value: WaypointOptimizationDriverOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "rest_cycles" in value:
        import capo_geo_routes.types.waypoint_optimization_rest_cycles

        out["rest_cycles"] = (
            capo_geo_routes.types.waypoint_optimization_rest_cycles.redact_sensitive(
                value["rest_cycles"]
            )
        )
    if "rest_profile" in value:
        import capo_geo_routes.types.waypoint_optimization_rest_profile

        out["rest_profile"] = (
            capo_geo_routes.types.waypoint_optimization_rest_profile.redact_sensitive(
                value["rest_profile"]
            )
        )
    if "treat_service_time_as" in value:
        out["treat_service_time_as"] = "*** Sensitive Data Redacted ***"
    return out
