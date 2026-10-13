"""Generated from Smithy shape ``com.amazonaws.grafana#UpdateWorkspaceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import capo_grafana.types.workspace_description


class UpdateWorkspaceResponse(TypedDict, closed=True):
    workspace: "capo_grafana.types.workspace_description.WorkspaceDescription"
    """<p>A structure containing data about the workspace that was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkspaceResponse) -> dict:
    out: dict = {}
    import capo_grafana.types.workspace_description

    out["workspace"] = capo_grafana.types.workspace_description.serialize_json(
        value["workspace"]
    )
    return out


def deserialize_json(data: dict) -> UpdateWorkspaceResponse:
    out: UpdateWorkspaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("workspace") is not None:
        import capo_grafana.types.workspace_description

        out["workspace"] = capo_grafana.types.workspace_description.deserialize_json(
            data["workspace"]
        )
    else:
        raise DeserializationError("UpdateWorkspaceResponse.workspace required")
    return out


def redact_sensitive(value: UpdateWorkspaceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "workspace" in value:
        import capo_grafana.types.workspace_description

        out["workspace"] = capo_grafana.types.workspace_description.redact_sensitive(
            value["workspace"]
        )
    return out
