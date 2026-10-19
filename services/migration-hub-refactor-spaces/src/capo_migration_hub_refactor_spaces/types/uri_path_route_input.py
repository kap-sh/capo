"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#UriPathRouteInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.boolean
    import capo_migration_hub_refactor_spaces.types.http_methods
    import capo_migration_hub_refactor_spaces.types.route_activation_state
    import capo_migration_hub_refactor_spaces.types.uri_path


class UriPathRouteInput(TypedDict, closed=True):
    source_path: "capo_migration_hub_refactor_spaces.types.uri_path.UriPath"
    """<p>This is the path that Refactor Spaces uses to match traffic. Paths must start with <code>/</code> and are relative to the base of the application. To use path parameters in the source path, add a variable in curly braces. For example, the resource path {user} represents a path parameter called 'user'.</p>"""
    activation_state: "capo_migration_hub_refactor_spaces.types.route_activation_state.RouteActivationState"
    """<p>If set to <code>ACTIVE</code>, traffic is forwarded to this route’s service after the route is created. </p>"""
    methods: NotRequired[
        "capo_migration_hub_refactor_spaces.types.http_methods.HttpMethods"
    ]
    """<p>A list of HTTP methods to match. An empty list matches all values. If a method is present, only HTTP requests using that method are forwarded to this route’s service. </p>"""
    include_child_paths: NotRequired[
        "capo_migration_hub_refactor_spaces.types.boolean.Boolean"
    ]
    """<p>Indicates whether to match all subpaths of the given source path. If this value is <code>false</code>, requests must match the source path exactly before they are forwarded to this route's service. </p>"""
    append_source_path: NotRequired[
        "capo_migration_hub_refactor_spaces.types.boolean.Boolean"
    ]
    """<p>If set to <code>true</code>, this option appends the source path to the service URL endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UriPathRouteInput) -> dict:
    out: dict = {}
    out["SourcePath"] = value["source_path"]
    out["ActivationState"] = value["activation_state"]
    if "methods" in value:
        import capo_migration_hub_refactor_spaces.types.http_methods

        out["Methods"] = (
            capo_migration_hub_refactor_spaces.types.http_methods.serialize_json(
                value["methods"]
            )
        )
    if "include_child_paths" in value:
        out["IncludeChildPaths"] = value["include_child_paths"]
    if "append_source_path" in value:
        out["AppendSourcePath"] = value["append_source_path"]
    return out


def deserialize_json(data: dict) -> UriPathRouteInput:
    out: UriPathRouteInput = {}  # type: ignore[typeddict-item]
    if data.get("SourcePath") is not None:
        out["source_path"] = data["SourcePath"]
    else:
        out["source_path"] = ""
    if data.get("ActivationState") is not None:
        out["activation_state"] = data["ActivationState"]
    else:
        out["activation_state"] = ""
    if data.get("Methods") is not None:
        import capo_migration_hub_refactor_spaces.types.http_methods

        out["methods"] = (
            capo_migration_hub_refactor_spaces.types.http_methods.deserialize_json(
                data["Methods"]
            )
        )
    if data.get("IncludeChildPaths") is not None:
        out["include_child_paths"] = data["IncludeChildPaths"]
    if data.get("AppendSourcePath") is not None:
        out["append_source_path"] = data["AppendSourcePath"]
    return out
