"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CreatePortalResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn
    import capo_workspaces_web.types.portal_endpoint


class CreatePortalResponse(TypedDict, closed=True):
    portal_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""
    portal_endpoint: "capo_workspaces_web.types.portal_endpoint.PortalEndpoint"
    """<p>The endpoint URL of the web portal that users access in order to start streaming sessions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePortalResponse) -> dict:
    out: dict = {}
    out["portalArn"] = value["portal_arn"]
    out["portalEndpoint"] = value["portal_endpoint"]
    return out


def deserialize_json(data: dict) -> CreatePortalResponse:
    out: CreatePortalResponse = {}  # type: ignore[typeddict-item]
    if data.get("portalArn") is not None:
        out["portal_arn"] = data["portalArn"]
    else:
        out["portal_arn"] = ""
    if data.get("portalEndpoint") is not None:
        out["portal_endpoint"] = data["portalEndpoint"]
    else:
        out["portal_endpoint"] = ""
    return out
