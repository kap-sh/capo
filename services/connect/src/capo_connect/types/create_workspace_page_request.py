"""Generated from Smithy shape ``com.amazonaws.connect#CreateWorkspacePageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.input_data
    import capo_connect.types.instance_id
    import capo_connect.types.page
    import capo_connect.types.slug
    import capo_connect.types.workspace_id


class CreateWorkspacePageRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Amazon Connect instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    workspace_id: "capo_connect.types.workspace_id.WorkspaceId"
    """<p>The identifier of the workspace.</p>"""
    resource_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the view to associate with the page.</p>"""
    page: "capo_connect.types.page.Page"
    """<p>The page identifier. Valid system pages include <code>HOME</code> and <code>AGENT_EXPERIENCE</code>. Custom pages cannot use the <code>aws:</code> or <code>connect:</code> prefixes.</p>"""
    slug: NotRequired["capo_connect.types.slug.Slug"]
    """<p>The URL-friendly identifier for the page.</p>"""
    input_data: NotRequired["capo_connect.types.input_data.InputData"]
    """<p>A JSON string containing input parameters for the view, validated against the view's input schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkspacePageRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["Page"] = value["page"]
    if "slug" in value:
        out["Slug"] = value["slug"]
    if "input_data" in value:
        out["InputData"] = value["input_data"]
    return out


def deserialize_json(data: dict) -> CreateWorkspacePageRequest:
    out: CreateWorkspacePageRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("CreateWorkspacePageRequest.resource_arn required")
    if data.get("Page") is not None:
        out["page"] = data["Page"]
    else:
        raise DeserializationError("CreateWorkspacePageRequest.page required")
    if data.get("Slug") is not None:
        out["slug"] = data["Slug"]
    if data.get("InputData") is not None:
        out["input_data"] = data["InputData"]
    return out
