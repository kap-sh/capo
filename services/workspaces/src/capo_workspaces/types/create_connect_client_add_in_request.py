"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateConnectClientAddInRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.add_in_name
    import capo_workspaces.types.add_in_url
    import capo_workspaces.types.directory_id


class CreateConnectClientAddInRequest(TypedDict, closed=True):
    resource_id: "capo_workspaces.types.directory_id.DirectoryId"
    """<p>The directory identifier for which to configure the client add-in.</p>"""
    name: "capo_workspaces.types.add_in_name.AddInName"
    """<p>The name of the client add-in.</p>"""
    url: "capo_workspaces.types.add_in_url.AddInUrl"
    """<p>The endpoint URL of the Connect Customer client add-in.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConnectClientAddInRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    out["Name"] = value["name"]
    out["URL"] = value["url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateConnectClientAddInRequest:
    out: CreateConnectClientAddInRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("URL") is not None:
        out["url"] = data["URL"]
    else:
        out["url"] = ""
    return out
