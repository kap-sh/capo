"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateWorkspacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.workspace_request_list


class CreateWorkspacesRequest(TypedDict, closed=True):
    workspaces: "capo_workspaces.types.workspace_request_list.WorkspaceRequestList"
    """<p>The WorkSpaces to create. You can specify up to 25 WorkSpaces.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWorkspacesRequest) -> dict:
    out: dict = {}
    import capo_workspaces.types.workspace_request_list

    out["Workspaces"] = (
        capo_workspaces.types.workspace_request_list.serialize_aws_json_1_1(
            value["workspaces"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWorkspacesRequest:
    out: CreateWorkspacesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Workspaces") is not None:
        import capo_workspaces.types.workspace_request_list

        out["workspaces"] = (
            capo_workspaces.types.workspace_request_list.deserialize_aws_json_1_1(
                data["Workspaces"]
            )
        )
    else:
        out["workspaces"] = []
    return out
