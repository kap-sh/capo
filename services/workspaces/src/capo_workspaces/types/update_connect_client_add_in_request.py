"""Generated from Smithy shape ``com.amazonaws.workspaces#UpdateConnectClientAddInRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.add_in_name
    import capo_workspaces.types.add_in_url
    import capo_workspaces.types.amazon_uuid
    import capo_workspaces.types.directory_id


class UpdateConnectClientAddInRequest(TypedDict, closed=True):
    add_in_id: "capo_workspaces.types.amazon_uuid.AmazonUuid"
    """<p>The identifier of the client add-in to update.</p>"""
    resource_id: "capo_workspaces.types.directory_id.DirectoryId"
    """<p>The directory identifier for which the client add-in is configured.</p>"""
    name: NotRequired["capo_workspaces.types.add_in_name.AddInName"]
    """<p>The name of the client add-in.</p>"""
    url: NotRequired["capo_workspaces.types.add_in_url.AddInUrl"]
    """<p>The endpoint URL of the Connect Customer client add-in.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateConnectClientAddInRequest) -> dict:
    out: dict = {}
    out["AddInId"] = value["add_in_id"]
    out["ResourceId"] = value["resource_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "url" in value:
        out["URL"] = value["url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateConnectClientAddInRequest:
    out: UpdateConnectClientAddInRequest = {}  # type: ignore[typeddict-item]
    if data.get("AddInId") is not None:
        out["add_in_id"] = data["AddInId"]
    else:
        out["add_in_id"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("URL") is not None:
        out["url"] = data["URL"]
    return out
