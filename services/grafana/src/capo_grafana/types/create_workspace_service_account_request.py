"""Generated from Smithy shape ``com.amazonaws.grafana#CreateWorkspaceServiceAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import capo_grafana.types.role
    import capo_grafana.types.service_account_name
    import capo_grafana.types.workspace_id


class CreateWorkspaceServiceAccountRequest(TypedDict, closed=True):
    name: "capo_grafana.types.service_account_name.ServiceAccountName"
    """<p>A name for the service account. The name must be unique within the workspace, as it determines the ID associated with the service account.</p>"""
    grafana_role: "capo_grafana.types.role.Role"
    """<p>The permission level to use for this service account.</p> <note> <p>For more information about the roles and the permissions each has, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-user-roles.html">User roles</a> in the <i>Amazon Managed Grafana User Guide</i>.</p> </note>"""
    workspace_id: "capo_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace within which to create the service account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkspaceServiceAccountRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["grafanaRole"] = value["grafana_role"]
    return out


def deserialize_json(data: dict) -> CreateWorkspaceServiceAccountRequest:
    out: CreateWorkspaceServiceAccountRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateWorkspaceServiceAccountRequest.name required")
    if data.get("grafanaRole") is not None:
        out["grafana_role"] = data["grafanaRole"]
    else:
        raise DeserializationError(
            "CreateWorkspaceServiceAccountRequest.grafana_role required"
        )
    return out
