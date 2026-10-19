"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#UpdateRouteRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.application_id
    import capo_migration_hub_refactor_spaces.types.environment_id
    import capo_migration_hub_refactor_spaces.types.route_activation_state
    import capo_migration_hub_refactor_spaces.types.route_id


class UpdateRouteRequest(TypedDict, closed=True):
    environment_identifier: (
        "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId"
    )
    """<p> The ID of the environment in which the route is being updated. </p>"""
    application_identifier: (
        "capo_migration_hub_refactor_spaces.types.application_id.ApplicationId"
    )
    """<p> The ID of the application within which the route is being updated. </p>"""
    route_identifier: "capo_migration_hub_refactor_spaces.types.route_id.RouteId"
    """<p> The unique identifier of the route to update. </p>"""
    activation_state: "capo_migration_hub_refactor_spaces.types.route_activation_state.RouteActivationState"
    """<p> If set to <code>ACTIVE</code>, traffic is forwarded to this route’s service after the route is updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRouteRequest) -> dict:
    out: dict = {}
    out["ActivationState"] = value["activation_state"]
    return out


def deserialize_json(data: dict) -> UpdateRouteRequest:
    out: UpdateRouteRequest = {}  # type: ignore[typeddict-item]
    if data.get("ActivationState") is not None:
        out["activation_state"] = data["ActivationState"]
    else:
        out["activation_state"] = ""
    return out
