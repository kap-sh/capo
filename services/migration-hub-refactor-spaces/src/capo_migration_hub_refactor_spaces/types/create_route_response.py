"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#CreateRouteResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.account_id
    import capo_migration_hub_refactor_spaces.types.application_id
    import capo_migration_hub_refactor_spaces.types.resource_arn
    import capo_migration_hub_refactor_spaces.types.route_id
    import capo_migration_hub_refactor_spaces.types.route_state
    import capo_migration_hub_refactor_spaces.types.route_type
    import capo_migration_hub_refactor_spaces.types.service_id
    import capo_migration_hub_refactor_spaces.types.tag_map
    import capo_migration_hub_refactor_spaces.types.timestamp
    import capo_migration_hub_refactor_spaces.types.uri_path_route_input


class CreateRouteResponse(TypedDict, closed=True):
    route_id: NotRequired["capo_migration_hub_refactor_spaces.types.route_id.RouteId"]
    """<p>The unique identifier of the route.</p>"""
    arn: NotRequired[
        "capo_migration_hub_refactor_spaces.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the route. The format for this ARN is <code>arn:aws:refactor-spaces:<i>region</i>:<i>account-id</i>:<i>resource-type/resource-id</i> </code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    owner_account_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.account_id.AccountId"
    ]
    """<p>The Amazon Web Services account ID of the route owner.</p>"""
    created_by_account_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.account_id.AccountId"
    ]
    """<p>The Amazon Web Services account ID of the route creator.</p>"""
    route_type: NotRequired[
        "capo_migration_hub_refactor_spaces.types.route_type.RouteType"
    ]
    """<p>The route type of the route.</p>"""
    service_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.service_id.ServiceId"
    ]
    """<p>The ID of service in which the route is created. Traffic that matches this route is forwarded to this service.</p>"""
    application_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.application_id.ApplicationId"
    ]
    """<p>The ID of the application in which the route is created.</p>"""
    uri_path_route: NotRequired[
        "capo_migration_hub_refactor_spaces.types.uri_path_route_input.UriPathRouteInput"
    ]
    """<p>Configuration for the URI path route type. </p>"""
    state: NotRequired[
        "capo_migration_hub_refactor_spaces.types.route_state.RouteState"
    ]
    """<p>The current state of the route. Activation state only allows <code>ACTIVE</code> or <code>INACTIVE</code> as user inputs. <code>FAILED</code> is a route state that is system generated.</p>"""
    tags: NotRequired["capo_migration_hub_refactor_spaces.types.tag_map.TagMap"]
    """<p>The tags assigned to the created route. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key-value pair. </p>"""
    last_updated_time: NotRequired[
        "capo_migration_hub_refactor_spaces.types.timestamp.Timestamp"
    ]
    """<p>A timestamp that indicates when the route was last updated. </p>"""
    created_time: NotRequired[
        "capo_migration_hub_refactor_spaces.types.timestamp.Timestamp"
    ]
    """<p>A timestamp that indicates when the route is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRouteResponse) -> dict:
    out: dict = {}
    if "route_id" in value:
        out["RouteId"] = value["route_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    if "created_by_account_id" in value:
        out["CreatedByAccountId"] = value["created_by_account_id"]
    if "route_type" in value:
        out["RouteType"] = value["route_type"]
    if "service_id" in value:
        out["ServiceId"] = value["service_id"]
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "uri_path_route" in value:
        import capo_migration_hub_refactor_spaces.types.uri_path_route_input

        out["UriPathRoute"] = (
            capo_migration_hub_refactor_spaces.types.uri_path_route_input.serialize_json(
                value["uri_path_route"]
            )
        )
    if "state" in value:
        out["State"] = value["state"]
    if "tags" in value:
        import capo_migration_hub_refactor_spaces.types.tag_map

        out["Tags"] = capo_migration_hub_refactor_spaces.types.tag_map.serialize_json(
            value["tags"]
        )
    if "last_updated_time" in value:
        import capo_migration_hub_refactor_spaces.types.timestamp

        out["LastUpdatedTime"] = (
            capo_migration_hub_refactor_spaces.types.timestamp.serialize_json(
                value["last_updated_time"]
            )
        )
    if "created_time" in value:
        import capo_migration_hub_refactor_spaces.types.timestamp

        out["CreatedTime"] = (
            capo_migration_hub_refactor_spaces.types.timestamp.serialize_json(
                value["created_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateRouteResponse:
    out: CreateRouteResponse = {}  # type: ignore[typeddict-item]
    if data.get("RouteId") is not None:
        out["route_id"] = data["RouteId"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("OwnerAccountId") is not None:
        out["owner_account_id"] = data["OwnerAccountId"]
    if data.get("CreatedByAccountId") is not None:
        out["created_by_account_id"] = data["CreatedByAccountId"]
    if data.get("RouteType") is not None:
        out["route_type"] = data["RouteType"]
    if data.get("ServiceId") is not None:
        out["service_id"] = data["ServiceId"]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    if data.get("UriPathRoute") is not None:
        import capo_migration_hub_refactor_spaces.types.uri_path_route_input

        out["uri_path_route"] = (
            capo_migration_hub_refactor_spaces.types.uri_path_route_input.deserialize_json(
                data["UriPathRoute"]
            )
        )
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("Tags") is not None:
        import capo_migration_hub_refactor_spaces.types.tag_map

        out["tags"] = capo_migration_hub_refactor_spaces.types.tag_map.deserialize_json(
            data["Tags"]
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_migration_hub_refactor_spaces.types.timestamp

        out["last_updated_time"] = (
            capo_migration_hub_refactor_spaces.types.timestamp.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    if data.get("CreatedTime") is not None:
        import capo_migration_hub_refactor_spaces.types.timestamp

        out["created_time"] = (
            capo_migration_hub_refactor_spaces.types.timestamp.deserialize_json(
                data["CreatedTime"]
            )
        )
    return out
