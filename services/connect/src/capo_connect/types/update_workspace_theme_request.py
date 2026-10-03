"""Generated from Smithy shape ``com.amazonaws.connect#UpdateWorkspaceThemeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.workspace_id
    import capo_connect.types.workspace_theme


class UpdateWorkspaceThemeRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Amazon Connect instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    workspace_id: "capo_connect.types.workspace_id.WorkspaceId"
    """<p>The identifier of the workspace.</p>"""
    theme: NotRequired["capo_connect.types.workspace_theme.WorkspaceTheme"]
    """<p>The theme configuration, including color schemes and visual styles.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkspaceThemeRequest) -> dict:
    out: dict = {}
    if "theme" in value:
        import capo_connect.types.workspace_theme

        out["Theme"] = capo_connect.types.workspace_theme.serialize_json(value["theme"])
    return out


def deserialize_json(data: dict) -> UpdateWorkspaceThemeRequest:
    out: UpdateWorkspaceThemeRequest = {}  # type: ignore[typeddict-item]
    if data.get("Theme") is not None:
        import capo_connect.types.workspace_theme

        out["theme"] = capo_connect.types.workspace_theme.deserialize_json(
            data["Theme"]
        )
    return out
