"""Generated from Smithy shape ``com.amazonaws.connect#UpdateWorkspacePageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.input_data
    import capo_connect.types.instance_id
    import capo_connect.types.page
    import capo_connect.types.slug
    import capo_connect.types.workspace_id


class UpdateWorkspacePageRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Amazon Connect instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    workspace_id: "capo_connect.types.workspace_id.WorkspaceId"
    """<p>The identifier of the workspace.</p>"""
    page: "capo_connect.types.page.Page"
    """<p>The current page identifier.</p>"""
    new_page: NotRequired["capo_connect.types.page.Page"]
    """<p>The new page identifier, if changing the page name.</p>"""
    resource_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the view to associate with the page.</p>"""
    slug: NotRequired["capo_connect.types.slug.Slug"]
    """<p>The URL-friendly identifier for the page.</p>"""
    input_data: NotRequired["capo_connect.types.input_data.InputData"]
    """<p>A JSON string containing input parameters for the view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkspacePageRequest) -> dict:
    out: dict = {}
    if "new_page" in value:
        out["NewPage"] = value["new_page"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "slug" in value:
        out["Slug"] = value["slug"]
    if "input_data" in value:
        out["InputData"] = value["input_data"]
    return out


def deserialize_json(data: dict) -> UpdateWorkspacePageRequest:
    out: UpdateWorkspacePageRequest = {}  # type: ignore[typeddict-item]
    if data.get("NewPage") is not None:
        out["new_page"] = data["NewPage"]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("Slug") is not None:
        out["slug"] = data["Slug"]
    if data.get("InputData") is not None:
        out["input_data"] = data["InputData"]
    return out
