"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifySelfservicePermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces.types.directory_id
    import capo_workspaces.types.selfservice_permissions


class ModifySelfservicePermissionsRequest(TypedDict, closed=True):
    resource_id: "capo_workspaces.types.directory_id.DirectoryId"
    """<p>The identifier of the directory.</p>"""
    selfservice_permissions: (
        "capo_workspaces.types.selfservice_permissions.SelfservicePermissions"
    )
    """<p>The permissions to enable or disable self-service capabilities.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifySelfservicePermissionsRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import capo_workspaces.types.selfservice_permissions

    out["SelfservicePermissions"] = (
        capo_workspaces.types.selfservice_permissions.serialize_aws_json_1_1(
            value["selfservice_permissions"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifySelfservicePermissionsRequest:
    out: ModifySelfservicePermissionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("SelfservicePermissions") is not None:
        import capo_workspaces.types.selfservice_permissions

        out["selfservice_permissions"] = (
            capo_workspaces.types.selfservice_permissions.deserialize_aws_json_1_1(
                data["SelfservicePermissions"]
            )
        )
    else:
        raise DeserializationError(
            "ModifySelfservicePermissionsRequest.selfservice_permissions required"
        )
    return out
