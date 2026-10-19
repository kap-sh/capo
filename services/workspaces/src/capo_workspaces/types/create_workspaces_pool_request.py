"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateWorkspacesPoolRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces.types.application_settings_request
    import capo_workspaces.types.bundle_id
    import capo_workspaces.types.capacity
    import capo_workspaces.types.directory_id
    import capo_workspaces.types.pools_running_mode
    import capo_workspaces.types.tag_list
    import capo_workspaces.types.timeout_settings
    import capo_workspaces.types.update_description
    import capo_workspaces.types.workspaces_pool_name


class CreateWorkspacesPoolRequest(TypedDict, closed=True):
    pool_name: "capo_workspaces.types.workspaces_pool_name.WorkspacesPoolName"
    """<p>The name of the pool.</p>"""
    description: "capo_workspaces.types.update_description.UpdateDescription"
    """<p>The pool description.</p>"""
    bundle_id: "capo_workspaces.types.bundle_id.BundleId"
    """<p>The identifier of the bundle for the pool.</p>"""
    directory_id: "capo_workspaces.types.directory_id.DirectoryId"
    """<p>The identifier of the directory for the pool.</p>"""
    capacity: "capo_workspaces.types.capacity.Capacity"
    """<p>The user capacity of the pool.</p>"""
    tags: NotRequired["capo_workspaces.types.tag_list.TagList"]
    """<p>The tags for the pool.</p>"""
    application_settings: NotRequired[
        "capo_workspaces.types.application_settings_request.ApplicationSettingsRequest"
    ]
    """<p>Indicates the application settings of the pool.</p>"""
    timeout_settings: NotRequired[
        "capo_workspaces.types.timeout_settings.TimeoutSettings"
    ]
    """<p>Indicates the timeout settings of the pool.</p>"""
    running_mode: NotRequired[
        "capo_workspaces.types.pools_running_mode.PoolsRunningMode"
    ]
    """<p>The running mode for the pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWorkspacesPoolRequest) -> dict:
    out: dict = {}
    out["PoolName"] = value["pool_name"]
    out["Description"] = value["description"]
    out["BundleId"] = value["bundle_id"]
    out["DirectoryId"] = value["directory_id"]
    import capo_workspaces.types.capacity

    out["Capacity"] = capo_workspaces.types.capacity.serialize_aws_json_1_1(
        value["capacity"]
    )
    if "tags" in value:
        import capo_workspaces.types.tag_list

        out["Tags"] = capo_workspaces.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "application_settings" in value:
        import capo_workspaces.types.application_settings_request

        out["ApplicationSettings"] = (
            capo_workspaces.types.application_settings_request.serialize_aws_json_1_1(
                value["application_settings"]
            )
        )
    if "timeout_settings" in value:
        import capo_workspaces.types.timeout_settings

        out["TimeoutSettings"] = (
            capo_workspaces.types.timeout_settings.serialize_aws_json_1_1(
                value["timeout_settings"]
            )
        )
    if "running_mode" in value:
        import capo_workspaces.types.pools_running_mode

        out["RunningMode"] = (
            capo_workspaces.types.pools_running_mode.serialize_aws_json_1_1(
                value["running_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWorkspacesPoolRequest:
    out: CreateWorkspacesPoolRequest = {}  # type: ignore[typeddict-item]
    if data.get("PoolName") is not None:
        out["pool_name"] = data["PoolName"]
    else:
        out["pool_name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        out["description"] = ""
    if data.get("BundleId") is not None:
        out["bundle_id"] = data["BundleId"]
    else:
        out["bundle_id"] = ""
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("Capacity") is not None:
        import capo_workspaces.types.capacity

        out["capacity"] = capo_workspaces.types.capacity.deserialize_aws_json_1_1(
            data["Capacity"]
        )
    else:
        raise DeserializationError("CreateWorkspacesPoolRequest.capacity required")
    if data.get("Tags") is not None:
        import capo_workspaces.types.tag_list

        out["tags"] = capo_workspaces.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("ApplicationSettings") is not None:
        import capo_workspaces.types.application_settings_request

        out["application_settings"] = (
            capo_workspaces.types.application_settings_request.deserialize_aws_json_1_1(
                data["ApplicationSettings"]
            )
        )
    if data.get("TimeoutSettings") is not None:
        import capo_workspaces.types.timeout_settings

        out["timeout_settings"] = (
            capo_workspaces.types.timeout_settings.deserialize_aws_json_1_1(
                data["TimeoutSettings"]
            )
        )
    if data.get("RunningMode") is not None:
        import capo_workspaces.types.pools_running_mode

        out["running_mode"] = (
            capo_workspaces.types.pools_running_mode.deserialize_aws_json_1_1(
                data["RunningMode"]
            )
        )
    return out
