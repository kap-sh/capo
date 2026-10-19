"""Generated from Smithy shape ``com.amazonaws.workspaces#UpdateConnectionAliasPermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces.types.connection_alias_id
    import capo_workspaces.types.connection_alias_permission


class UpdateConnectionAliasPermissionRequest(TypedDict, closed=True):
    alias_id: "capo_workspaces.types.connection_alias_id.ConnectionAliasId"
    """<p>The identifier of the connection alias that you want to update permissions for.</p>"""
    connection_alias_permission: (
        "capo_workspaces.types.connection_alias_permission.ConnectionAliasPermission"
    )
    """<p>Indicates whether to share or unshare the connection alias with the specified Amazon Web Services account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateConnectionAliasPermissionRequest) -> dict:
    out: dict = {}
    out["AliasId"] = value["alias_id"]
    import capo_workspaces.types.connection_alias_permission

    out["ConnectionAliasPermission"] = (
        capo_workspaces.types.connection_alias_permission.serialize_aws_json_1_1(
            value["connection_alias_permission"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateConnectionAliasPermissionRequest:
    out: UpdateConnectionAliasPermissionRequest = {}  # type: ignore[typeddict-item]
    if data.get("AliasId") is not None:
        out["alias_id"] = data["AliasId"]
    else:
        out["alias_id"] = ""
    if data.get("ConnectionAliasPermission") is not None:
        import capo_workspaces.types.connection_alias_permission

        out["connection_alias_permission"] = (
            capo_workspaces.types.connection_alias_permission.deserialize_aws_json_1_1(
                data["ConnectionAliasPermission"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateConnectionAliasPermissionRequest.connection_alias_permission required"
        )
    return out
