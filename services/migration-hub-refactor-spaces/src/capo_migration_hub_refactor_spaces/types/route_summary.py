"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#RouteSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.account_id
    import capo_migration_hub_refactor_spaces.types.application_id
    import capo_migration_hub_refactor_spaces.types.boolean
    import capo_migration_hub_refactor_spaces.types.environment_id
    import capo_migration_hub_refactor_spaces.types.error_response
    import capo_migration_hub_refactor_spaces.types.http_methods
    import capo_migration_hub_refactor_spaces.types.path_resource_to_id
    import capo_migration_hub_refactor_spaces.types.resource_arn
    import capo_migration_hub_refactor_spaces.types.route_id
    import capo_migration_hub_refactor_spaces.types.route_state
    import capo_migration_hub_refactor_spaces.types.route_type
    import capo_migration_hub_refactor_spaces.types.service_id
    import capo_migration_hub_refactor_spaces.types.tag_map
    import capo_migration_hub_refactor_spaces.types.timestamp
    import capo_migration_hub_refactor_spaces.types.uri_path


class RouteSummary(TypedDict, closed=True):
    route_id: NotRequired["capo_migration_hub_refactor_spaces.types.route_id.RouteId"]
    """<p>The unique identifier of the route. </p>"""
    arn: NotRequired[
        "capo_migration_hub_refactor_spaces.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the route. </p>"""
    owner_account_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.account_id.AccountId"
    ]
    """<p>The Amazon Web Services account ID of the route owner.</p>"""
    created_by_account_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.account_id.AccountId"
    ]
    """<p>The Amazon Web Services account ID of the route creator. </p>"""
    route_type: NotRequired[
        "capo_migration_hub_refactor_spaces.types.route_type.RouteType"
    ]
    """<p>The route type of the route. </p>"""
    service_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.service_id.ServiceId"
    ]
    """<p>The unique identifier of the service. </p>"""
    application_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.application_id.ApplicationId"
    ]
    """<p>The unique identifier of the application. </p>"""
    environment_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId"
    ]
    """<p>The unique identifier of the environment. </p>"""
    source_path: NotRequired[
        "capo_migration_hub_refactor_spaces.types.uri_path.UriPath"
    ]
    """<p>This is the path that Refactor Spaces uses to match traffic. Paths must start with <code>/</code> and are relative to the base of the application. To use path parameters in the source path, add a variable in curly braces. For example, the resource path {user} represents a path parameter called 'user'.</p>"""
    methods: NotRequired[
        "capo_migration_hub_refactor_spaces.types.http_methods.HttpMethods"
    ]
    """<p>A list of HTTP methods to match. An empty list matches all values. If a method is present, only HTTP requests using that method are forwarded to this route’s service. </p>"""
    include_child_paths: NotRequired[
        "capo_migration_hub_refactor_spaces.types.boolean.Boolean"
    ]
    """<p>Indicates whether to match all subpaths of the given source path. If this value is <code>false</code>, requests must match the source path exactly before they are forwarded to this route's service.</p>"""
    path_resource_to_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.path_resource_to_id.PathResourceToId"
    ]
    """<p>A mapping of Amazon API Gateway path resources to resource IDs. </p>"""
    state: NotRequired[
        "capo_migration_hub_refactor_spaces.types.route_state.RouteState"
    ]
    """<p>The current state of the route. </p>"""
    tags: NotRequired["capo_migration_hub_refactor_spaces.types.tag_map.TagMap"]
    """<p>The tags assigned to the route. </p>"""
    error: NotRequired[
        "capo_migration_hub_refactor_spaces.types.error_response.ErrorResponse"
    ]
    """<p>Any error associated with the route resource. </p>"""
    last_updated_time: NotRequired[
        "capo_migration_hub_refactor_spaces.types.timestamp.Timestamp"
    ]
    """<p>A timestamp that indicates when the route was last updated. </p>"""
    created_time: NotRequired[
        "capo_migration_hub_refactor_spaces.types.timestamp.Timestamp"
    ]
    """<p>A timestamp that indicates when the route is created. </p>"""
    append_source_path: NotRequired[
        "capo_migration_hub_refactor_spaces.types.boolean.Boolean"
    ]
    """<p>If set to <code>true</code>, this option appends the source path to the service URL endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteSummary) -> dict:
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
    if "environment_id" in value:
        out["EnvironmentId"] = value["environment_id"]
    if "source_path" in value:
        out["SourcePath"] = value["source_path"]
    if "methods" in value:
        import capo_migration_hub_refactor_spaces.types.http_methods

        out["Methods"] = (
            capo_migration_hub_refactor_spaces.types.http_methods.serialize_json(
                value["methods"]
            )
        )
    if "include_child_paths" in value:
        out["IncludeChildPaths"] = value["include_child_paths"]
    if "path_resource_to_id" in value:
        import capo_migration_hub_refactor_spaces.types.path_resource_to_id

        out["PathResourceToId"] = (
            capo_migration_hub_refactor_spaces.types.path_resource_to_id.serialize_json(
                value["path_resource_to_id"]
            )
        )
    if "state" in value:
        out["State"] = value["state"]
    if "tags" in value:
        import capo_migration_hub_refactor_spaces.types.tag_map

        out["Tags"] = capo_migration_hub_refactor_spaces.types.tag_map.serialize_json(
            value["tags"]
        )
    if "error" in value:
        import capo_migration_hub_refactor_spaces.types.error_response

        out["Error"] = (
            capo_migration_hub_refactor_spaces.types.error_response.serialize_json(
                value["error"]
            )
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
    if "append_source_path" in value:
        out["AppendSourcePath"] = value["append_source_path"]
    return out


def deserialize_json(data: dict) -> RouteSummary:
    out: RouteSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("EnvironmentId") is not None:
        out["environment_id"] = data["EnvironmentId"]
    if data.get("SourcePath") is not None:
        out["source_path"] = data["SourcePath"]
    if data.get("Methods") is not None:
        import capo_migration_hub_refactor_spaces.types.http_methods

        out["methods"] = (
            capo_migration_hub_refactor_spaces.types.http_methods.deserialize_json(
                data["Methods"]
            )
        )
    if data.get("IncludeChildPaths") is not None:
        out["include_child_paths"] = data["IncludeChildPaths"]
    if data.get("PathResourceToId") is not None:
        import capo_migration_hub_refactor_spaces.types.path_resource_to_id

        out["path_resource_to_id"] = (
            capo_migration_hub_refactor_spaces.types.path_resource_to_id.deserialize_json(
                data["PathResourceToId"]
            )
        )
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("Tags") is not None:
        import capo_migration_hub_refactor_spaces.types.tag_map

        out["tags"] = capo_migration_hub_refactor_spaces.types.tag_map.deserialize_json(
            data["Tags"]
        )
    if data.get("Error") is not None:
        import capo_migration_hub_refactor_spaces.types.error_response

        out["error"] = (
            capo_migration_hub_refactor_spaces.types.error_response.deserialize_json(
                data["Error"]
            )
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
    if data.get("AppendSourcePath") is not None:
        out["append_source_path"] = data["AppendSourcePath"]
    return out


def redact_sensitive(value: RouteSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
