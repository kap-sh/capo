"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateStandbyWorkspacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.region
    import capo_workspaces.types.standby_workspaces_list


class CreateStandbyWorkspacesRequest(TypedDict, closed=True):
    primary_region: "capo_workspaces.types.region.Region"
    """<p>The Region of the primary WorkSpace.</p>"""
    standby_workspaces: (
        "capo_workspaces.types.standby_workspaces_list.StandbyWorkspacesList"
    )
    """<p>Information about the standby WorkSpace to be created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateStandbyWorkspacesRequest) -> dict:
    out: dict = {}
    out["PrimaryRegion"] = value["primary_region"]
    import capo_workspaces.types.standby_workspaces_list

    out["StandbyWorkspaces"] = (
        capo_workspaces.types.standby_workspaces_list.serialize_aws_json_1_1(
            value["standby_workspaces"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateStandbyWorkspacesRequest:
    out: CreateStandbyWorkspacesRequest = {}  # type: ignore[typeddict-item]
    if data.get("PrimaryRegion") is not None:
        out["primary_region"] = data["PrimaryRegion"]
    else:
        out["primary_region"] = ""
    if data.get("StandbyWorkspaces") is not None:
        import capo_workspaces.types.standby_workspaces_list

        out["standby_workspaces"] = (
            capo_workspaces.types.standby_workspaces_list.deserialize_aws_json_1_1(
                data["StandbyWorkspaces"]
            )
        )
    else:
        out["standby_workspaces"] = []
    return out
