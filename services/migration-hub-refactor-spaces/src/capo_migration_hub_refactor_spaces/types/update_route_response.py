"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#UpdateRouteResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.application_id
    import capo_migration_hub_refactor_spaces.types.resource_arn
    import capo_migration_hub_refactor_spaces.types.route_id
    import capo_migration_hub_refactor_spaces.types.route_state
    import capo_migration_hub_refactor_spaces.types.service_id
    import capo_migration_hub_refactor_spaces.types.timestamp


class UpdateRouteResponse(TypedDict, closed=True):
    route_id: NotRequired["capo_migration_hub_refactor_spaces.types.route_id.RouteId"]
    """<p> The unique identifier of the route. </p>"""
    arn: NotRequired[
        "capo_migration_hub_refactor_spaces.types.resource_arn.ResourceArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the route. The format for this ARN is <code>arn:aws:refactor-spaces:<i>region</i>:<i>account-id</i>:<i>resource-type/resource-id</i> </code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>. </p>"""
    service_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.service_id.ServiceId"
    ]
    """<p> The ID of service in which the route was created. Traffic that matches this route is forwarded to this service. </p>"""
    application_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.application_id.ApplicationId"
    ]
    """<p> The ID of the application in which the route is being updated. </p>"""
    state: NotRequired[
        "capo_migration_hub_refactor_spaces.types.route_state.RouteState"
    ]
    """<p> The current state of the route. </p>"""
    last_updated_time: NotRequired[
        "capo_migration_hub_refactor_spaces.types.timestamp.Timestamp"
    ]
    """<p> A timestamp that indicates when the route was last updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRouteResponse) -> dict:
    out: dict = {}
    if "route_id" in value:
        out["RouteId"] = value["route_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "service_id" in value:
        out["ServiceId"] = value["service_id"]
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "state" in value:
        out["State"] = value["state"]
    if "last_updated_time" in value:
        import capo_migration_hub_refactor_spaces.types.timestamp

        out["LastUpdatedTime"] = (
            capo_migration_hub_refactor_spaces.types.timestamp.serialize_json(
                value["last_updated_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRouteResponse:
    out: UpdateRouteResponse = {}  # type: ignore[typeddict-item]
    if data.get("RouteId") is not None:
        out["route_id"] = data["RouteId"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("ServiceId") is not None:
        out["service_id"] = data["ServiceId"]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("LastUpdatedTime") is not None:
        import capo_migration_hub_refactor_spaces.types.timestamp

        out["last_updated_time"] = (
            capo_migration_hub_refactor_spaces.types.timestamp.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    return out
