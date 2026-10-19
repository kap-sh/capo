"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspacesPool``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces.types.application_settings_response
    import capo_workspaces.types.arn
    import capo_workspaces.types.bundle_id
    import capo_workspaces.types.capacity_status
    import capo_workspaces.types.directory_id
    import capo_workspaces.types.pools_running_mode
    import capo_workspaces.types.timeout_settings
    import capo_workspaces.types.timestamp
    import capo_workspaces.types.update_description
    import capo_workspaces.types.workspaces_pool_errors
    import capo_workspaces.types.workspaces_pool_id
    import capo_workspaces.types.workspaces_pool_name
    import capo_workspaces.types.workspaces_pool_state


class WorkspacesPool(TypedDict, closed=True):
    pool_id: "capo_workspaces.types.workspaces_pool_id.WorkspacesPoolId"
    """<p>The identifier of a pool.</p>"""
    pool_arn: "capo_workspaces.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the pool.</p>"""
    capacity_status: "capo_workspaces.types.capacity_status.CapacityStatus"
    """<p>The capacity status for the pool</p>"""
    pool_name: "capo_workspaces.types.workspaces_pool_name.WorkspacesPoolName"
    """<p>The name of the pool.</p>"""
    description: NotRequired[
        "capo_workspaces.types.update_description.UpdateDescription"
    ]
    """<p>The description of the pool.</p>"""
    state: "capo_workspaces.types.workspaces_pool_state.WorkspacesPoolState"
    """<p>The current state of the pool.</p>"""
    created_at: "capo_workspaces.types.timestamp.Timestamp"
    """<p>The time the pool was created.</p>"""
    bundle_id: "capo_workspaces.types.bundle_id.BundleId"
    """<p>The identifier of the bundle used by the pool.</p>"""
    directory_id: "capo_workspaces.types.directory_id.DirectoryId"
    """<p>The identifier of the directory used by the pool.</p>"""
    errors: NotRequired[
        "capo_workspaces.types.workspaces_pool_errors.WorkspacesPoolErrors"
    ]
    """<p>The pool errors.</p>"""
    application_settings: NotRequired[
        "capo_workspaces.types.application_settings_response.ApplicationSettingsResponse"
    ]
    """<p>The persistent application settings for users of the pool.</p>"""
    timeout_settings: NotRequired[
        "capo_workspaces.types.timeout_settings.TimeoutSettings"
    ]
    """<p>The amount of time that a pool session remains active after users disconnect. If they try to reconnect to the pool session after a disconnection or network interruption within this time interval, they are connected to their previous session. Otherwise, they are connected to a new session with a new pool instance.</p>"""
    running_mode: "capo_workspaces.types.pools_running_mode.PoolsRunningMode"
    """<p>The running mode of the pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspacesPool) -> dict:
    out: dict = {}
    out["PoolId"] = value["pool_id"]
    out["PoolArn"] = value["pool_arn"]
    import capo_workspaces.types.capacity_status

    out["CapacityStatus"] = (
        capo_workspaces.types.capacity_status.serialize_aws_json_1_1(
            value["capacity_status"]
        )
    )
    out["PoolName"] = value["pool_name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_workspaces.types.workspaces_pool_state

    out["State"] = capo_workspaces.types.workspaces_pool_state.serialize_aws_json_1_1(
        value["state"]
    )
    import capo_workspaces.types.timestamp

    out["CreatedAt"] = capo_workspaces.types.timestamp.serialize_aws_json_1_1(
        value["created_at"]
    )
    out["BundleId"] = value["bundle_id"]
    out["DirectoryId"] = value["directory_id"]
    if "errors" in value:
        import capo_workspaces.types.workspaces_pool_errors

        out["Errors"] = (
            capo_workspaces.types.workspaces_pool_errors.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    if "application_settings" in value:
        import capo_workspaces.types.application_settings_response

        out["ApplicationSettings"] = (
            capo_workspaces.types.application_settings_response.serialize_aws_json_1_1(
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
    import capo_workspaces.types.pools_running_mode

    out["RunningMode"] = (
        capo_workspaces.types.pools_running_mode.serialize_aws_json_1_1(
            value.get("running_mode", "AUTO_STOP")
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkspacesPool:
    out: WorkspacesPool = {}  # type: ignore[typeddict-item]
    if data.get("PoolId") is not None:
        out["pool_id"] = data["PoolId"]
    else:
        out["pool_id"] = ""
    if data.get("PoolArn") is not None:
        out["pool_arn"] = data["PoolArn"]
    else:
        out["pool_arn"] = ""
    if data.get("CapacityStatus") is not None:
        import capo_workspaces.types.capacity_status

        out["capacity_status"] = (
            capo_workspaces.types.capacity_status.deserialize_aws_json_1_1(
                data["CapacityStatus"]
            )
        )
    else:
        raise DeserializationError("WorkspacesPool.capacity_status required")
    if data.get("PoolName") is not None:
        out["pool_name"] = data["PoolName"]
    else:
        out["pool_name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("State") is not None:
        import capo_workspaces.types.workspaces_pool_state

        out["state"] = (
            capo_workspaces.types.workspaces_pool_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_workspaces.types.workspaces_pool_state.WorkspacesPoolState", ""
        )
    if data.get("CreatedAt") is not None:
        import capo_workspaces.types.timestamp

        out["created_at"] = capo_workspaces.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("BundleId") is not None:
        out["bundle_id"] = data["BundleId"]
    else:
        out["bundle_id"] = ""
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("Errors") is not None:
        import capo_workspaces.types.workspaces_pool_errors

        out["errors"] = (
            capo_workspaces.types.workspaces_pool_errors.deserialize_aws_json_1_1(
                data["Errors"]
            )
        )
    if data.get("ApplicationSettings") is not None:
        import capo_workspaces.types.application_settings_response

        out["application_settings"] = (
            capo_workspaces.types.application_settings_response.deserialize_aws_json_1_1(
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
    else:
        out["running_mode"] = "AUTO_STOP"
    return out
