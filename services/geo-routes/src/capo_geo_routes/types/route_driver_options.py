"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteDriverOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_driver_schedule_interval_list


class RouteDriverOptions(TypedDict, closed=True):
    schedule: NotRequired[
        "capo_geo_routes.types.route_driver_schedule_interval_list.RouteDriverScheduleIntervalList"
    ]
    """<p>Driver work-rest schedule. Stops are added to fulfil the provided rest schedule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteDriverOptions) -> dict:
    out: dict = {}
    if "schedule" in value:
        import capo_geo_routes.types.route_driver_schedule_interval_list

        out["Schedule"] = (
            capo_geo_routes.types.route_driver_schedule_interval_list.serialize_json(
                value["schedule"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteDriverOptions:
    out: RouteDriverOptions = {}  # type: ignore[typeddict-item]
    if data.get("Schedule") is not None:
        import capo_geo_routes.types.route_driver_schedule_interval_list

        out["schedule"] = (
            capo_geo_routes.types.route_driver_schedule_interval_list.deserialize_json(
                data["Schedule"]
            )
        )
    return out


def redact_sensitive(value: RouteDriverOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "schedule" in value:
        import capo_geo_routes.types.route_driver_schedule_interval_list

        out["schedule"] = (
            capo_geo_routes.types.route_driver_schedule_interval_list.redact_sensitive(
                value["schedule"]
            )
        )
    return out
