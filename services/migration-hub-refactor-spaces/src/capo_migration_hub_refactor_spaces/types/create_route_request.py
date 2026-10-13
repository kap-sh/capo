"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#CreateRouteRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_migration_hub_refactor_spaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.application_id
    import capo_migration_hub_refactor_spaces.types.client_token
    import capo_migration_hub_refactor_spaces.types.default_route_input
    import capo_migration_hub_refactor_spaces.types.environment_id
    import capo_migration_hub_refactor_spaces.types.route_type
    import capo_migration_hub_refactor_spaces.types.service_id
    import capo_migration_hub_refactor_spaces.types.tag_map
    import capo_migration_hub_refactor_spaces.types.uri_path_route_input


class CreateRouteRequest(TypedDict, closed=True):
    environment_identifier: (
        "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId"
    )
    """<p>The ID of the environment in which the route is created.</p>"""
    application_identifier: (
        "capo_migration_hub_refactor_spaces.types.application_id.ApplicationId"
    )
    """<p>The ID of the application within which the route is being created.</p>"""
    service_identifier: "capo_migration_hub_refactor_spaces.types.service_id.ServiceId"
    """<p>The ID of the service in which the route is created. Traffic that matches this route is forwarded to this service.</p>"""
    route_type: "capo_migration_hub_refactor_spaces.types.route_type.RouteType"
    """<p>The route type of the route. <code>DEFAULT</code> indicates that all traffic that does not match another route is forwarded to the default route. Applications must have a default route before any other routes can be created. <code>URI_PATH</code> indicates a route that is based on a URI path.</p>"""
    default_route: NotRequired[
        "capo_migration_hub_refactor_spaces.types.default_route_input.DefaultRouteInput"
    ]
    """<p> Configuration for the default route type. </p>"""
    uri_path_route: NotRequired[
        "capo_migration_hub_refactor_spaces.types.uri_path_route_input.UriPathRouteInput"
    ]
    """<p>The configuration for the URI path route type. </p>"""
    tags: NotRequired["capo_migration_hub_refactor_spaces.types.tag_map.TagMap"]
    """<p>The tags to assign to the route. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key-value pair.. </p>"""
    client_token: NotRequired[
        "capo_migration_hub_refactor_spaces.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRouteRequest) -> dict:
    out: dict = {}
    out["ServiceIdentifier"] = value["service_identifier"]
    out["RouteType"] = value["route_type"]
    if "default_route" in value:
        import capo_migration_hub_refactor_spaces.types.default_route_input

        out["DefaultRoute"] = (
            capo_migration_hub_refactor_spaces.types.default_route_input.serialize_json(
                value["default_route"]
            )
        )
    if "uri_path_route" in value:
        import capo_migration_hub_refactor_spaces.types.uri_path_route_input

        out["UriPathRoute"] = (
            capo_migration_hub_refactor_spaces.types.uri_path_route_input.serialize_json(
                value["uri_path_route"]
            )
        )
    if "tags" in value:
        import capo_migration_hub_refactor_spaces.types.tag_map

        out["Tags"] = capo_migration_hub_refactor_spaces.types.tag_map.serialize_json(
            value["tags"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateRouteRequest:
    out: CreateRouteRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceIdentifier") is not None:
        out["service_identifier"] = data["ServiceIdentifier"]
    else:
        raise DeserializationError("CreateRouteRequest.service_identifier required")
    if data.get("RouteType") is not None:
        out["route_type"] = data["RouteType"]
    else:
        raise DeserializationError("CreateRouteRequest.route_type required")
    if data.get("DefaultRoute") is not None:
        import capo_migration_hub_refactor_spaces.types.default_route_input

        out["default_route"] = (
            capo_migration_hub_refactor_spaces.types.default_route_input.deserialize_json(
                data["DefaultRoute"]
            )
        )
    if data.get("UriPathRoute") is not None:
        import capo_migration_hub_refactor_spaces.types.uri_path_route_input

        out["uri_path_route"] = (
            capo_migration_hub_refactor_spaces.types.uri_path_route_input.deserialize_json(
                data["UriPathRoute"]
            )
        )
    if data.get("Tags") is not None:
        import capo_migration_hub_refactor_spaces.types.tag_map

        out["tags"] = capo_migration_hub_refactor_spaces.types.tag_map.deserialize_json(
            data["Tags"]
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out


def redact_sensitive(value: CreateRouteRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
