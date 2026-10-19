"""Generated from Smithy shape ``com.amazonaws.workspaces#UpdateWorkspacesPoolRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.application_settings_request
    import capo_workspaces.types.bundle_id
    import capo_workspaces.types.capacity
    import capo_workspaces.types.directory_id
    import capo_workspaces.types.pools_running_mode
    import capo_workspaces.types.timeout_settings
    import capo_workspaces.types.update_description
    import capo_workspaces.types.workspaces_pool_id


class UpdateWorkspacesPoolRequest(TypedDict, closed=True):
    pool_id: "capo_workspaces.types.workspaces_pool_id.WorkspacesPoolId"
    """<p>The identifier of the specified pool to update.</p>"""
    description: NotRequired[
        "capo_workspaces.types.update_description.UpdateDescription"
    ]
    """<p>Describes the specified pool to update.</p>"""
    bundle_id: NotRequired["capo_workspaces.types.bundle_id.BundleId"]
    """<p>The identifier of the bundle.</p>"""
    directory_id: NotRequired["capo_workspaces.types.directory_id.DirectoryId"]
    """<p>The identifier of the directory.</p>"""
    capacity: NotRequired["capo_workspaces.types.capacity.Capacity"]
    """<p>The desired capacity for the pool.</p>"""
    application_settings: NotRequired[
        "capo_workspaces.types.application_settings_request.ApplicationSettingsRequest"
    ]
    """<p>The persistent application settings for users in the pool.</p>"""
    timeout_settings: NotRequired[
        "capo_workspaces.types.timeout_settings.TimeoutSettings"
    ]
    """<p>Indicates the timeout settings of the specified pool.</p>"""
    running_mode: NotRequired[
        "capo_workspaces.types.pools_running_mode.PoolsRunningMode"
    ]
    """<p>The desired running mode for the pool. The running mode can only be updated when the pool is in a stopped state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWorkspacesPoolRequest) -> dict:
    out: dict = {}
    out["PoolId"] = value["pool_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "bundle_id" in value:
        out["BundleId"] = value["bundle_id"]
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "capacity" in value:
        import capo_workspaces.types.capacity

        out["Capacity"] = capo_workspaces.types.capacity.serialize_aws_json_1_1(
            value["capacity"]
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


def deserialize_aws_json_1_1(data: dict) -> UpdateWorkspacesPoolRequest:
    out: UpdateWorkspacesPoolRequest = {}  # type: ignore[typeddict-item]
    if data.get("PoolId") is not None:
        out["pool_id"] = data["PoolId"]
    else:
        out["pool_id"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("BundleId") is not None:
        out["bundle_id"] = data["BundleId"]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("Capacity") is not None:
        import capo_workspaces.types.capacity

        out["capacity"] = capo_workspaces.types.capacity.deserialize_aws_json_1_1(
            data["Capacity"]
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
